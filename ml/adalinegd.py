#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:51:48 2018

@author: liux
"""

import numpy as np

#Adaline-Gradient descent
class AdalineGD(object):
    """
    eta:float
    学习效率,处于0和1
    
    n_iter:
    对训练数据进行学习改进次数
    
    w_:一维向量
    存储权重数值
    
    errors_:
    存储每次迭代改进时,网络对数据进行错误判断的次数
    """    
    def __init__(self, eta=0.01,n_iter=100):
        self.eta = eta
        self.n_iter = n_iter
        self.errors_ = []
        
    def fit(self, X, y):
        """
        X:二维数组[n_samples, n_features]
        n_samples 表示X中含有训练数据条目数
        n_features 含有4个数据的一维向量,用于表示一条训练条目
        
        y:一维向量
        用于存储每一训练条目对应的正确分类
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, X):
        return self.net_input(X)
    
    def predict(self, X):
        return np.where(self.activation(X) >= 0, 1, -1)
    
    
file = '/home/liux/PycharmProjects/test/ml/iris.data'
import pandas as pd
df = pd.read_csv(file, header=None)
#print(df.head(10))

#view data by graph
import matplotlib.pyplot as plt

y = df.loc[0:99, 4].values
y = np.where(y == 'Iris-setosa', -1 ,1)

X = df.iloc[0:100, [0, 2]].values


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
    

ada = AdalineGD(eta=0.0001, n_iter=200)
ada.fit(X, y)
plot_decision_regions(X, y, classifier=ada)
plt.title('Adaline-Gradient descent')
plt.xlabel('huaban length')
plt.ylabel('huajing length')
plt.legend(loc='upper left')
plt.show()

plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('sum-squard-error')
plt.show()