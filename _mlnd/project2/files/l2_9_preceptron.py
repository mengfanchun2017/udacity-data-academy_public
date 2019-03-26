import numpy as np
import pandas as pd
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

# vs报错的处理方法，感觉奇怪，tbc
# include_dirs=[np.get_include()]
import matplotlib as plt

# Read the data.
data = np.asarray(pd.read_csv('l2_9_data.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y. 
X = data[:,0:2]
y = data[:,2]

# 阶跃函数
## 解决的是当点不一致时w和b变化方向的问题
## 如果是
def stepFunction(t):
    if t >= 0:
        return 1
    return 0

# 预测函数
## 对X，W做矩阵乘法，并加上b截距
## 结果使用阶跃函数进行0，1输出的转换
def prediction(X, W, b):
    #np.matmul是矩阵乘法，把未知数X和W系数乘起来
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
    
def perceptronStep(X, y, W, b, learn_rate = 0.0001):
    # 对所有行依次进行计算
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.

def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines

# 后续研究，问问题
trainPerceptronAlgorithm(X, y)

# 执行看没有问题X为x1，x2对应的点，y为分类0，1
# 图出不来，还要继续加画图的代码