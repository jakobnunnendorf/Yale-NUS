# Introduction to `scikit-learn`

In this notebook we will introduce the `scikit-learn` package for fitting linear models. We will also discuss the advantages of using `scikit-learn` over implementing models yourself using `numpy`.

Scikit-learn, or as the cool kids call it sklearn (pronounced s-k-learn), is an large package of useful machine learning algorithms. For this lecture, we will use the `LinearRegression` model in the [`linear_model`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model) module.  The fact that there is an entire module with many different models within the `linear_model` module might suggest that we have a lot to cover still (we do!).  

**What you should know about `sklearn` models:**

1. Models are created by first building an instance of the model:
```python
model = SuperCoolModelType(args)
```
1. You then fit the model by calling the **fit** function passing in data:
```python
model.fit(df[['X1' 'X2']], df[['Y']])
```
1. You then can make predictions by calling **predict**:
```python
model.predict(df2[['X1' 'X2']])
```

The neat part about sklearn is most models behave like this.  So if you want to try a cool new model you just change the class of mode you are using. 


```python
import pandas as pd
import numpy as np
from seaborn import load_dataset
```

For this notebook, we will use the seaborn `mpg` data set which describes the fuel mileage (measured in miles per gallon, or mpg) of various cars along with characteristics of those cars. Our goal will be to build a model that can predict the fuel mileage of a car based on the characteristics of that car.

This data has some rows with missing data. We will ignore those rows until later for the sake of this lecture. We can use the Pandas DataFrame.isna function to find rows with missing values and drop them.



```python
data = load_dataset("mpg")

# Drop rows with null values for this example
data = data[~data.isna().any(axis=1)]

# Focus on only quantitative terms for this example
data = data.drop(columns=['origin', 'name'])
data.head()
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
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>8</td>
      <td>307.0</td>
      <td>130.0</td>
      <td>3504</td>
      <td>12.0</td>
      <td>70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>8</td>
      <td>350.0</td>
      <td>165.0</td>
      <td>3693</td>
      <td>11.5</td>
      <td>70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>8</td>
      <td>318.0</td>
      <td>150.0</td>
      <td>3436</td>
      <td>11.0</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.0</td>
      <td>8</td>
      <td>304.0</td>
      <td>150.0</td>
      <td>3433</td>
      <td>12.0</td>
      <td>70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.0</td>
      <td>8</td>
      <td>302.0</td>
      <td>140.0</td>
      <td>3449</td>
      <td>10.5</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



## (Out of scope) Fitting linear models using the normal equations

Let's remind ourselves of how we have been fitting models so far.


```python
# Create a column of 1's to represent the intercept term
data['intercept'] = pd.Series(data=[1] * len(data), index=data.index)

# Create the design matrix X and the target vector y
y = data['mpg'].to_numpy()
X = data.drop(columns=['mpg']).to_numpy()

# Fit the model (i.e. set up and solve the normal equations)
theta_hat = np.linalg.inv(X.T @ X) @ (X.T @ y)
theta_hat
```




    array([-3.29859089e-01,  7.67843024e-03, -3.91355574e-04, -6.79461791e-03,
            8.52732469e-02,  7.53367180e-01, -1.45352505e+01])



To make predictions using our model, we use the parameter vector $\hat{\theta}$ as shown below. This effectively means our entire model is captured in the $\hat{\theta}$ vector.


```python
# Make predictions using the model
preds = X @ theta_hat
preds[:10]
```




    array([15.08291904, 14.07257469, 15.53631544, 15.53447451, 15.28640745,
           10.13543367, 10.14518132, 10.2823774 ,  9.75375835, 13.04735326])



## Fitting linear models using `scikit-learn`


```python
# Load a fresh dataset for scikit-learn demo
data = load_dataset("mpg")
data = data[~data.isna().any(axis=1)]
data = data.drop(columns=['origin', 'name'])
data.head()
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
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>8</td>
      <td>307.0</td>
      <td>130.0</td>
      <td>3504</td>
      <td>12.0</td>
      <td>70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>8</td>
      <td>350.0</td>
      <td>165.0</td>
      <td>3693</td>
      <td>11.5</td>
      <td>70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>8</td>
      <td>318.0</td>
      <td>150.0</td>
      <td>3436</td>
      <td>11.0</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.0</td>
      <td>8</td>
      <td>304.0</td>
      <td>150.0</td>
      <td>3433</td>
      <td>12.0</td>
      <td>70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.0</td>
      <td>8</td>
      <td>302.0</td>
      <td>140.0</td>
      <td>3449</td>
      <td>10.5</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



The `scikit-learn` package has many features that are useful for modeling, feature engineering, and more. In this notebook, we will show the functionality `scikit-learn` has for modeling.

To fit an ordinary least squares model using `scikit-learn`, we first have to import the `LinearRegression` [object](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) from `scikit-learn`:


```python
# Import the LinearRegression object, which represents an ordinary least squares model
from sklearn.linear_model import LinearRegression
```

The next step is to create an instance of the LinearRegression object:


```python
# Instantiate a model
model = LinearRegression()
```

Next, we fit our model to the data:


```python
# Create the design matrix X and the target vector y
y = data['mpg']
X = data.drop(columns=['mpg'])

# Fit the model (notice no normal equations!)
model.fit(X, y)
```




    LinearRegression()



Now we can use our model to make predictions:


```python
# Make predictions using the model
model.predict(X)[:10]
```




    array([15.08291904, 14.07257469, 15.53631544, 15.53447451, 15.28640745,
           10.13543367, 10.14518132, 10.2823774 ,  9.75375835, 13.04735326])



What happened to the $\hat{\theta}$ vector? How are we able to make predictions without computing $\hat{\theta}$?

When we fit the model using `model.fit(X, y)`, `scikit-learn` computes and saves $\hat{\theta}$ so that when we do `model.predict(X)`, the model already knows what $\hat{\theta}$ is and can use it to make predictions.

We can even look at the $\hat{\theta}$ vector computed by `model.fit(X, y)`:


```python
model.coef_
```




    array([-3.29859089e-01,  7.67843024e-03, -3.91355574e-04, -6.79461791e-03,
            8.52732469e-02,  7.53367180e-01])



There are only 6 coefficients! What happened to the intercept term?


```python
model.intercept_
```




    -14.535250480506168



By default, `scikit-learn` will add an intercept term to the model for you. This means you don't have to go through the trouble of adding it yourself! This is just one of the many advantages using `scikit-learn` has.

## Advantages of scikit-learn

While this example of an OLS model might not clearly show why `scikit-learn` is preferred over implementing everything yourself using something like `numpy`, there are a few important advantages to using `scikit-learn`:

- using `scikit-learn` abstracts model details (e.g. normal equations)
- consistent interface across models makes it easy to try different models (example below)
- interoperability with other `scikit-learn` features


```python
from sklearn.linear_model import *
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

model_types = [
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet,
    DecisionTreeRegressor
]

for model_type in model_types:
    model = model_type().fit(X, y)
    preds = model.predict(X)
    print(f"{model} RMSE: {mean_squared_error(y, preds, squared=False)}")
```

    LinearRegression() RMSE: 3.4044340177796406
    Ridge() RMSE: 3.404434439176605
    Lasso() RMSE: 3.4249669617779075
    ElasticNet() RMSE: 3.4214869327992687
    DecisionTreeRegressor() RMSE: 0.0

