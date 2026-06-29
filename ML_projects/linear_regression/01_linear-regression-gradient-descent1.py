import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

x = (x - np.mean(x))/np.std(x)
y = (y - np.mean(y))/np.std(y)

w = 0.0
b = 0.0
lr = 0.01

#forward pass(prediction)
y_pred = w*x + b

#compute loss (error)
loss = np.mean((y - y_pred)**2)

#backward pass (gradient)

dw = (-2/len(x))*np.sum(x*(y - y_pred))
db = (-2/len(x))*np.sum(y - y_pred)
# -> this means:
#if w is too big -> decrease it & if too small -> increase it.

#update parameters
lr = 0.01

w = w - lr*dw
b = b - lr*db
#lr = learning rate(step size)

#training loop

for i in range(3000):

    #forward
    y_pred = w*x + b

    #loss
    loss = np.mean((y - y_pred)**2)

    #gradients
    dw = (-2/len(x))*np.sum(x*(y - y_pred))
    db = (-2/len(x))*np.sum(y - y_pred)

    #update

    w -= lr*dw
    b -= lr*db

    if i%500 == 0:
        print(loss)

#this is gradient descent


print("w:", w, "b:", b, "loss:", loss)

