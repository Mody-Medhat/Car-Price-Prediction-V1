#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Major Libraries
import pandas as pd
import numpy as np


## sklearn -- for pipeline and preprocessing
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn_features.transformers import DataFrameSelector

import os


# In[3]:


## load the data Using 'OS'
FILE_PATH = os.path.join(os.getcwd(),'CarData.csv')
## Read the CSV file using pandas
df = pd.read_csv(FILE_PATH)


# In[4]:


df.columns = df.columns.str.lower().str.replace(' ', '_')
string_columns = list(df.dtypes[df.dtypes == 'object'].index)
for col in string_columns:
    df[col] = df[col].str.lower().str.replace(' ', '_')


# In[5]:


df.rename(columns = {'msrp': 'price'}, inplace = True)


# In[6]:


df['log_price'] = np.log1p(df.price)


# In[7]:


## Split the whole Dataset to Feature & Target
X = df.drop(['price' , 'log_price' ,'popularity' ] , axis=1)
y = df['log_price']


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, shuffle=True, random_state=42)


# In[9]:


## Separete the columns according to type (numerical or categorical)
num_cols = [col for col in X_train.columns if X_train[col].dtype in ['float32', 'float64', 'int32', 'int64']]
categ_cols = [col for col in X_train.columns if X_train[col].dtype not in ['float32', 'float64', 'int32', 'int64']]


# In[10]:


## We can get much much easier like the following
## numerical pipeline
num_pipeline = Pipeline([
                        ('selector', DataFrameSelector(num_cols)),    ## select only these columns
                        ('imputer', SimpleImputer(strategy='median')),
                        ('scaler', StandardScaler())
                        ])

## categorical pipeline
categ_pipeline = Pipeline(steps=[
            ('selector', DataFrameSelector(categ_cols)),    ## select only these columns
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('OHE', OneHotEncoder(sparse=False , handle_unknown='ignore'))])

## concatenate both two pipelines
total_pipeline = FeatureUnion(transformer_list=[
                                            ('num_pipe', num_pipeline),
                                            ('categ_pipe', categ_pipeline)
                                               ]
                             )

X_train_final = total_pipeline.fit_transform(X_train) ## fit


# In[11]:


def preprocess_new(X_new):
    
    X_new.columns = X_new.columns.str.lower().str.replace(' ', '_')
    string_columns = list(X_new.dtypes[X_new.dtypes == 'object'].index)
    
    for col in string_columns:
        X_new[col] = X_new[col].str.lower().str.replace(' ', '_')
        
    return total_pipeline.transform(X_new)

