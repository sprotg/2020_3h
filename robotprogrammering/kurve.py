from math import sin

t_vals = [0.01*i for i in range(0,100)]

A1 = 3
A2 = 3
w1 = 1
w2 = 1
k1 = 0
k2 = 0
phi = 0

x_vals = [A1*sin(w1*t + phi) + k1 for t in t_vals]
y_vals = [A2*sin(w2*t) + k2 for t in t_vals]

for i in range(100):
    print(x_vals[i], y_vals[i])
