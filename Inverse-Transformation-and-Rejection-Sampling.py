import numpy as np
import random
from matplotlib import pyplot as plt
# Experiment 2

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
iterations = 30000
length = iterations

def inverse_cdf(u):
    return u ** 0.5

total_Xa = 0
average_Xa = 0

for i in range(1, iterations + 1):
    u = random.random()
    xa = inverse_cdf(u)

    U.append(u)
    Xa.append(xa)

    #calculating the total and average of Xa
    total_Xa += xa
    average_Xa = total_Xa / i

    av_Xa.append(average_Xa)

#calculating the variance of Xa
square_of_differences_of_Xa = 0
for j in range(1,length + 1):

    #by the formula:
    #var = (sum of (Xi - avXi)^2) / (n-1)
    square_of_differences_of_Xa += (Xa[j-1] - av_Xa[j-1])**2

    var_Xa = square_of_differences_of_Xa / j
    vr_Xa.append(var_Xa)

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))
plt.show()
# Plot the average and variance values.
### YOUR CODE HERE ###

x_values_Xa = range(len(Xa))
# Plotting Average Xa
plt.figure()
plt.plot(x_values_Xa, av_Xa, label='Average Xa')
plt.legend()
plt.grid()

# Plotting variance of Xa
plt.figure()
plt.plot(x_values_Xa, vr_Xa, label='Variance of Xa')
plt.legend()
plt.grid()

plt.show()


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.

def rejection_method(x):
    return x * 2

#0 <= x <= 1 
a = 0
b = 1

#simulating
for i in range(1, iterations + 1):

    #0 <= x < 1
    xb = random.random()
    yb = rejection_method(b) * random.random()
    if yb <= rejection_method(xb):
        Xb.append(xb)

total_Xb = 0
for i in range(1, len(Xb)+1):
    #calculating the total and average of Xb
    total_Xb += Xb[i-1]
    average_Xb = total_Xb / i

    av_Xb.append(average_Xb)

#calculating the variance of Xb
square_of_differences_of_Xb = 0
for j in range(1,(len(Xb) + 1)):

    #by the formula:
    #var = (sum of (Xi - avXi)^2) / (n-1)
    square_of_differences_of_Xb += (Xb[j-1] - av_Xb[j-1])**2

    var_Xb = square_of_differences_of_Xb / j
    vr_Xb.append(var_Xb)


# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
x_values_avXb = range(len(av_Xb))
# Plotting Average Xb
plt.figure()
plt.plot(x_values_avXb, av_Xb, label='Average Xb')
plt.legend()
plt.grid()

x_values_vrXb = range(len(vr_Xb))
# Plotting variance of Xb
plt.figure()
plt.plot(x_values_vrXb, vr_Xb, label='Variance of Xb')
plt.legend()
plt.grid()

plt.show()