import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
x = x.reshape(5,2)
print(x)
print("============")
print(x.size)
for i in range (5):
    print(x[i])

print("============")

x = np.array([1,2,3,4,5,6,7,8,9,10])
print(x)
x = np.append(x,11)
print(x)    
