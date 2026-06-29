#____________________________________DATA_LOADING________________________________________________________________________________

# This is for loading messy data with different separators which our python fails to encode and recognize.
#---------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
from ftfy import fix_text


import pandas as pd

df = pd.read_csv(
    "messy_IMDB.csv",
    sep=";",
    encoding="latin-1",   # most stable fallback
    engine="python",
    on_bad_lines="skip"
)

from ftfy import fix_text

text_cols = df.select_dtypes(include="object").columns
df[text_cols] = df[text_cols].apply(
    lambda col: col.map(lambda x: fix_text(x) if isinstance(x, str) else x)
)

print(df.head())
print(df.columns)
print(df.info())
#_______________________________DATA_LOADING_ENDED_______________________________________________________________________________________________


#_________________________________COLUMN'S_NAME_CLEANING_AND_DROPPING_______________________________________________________________________________________________________________

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.rename(columns= {"original_titlê" : "original_title", "genrë¨" : "genre"})
df = df.drop(columns= "unnamed:_8")
#_______________________________________END________________________________________________________________________________________________________________________________

#_____________________________________INCOME_CLEANING________________________________________________________________________________________________________________________________
df["income"] = pd.to_numeric(df["income"].astype(str)
                             .str.replace("$", "", regex = False)
                             .str.replace(",", "", regex = False)
                             .str.replace("o", "0"), errors = "coerce")
#_______________________________________END________________________________________________________________________________________________________________________________

#____________________________________RELEASE_YEAR_CLEANING___________________________________________________________________________________________________________________________________
df["release_year"] = pd.to_datetime(df["release_year"].astype(str)
                                    .str.strip(),format= "mixed", 
                                      dayfirst=True, errors = "coerce")
#___________________________________________END__________________________________________________________________________________________________________________________

#___________________________________CONTENT_RATING_CLEANING____________________________________________________________________________________________________________________________________
df["content_rating"]=(df["content_rating"].astype(str)
                      .str.strip().str.lower()
                      .str.replace({
                          
                         " " : "_",
                         "-" : "_"

                                 })
                       .str.upper()          
                     )
df.fillna({"content_rating": df["content_rating"].mode()[0]}, inplace=True)
#________________________________END____________________________________________________________________________________________________________________________________


#_______________________________________________SCORE_CLEANING__________________________________________________________________________________________________________

# This function is for cleaning messy numeric values.
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def clean_numeric(series):
    s = series.astype(str)
    s = s.str.replace(',', '.', regex=False)
    s = s.str.replace(':', '.', regex=False)
    s = s.str.extract(r'([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)')[0]
    return pd.to_numeric(s, errors='coerce')
#------------------------------------------------------------------------------------------------------------------------------------------------------


# applying above function to clean the score column and collect it in a new column called "score_clean".
#------------------------------------------------------------------------------------------------------------------------------------------------------
df['score_cleaned'] = clean_numeric(df['score'])
#------------------------------------------------------------------------------------------------------------------------------------------------------

df.fillna({"score_cleaned" : df["score_cleaned"].median()}, inplace = True)
#___________________________________END____________________________________________________________________________________________________________________


#___________________________________________COUNTRY_CLEANING_________________________________________________________________________________________________

print(df["country"].value_counts())
print(df["country"].sum())

from rapidfuzz import process

standard_countries = ["NEW_ZEALAND", "USA", "UK", "INDIA", "ITALY", "BRAZIL", "JAPAN", "GERMANY", "WEST_GERMANY", "SOUTH_KOREA", "FRANCE", "DENMARK", "IRAN"]

def fix_country(value):
    if pd.isna(value):
        return None

    match, score, _ = process.extractOne(
        str(value).upper(),
        standard_countries
    )

    return match if score > 80 else np.nan

df["country"] = df["country"].apply(fix_country)

df.fillna({"country": df["country"].mode()[0]}, inplace=True)
#________________________________________________END______________________________________________________________________________________________________________


#______________________VOTES_CLEANING______________________________________________________________________________________________________________________________

df["votes"] = pd.to_numeric(df["votes"].astype(str).str.strip().str.replace(".", ""))
df.fillna({"votes" : df["votes"].median()}, inplace=True)
df["votes"] = df["votes"].round(0).astype("Int64")
#______________________END______________________________________________________________________________________________________________________________



#______________________GENRE_CLEANING______________________________________________________________________________________________________________________________

# strip spaces, lowercase, split by comma
df['genre_clean'] = (
    df['genre']
    .str.lower()
    .str.split(',')
)

# remove extra spaces
df['genre_clean'] = df['genre_clean'].apply(
    lambda x: [g.strip() for g in x] if isinstance(x, list) else x
)

#______________________END______________________________________________________________________________________________________________________________



#______________________DURATION_CLEANING__________________________________________________________________________________________________________________

df["duration_clean"] = pd.to_numeric(df["duration"].astype(str).str.strip().str.replace(r"[^0-9.]", "", regex = True))
df.fillna({"duration_clean" : df["duration_clean"].mean()}, inplace=True)
df["duration_clean"] = df["duration_clean"].round(0).astype("Int64")

#______________________END______________________________________________________________________________________________________________________________


#______________________ORIGINAL_TITLE_CLEAN_______________________________________________________________________________________________________________

df["original_title_clean"] = df["original_title"].astype(str).str.strip().str.lower()

#______________________END________________________________________________________________________________________________________________________________



#_____________________DIRECTOR_CLEANING_________________________________________________________________________________________________________________________________

df["director"] = df["director"].astype(str).str.strip().str.lower()

#______________________END________________________________________________________________________________________________________________________________
                    


print(df.head())
print("\n")
print(df.tail())
print("\n")
print(df.isnull().sum())
print(df.isnull().mean())
print("\n")
print(df["director"].unique()[:50])
print(df["director"].value_counts())
#print(df["genre_clean"])