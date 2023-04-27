```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
```

## Bias- Variance Plot


```python
train = pd.read_csv('train.csv')
train
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.127868</td>
      <td>4.695017</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.427134</td>
      <td>1.184627</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.168831</td>
      <td>4.671386</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-4.940390</td>
      <td>1.758916</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-5.792271</td>
      <td>2.064704</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.255292</td>
      <td>0.624571</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.744530</td>
      <td>0.971312</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9.070997</td>
      <td>7.444385</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-3.064917</td>
      <td>1.483040</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.959275</td>
      <td>1.423652</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (6, 4), dpi = 100)
sns.scatterplot(x = 'x', y = 'y', data = train)
```




    <Axes: xlabel='x', ylabel='y'>




    
![png](Bias%20Variance-demo_files/Bias%20Variance-demo_3_1.png)
    



```python
from sklearn.linear_model import LinearRegression
```


```python
def polynomial_design_matrix(X, n):
    polynomial_features = np.empty(shape = (X.shape[0], n))
    for i in range(1, n + 1):
        polynomial_features[:, i - 1] = X**i
    return polynomial_features
```


```python
# up to second order polynomial
polynomial_design_matrix(train['x'], 2)
```




    array([[ 7.12786780e+00,  5.08064994e+01],
           [-1.42713404e+00,  2.03671157e+00],
           [ 7.16883095e+00,  5.13921372e+01],
           [-4.94038991e+00,  2.44074524e+01],
           [-5.79227110e+00,  3.35504045e+01],
           [ 2.55292364e-01,  6.51741910e-02],
           [-7.44529526e-01,  5.54324215e-01],
           [ 9.07099700e+00,  8.22829865e+01],
           [-3.06491740e+00,  9.39371865e+00],
           [ 1.95927485e+00,  3.83875794e+00]])




```python
# up to third order polynomial
polynomial_design_matrix(train['x'], 3)
```




    array([[ 7.12786780e+00,  5.08064994e+01,  3.62142011e+02],
           [-1.42713404e+00,  2.03671157e+00, -2.90666042e+00],
           [ 7.16883095e+00,  5.13921372e+01,  3.68421543e+02],
           [-4.94038991e+00,  2.44074524e+01, -1.20582332e+02],
           [-5.79227110e+00,  3.35504045e+01, -1.94333039e+02],
           [ 2.55292364e-01,  6.51741910e-02,  1.66384733e-02],
           [-7.44529526e-01,  5.54324215e-01, -4.12710745e-01],
           [ 9.07099700e+00,  8.22829865e+01,  7.46388724e+02],
           [-3.06491740e+00,  9.39371865e+00, -2.87909717e+01],
           [ 1.95927485e+00,  3.83875794e+00,  7.52118189e+00]])




```python
# up to fourth order polynomial
polynomial_design_matrix(train['x'], 4)
```




    array([[ 7.12786780e+00,  5.08064994e+01,  3.62142011e+02,
             2.58130038e+03],
           [-1.42713404e+00,  2.03671157e+00, -2.90666042e+00,
             4.14819403e+00],
           [ 7.16883095e+00,  5.13921372e+01,  3.68421543e+02,
             2.64115176e+03],
           [-4.94038991e+00,  2.44074524e+01, -1.20582332e+02,
             5.95723734e+02],
           [-5.79227110e+00,  3.35504045e+01, -1.94333039e+02,
             1.12562965e+03],
           [ 2.55292364e-01,  6.51741910e-02,  1.66384733e-02,
             4.24767517e-03],
           [-7.44529526e-01,  5.54324215e-01, -4.12710745e-01,
             3.07275336e-01],
           [ 9.07099700e+00,  8.22829865e+01,  7.46388724e+02,
             6.77048987e+03],
           [-3.06491740e+00,  9.39371865e+00, -2.87909717e+01,
             8.82419500e+01],
           [ 1.95927485e+00,  3.83875794e+00,  7.52118189e+00,
             1.47360625e+01]])




```python
plt.figure(figsize = (6, 4), dpi = 100)
ax = sns.scatterplot(x = 'x', y = 'y', data = train)

# n = 1
n = 1
model = LinearRegression(fit_intercept = True)
X_poly = polynomial_design_matrix(train['x'], n)
model.fit(X_poly, train['y'])
rmse = np.sqrt(np.mean((model.predict(X_poly) - train['y'])**2))

x_to_plot = np.arange(-10, 10.1, .1)
x_to_plot_poly = polynomial_design_matrix(x_to_plot, n)
fitted_line = x_to_plot_poly @ model.coef_ + model.intercept_
ax = sns.lineplot(x = x_to_plot, y = fitted_line, ax = ax, lw = 2/3)
ax.set_ylim(0, 9)
ax.set_xlim(-10, 10);

rmse
```




    1.2506895836230856




    
![png](Bias%20Variance-demo_files/Bias%20Variance-demo_9_1.png)
    



```python
plt.figure(figsize = (6, 4), dpi = 100)
ax = sns.scatterplot(x = 'x', y = 'y', data = train)

# n = 2
n = 2
model = LinearRegression(fit_intercept = True)
X_poly = polynomial_design_matrix(train['x'], n)
model.fit(X_poly, train['y'])
rmse = np.sqrt(np.mean((model.predict(X_poly) - train['y'])**2))

x_to_plot = np.arange(-10, 10.1, .1)
x_to_plot_poly = polynomial_design_matrix(x_to_plot, n)
fitted_line = x_to_plot_poly @ model.coef_ + model.intercept_
ax = sns.lineplot(x = x_to_plot, y = fitted_line, ax = ax, lw = 2/3)
ax.set_ylim(0, 9)
ax.set_xlim(-10, 10);

rmse
```




    0.25538584218499394




    
![png](Bias%20Variance-demo_files/Bias%20Variance-demo_10_1.png)
    



```python
plt.figure(figsize = (6, 4), dpi = 100)
ax = sns.scatterplot(x = 'x', y = 'y', data = train)

# n = 3
n = 3
model = LinearRegression(fit_intercept = True)
X_poly = polynomial_design_matrix(train['x'], n)
model.fit(X_poly, train['y'])
rmse = np.sqrt(np.mean((model.predict(X_poly) - train['y'])**2))

x_to_plot = np.arange(-10, 10.1, .1)
x_to_plot_poly = polynomial_design_matrix(x_to_plot, n)
fitted_line = x_to_plot_poly @ model.coef_ + model.intercept_
ax = sns.lineplot(x = x_to_plot, y = fitted_line, ax = ax, lw = 2/3)
ax.set_ylim(0, 9)
ax.set_xlim(-10, 10);

rmse
```




    0.1470270907185259




    
![png](Bias%20Variance-demo_files/Bias%20Variance-demo_11_1.png)
    



```python
plt.figure(figsize = (6, 4), dpi = 100)
ax = sns.scatterplot(x = 'x', y = 'y', data = train)

# n = 4
n = 4
model = LinearRegression(fit_intercept = True)
X_poly = polynomial_design_matrix(train['x'], n)
model.fit(X_poly, train['y'])
rmse = np.sqrt(np.mean((model.predict(X_poly) - train['y'])**2))

x_to_plot = np.arange(-10, 10.1, .1)
x_to_plot_poly = polynomial_design_matrix(x_to_plot, n)
fitted_line = x_to_plot_poly @ model.coef_ + model.intercept_
ax = sns.lineplot(x = x_to_plot, y = fitted_line, ax = ax, lw = 2/3)
ax.set_ylim(0, 9)
ax.set_xlim(-10, 10);

rmse
```




    0.14614304364333908




    
![png](Bias%20Variance-demo_files/Bias%20Variance-demo_12_1.png)
    



```python
plt.figure(figsize = (6, 4), dpi = 100)
ax = sns.scatterplot(x = 'x', y = 'y', data = train)

n = 9
model = LinearRegression(fit_intercept = True)
X_poly = polynomial_design_matrix(train['x'], n)
model.fit(X_poly, train['y'])
rmse = np.sqrt(np.mean((model.predict(X_poly) - train['y'])**2))

x_to_plot = np.arange(-10, 10.1, .1)
x_to_plot_poly = polynomial_design_matrix(x_to_plot, n)
fitted_line = x_to_plot_poly @ model.coef_ + model.intercept_
ax = sns.lineplot(x = x_to_plot, y = fitted_line, ax = ax, lw = 2/3)
ax.set_ylim(0, 9)
ax.set_xlim(-10, 10);

rmse
```




    2.0178334331880716e-09




    
![png](Bias%20Variance-demo_files/Bias%20Variance-demo_13_1.png)
    



```python
rmses = []
for n in range(1, 10):
    model = LinearRegression(fit_intercept = True)
    X_poly = polynomial_design_matrix(train['x'], n)
    model.fit(X_poly, train['y'])
    rmse = np.sqrt(np.mean((model.predict(X_poly) - train['y'])**2))
    print(n, rmse)
    rmses.append(rmse)
```

    1 1.2506895836230856
    2 0.25538584218499394
    3 0.1470270907185259
    4 0.1461430436433391
    5 0.13854530489262498
    6 0.07189482017386772
    7 0.02014778411746283
    8 0.01470039669407801
    9 2.0178334331880716e-09



```python
# unseen data
test = pd.read_csv('test.csv')
test.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.868099</td>
      <td>1.026507</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-4.432612</td>
      <td>1.655747</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.509648</td>
      <td>1.256400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.895523</td>
      <td>4.313916</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-9.905623</td>
      <td>2.784235</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize = (6,4), dpi = 100)
ax = sns.scatterplot(x = train['x'], y = train['y'], s = 10, color = 'red', zorder = 10)
ax = sns.scatterplot(x = test['x'], y = test['y'], s = 3, zorder = 1)

n = 9
model = LinearRegression(fit_intercept = True)
X_poly = polynomial_design_matrix(train['x'], n)
model.fit(X_poly, train['y'])

x_to_plot_poly = polynomial_design_matrix(x_to_plot, n)
fitted_line = x_to_plot_poly @ model.coef_ + model.intercept_
ax = sns.lineplot(x = x_to_plot, y = fitted_line, lw = 2/3, color = 'green')
ax.set_xlim(-10, 10)
ax.set_ylim(0, 9)

X_test_poly = polynomial_design_matrix(test['x'], n)
test_rmse = np.sqrt(np.mean((model.predict(X_test_poly) - test['y'])**2))
test_rmse
```




    110.77107755821397




    
![png](Bias%20Variance-demo_files/Bias%20Variance-demo_16_1.png)
    



```python
test_rmses = []
for n in range(1, 10):
    model = LinearRegression(fit_intercept = True)
    X_poly = polynomial_design_matrix(train['x'], n)
    model.fit(X_poly, train['y'])
    X_test_poly = polynomial_design_matrix(test['x'], n)
    test_rmse = np.sqrt(np.mean((model.predict(X_test_poly) - test['y'])**2))
    print(n, test_rmse)
    test_rmses.append(test_rmse)
```

    1 1.8585554486548226
    2 0.7713562614108714
    3 0.16912900333224853
    4 0.20723955870790853
    5 1.2974799641185821
    6 8.7751290607739
    7 13.649732852497458
    8 27.66658854987569
    9 110.77107755821397



```python

```
