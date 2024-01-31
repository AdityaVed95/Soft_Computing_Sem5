import matplotlib.pyplot as plt
import numpy as np

A = {"x1":0.2,"x2":0.3,"x3":0.7,"x4":0.9,"x5":0,"x7":0}
B = {"x1":0.1,"x2":0.2,"x3":0.5,"x4":0,"x5":0.7,"x7":0.3}

# A = {1:0.2,2:0.3,3:0.7,4:0.9,5:0,7:0}
# B = {1:0.1,2:0.2,3:0.5,4:0,5:0.7,7:0.3}

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

# Extract keys and values
labels = list(A.keys())
A_vals = list(A.values())
B_vals = list(B.values())
A_union_B_vals = list(A_union_B.values())
A_intersection_B_vals = list(A_intersection_B.values())
A_complement_vals = list(A_complement.values())
B_complement_vals = list(B_complement.values())

# Set the bar width and positions
bar_width = 0.1
index = np.arange(len(labels))

bar1 = plt.bar(index, A_vals, bar_width, label='A', color='b', align='center')
bar2 = plt.bar(index + bar_width, B_vals, bar_width, label='B', color='r', align='center')
bar3 = plt.bar(index + 2*bar_width, A_union_B_vals, bar_width, label='A union B', color='g', align='center')
bar4 = plt.bar(index + 3*bar_width, A_intersection_B_vals, bar_width, label='A intersection B', color='c', align='center')
bar5 = plt.bar(index + 4*bar_width, A_complement_vals, bar_width, label='A complement', color='m', align='center')
bar6 = plt.bar(index + 5*bar_width, B_complement_vals, bar_width, label='B complement', color='y', align='center')

# Labeling
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Side by side bar chart of A and B')
plt.xticks(index + bar_width / 2, labels)  # Set the position of the x ticks
plt.legend()
plt.show()
