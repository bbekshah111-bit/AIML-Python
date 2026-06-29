import numpy as np

a = np.arange(12)
a = a.reshape(3, 4)
a = a.astype(np.float32)
print(a.shape)
print(a.dtype)

b = np.array([1, 2, 3, 4])
print(b.shape)
print(b.dtype)

c = a + b
print(c)
print(c.shape)
print(c.dtype)