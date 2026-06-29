import numpy as np

x = np.array([
    [1, 10],
    [2, 20],
    [3, 30],
    [4, 40],
    [5, 50]
], dtype = float)

print(x.shape)

y = np.array([32, 64, 96, 128, 160], dtype = float)
print(y.shape)

x_mean = np.mean(x, axis = 0)
x_std = np.std(x, axis = 0)

y_mean = np.mean(y)
y_std = np.std(y)

y_scaled = (y - y_mean)/y_std
x_scaled = (x - x_mean)/x_std

n = len(x)
w = np.zeros(2)
print(w.shape)
b = 0
lr = 0.01
epochs = 1000

#learning loop
for epoch in range(epochs):

    y_pred = x_scaled @ w + b

    loss = np.mean((y_scaled - y_pred)**2)

    dw = (-2/n)*(x_scaled.T@(y_scaled - y_pred))
    db = (-2/n)*np.sum(y_scaled - y_pred)

    w -= lr*dw
    b -= lr*db

y_pred_scaled = x_scaled @ w + b
y_pred_org = y_pred_scaled * y_std + y_mean


print("w: ", w)
print("b: ", b)
print("loss: ", loss)
print("y_pred_org: ", y_pred_org)
print(y_pred.shape)