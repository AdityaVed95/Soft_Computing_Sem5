import numpy as np
import matplotlib.pyplot as plt

def mu_Bad(x):
    if x < 35:
        return 1
    elif 35 <= x < 50:
        return (50-x)/15
    else:
        return 0

def mu_Poor(x):
    if x == 50:
        return 1
    elif 35 <= x < 50:
        return (x-35)/15
    elif 50 <= x < 60:
        return (60-x)/10
    else:
        return 0

def mu_Average(x):
    if 60 <= x < 70:
        return 1
    elif 50 <= x < 60:
        return (x-50)/10
    elif 70 <= x < 80:
        return (80-x)/10
    else:
        return 0

def mu_Good(x):
    if 80 <= x < 90:
        return (90-x)/10
    elif 70 <= x < 80:
        return (x-70)/10
    else:
        return 0

def mu_VeryGood(x):
    if x == 80:
        return 1
    elif 80 <= x < 90:
        return (x-80)/10
    else:
        return 0

def mu_Excellent(x):
    if x >= 90:
        return (x-90)/10
    else:
        return 0

x = np.linspace(0, 100, 400)
y_bad = [mu_Bad(i) for i in x]
y_poor = [mu_Poor(i) for i in x]
y_avg = [mu_Average(i) for i in x]
y_good = [mu_Good(i) for i in x]
y_vgood = [mu_VeryGood(i) for i in x]
y_excellent = [mu_Excellent(i) for i in x]

plt.figure(figsize=(10, 6))
plt.plot(x, y_bad, label="Bad")
plt.plot(x, y_poor, label="Poor")
plt.plot(x, y_avg, label="Average")
plt.plot(x, y_good, label="Good")
plt.plot(x, y_vgood, label="Very Good")
plt.plot(x, y_excellent, label="Excellent")
plt.title("Fuzzy Membership Functions")
plt.xlabel("Marks")
plt.ylabel("Degree of Membership")
plt.legend()
plt.grid(True)
plt.show()
