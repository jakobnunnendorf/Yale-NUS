# Lecture 20



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from scipy.optimize import minimize
import sklearn.linear_model as lm

# plt.rcParams['figure.figsize'] = (4, 4)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['lines.linewidth'] = 3
sns.set()
```


```python
df = pd.read_csv('nba.csv')
```


```python
df["WON"] = df["WL"]
df["WON"] = df["WON"].replace("W", 1)
df["WON"] = df["WON"].replace("L", 0)
```


```python
one_team = df.groupby("GAME_ID").first()
opponent = df.groupby("GAME_ID").last()
games = one_team.merge(opponent, left_index = True, right_index = True, suffixes = ["", "_OPP"])
games["FG_PCT_DIFF"] = games["FG_PCT"] - games["FG_PCT_OPP"]
games['WON'] = games['WL'].replace('L', 0).replace('W', 1)
games = games[['TEAM_NAME', 'MATCHUP', 'WON', 'FG_PCT_DIFF']]
```


```python
bins = pd.cut(games["FG_PCT_DIFF"], 20)
games["bin"] = [(b.left + b.right) / 2 for b in bins]
win_rates_by_bin = games.groupby("bin")["WON"].mean()
```


```python
def sigma(t):
    return 1 / (1 + np.exp(-t))
```

## Logistic Regression with Squared Loss

We've chosen a model. It's now time to choose a loss function. Why not squared loss?


```python
def mse_loss_single_arg_nba(theta):
    x = games["FG_PCT_DIFF"]
    y_obs = games["WON"]
    y_hat = sigma(x * theta)
    return np.mean((y_hat - y_obs) ** 2)  
```


```python
thetas = np.linspace(-50, 50, 100)
plt.plot(thetas, [mse_loss_single_arg_nba(theta) for theta in thetas])
plt.ylabel('MSE')
plt.xlabel(r'$\theta$');
```


    
![png](Lec20-demo_files/Lec20-demo_9_0.png)
    



```python
minimize(mse_loss_single_arg_nba, x0 = 0)
```




      message: Optimization terminated successfully.
      success: True
       status: 0
          fun: 0.14105789850974032
            x: [ 2.913e+01]
          nit: 7
          jac: [-8.788e-06]
     hess_inv: [[ 1.272e+04]]
         nfev: 24
         njev: 12




```python
minimize(mse_loss_single_arg_nba, x0 = 500)
```




      message: Optimization terminated successfully.
      success: True
       status: 0
          fun: 0.1410573027635218
            x: [ 2.925e+01]
          nit: 1
          jac: [-1.239e-06]
     hess_inv: [[1]]
         nfev: 54
         njev: 27




```python
plt.plot(win_rates_by_bin, 'r', linewidth = 5);
x = win_rates_by_bin.index
plt.plot(x, sigma(x * 29.13), 'black', linewidth = 5);
plt.xlabel('FG_PCT_DIFF')
plt.ylabel('WON');
```


    
![png](Lec20-demo_files/Lec20-demo_12_0.png)
    


So squared loss worked just fine here. But that won't always be the case! Consider this manufacturered example.


```python
rand_x = np.array([[-0.04185564],
       [ 0.12799961],
       [-0.09528101],
       [-0.0058139 ],
       [ 0.0870956 ]])

rand_y = np.array([[0],
       [0],
       [1],
       [0],
       [1]])
```


```python
plt.plot(rand_x, rand_y, 'b*')
plt.xlabel('x')
plt.ylabel('y');
```


    
![png](Lec20-demo_files/Lec20-demo_15_0.png)
    



```python
def mse_loss_single_arg_toy(theta):
    x = rand_x
    y_obs = rand_y
    y_hat = sigma(x * theta)
    return np.mean((y_obs - y_hat)**2)
```


```python
mse_loss_single_arg_toy(10)
```




    0.3226572801334151



Let's plot the loss surface for this toy data using squared loss with the model $\hat{y} = \sigma(\theta x)$, where $\theta$ and $x$ are both scalars.


```python
thetas = np.linspace(-1000, 1000, 100)
plt.plot(thetas, [mse_loss_single_arg_toy(theta) for theta in thetas])
plt.ylabel(r'MSE($\theta$)')
plt.xlabel(r'$\theta$');
```


    
![png](Lec20-demo_files/Lec20-demo_19_0.png)
    


This loss surface is not convex! Depending on where we start our optimization search, we'll end up with different results. Let's explore with `scipy.optimize.minimize`.


```python
best_theta = minimize(mse_loss_single_arg_toy, x0 = 0)["x"][0]
best_theta
```




    -4.801981341432673




```python
plt.plot(rand_x, rand_y, 'b*')
xs = np.linspace(-1, 1, 100)
plt.plot(xs, sigma(xs * best_theta), color='orange')
plt.xlabel('x')
plt.legend(['$y$', '$\hat{y}$']);
```


    
![png](Lec20-demo_files/Lec20-demo_22_0.png)
    



```python
best_theta_2 = minimize(mse_loss_single_arg_toy, x0 = 500)["x"][0]
best_theta_2
```




    500.0




```python
plt.plot(rand_x, rand_y, 'b*')
xs = np.linspace(min(rand_x), max(rand_x), 100)
plt.plot(xs, sigma(xs * best_theta_2), color='orange')
plt.xlabel('x')
plt.legend(['$y$', '$\hat{y}$']);
```


    
![png](Lec20-demo_files/Lec20-demo_24_0.png)
    


Not only is it not convex, leading to the weird issues above, but squared loss just isn't well-suited for a probability task. Since $\hat{y_i}$ is between 0 and 1, and $y_i$ is either 0 or 1, the squared loss for a single point $(y_i - \hat{y_i})^2$ is bounded between 0 and 1.

What this means in practice: even if our prediction is terrible, the squared loss is never that large.


```python
y_hat = np.arange(0.001, 0.999, 0.01)
loss = (1 - y_hat)**2
plt.plot(y_hat, loss, color='k')
plt.xlabel('$\hat{y}$: Predicted Chance of Correct Class')
plt.ylabel('$(1 - \hat{y})^2$')
plt.title('Squared Loss for One Individual');
```


    
![png](Lec20-demo_files/Lec20-demo_26_0.png)
    


## Motivating Cross-Entropy Loss

Let's look at a new loss, called the log loss, for when our true observation is 1.


```python
y_hat = np.arange(0.001, 0.999, 0.01)
loss = -np.log(y_hat)
plt.plot(y_hat, loss, color='k')
plt.xlabel('$\hat{y}$: Predicted Chance of Correct Class')
plt.ylabel('$-\log(\hat{y})$')
plt.title('Log Loss for one observation when $y = 1$');
```


    
![png](Lec20-demo_files/Lec20-demo_29_0.png)
    


We can see that this penalizes wrong predictions far more than squared loss does.

How to read this plot: Suppose the observation we're trying to predict is actually in class 1. If our model gives an 80% chance of being in class 1, the loss is relatively small (around 0.25). 

If we give only a 40% of being in class 1, the loss is larger (around 1).

If we give only a 5% chance of being in class 1, the loss is 3.

And if we give a 0% chance of being in class 1, the loss is infinite.

What about when the true observation is 0?


```python
y_hat = np.arange(0.001, 0.999, 0.01)
loss = -np.log(1 - y_hat)
plt.plot(y_hat, loss, color='k')
plt.xlabel('$\hat{y}$: Predicted Chance of Correct Class')
plt.ylabel('$-\log(1 - \hat{y})$')
plt.title('Log Loss for one observation when $y = 0$');
```


    
![png](Lec20-demo_files/Lec20-demo_31_0.png)
    


Much of the formal derivation is in the slides. But the equation for cross-entropy loss for a single observation is

$$\textrm{loss} = -y \log(\hat{y}) - (1-y)\log(1-\hat{y})$$

For us, since $\hat{y} = \sigma(x^T \theta)$, the expression for average cross-entropy loss is

$$R(\theta) = -\frac{1}{n} \sum_{i = 1}^n \big(y_i \log (\sigma(\mathbb{X}_i^T \theta)) + (1 - y_i) \log (1 - \sigma(\mathbb{X}_i^T \theta))\big)$$

Let's look at the loss surface for average cross-entropy loss, on our toy data from before.


```python
def cross_entropy(y, yhat):
    return - y * np.log(yhat) - (1 - y) * np.log(1 - yhat)
```


```python
def mce_loss_single_arg_toy(theta):
    x = rand_x
    y_obs = rand_y
    y_hat = sigma(x * theta)
    return np.mean(cross_entropy(y_obs, y_hat))
```


```python
thetas = np.linspace(-1000, 1000, 100)
plt.plot(thetas, [mce_loss_single_arg_toy(theta) for theta in thetas], color = 'green')
plt.ylabel(r'Mean Cross-Entropy($\theta$)')
plt.xlabel(r'$\theta$');
```

    /var/folders/w7/5j9sp5kd0nv96pdk3dvg9wt00000gq/T/ipykernel_47372/529625363.py:2: RuntimeWarning:
    
    divide by zero encountered in log
    
    /var/folders/w7/5j9sp5kd0nv96pdk3dvg9wt00000gq/T/ipykernel_47372/529625363.py:2: RuntimeWarning:
    
    invalid value encountered in multiply
    



    
![png](Lec20-demo_files/Lec20-demo_35_1.png)
    



```python
best_theta_mce = minimize(mce_loss_single_arg_toy, x0 = 0)["x"][0]
best_theta_mce
```




    -5.213601516313596



We see the resulting optimal $\hat{\theta}$ is slightly different than the one that minimized MSE:


```python
best_theta
```




    -4.801981341432673



And lastly, we can determine the $\hat{\theta}$ that minimizes mean cross-entropy loss for our NBA dataset from earlier:


```python
def mce_loss_single_arg_nba(theta):
    x = games["FG_PCT_DIFF"]
    y_obs = games["WON"]
    y_hat = sigma(theta * x)
    return np.mean(cross_entropy(y_obs, y_hat))
```


```python
best_theta_mce_nba = minimize(mce_loss_single_arg_nba, x0 = 0)["x"][0]
best_theta_mce_nba
```




    30.578808323155144



Again, this is different than the $\hat{\theta}$ that minimizes mean squared error for the NBA dataset:


```python
minimize(mse_loss_single_arg_nba, x0 = 0)["x"][0]
```




    29.130078012616185



## Predicting Probabilities

We can manually call `scipy.optimize.minimize` to determine the model parameters that minimize average cross-entropy loss, as we did above. We can then predict probabilities.


```python
best_theta_mce_nba = minimize(mce_loss_single_arg_nba, x0 = 0)["x"][0]
best_theta_mce_nba
```




    30.578971781696595




```python
def predict_probabilities(X, theta):
    return sigma(X * theta)
```


```python
predict_probabilities(games['FG_PCT_DIFF'], best_theta_mce_nba)
```




    GAME_ID
    21700001    0.182669
    21700002    0.834890
    21700003    0.285494
    21700004    0.777946
    21700005    0.783184
                  ...   
    21701226    0.996919
    21701227    0.891866
    21701228    0.627111
    21701229    0.059968
    21701230    0.048978
    Name: FG_PCT_DIFF, Length: 1230, dtype: float64



Once again, `scikit-learn` can do this for us.

The `lm.LogisticRegression` model is what we want to use here. In order to recreate our specific model, there are a few parameters we need to set:
- `penalty = 'none'`: by default, `lm.LogisticRegression` uses regularization. This is generally a good idea, but we haven't yet covered regularization with logistic regression.
- `fit_intercept = False`: our toy model does not currently have an intercept term.
- `solver = 'lbgfs'`: need to specify a numerical optimization routine for the model (similar to gradient descent). `lbfgs` is one such type, and it's the new default in `scikit-learn`.


```python
model = lm.LogisticRegression(penalty = 'none', fit_intercept = False, solver = 'lbfgs')
```


```python
model.fit(games[['FG_PCT_DIFF']], games['WON'])
```

    /opt/homebrew/lib/python3.11/site-packages/sklearn/linear_model/_logistic.py:1173: FutureWarning:
    
    `penalty='none'`has been deprecated in 1.2 and will be removed in 1.4. To keep the past behaviour, set `penalty=None`.
    





<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LogisticRegression(fit_intercept=False, penalty=&#x27;none&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegression</label><div class="sk-toggleable__content"><pre>LogisticRegression(fit_intercept=False, penalty=&#x27;none&#x27;)</pre></div></div></div></div></div>



We can see that the optimal theta (here there's just one, because our model only has one feature) found via `scikit-learn` is the same that we found manually before. (Small deviations due to numerical precision issues.)


```python
model.coef_
```




    array([[30.57950163]])




```python
best_theta_mce_nba
```




    30.578808323155144



`scikit-learn` has a built-in `.predict_proba` method that allows us to get the predicted probabilities under our model.


```python
model.predict_proba([[0.1]])
```

    /opt/homebrew/lib/python3.11/site-packages/sklearn/base.py:439: UserWarning:
    
    X does not have valid feature names, but LogisticRegression was fitted with feature names
    





    array([[0.04487548, 0.95512452]])



This is saying that if `FG_PCT_DIFF = 0.1`, that is, if you shoot 10% better than your opponent, there is a 95.5% chance you will win.

We can also apply this to our entire training set at once.


```python
model.predict_proba(games[['FG_PCT_DIFF']])
```




    array([[0.81733506, 0.18266494],
           [0.16510648, 0.83489352],
           [0.71450899, 0.28549101],
           ...,
           [0.37288695, 0.62711305],
           [0.94003495, 0.05996505],
           [0.95102413, 0.04897587]])




```python
model.predict_proba(games[['FG_PCT_DIFF']])[:, 1]
```




    array([0.18266494, 0.83489352, 0.28549101, ..., 0.62711305, 0.05996505,
           0.04897587])



These values are the same as we computed manually above, as well!


```python
predict_probabilities(games['FG_PCT_DIFF'], best_theta_mce_nba)
```




    GAME_ID
    21700001    0.182670
    21700002    0.834888
    21700003    0.285495
    21700004    0.777945
    21700005    0.783183
                  ...   
    21701226    0.996919
    21701227    0.891865
    21701228    0.627110
    21701229    0.059969
    21701230    0.048979
    Name: FG_PCT_DIFF, Length: 1230, dtype: float64



## Making Classifications

`scikit-learn` also has an in-built `.predict` method. Let's see what it does:


```python
model.predict(games[['FG_PCT_DIFF']])
```




    array([0, 1, 0, ..., 1, 0, 0])



How did it come up with these 1s and 0s?
