import matplotlib.pyplot as plt
import numpy as np

A = {"x1":0.2,"x2":0.3,"x3":0.7,"x4":0.9,"x5":0,"x7":0}
B = {"x1":0.1,"x2":0.2,"x3":0.5,"x4":0,"x5":0.7,"x7":0.3}

A_union_B = {}
A_intersection_B = {}
A_complement = {}
B_complement = {}

for (k1,v1) , (k2,v2) in zip(A.items(),B.items()):
    A_union_B.update({k1:max(v1,v2)})
    A_intersection_B.update({k1:min(v1,v2)})
    A_complement.update({k1:float(format(1-v1,".1f"))})
    B_complement.update({k2:float(format(1-v2,".1f"))})

print("\n\nA is : ",A)   
print("B is : ",B)
print("\nA union B is : ",A_union_B)
print("A intersection B is : ",A_intersection_B)
print("A Complement is : ",A_complement)
print("B Complement is : ",B_complement)