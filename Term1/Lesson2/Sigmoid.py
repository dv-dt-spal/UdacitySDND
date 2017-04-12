import numpy as np
#y = f(h) = sigmoid(Summation(weights * input x) + bias)
def sigmoid(x):
    return 1/(1+np.exp(-x))

inputs = np.array([0.2, -0.6])
weights = np.array([0.5, 0.3])
bias = -0.1

output = sigmoid(np.dot(weights,inputs)+bias)

print('Output:')
print(output)
