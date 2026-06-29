import numpy as np

x = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12],
    [5, 10, 15]
], dtype = float)

y = np.array([14, 28, 42, 56, 70], dtype = float)

x_mean = np.mean(x, axis = 0)
x_std = np.std(x, axis = 0)

y_mean = np.mean(y)
y_std = np.std(y)

x_scaled = (x - x_mean)/x_std
y_scaled = (y - y_mean)/y_std

n = len(x)
w = np.zeros(3)
b = 0
lr = 0.01
epochs = 1000


#training loop
for epoch in range(epochs):

    y_pred = x_scaled @ w + b

    loss = np.mean((y_scaled - y_pred)**2)

    dw = (-2/n)*(x_scaled.T@(y_scaled - y_pred))
    db = (-2/n)*np.sum(y_scaled - y_pred)

    w -= lr*dw
    b -= lr*db

    if epoch%100 == 0:
        print("loss: ", loss)

y_pred_scaled = x_scaled @ w + b
y_pred_org = y_pred_scaled * y_std + y_mean

print("w: ", w)
print("b: ", b)
print("loss: ", loss)
print("y_pred_org: ", y_pred_org)