import numpy as np


class LinearRegressionScratch:
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.w = None
        self.b = None
        self.loss_history = []

    def fit(self, x, y):
        n_samples = x.shape[0]

        # Initialize parameters
        self.w = 0.0
        self.b = 0.0

        # Training loop
        for epoch in range(self.n_iters):

            # Forward pass
            y_pred = self.w * x + self.b

            # Compute gradients
            dw = (-2 / n_samples) * np.sum(x * (y - y_pred))
            db = (-2 / n_samples) * np.sum(y - y_pred)

            # Update parameters
            self.w -= self.lr * dw
            self.b -= self.lr * db

            # Compute loss
            loss = np.mean((y - y_pred) ** 2)
            self.loss_history.append(loss)

    def predict(self, x):
        return self.w * x + self.b


# Dataset
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

# Train model
model = LinearRegressionScratch(lr=0.01, n_iters=1000)
model.fit(x, y)

# Predictions
predictions = model.predict(x)

# Results
print("Weight:", model.w)
print("Bias:", model.b)
print("Predictions:", predictions)
print("Final Loss:", model.loss_history[-1])