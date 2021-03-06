#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:28:49 2019

@author: student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("/home/student/Desktop/Data_Aug2019/Python/Programs/Classification/Default_Assignment/Default.csv")
X=dataset.iloc[:,[1,2,3]].values
Y=dataset.iloc[:,0:1].values

from sklearn.preprocessing import LabelEncoder
labelencoder_X=LabelEncoder()
labelencoder_Y=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
Y=labelencoder_Y.fit_transform(Y)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)

d = {}

###1
from sklearn.linear_model import LogisticRegression
classifier1 = LogisticRegression(random_state=0)
#classifier1.fit(X,Y)

from sklearn.model_selection import cross_val_score
score1=cross_val_score(classifier1,X,Y,cv=5)
avg1=np.average(score1)
print("Logistic Regression Score :",avg1)

d["Logistic Regression Score :"] = avg1


###2
from sklearn.svm import SVC
classifier2=SVC(kernel='linear',random_state=0)
#classifier2.fit(X1,Y)

score2=cross_val_score(classifier2,X,Y,cv=5)
avg2=np.average(score2)                 
print("SVR Linear Score:",avg2)    

d["SVR Linear Score:"] = avg2

#####3

from sklearn.svm import SVC
#classifier=SVC(kernel='rbf',random_state=0)
classifier3=SVC(kernel='poly',degree=3,random_state=0) ## by default degree=3
#classifier3.fit(X1,Y)

score3=cross_val_score(classifier3,X,Y,cv=5)
avg3=np.average(score3)                 
print("SVR Kernel(poly) Score:",avg3)    

d["SVR Kernel(poly) Score:"] = avg3

from sklearn.svm import SVC
classifier8=SVC(kernel='rbf',random_state=0)
#classifier3.fit(X1,Y)

score8=cross_val_score(classifier8,X,Y,cv=5)
avg8=np.average(score8)                 
print("SVR Kernel(rbf) Score:",avg8)    

d["SVR Kernel(rbf) Score:"] = avg8

######4

from sklearn.tree import DecisionTreeClassifier
classifier4=DecisionTreeClassifier(criterion='entropy',random_state=0)
#classifier4.fit(X,Y)

score4=cross_val_score(classifier4,X,Y,cv=5)
avg4=np.average(score4)
print("Decesion Tree Score:",avg4)

d["Decesion Tree Score:"] = avg4
#######5
from sklearn.ensemble import RandomForestClassifier
classifier5=RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=0)
#classifier5.fit(X,Y)

score5=cross_val_score(classifier5,X,Y,cv=5)
avg5=np.average(score5)
print("Random Forest Score:",avg5)

d["Random Forest Score:"] = avg5


#####6
from sklearn.neighbors import KNeighborsClassifier
classifier6=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
#classifier6.fit(X1,Y)

from sklearn.model_selection import cross_val_score
score6=cross_val_score(classifier6,X,Y,cv=5)
avg6=np.average(score6)
print("KNN Score:",avg6)
d["KNN Score:"] = avg6


#####7
from sklearn.naive_bayes import GaussianNB
classifier7=GaussianNB()
#classifier7.fit(X,Y)

from sklearn.model_selection import cross_val_score
score7=cross_val_score(classifier7,X,Y,cv=5)
avg7=np.average(score7)
print("Naive Bays Score:",avg7)

d["Naive Bays Score:"] = avg7


m = max(d.values())

for i in d.items():
    if i[1] == m:
        print('-------------------------------------------------------')
        print(i[0],i[1],"Is the best model")