import numpy as np

def track(name, arr):
    print(f"{name}:")
    print(arr)
    print("id: ", id(arr))
    print("base: ", arr.base is not None)
    print("C_contiguous: ", arr.flags['C_CONTIGUOUS'])
    print("-"* 40)

a = np.arange(10)
track("a", a)

b = a[2:8]
c = [[2, 4, 6]]
d = a.reshape(2,5)

track("b", b)
track("d", d)

b[0] = 100

track("a", a)
track("b", b)

e = d.T
f = e.ravel()

track("e", e)
track("f", f)

f[0] = 99

track("a", a)
track("f", f)

b = a[2:8]
track("b(slice)", b)

c = a[::2]
track("c(step slice)", c)

d = a.reshape(2, 5)
track("d(reshape)", d)

e = d.T
track("e(transpose)", e)