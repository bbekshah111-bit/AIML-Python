import numpy as np

#step 1: Create  base array

a = np.arange(12).reshape(3, 4)
print("a: ")
print(a)
print("id: ", id(a))
print("base: ", a.base)
print("strides: ", a.strides)
print("C_contiguous: ", a.flags['C_CONTIGUOUS'])
print()

#step 2: create a view (slicing)

b = a[:, :2]  #slice -> usually view
print("b: ")
print(b)
print("base is a: ", b.base is a)
print("strides: ", b.strides)
print("C_contiguous: ", b.flags['C_CONTIGUOUS'])
print()

#step 3: mutate and observe

b[0, 0] = 999

print("after modifying b: ")
print("a: ")
print(a)
print("b: ")
print(b)
print()
# -> if a changes then its a view

#step 4: create a copy (fancy indexing)

c = a[[0, 1]]  # fancy indexing -> copy

print("c: ")
print(c)
print("base: ", c.base)
print("id: ", id(c))

#step 5: mutate copy

c[0, 0] = -1
print("after modifying c: ")
print("a: ")
print(a)
print("c: ")
print(c)
# -> a shouldnot change because its a copy

#step 6: transpose behavour

d = a.T
print("d :")
print(d)
print("base is a:", d.base is a)
print("C_contiguous :", d.flags['C_CONTIGUOUS'],"\n" "F_contiguous :", d.flags['F_CONTIGUOUS'])
print("strides :", d.strides)


#step 7: mutations via transpose

d[0, 0] = 500
print("after modifying d: ")
print("a: ")
print(a)
print("d: ")
print(d)

#step 8: flatten vs ravel

e = a.ravel()
f = a.flatten()

print("ravel base: ", e.base is a)
print("flatten base: ", f.base)

#mutating both
e[0] = 111
f[1] = 222

print("a after ravel mutation: ")
print(a)





