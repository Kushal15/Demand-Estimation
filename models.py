#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[2]:


dset1=pd.read_excel('final4.xlsx')


# In[3]:


dset1 = dset1.dropna(axis=0)

dset1


# In[4]:


X = dset1.iloc[:,3:-2]

#X = X.drop(columns='Total Absorption in units')
X


# In[5]:


y = dset1.iloc[:,-2]
y


# In[6]:


from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression


# In[7]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linreg = LinearRegression().fit(X_train_scaled, y_train)

print('linear model coeff (w): {}'
     .format(linreg.coef_))
print('linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))
print('R-squared score (training): {:.3f}'
     .format(linreg.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linreg.score(X_test_scaled, y_test)))


# In[8]:


coeff_df = pd.DataFrame(linreg.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False).head(10)


# In[9]:


from sklearn.linear_model import Ridge
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   random_state = 0)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linridge = Ridge(alpha=0.0).fit(X_train_scaled, y_train)

print('ridge regression linear model intercept: {}'
     .format(linridge.intercept_))
print('ridge regression linear model coeff:\n{}'
     .format(linridge.coef_))
print('R-squared score (training): {:.3f}'
     .format(linridge.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linridge.score(X_test_scaled, y_test)))
print('Number of non-zero features: {}'
     .format(np.sum(linridge.coef_ != 0)))


# In[10]:


coeff_df = pd.DataFrame(linridge.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False).head(10)


# In[11]:


from sklearn.linear_model import Lasso

linlasso = Lasso(alpha=0.1, max_iter = 10000).fit(X_train_scaled, y_train)
print('lasso regression linear model intercept: {}'
     .format(linlasso.intercept_))
print('lasso regression linear model coeff:\n{}'
     .format(linlasso.coef_))
print('Non-zero features: {}'
     .format(np.sum(linlasso.coef_ != 0)))
print('R-squared score (training): {:.3f}'
     .format(linlasso.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}\n'
     .format(linlasso.score(X_test_scaled, y_test)))
print('Features with non-zero weight (sorted by absolute magnitude):')

for e in sorted (list(zip(list(X), linlasso.coef_)),
                key = lambda e: -abs(e[1])):
    if e[1] != 0:
        print('\t{}, {:.3f}'.format(e[0], e[1]))


# In[12]:


coeff_df = pd.DataFrame(linlasso.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False)


# In[13]:


from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor(max_features=50, random_state=0).fit(X_train, y_train)
print('Accuracy of RF classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of RF classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[14]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False)


# In[15]:


from sklearn.ensemble import GradientBoostingRegressor

clf = GradientBoostingRegressor(learning_rate=0.1, random_state=0).fit(X_train, y_train)
print('Accuracy of GBDT classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of GBDT classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[16]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False).head(10)


# # Without absorption columns

# In[17]:


dset2 = dset1.copy()
dset2.columns[49:67]


# In[18]:


dset2 = dset2.drop(columns=dset2.columns[49:67])
dset2


# In[508]:


X = dset2.iloc[:,3:-2]
y = dset2.iloc[:,-2]


# In[510]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linreg = LinearRegression().fit(X_train_scaled, y_train)

print('linear model coeff (w): {}'
     .format(linreg.coef_))
print('linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))
print('R-squared score (training): {:.3f}'
     .format(linreg.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linreg.score(X_test_scaled, y_test)))


# In[21]:


coeff_df = pd.DataFrame(linreg.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False).head(10)


# In[22]:


linridge = Ridge(alpha=0.0).fit(X_train_scaled, y_train)

print('ridge regression linear model intercept: {}'
     .format(linridge.intercept_))
print('ridge regression linear model coeff:\n{}'
     .format(linridge.coef_))
print('R-squared score (training): {:.3f}'
     .format(linridge.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linridge.score(X_test_scaled, y_test)))
print('Number of non-zero features: {}'
     .format(np.sum(linridge.coef_ != 0)))


# In[23]:




coeff_df = pd.DataFrame(linridge.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False).head(10)


# In[24]:


linlasso = Lasso(alpha=0.1, max_iter = 10000).fit(X_train_scaled, y_train)
print('lasso regression linear model intercept: {}'
     .format(linlasso.intercept_))
print('lasso regression linear model coeff:\n{}'
     .format(linlasso.coef_))
print('Non-zero features: {}'
     .format(np.sum(linlasso.coef_ != 0)))
print('R-squared score (training): {:.3f}'
     .format(linlasso.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}\n'
     .format(linlasso.score(X_test_scaled, y_test)))
print('Features with non-zero weight (sorted by absolute magnitude):')

for e in sorted (list(zip(list(X), linlasso.coef_)),
                key = lambda e: -abs(e[1])):
    if e[1] != 0:
        print('\t{}, {:.3f}'.format(e[0], e[1]))


# In[ ]:


print('Lasso regression: effect of alpha regularization\nparameter on number of features kept in final model\n')

for alpha in [0.1, 0.5, 1, 2, 3, 5, 10, 20, 50]:
    linlasso = Lasso(alpha, max_iter = 10000).fit(X_train_scaled, y_train)
    r2_train = linlasso.score(X_train_scaled, y_train)
    r2_test = linlasso.score(X_test_scaled, y_test)
    
    print('Alpha = {:.2f}\nFeatures kept: {}, r-squared training: {:.2f}, r-squared test: {:.2f}\n'
         .format(alpha, np.sum(linlasso.coef_ != 0), r2_train, r2_test))


# In[25]:


coeff_df = pd.DataFrame(linlasso.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False).head(10)


# In[513]:


clf = RandomForestRegressor(max_features=210,random_state=0).fit(X_train, y_train)
print('Accuracy of RF regressor on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of RF regressor on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[514]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False).head(10)


# In[511]:


clf = GradientBoostingRegressor(learning_rate=0.1, random_state=0).fit(X_train, y_train)
print('Accuracy of GBDT regressor on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of GBDT regressor on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[512]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False).head(10)


# In[6]:


dset3 = pd.read_excel('final4.xlsx',parse_dates=['index'])
dset3


# In[7]:


dset3 = dset3.dropna(axis=0)
dset3


# In[79]:


markets = dset3['MicroMarket'].unique()


# In[8]:


get_ipython().run_line_magic('matplotlib', 'notebook')

import matplotlib.pyplot as plt


# In[35]:


from statsmodels.tsa.arima_model import ARIMA


# In[39]:


from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm


# In[155]:


from statsmodels.tsa.vector_ar.vecm import coint_johansen


# In[9]:


markets=['Cenotaph Road', 'Teynampet', 'Ambattur Ind.Estate', 'Aminijkarai',
       'Anna Nagar', 'Balaji Nagar', 'Anna Salai', 'Mahindra World City',
       'Ayanavaram', 'Besant Nagar', 'Chromepet',
       'Purasawalkam', 'Egmore', 'Gopalapuram', 'Kalavakkam',
     'Rajakilpakkam', 'Camp Road', 'Selaiyur',
       'K.K Nagar', 'Kilpauk', 'Medavakkam', 'Kodambakkam',
       'Ottiambakkam', 'Madipakkam', 'Kancheepuram', 'Mandaveli',
       'Mylapore', 'Nandambakam', 'Ramapuram', 'Nanganallur',
       'Nungambakkam', 'Perambur', 'R A Puram', 'MRC Nagar', 'Roya Puram',
       'Royapettah', 'Pudupakkam', 'Saidapet', 'T. Nagar', 'Lakshmipuram',
       'Tambaram', 'Thirumangalam', 'Thiruvanmiyur', 'Neelankarai',
       'Palavakkam', 'Vadapalani', 'Velachery', 'Vepery',
       'Virugambakkam', 'Adyar', 'Indira Nagar', 'Adambakam', 'Padi',
       'Perungudi', 'Tharamani', 'Mogappair', 'Ashok Nagar', 'East Coast Road', 'Sholinganallur',
       'Semmancherry', 'Arasankazhani', 'Uthandi', 'karapakkam',
       'Pallavaram', 'Nanmangalam', 'Keelakattalai', 'Manikandan Nagar',
       'Manimangalam', 'Thoraipakkam', 'Mahabalipuram', 'Porur',
       'Sriperumbudur', 'Thirumullaivoyal', 'Padur', 'Thalambur',
       'Egattur', 'Siruseri SIPCOT', 'Alandur', 'Mambalam', 'Choolaimedu',
       'Tondiarpet', 'Vinayagapuram', 'Saligramam', 'Maraimalai Nagar',
       'Koyambedu', 'Injambakkam', 'Poonamalle', 'Kattupakkam',
       'Madhavaram', 'Kotturpuram', 'Tiruvallur', 'Pallikaranai',
       'Shantosapuram', 'Perumbakkam', 'Guindy', 'Ekkatuthangal',
       'GST Road', 'Urapakkam', 'Padappai', 'Manapakkam',
       'Valasaravakkam', 'Kalpakkam', 'Vayalur', 'Perungalathur',
       'Chengalpattu', 'Kelambakkam', 'Vengaivasal Main RD',
       'Guduvancheri', 'Nellikuppam', 'Minjur', 'NH-5', 'Vanagaram',
       'Maduravoyal', 'Aynambakkam', 'Thiruverkkadu', 'Korattur',
       'Villivakkam', 'Vandalur', 'Nallambakkam', 'Mambakkam',
       'Mannivakkam', 'Ponmar', 'Rathinamangalam', 'Polachery',
       'Mudichur', 'Oragadam', 'Ayappakkam', 'Potheri',
       'Poonamallee High Road', 'Avadi', 'Ambattur', 'Thiruvidandhai',
       'Muttukadu', 'Kovalam', 'Chembarambakkam', 'Thirumudivakkam',
       'Kundrathur', 'Pattabiram', 'Thiruninravur', 'Thirumazhisai',
       'Tiruvottiyur', 'Singaperumal Koil', 'Iyappanthangal', 'Kovur',
       'Mangadu', 'Thiruporur', 'Anakaputhur', 'Kolathur', 'Vedanthangal',
       'Madambakkam', 'Ponneri', 'Perur',
       'Sunguvarchatram', 'Periyapalayam', 'Walajabad', 'Gerugambakkam',
       'Kolapakkam']


# In[10]:


from statsmodels.tsa.vector_ar.var_model import VAR


# In[27]:


pred = pd.DataFrame(columns=['open_stock_units', 'Unsold in units', 'overhang'])
actual = pd.DataFrame(columns=usable)
ls = []


# In[28]:


for mar in markets:
    data = dset3[dset3['MicroMarket']==mar][usable]
    train = data[:int(0.9*(len(data)))][['open_stock_units', 'Unsold in units', 'overhang']]
    valid = data[int(0.9*(len(data))):]
    for i in range(len(valid)):
        ls.append(mar)
    model = VAR(endog=train)
    model_fit = model.fit()
    prediction = model_fit.forecast(model_fit.y, steps=len(valid))
    actual = actual.append(valid,ignore_index=True)
    pred = pred.append(pd.DataFrame(prediction,columns=['open_stock_units', 'Unsold in units', 'overhang']),ignore_index=True)
    
pred['MicroMarket']=ls


# In[34]:


actual['Total Absorption in units'] = (actual['open_stock_units']-actual['Unsold in units'])
actual


# In[40]:


pred['Total Absorption in units'] = (pred['open_stock_units']-pred['Unsold in units'])
pred['Total Absorption in units']=pred['Total Absorption in units'].round()
pred = pred[['MicroMarket', 'open_stock_units', 'Unsold in units', 'overhang', 'Total Absorption in units']]
pred


# In[56]:


rmosu = (((pred['open_stock_units']-actual['open_stock_units'])**2).mean())**.5
print('rmse of open_stock_units: {}'.format(rmosu))


# In[57]:


rmunu = (((pred['Unsold in units']-actual['Unsold in units'])**2).mean())**.5
print('rmse of Unsold in units: {}'.format(rmunu))


# In[58]:


rmov = (((pred['overhang']-actual['overhang'])**2).mean())**.5
print('rmse of overhang: {}'.format(rmov))


# In[59]:


rmtau = (((pred['Total Absorption in units']-actual['Total Absorption in units'])**2).mean())**.5
print('rmse of Total Absorption in units: {}'.format(rmtau))


# In[1]:


usable = ['MicroMarket','open_stock_units', 'Unsold in units', 'overhang']


# In[2]:


usable


# In[60]:


index = ['2020Q2', '2020Q3', '2020Q4', '2021Q1', '2021Q2', '2021Q3', '2021Q4']
forecasted = pd.DataFrame(columns=['open_stock_units', 'Unsold in units', 'overhang'])
locs = []
for mar in markets:
    data = dset3[dset3['MicroMarket']==mar][['open_stock_units', 'Unsold in units', 'overhang']]
    for i in range(0,7):
        locs.append(mar)
    model = VAR(endog=data)
    model_fit = model.fit()
    prediction = model_fit.forecast(model_fit.y, steps=7)
    forecasted = forecasted.append(pd.DataFrame(prediction,columns=['open_stock_units', 'Unsold in units', 'overhang'],index=index))
    


# In[61]:


forecasted['MicroMarket']=locs
forecasted = forecasted[['MicroMarket', 'open_stock_units', 'Unsold in units', 'overhang']]
forecasted['Total Absorption in units'] = forecasted['open_stock_units']-forecasted['Unsold in units']
forecasted


# In[62]:


forecasted.to_excel('Forecast.xlsx')


# In[ ]:




