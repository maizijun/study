import numpy as np
import pandas as pd 

from sklearn import svm

x1 = np.random.normal(loc=4,scale=2,size=100)
x2 = np.random.normal(loc=-1,scale=1,size=100)

X = pd.DataFrame(x1,columns=['x1'])
X['x2'] = x2
X['y'] = X['x1']**2 + 1/2*X['x2'] +  1/10*X['x2']**2

reg = svm.SVR(kernel='poly',degree=2)
# reg = svm.SVR(kernel='rbf')

reg.fit(X[['x1','x2']],X['y'])
X['y_pred'] = reg.predict(X[['x1','x2']])

# print(X.head())

print(X.mean().round(2))
print(np.mean(np.abs(X['y_pred']-X['y'])))


#### note #### 
'''
for svm algorithm, cost function is 

min 1/2*(|w|^2) + C*Σ(i)ζi, and ζ is defined as slack variable
st yi(w*xi+b) >= 1-ζi, ζi >= 0

transforming to Lagrange formula：
min(w)max(α,β) = L(w,α,β) = 1/2*(|w|^2) + C*Σζi - Σ(i)αi(yi(w*xi+b)-1+ζi) - Σ(i)βiζi

according to dual problem,
max(α,β)min(w) = L(w,α,β) = 1/2*(|w|^2) + C*Σζi - Σ(i)αi(yi(w*xi+b)-1+ζi) - Σ(i)βiζi

get derivative from L to w,b,ζ, and set equal to 0
β could be eliminated in contrains

at last we could get a quadratic target about α，so we could get αi in the convex quadnratic problem, so as w and b
and b determines the support vector  

'''
