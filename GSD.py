import math

import numpy as np

x1 = (np.arange(1,11,dtype = int))
print(x1)
x2 = np.asarray(np.random.randint(1,20,len(x1)),dtype=int)
print(x2)
op = np.asarray(np.random.randint(0,2,len(x1)),dtype=int)
print(op)

epoch = 10 * len(x1)
lr =0.01
m1=0
m2=0
c=0
n = float(len(x1))
findmc=[]
findc=[]
for i in range(epoch):

    predy = (m1 *x1)+(m2*x2) +c #D_m = (-2/n) * sum(X * (Y - Y_pred))
    #print("m :",m," c:",c , " index :",i)
    D_m = (-2/n) * (sum(x1* (op-predy))+sum(x2*(op)) )
    D_c = (-2/n) * sum(y1-predy)
    m = m- lr *D_m
    c = c - lr * D_c
    #print((y1-predy),(x1*(y1-predy)),sum(x1* (y1-predy)),(-2/n),D_m)
    #print("D-m :" ,D_m," D_c :",D_c)
    findmc.append(m)
    findc.append(c)

# print("Mx :",findmc)
# print("Min m value :",min(findmc))
# print("Mc :",findc)
# print("Min Coeff value:",min(findc))





print("M :",m,"  c:",c)
predy1=[]
for i in range (len(x1)):
    predy1.append(math.ceil(m*x1[i]+c))

print(predy1)
from sklearn.metrics import accuracy_score,confusion_matrix,mean_absolute_error,explained_variance_score, \
max_error , r2_score,mean_squared_error
print("Accuracy score : ",accuracy_score(y1,predy1))
print("Mean abs error :",mean_absolute_error(y1,predy1))
print("Mean square error :",mean_squared_error(y1,predy1))
print("explained_variance_score :",explained_variance_score(y1,predy1))
print("max_error :",max_error(y1,predy1))
print("R2 score :",r2_score(y1,predy1))