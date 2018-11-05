# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#define class
import numpy as np
class Perceptron(object):
    """
    eta: 学习率
    n_iter: 训练权重向量的重复次数
    w_: 神经元分叉权重向量
    errors_: 队列,记录神经元对样本预测时错误次数
    """
    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta
        self.n_iter = n_iter
        self.errors_ = []
    
    def fit(self, X, y):
        """
        输入训练数据,培训神经元, X输入向量样本, y对应样本正确分类
        X:shape[n_samples, n_features]
        X:[[1, 2, 3], [4, 5, 6]]
        n_samples:2
        n_features:3
        
        y:[1, -1]
        样本向量[1,2,3]属于分类1
        样本向量[4,5,6]属于分类-1
        """
        
        """
        初始化权重向量为0
        加一是因为前面算法提到的w0,也就是步调函数阈值
        """
        self.w_ = np.zeros(1 + X.shape[1])
        print('fit begin --------')
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                predict_xi = self.predict(xi)
                update = self.eta * (target - predict_xi)
#                print('fit', target, predict_xi, update)
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
                self.errors_.append(errors)
            print(_,len(self.errors_),self.w_[:])
#        print('a',len(self.errors_))
        print('fit end --------')
    
    def net_input(self, X):
        """
        z = W0*1 + W1*X1 + ... + Wn*Xn
        """
        z = np.dot(X, self.w_[1:]) + self.w_[0]
#        print('net_input',z, np.dot(X, self.w_[1:]) ,self.w_[0] ,self.w_[:])
        return z
    
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0 , 1 , -1)
    
#import data
file = '/home/liux/PycharmProjects/test/ml/iris.data'
import pandas as pd
df = pd.read_csv(file, header=None)
#print(df.head(10))

#view data by graph
import matplotlib.pyplot as plt

y = df.loc[0:99, 4].values
y = np.where(y == 'Iris-setosa', -1 ,1)

X = df.iloc[0:100, [0, 2]].values

#plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
#plt.scatter(X[50:100, 0], X[50:100, 1], color='green', marker='+', label='versicolor')
#plt.xlabel('huaban length')
#plt.ylabel('huajing length')
#plt.legend(loc='upper left')
#plt.show()
    
#
ppn=Perceptron(eta = 0.1,n_iter = 10)
ppn.fit(X,y)    
#plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='*')
#print(range(1, len(ppn.errors_) + 1))
#plt.xlabel('Epochs')
#plt.ylabel('error category times')
#plt.show()


#
from matplotlib.colors import ListedColormap
def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('+', 'x', 's', 'o')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    x1_min, x1_max = X[:, 0].min() -1 , X[:, 0].max()
    x2_min, x2_max = X[:, 1].min() -1 , X[:, 1].max()
    
#    print(x1_min, x1_max)
#    print(x2_min, x2_max)
    
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    
#    print(np.arange(x1_min, x1_max, resolution).shape)
#    print(np.arange(x1_min, x1_max, resolution))
#    print(np.arange(x2_min, x2_max, resolution).shape)
#    print(np.arange(x2_min, x2_max, resolution))
#    
#    print()
#    print(xx1.shape, xx1)
#    print(xx2.shape, xx2)
    
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max()) 
    plt.ylim(xx2.min(), xx2.max())
    
    for idx, c1 in enumerate(np.unique(y)):
#        print('---')
#        print(idx, c1)
#        print(X[y==c1,0], X[y==c1, 1])
#        print(cmap(idx), markers[idx])
        plt.scatter(x=X[y==c1, 0], y=X[y==c1, 1], alpha=0.8, c=cmap(idx), 
                    marker=markers[idx], label=c1)
    
    

plot_decision_regions(X, y, ppn, resolution=0.02)
plt.xlabel('huaban length')
plt.ylabel('huajing length')
plt.legend(loc='upper left')
plt.show()
