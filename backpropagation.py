import random
import numpy as np
import matplotlib.pyplot as plt
from math import e

file = open("backpropagation_data.txt", "r")
Data = file.readlines()
random.shuffle(Data)
file.close()

# create list of input and output vectors
X, Y = [], []

for data in Data:
    point = data.split('\t')
    X.append([1, float(point[0]), float(point[1])])
    
    if '1' in point[2]: Y.append([1, 0])
    else: Y.append([0, 1])

# parameters
N = len(Data)      # length of the dataset
n, m = 3, 2        # length of appended input vector and output vector
k = 5              # cross-validation factor
size = int(N/k)    # size of a bucket for cross validation
N1 = size          # length of test set
N2 = N - size      # length of training set
max_epoch = 500    # maximum iterations of back propagation
eta = 0.1          # learning factor

# keep the i-th bucket for test and the remaining 
def split_on_bucket(i):
    X_train = X[: size*i] + X[size*(i + 1):]
    X_test = X[size*i : size*(i + 1)]
    Y_train = Y[: size*i] + Y[size*(i + 1):]
    Y_test = Y[size*i : size*(i + 1)]
    return [X_train, Y_train, X_test, Y_test]

# useful functions
def sigmoid(x): 
    return 1/(1 + (e**( (-0.1)*x )))

#inner product of the vectors x and y
def inner_product(x, y):
    d = len(x)
    value = 0
    for i in range(d):
        value += x[i]*y[i]
    return value

# euclidean distance between the vectors x and y scaled to their size
def distance(x, y):
    d = len(x)
    value = 0
    for i in range(d):
        value += (x[i] - y[i])**2
    return value/d

# calculate y-hat corresponding to the machine W
def calculate_y_hat(W, x):
    _y = []
    for w in W:
        _y.append(sigmoid(inner_product(w, x)))
    return _y

# the mean-sqaured-error of the machine W in the testing input-output set X, Y
def error_on_set(X, Y, W):
    L = len(X)
    error = 0
    for i in range(L):
        _y = calculate_y_hat(W, X[i])
        error += distance(_y, Y[i])
    return error/L

# training the machine
def machine(X, Y, max_epoch, eta):
    W = [[1 for j in range(n)] for i in range(m)]
    loss = error_on_set(X, Y, W)
    Loss = [loss]
    epoch = 0
    
    while loss > 0.01 and epoch < max_epoch:
        for l in range(N1):
            x, y = X[l], Y[l]
            _y = calculate_y_hat(W, x)
            
            for i in range(m):
                for j in range(n):
                    # online learning by backpropagation
                    partial = (y[i] - _y[i])*(1 - _y[i])*_y[i]*x[j]
                    W[i][j] += eta * partial
    
        loss = error_on_set(X, Y, W)
        Loss.append(loss)
        epoch += 1
                
    return [W, Loss]

# k-fold cross-validation and learning on the respective buckets
total_error = 0
print("The following errors are obtained in the five fold training and testing on the given data.\n")
print("Bucket - Training Error - Testing error")

for i in range(k):
    data = split_on_bucket(i)
    X_train, Y_train, X_test, Y_test = data[0], data[1], data[2], data[3]
    result = machine(X_train, Y_train, max_epoch, eta)
    W, Loss = result[0], result[1]
    
    training_error = Loss[-1]
    testing_error = error_on_set(X_test, Y_test, W)
    total_error += testing_error
    print("%6d %16f %15f" % (i + 1, training_error, testing_error))

# Plotting decreasing J
t = np.linspace(0, max_epoch, max_epoch + 1)
plt.title("Decreasing Error on a training bucket")
plt.plot(t, Loss)

# Final k-fold error
print("The k-fold (k = 5) estimate of the generalization error is", total_error/5)