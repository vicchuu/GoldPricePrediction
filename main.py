

import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import plotly.io as pio
def startDataPreprocessing(dataset):

    "Printing info about the CSV file"

    #print(dataset.info())#---> Yes there is a null based value lets check what are thevalue which is null and not null


    #lets check with image plotting using mat plot lib
    #plotmyDataset(dataset)
    fillMissingData(dataset) #-->perfect it fill alldata with its mean due to numerical value
    #print(dataset.isnull().sum())

    #print(dataset.describe().to_string())
    #printLowandHigh(dataset)
    return dataset

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor

from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error ,plot_confusion_matrix,accuracy_score
"""I think this model is so good in regression kind of model"""
def findBetterModel(X1,Y1,X2,Y2):
    param={
        'Lasso':{
        'model':Lasso(alpha=0.1),
        'params':{
            'selection':["cyclic","random"]
        }
        },
        # 'logistic_regression': {
        #     'model': LogisticRegression(),
        #     'params': {
        #         'C': [1, 5, 10]
        #     }
        # },
        # 'DecisionTreeRegressor': {
        #     'model': DecisionTreeRegressor(),
        #     'params': {
        #         'criterion': ["squared_error", "absolute_error"],
        #         'splitter': ["best", "rndom"]
        #     }
        # },
        # 'RandomForestRegressor': {
        #
        #     'model': RandomForestRegressor(),
        #     'params': {
        #
        #         'criterion': ["squared_error", "absolute_error", "poisson"],
        #         'max_features': ["sqrt", "log2"]
        #
        #     }
        # },

    }
    ans=[]
    for modelname,modelValue  in param.items():
        #print(modelname)
        #mod = RandomizedSearchCV(modelValue['model'], modelValue['params'],cv=3,return_train_score=False)
        mod = RandomForestRegressor()
       # print(X1[:20],Y1.shape)
        mod.fit(X1,Y1)
        pred = mod.predict(X2)
        Score = (accuracy_score(Y2,pred))
        print(Score)
        #ans.append(mod.best_params_)

    return ans



def printLowandHigh(dataset):

    for a in dataset.columns:
        if a !="Date":
            print("************************")
            print("Country for Gold price :",a)
            maxi = max(dataset[a])
            index1 = (dataset[dataset[a]==maxi].index)
            month = dataset["Date"][index1[0]]
            mini = min(dataset[a])
            index2 = dataset[dataset[a]==mini].index
            mini2 = dataset["Date"][index2[0]]
            print("Maximum value on month is :",month ," Value is :",maxi)
            print("Minimum value is :",mini2,"Value is :",mini)
            print()


def fillMissingData(dataset):

    for a in dataset.columns:
        if dataset[a].isnull().sum()>0:
            dataset[a]=dataset[a].fillna(dataset[a].mean())
    return dataset


def plotmyDataset(dataset):

    pio.templates.default= "plotly_dark"
   # fig = px.line(dataset,x="Date",y="India(INR)",title="INDIAN Gold Price Since 1970")
   # fig = px.bar(dataset[-20:],x="Date",color='Date',y="India(INR)",title="INDIAN Gold Price Since 1970")
    fig = px.bar(dataset[-20:],x="Date",y=["India(INR)","United States(USD)"],hover_data={"Date"},title="Gold rate in various countries")
    fig.show()







from sklearn.model_selection import train_test_split
from datetime import datetime
from sklearn.preprocessing import StandardScaler
if __name__ == "__main__":

    dataSet_0 = pd.read_csv("1979-2021.csv")
    dataSet_1 = startDataPreprocessing(dataSet_0)
    """for need of time series and to split data into year basd we use datetime """

    #dataSet_1['Date'] = dataSet_1['Date'].dt.strftime('%m-%d-%Y')
    #dataSet_1["Date"] = dataSet_1["Date"].apply(
    #     lambda x: datetime.strptime(x, '%d-%m-%Y'))  # according to input we need to add DDMMYY wont work

    month=[]
    year=[]
    for a in dataSet_1["Date"]:
        month.append(int(a[3:5]))
        year.append(int(a[6:]))
        #print(m,y)
    dataSet_1["month"] = month
    dataSet_1["year"] = year
    dataSet_1.drop("Date",axis=1,inplace=True)
    #print(dataSet_1[:100].to_string())
    ax=["month","year"]
    x = dataSet_1[ax]
    y = dataSet_1["India(INR)"]


    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(x)
    #X_test = sc_X.transform(X_test)
    xtrain,xtest,ytrain,ytest = train_test_split(X_train,y,test_size=0.15,random_state=42,shuffle=False)
    print(xtrain.shape,ytrain.shape,xtest.shape,ytest.shape)
    res = findBetterModel(xtrain,ytrain,xtest,ytest)
    # print(res)
