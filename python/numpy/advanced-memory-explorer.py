#step 1: Advanced Tracker function

import numpy as np

def analyze(name, arr):
    print(f"\n{name}")
    print("-"*30)
    print("shape: ", arr.shape)
    print("id: ", id(arr))
    print("base: ", "None" if arr.base is None else "Has base")
    print("shares_memory: ", arr.base is not None)
    print("strides: ", arr.strides)
    print("C: ", arr.flags['C_CONTIGUOUS'], "| F: ", arr.flags['F_CONTIGUOUS'])
    print(arr)

#step 2: Build data pipeline

a = np.arange(16).reshape(4, 4)
analyze("a: ", a )

b = a[:, :3]
analyze("b = slice ", b)

c = b*2
analyze("c = operator: ", c)

d = c.T
analyze("d = Transpose: ", d)

e = d.ravel()
analyze("e = ravel: ", e)

#step 3: mutation tracking

print("\n---mutation test---")

b[0, 0] = 999

print("after modifying b: ")
analyze("a", a)
analyze("b", b)
analyze("c", c)

#step 4: memory relationship checker

def check_relationship(x, y, name1, name2):
    print(f"{name1} & {name2} share memory?", np.shares_memory(x, y))


check_relationship(a, b, "a", "b")
check_relationship(a, c, "a", "c")
check_relationship(c, d, "c", "d")

#step 5: Break the system (advenced)

f = a[:, ::2]
analyze("f = step slice: ", f)

g = f.reshape(-1)
analyze("g = reshape", g)

#step 6: Real ML bug simultation

data = np.arange(10)

features = data[::2] #view

processed = features.copy()
features[0] = 999  #accidental mutation

print("data: ", data)
print("features: ", features)
print("processed: ", processed)


