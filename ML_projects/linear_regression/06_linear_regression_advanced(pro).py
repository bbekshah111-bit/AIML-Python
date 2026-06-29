import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionPro:
    def __init__(self, lr=0.01, n_iters=3000, lambda_=0.0):
        self.lr = lr
        self.n_iters = n_iters
        self.lambda_ = lambda_  # L2 (Ridge) regularization strength

        self.w = None
        self.b = None

        self.loss_history = []

    def _initialize_params(self, n_features):
        self.w = np.zeros(n_features)
        self.b = 0.0

    def _compute_loss(self, y, y_pred):
        mse = np.mean((y - y_pred) ** 2)
        reg = self.lambda_ * np.sum(self.w ** 2)
        return mse + reg

    def fit(self, x, y):

        # Ensure 2D input
        if x.ndim == 1:
            x = x.reshape(-1, 1)

        n_samples, n_features = x.shape

        self._initialize_params(n_features)

        self.loss_history = []

        for epoch in range(self.n_iters):

            # Prediction
            y_pred = np.dot(x, self.w) + self.b

            # Gradients
            dw = (-2 / n_samples) * np.dot(x.T, (y - y_pred)) + 2 * self.lambda_ * self.w
            db = (-2 / n_samples) * np.sum(y - y_pred)

            # Update
            self.w -= self.lr * dw
            self.b -= self.lr * db

            # Loss
            loss = self._compute_loss(y, y_pred)
            self.loss_history.append(loss)

    def predict(self, x):

        if self.w is None:
            raise ValueError("Model has not been fitted yet.")

        if x.ndim == 1:
            x = x.reshape(-1, 1)

        return np.dot(x, self.w) + self.b

    def r2_score(self, y_true, y_pred):
        ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
        ss_residual = np.sum((y_true - y_pred) ** 2)

        return 1 - (ss_residual / ss_total)

    def evaluate(self, x, y):
        y_pred = self.predict(x)

        return {
            "MSE": np.mean((y - y_pred) ** 2),
            "R2": self.r2_score(y, y_pred)
        }

    def plot_loss(self):
        plt.figure(figsize=(6, 4))
        plt.plot(self.loss_history)
        plt.title("Training Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.grid(True)
        plt.show()


# ---------------- Example ----------------

x = np.array([2, 4, 8, 10, 12], dtype=float)
y = np.array([5, 9, 17, 21, 25], dtype=float)

model = LinearRegressionPro()

model.fit(x, y)

predictions = model.predict(x)

print("Weight:", model.w)
print("Bias:", model.b)
print("Predictions:", predictions)
print("Metrics:", model.evaluate(x, y))

model.plot_loss()