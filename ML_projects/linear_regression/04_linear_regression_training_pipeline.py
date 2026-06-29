#step 1: Create Dataset

import numpy as np

np.random.seed(42)

#100 samples, 1 feature
x = 2 * np.random.rand(100, 1)

#true relatonship: y = 4 + 3x + noise
y = 4 + 3 * x + np.random.randn(100, 1)


#step 2: feature scaling
x_mean = np.mean(x, axis=0)
x_std = np.std(x, axis=0)

x_scaled = (x - x_mean)/x_std

y_mean = np.mean(y, axis = 0)
y_std = np.std(y, axis = 0)

y_scaled = (y - y_mean)/ y_std

#step 3: initialize parameters
w = np.random.randn(1, 1)
b = np.zeros((1,))

#step 4: forward pass
y_pred = x_scaled @ w + b

#step 5: loss (error)
loss = y_pred - y_scaled

#step 6: gradient caculation
dw = x_scaled.T @ loss / len(x)
db = np.mean(loss)

#step 7: gradient update
learning_rate = 0.01

w = w - learning_rate * dw
b = b - learning_rate * db

#step 8: full training loop
epochs = 1000

for epoch in range(epochs):

    #forward
    y_pred = x_scaled @ w + b

    #loss
    loss = y_pred - y_scaled
    
    #gradients
    dw = x_scaled.T @ loss / len(x)
    db = np.mean(loss)


    #update
    w -= learning_rate * dw
    b -= learning_rate * db


    if epoch % 100 == 0:
        print(f"Epochs {epoch}, Loss: {np.mean(loss**2)}")


#step 9: final result
print("Learned w: ", w)
print("Learned b: ", b)


w_org = w * (y_std / x_std)
b_org = y_mean + y_std*b - w_org * x_mean

print("original w: ", w_org)
print("original b: ", b_org)
