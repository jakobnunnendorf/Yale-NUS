# Lecture 18

## Cross Validation and Regularization

In this section we will work through the train test-split and the process of cross validation.  

## Imports

As with other notebooks we will use the same set of standard imports.


```python
import numpy as np
import pandas as pd
```


```python
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
#import cufflinks as cf
#cf.set_config_file(offline=True, sharing=False, theme='ggplot');
```


```python
from sklearn.linear_model import LinearRegression
```

## The Data

For this notebook, we will use the seaborn `mpg` dataset which describes the fuel mileage (measured in miles per gallon or mpg) of various cars along with characteristics of those cars.  Our goal will be to build a model that can predict the fuel mileage of a car based on the characteristics of that car.


```python
from seaborn import load_dataset
data = load_dataset("mpg")
data
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
      <th>origin</th>
      <th>name</th>
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
      <td>usa</td>
      <td>chevrolet chevelle malibu</td>
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
      <td>usa</td>
      <td>buick skylark 320</td>
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
      <td>usa</td>
      <td>plymouth satellite</td>
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
      <td>usa</td>
      <td>amc rebel sst</td>
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
      <td>usa</td>
      <td>ford torino</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>393</th>
      <td>27.0</td>
      <td>4</td>
      <td>140.0</td>
      <td>86.0</td>
      <td>2790</td>
      <td>15.6</td>
      <td>82</td>
      <td>usa</td>
      <td>ford mustang gl</td>
    </tr>
    <tr>
      <th>394</th>
      <td>44.0</td>
      <td>4</td>
      <td>97.0</td>
      <td>52.0</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
      <td>europe</td>
      <td>vw pickup</td>
    </tr>
    <tr>
      <th>395</th>
      <td>32.0</td>
      <td>4</td>
      <td>135.0</td>
      <td>84.0</td>
      <td>2295</td>
      <td>11.6</td>
      <td>82</td>
      <td>usa</td>
      <td>dodge rampage</td>
    </tr>
    <tr>
      <th>396</th>
      <td>28.0</td>
      <td>4</td>
      <td>120.0</td>
      <td>79.0</td>
      <td>2625</td>
      <td>18.6</td>
      <td>82</td>
      <td>usa</td>
      <td>ford ranger</td>
    </tr>
    <tr>
      <th>397</th>
      <td>31.0</td>
      <td>4</td>
      <td>119.0</td>
      <td>82.0</td>
      <td>2720</td>
      <td>19.4</td>
      <td>82</td>
      <td>usa</td>
      <td>chevy s-10</td>
    </tr>
  </tbody>
</table>
<p>398 rows × 9 columns</p>
</div>



This data has some rows with missing data. We will ignore those rows until later for the sake of this lecture. We can use the Pandas `DataFrame.isna` function to find rows with missing values and drop them, although of course, this is not always the best idea!


```python
data = data[~data.isna().any(axis=1)].copy()
```

### Using SKLearn

We can use the `train_test_split` function from `sklearn.model_selection` to do this easily.


```python
from sklearn.model_selection import train_test_split
```


```python
tr, te = train_test_split(data, test_size = 0.1,random_state=83)
```


```python
len(tr), len(te)
```




    (352, 40)




```python
tr.head()
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
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>14.0</td>
      <td>8</td>
      <td>454.0</td>
      <td>220.0</td>
      <td>4354</td>
      <td>9.0</td>
      <td>70</td>
      <td>usa</td>
      <td>chevrolet impala</td>
    </tr>
    <tr>
      <th>352</th>
      <td>29.9</td>
      <td>4</td>
      <td>98.0</td>
      <td>65.0</td>
      <td>2380</td>
      <td>20.7</td>
      <td>81</td>
      <td>usa</td>
      <td>ford escort 2h</td>
    </tr>
    <tr>
      <th>47</th>
      <td>19.0</td>
      <td>6</td>
      <td>250.0</td>
      <td>100.0</td>
      <td>3282</td>
      <td>15.0</td>
      <td>71</td>
      <td>usa</td>
      <td>pontiac firebird</td>
    </tr>
    <tr>
      <th>39</th>
      <td>14.0</td>
      <td>8</td>
      <td>400.0</td>
      <td>175.0</td>
      <td>4464</td>
      <td>11.5</td>
      <td>71</td>
      <td>usa</td>
      <td>pontiac catalina brougham</td>
    </tr>
    <tr>
      <th>304</th>
      <td>37.3</td>
      <td>4</td>
      <td>91.0</td>
      <td>69.0</td>
      <td>2130</td>
      <td>14.7</td>
      <td>79</td>
      <td>europe</td>
      <td>fiat strada custom</td>
    </tr>
  </tbody>
</table>
</div>




```python
te.head()
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
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>87</th>
      <td>13.0</td>
      <td>8</td>
      <td>350.0</td>
      <td>145.0</td>
      <td>3988</td>
      <td>13.0</td>
      <td>73</td>
      <td>usa</td>
      <td>chevrolet malibu</td>
    </tr>
    <tr>
      <th>279</th>
      <td>29.5</td>
      <td>4</td>
      <td>98.0</td>
      <td>68.0</td>
      <td>2135</td>
      <td>16.6</td>
      <td>78</td>
      <td>japan</td>
      <td>honda accord lx</td>
    </tr>
    <tr>
      <th>319</th>
      <td>31.3</td>
      <td>4</td>
      <td>120.0</td>
      <td>75.0</td>
      <td>2542</td>
      <td>17.5</td>
      <td>80</td>
      <td>japan</td>
      <td>mazda 626</td>
    </tr>
    <tr>
      <th>173</th>
      <td>24.0</td>
      <td>4</td>
      <td>119.0</td>
      <td>97.0</td>
      <td>2545</td>
      <td>17.0</td>
      <td>75</td>
      <td>japan</td>
      <td>datsun 710</td>
    </tr>
    <tr>
      <th>148</th>
      <td>26.0</td>
      <td>4</td>
      <td>116.0</td>
      <td>75.0</td>
      <td>2246</td>
      <td>14.0</td>
      <td>74</td>
      <td>europe</td>
      <td>fiat 124 tc</td>
    </tr>
  </tbody>
</table>
</div>



## Building A Basic Model

Let's go through the process of building a model. Let's start by looking at the raw quantitative features available. We will first use just our own feature function (as we did in previous lectures). This function will just extract the quantitative features we can use for our model.


```python
def basic_design_matrix(df):
    X = df[["cylinders", "displacement", 
          "horsepower", "weight", "acceleration", "model_year"]]
    return X

basic_design_matrix(tr)
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
      <th>6</th>
      <td>8</td>
      <td>454.0</td>
      <td>220.0</td>
      <td>4354</td>
      <td>9.0</td>
      <td>70</td>
    </tr>
    <tr>
      <th>352</th>
      <td>4</td>
      <td>98.0</td>
      <td>65.0</td>
      <td>2380</td>
      <td>20.7</td>
      <td>81</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6</td>
      <td>250.0</td>
      <td>100.0</td>
      <td>3282</td>
      <td>15.0</td>
      <td>71</td>
    </tr>
    <tr>
      <th>39</th>
      <td>8</td>
      <td>400.0</td>
      <td>175.0</td>
      <td>4464</td>
      <td>11.5</td>
      <td>71</td>
    </tr>
    <tr>
      <th>304</th>
      <td>4</td>
      <td>91.0</td>
      <td>69.0</td>
      <td>2130</td>
      <td>14.7</td>
      <td>79</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>394</th>
      <td>4</td>
      <td>97.0</td>
      <td>52.0</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
    </tr>
    <tr>
      <th>258</th>
      <td>6</td>
      <td>231.0</td>
      <td>105.0</td>
      <td>3380</td>
      <td>15.8</td>
      <td>78</td>
    </tr>
    <tr>
      <th>297</th>
      <td>5</td>
      <td>183.0</td>
      <td>77.0</td>
      <td>3530</td>
      <td>20.1</td>
      <td>79</td>
    </tr>
    <tr>
      <th>23</th>
      <td>4</td>
      <td>121.0</td>
      <td>113.0</td>
      <td>2234</td>
      <td>12.5</td>
      <td>70</td>
    </tr>
    <tr>
      <th>83</th>
      <td>4</td>
      <td>98.0</td>
      <td>80.0</td>
      <td>2164</td>
      <td>15.0</td>
      <td>72</td>
    </tr>
  </tbody>
</table>
<p>352 rows × 6 columns</p>
</div>



Then we fit a `scikit-learn` `LinearRegression` model to our training data.


```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```


```python
model.fit(basic_design_matrix(tr), tr['mpg'])
```




<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>



To evaluate the error we will use the **Root Mean Squared Error (RMSE)** which is like the mean squared error but in the correct units (mpg) instead of (mpg^2). 


```python
def rmse(y, yhat):
    return np.sqrt(np.mean((y - yhat)**2))
```

The training error is:


```python
Y_hat = model.predict(basic_design_matrix(tr))
Y = tr['mpg']
print("Training Error (RMSE):", rmse(Y, Y_hat))
```

    Training Error (RMSE): 3.3745826999424584


Oh no! We just used the test data to evaluate our model! We shouldn't have done that.  

(Don't worry, this is only for demonstration purposes. But seriously, don't try this at home.)  

**Notice:** The test error is slightly higher than the training error. This is typically (but not always) the case. Sometimes we get lucky and the test data is "easier to predict" or happens to closely follow the training data.

## Cross-Validation

#### Keeping track of all the models.

In this notebook we will want to keep track of all our models. 

We store our model settings in a dictionary. The key is some identifying name, and the value is a 2-element tuple, with the first element being the transformation function (e.g. `basic_design_matrix`), and the second element being an empty model object (e.g. `LinearRegression()`).


```python
models = {"quant": (basic_design_matrix, LinearRegression())}
```

### More Feature Transformations

As in previous lecture, we might want to look at the displacement per cylinder as well.


```python
def dispcyl_design_matrix(df):
    X = basic_design_matrix(df)
    X['displacement/cylinder'] = X['displacement'] / X['cylinders']
    return X

dispcyl_design_matrix(tr)
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
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>displacement/cylinder</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>454.0</td>
      <td>220.0</td>
      <td>4354</td>
      <td>9.0</td>
      <td>70</td>
      <td>56.750000</td>
    </tr>
    <tr>
      <th>352</th>
      <td>4</td>
      <td>98.0</td>
      <td>65.0</td>
      <td>2380</td>
      <td>20.7</td>
      <td>81</td>
      <td>24.500000</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6</td>
      <td>250.0</td>
      <td>100.0</td>
      <td>3282</td>
      <td>15.0</td>
      <td>71</td>
      <td>41.666667</td>
    </tr>
    <tr>
      <th>39</th>
      <td>8</td>
      <td>400.0</td>
      <td>175.0</td>
      <td>4464</td>
      <td>11.5</td>
      <td>71</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>304</th>
      <td>4</td>
      <td>91.0</td>
      <td>69.0</td>
      <td>2130</td>
      <td>14.7</td>
      <td>79</td>
      <td>22.750000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>394</th>
      <td>4</td>
      <td>97.0</td>
      <td>52.0</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
      <td>24.250000</td>
    </tr>
    <tr>
      <th>258</th>
      <td>6</td>
      <td>231.0</td>
      <td>105.0</td>
      <td>3380</td>
      <td>15.8</td>
      <td>78</td>
      <td>38.500000</td>
    </tr>
    <tr>
      <th>297</th>
      <td>5</td>
      <td>183.0</td>
      <td>77.0</td>
      <td>3530</td>
      <td>20.1</td>
      <td>79</td>
      <td>36.600000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>4</td>
      <td>121.0</td>
      <td>113.0</td>
      <td>2234</td>
      <td>12.5</td>
      <td>70</td>
      <td>30.250000</td>
    </tr>
    <tr>
      <th>83</th>
      <td>4</td>
      <td>98.0</td>
      <td>80.0</td>
      <td>2164</td>
      <td>15.0</td>
      <td>72</td>
      <td>24.500000</td>
    </tr>
  </tbody>
</table>
<p>352 rows × 7 columns</p>
</div>



We can build a linear model using the same quantitative features as before, but with this new "displacement per cylinder" feature.


```python
model = LinearRegression()
model.fit(dispcyl_design_matrix(tr), tr['mpg'])

models['quant+dc'] = (dispcyl_design_matrix, LinearRegression())
```


```python
Y_hat = model.predict(dispcyl_design_matrix(tr))
Y = tr['mpg']
print("Training Error (RMSE):", rmse(Y, Y_hat))
```

    Training Error (RMSE): 3.033309344625912


Our training error is definitely lower than with the previous model, but what we really care about is the model's performance on new data. But we shouldn't actually ever look at the test data. Instead, to compare these models, we can use cross-validation to "mimic" the train-test split.

In the following function we use the sklearn `KFold` cross validation class. 

Here we define a five fold cross validation with 

```python 
five_fold = KFold(n_splits=5)
```

Then we loop over the 5 splits and get the indicies (`tr_ind`) in the training data to use for training and the indices (`va_ind`) in the training data to use for validation:

```python
for tr_ind, te_ind in five_fold.split(tr):
```


```python
from sklearn.model_selection import KFold
from sklearn.base import clone

def cross_validate_rmse(phi_function, model):
    model = clone(model)
    five_fold = KFold(n_splits = 5, random_state = 100, shuffle = True)
    rmse_values = []
    for tr_ind, va_ind in five_fold.split(tr):
        
        X_train = phi_function(tr.iloc[tr_ind, :])
        y_train = tr['mpg'].iloc[tr_ind]
        X_val = phi_function(tr.iloc[va_ind, :])
        y_val = tr['mpg'].iloc[va_ind]
        
        model.fit(X_train, y_train)
        
        rmse_values.append(rmse(y_val, model.predict(X_val)))
        
    return np.mean(rmse_values)

```

Valiating the model


```python
cross_validate_rmse(dispcyl_design_matrix, LinearRegression())
```




    3.111315976504573



The following helper function generates a plot comparing all the models in the `transformations` dictionary.


```python
def compare_models(models):
    
    # Compute the training error for each model
    training_rmse = []
    for transformation, model in models.values():
        model = clone(model)
        model.fit(transformation(tr), tr['mpg'])
        training_rmse.append(rmse(tr['mpg'], model.predict(transformation(tr))))
    
    # Compute the cross validation error for each model
    validation_rmse = [cross_validate_rmse(transformation, model) for transformation, model in models.values()]
    
    names = list(models.keys())
    fig = go.Figure([
        go.Bar(x = names, y = training_rmse, name="Training RMSE"),
        go.Bar(x = names, y = validation_rmse, name="CV RMSE")])
    return fig
```


```python
fig = compare_models(models)
fig.update_yaxes(range = [0, 4], title = "RMSE")
```


<div>                            <div id="51a5d593-2c72-4cea-b353-1be4ac0727fb" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("51a5d593-2c72-4cea-b353-1be4ac0727fb")) {                    Plotly.newPlot(                        "51a5d593-2c72-4cea-b353-1be4ac0727fb",                        [{"name":"Training RMSE","x":["quant","quant+dc"],"y":[3.3745826999424584,3.033309344625912],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc"],"y":[3.4559015156162536,3.111315976504573],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('51a5d593-2c72-4cea-b353-1be4ac0727fb');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


So not only did the new displacement / cylinders feature improve our training error, it also improved our cross-validation error. This indicates that this feature helps our model generalize, or in other words, that it has "predictive power."

Now let's try adding some categorical data, such as the `origin` column. As this is categorical data, we will have to one-hot encode this variable.


```python
data['origin'].value_counts()
```




    usa       245
    japan      79
    europe     68
    Name: origin, dtype: int64



Fortunately, it looks like we have only three possible values for `origin`. We will use `scikit-learn`'s one-hot encoder to do the transformation. Check out Lecture 16 for a refresher on how this works.


```python
from sklearn.preprocessing import OneHotEncoder
oh_enc = OneHotEncoder()
oh_enc.fit(data[['origin']])

def origin_design_matrix(df):
    X = dispcyl_design_matrix(df)
    ohe_cols = pd.DataFrame(oh_enc.transform(df[['origin']]).todense(), 
                           columns = oh_enc.get_feature_names_out(),
                           index = df.index)
    return X.join(ohe_cols)

models['quant+dc+o'] = (origin_design_matrix, LinearRegression())

origin_design_matrix(tr)
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
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>displacement/cylinder</th>
      <th>origin_europe</th>
      <th>origin_japan</th>
      <th>origin_usa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>454.0</td>
      <td>220.0</td>
      <td>4354</td>
      <td>9.0</td>
      <td>70</td>
      <td>56.750000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>352</th>
      <td>4</td>
      <td>98.0</td>
      <td>65.0</td>
      <td>2380</td>
      <td>20.7</td>
      <td>81</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6</td>
      <td>250.0</td>
      <td>100.0</td>
      <td>3282</td>
      <td>15.0</td>
      <td>71</td>
      <td>41.666667</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>8</td>
      <td>400.0</td>
      <td>175.0</td>
      <td>4464</td>
      <td>11.5</td>
      <td>71</td>
      <td>50.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>304</th>
      <td>4</td>
      <td>91.0</td>
      <td>69.0</td>
      <td>2130</td>
      <td>14.7</td>
      <td>79</td>
      <td>22.750000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>394</th>
      <td>4</td>
      <td>97.0</td>
      <td>52.0</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
      <td>24.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>258</th>
      <td>6</td>
      <td>231.0</td>
      <td>105.0</td>
      <td>3380</td>
      <td>15.8</td>
      <td>78</td>
      <td>38.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>297</th>
      <td>5</td>
      <td>183.0</td>
      <td>77.0</td>
      <td>3530</td>
      <td>20.1</td>
      <td>79</td>
      <td>36.600000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>4</td>
      <td>121.0</td>
      <td>113.0</td>
      <td>2234</td>
      <td>12.5</td>
      <td>70</td>
      <td>30.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>4</td>
      <td>98.0</td>
      <td>80.0</td>
      <td>2164</td>
      <td>15.0</td>
      <td>72</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>352 rows × 10 columns</p>
</div>




```python
fig = compare_models(models)
fig.update_yaxes(range = [0, 4], title = "RMSE")
```


<div>                            <div id="e0c79214-c572-4174-b88d-ca9e066d5ff1" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("e0c79214-c572-4174-b88d-ca9e066d5ff1")) {                    Plotly.newPlot(                        "e0c79214-c572-4174-b88d-ca9e066d5ff1",                        [{"name":"Training RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o"],"y":[3.3745826999424584,3.033309344625912,2.8664339999878297,3.012941172853171],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o"],"y":[3.4559015156162536,3.111315976504573,3.1849476048477237,3.1207285180151905],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('e0c79214-c572-4174-b88d-ca9e066d5ff1');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


It looks like adding these new features about origin didn't really affect our model.

Let's try if we can gain any information from the `name` column. This column contains the make and model of each car. The models are fairly unique, so let's try to extract information about the brand (e.g. `ford`). The following cell shows the top 20 words that appear in this column.


```python
tr['name'].str.split().explode().value_counts().head(20)
```




    ford          44
    chevrolet     37
    plymouth      28
    (sw)          27
    amc           26
    dodge         26
    toyota        22
    datsun        17
    custom        17
    buick         16
    volkswagen    14
    pontiac       14
    oldsmobile    10
    mercury       10
    rabbit        10
    honda         10
    brougham      10
    corolla        9
    mazda          9
    colt           7
    Name: name, dtype: int64



It looks like there is at least one model here (`corolla`), but it does show the most common brands. We will add one column for each of these strings, with a `1` for a specific car indicating that the name of the car contains the string.

Note: In practice, you would use `scikit-learn` or some other package, but we will do this manually just to be explicit about what we're doing.


```python
brands = tr['name'].str.split().explode().value_counts().head(20).index

def brands_design_matrix(df):
    X = origin_design_matrix(df)
    for brand in brands:
        X[brand] = df['name'].str.contains(brand, regex = False).astype(float)
    return X

models['quant+dc+o+b'] = (brands_design_matrix, LinearRegression())

brands_design_matrix(tr)
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
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>displacement/cylinder</th>
      <th>origin_europe</th>
      <th>origin_japan</th>
      <th>origin_usa</th>
      <th>...</th>
      <th>volkswagen</th>
      <th>pontiac</th>
      <th>oldsmobile</th>
      <th>mercury</th>
      <th>rabbit</th>
      <th>honda</th>
      <th>brougham</th>
      <th>corolla</th>
      <th>mazda</th>
      <th>colt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>454.0</td>
      <td>220.0</td>
      <td>4354</td>
      <td>9.0</td>
      <td>70</td>
      <td>56.750000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>352</th>
      <td>4</td>
      <td>98.0</td>
      <td>65.0</td>
      <td>2380</td>
      <td>20.7</td>
      <td>81</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6</td>
      <td>250.0</td>
      <td>100.0</td>
      <td>3282</td>
      <td>15.0</td>
      <td>71</td>
      <td>41.666667</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>8</td>
      <td>400.0</td>
      <td>175.0</td>
      <td>4464</td>
      <td>11.5</td>
      <td>71</td>
      <td>50.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>304</th>
      <td>4</td>
      <td>91.0</td>
      <td>69.0</td>
      <td>2130</td>
      <td>14.7</td>
      <td>79</td>
      <td>22.750000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>394</th>
      <td>4</td>
      <td>97.0</td>
      <td>52.0</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
      <td>24.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>258</th>
      <td>6</td>
      <td>231.0</td>
      <td>105.0</td>
      <td>3380</td>
      <td>15.8</td>
      <td>78</td>
      <td>38.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>297</th>
      <td>5</td>
      <td>183.0</td>
      <td>77.0</td>
      <td>3530</td>
      <td>20.1</td>
      <td>79</td>
      <td>36.600000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>4</td>
      <td>121.0</td>
      <td>113.0</td>
      <td>2234</td>
      <td>12.5</td>
      <td>70</td>
      <td>30.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>4</td>
      <td>98.0</td>
      <td>80.0</td>
      <td>2164</td>
      <td>15.0</td>
      <td>72</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>352 rows × 30 columns</p>
</div>




```python
fig = compare_models(models)
fig.update_yaxes(range = [0, 4], title = "RMSE")
```


<div>                            <div id="b3d8ad23-625c-4afe-a6f6-2fad7c0d4ab4" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("b3d8ad23-625c-4afe-a6f6-2fad7c0d4ab4")) {                    Plotly.newPlot(                        "b3d8ad23-625c-4afe-a6f6-2fad7c0d4ab4",                        [{"name":"Training RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o"],"y":[3.3745826999424584,3.033309344625912,2.8664339999878297,3.012941172853171],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o"],"y":[3.4559015156162536,3.111315976504573,3.1849476048477237,3.1207285180151905],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('b3d8ad23-625c-4afe-a6f6-2fad7c0d4ab4');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


Interesting. Adding the brand information to our design matrix decreased our training error, but it increased our cross-validation error. Looks like we overfit!

## Regularization

In this section we explore the use of regularization techniques to address overfitting.

### Ridge Regression

Ridge regression combines the ridge (L2, Squared) regularization function with the least squares loss.  

$$
\hat{\theta}_\alpha = \arg \min_\theta \left[ \left(\frac{1}{n} \sum_{i=1}^n \left(Y_i -  f_\theta(X_i)\right)^2 \right) + \alpha \sum_{k=1}^d \theta_k^2 \right]
$$
### The Regularization Hyperparameter

The $\alpha$ parameter is our regularization **hyperparameter**. It is a hyperparameter because it is not a model parameter but a choice of how we want to balance fitting the data and "over-fitting". The goal is to find a value of this hyper"parameter to maximize our accuracy on the **test data**. However, **we can't use the test data to make modeling decisions** so we turn to cross validation. The standard way to find the best $\alpha$ is to try a bunch of values and take the one with the lowest cross validation error. 


### Ridge Regression in SK Learn

Both Ridge Regression and Lasso are built-in functions in SKLearn.  Let's start by importing the `Ridge` Regression class which behaves identically to the `LinearRegression` class we used earlier:


```python
from sklearn.linear_model import Ridge
```

Take a look at the documentation.  Notice the regularized loss function. 


```python
Ridge?
```

Instead of just looking at the top 20 brands, let's bag-of-words encode the entire name column.


```python
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(tr['name'])
```




<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-2" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>CountVectorizer()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">CountVectorizer</label><div class="sk-toggleable__content"><pre>CountVectorizer()</pre></div></div></div></div></div>




```python
def name_design_matrix(df):
    X = origin_design_matrix(df)
    X_encoding = pd.DataFrame(
        vectorizer.transform(df['name']).todense(), 
        columns=vectorizer.get_feature_names_out(),
        index = df.index)
    return X.join(X_encoding)

name_design_matrix(tr)
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
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>displacement/cylinder</th>
      <th>origin_europe</th>
      <th>origin_japan</th>
      <th>origin_usa</th>
      <th>...</th>
      <th>volare</th>
      <th>volkswagen</th>
      <th>volvo</th>
      <th>vw</th>
      <th>wagon</th>
      <th>woody</th>
      <th>xe</th>
      <th>yorker</th>
      <th>zephyr</th>
      <th>zx</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>454.0</td>
      <td>220.0</td>
      <td>4354</td>
      <td>9.0</td>
      <td>70</td>
      <td>56.750000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>352</th>
      <td>4</td>
      <td>98.0</td>
      <td>65.0</td>
      <td>2380</td>
      <td>20.7</td>
      <td>81</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>6</td>
      <td>250.0</td>
      <td>100.0</td>
      <td>3282</td>
      <td>15.0</td>
      <td>71</td>
      <td>41.666667</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>8</td>
      <td>400.0</td>
      <td>175.0</td>
      <td>4464</td>
      <td>11.5</td>
      <td>71</td>
      <td>50.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>304</th>
      <td>4</td>
      <td>91.0</td>
      <td>69.0</td>
      <td>2130</td>
      <td>14.7</td>
      <td>79</td>
      <td>22.750000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>394</th>
      <td>4</td>
      <td>97.0</td>
      <td>52.0</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
      <td>24.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>258</th>
      <td>6</td>
      <td>231.0</td>
      <td>105.0</td>
      <td>3380</td>
      <td>15.8</td>
      <td>78</td>
      <td>38.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>297</th>
      <td>5</td>
      <td>183.0</td>
      <td>77.0</td>
      <td>3530</td>
      <td>20.1</td>
      <td>79</td>
      <td>36.600000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>4</td>
      <td>121.0</td>
      <td>113.0</td>
      <td>2234</td>
      <td>12.5</td>
      <td>70</td>
      <td>30.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>4</td>
      <td>98.0</td>
      <td>80.0</td>
      <td>2164</td>
      <td>15.0</td>
      <td>72</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>352 rows × 294 columns</p>
</div>




```python
cross_validate_rmse(name_design_matrix, LinearRegression())
```




    434576644.31252116



Woah, our RMSE is really, really large! 

To get around this, let's try regularization. As we're introducing regularization, let's also standardize our quantitative features:


```python
from sklearn.preprocessing import StandardScaler
quantitative_features = ["cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year"]
scaler = StandardScaler()
scaler.fit(basic_design_matrix(tr[quantitative_features]))
```




<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-3" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>StandardScaler()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-3" type="checkbox" checked><label for="sk-estimator-id-3" class="sk-toggleable__label sk-toggleable__label-arrow">StandardScaler</label><div class="sk-toggleable__content"><pre>StandardScaler()</pre></div></div></div></div></div>




```python
StandardScaler.fit?
```


```python
def name_design_matrix_std(df):
    X = name_design_matrix(df)
    X[quantitative_features] = scaler.transform(X[quantitative_features])
    return X

name_design_matrix_std(tr)
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
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>displacement/cylinder</th>
      <th>origin_europe</th>
      <th>origin_japan</th>
      <th>origin_usa</th>
      <th>...</th>
      <th>volare</th>
      <th>volkswagen</th>
      <th>volvo</th>
      <th>vw</th>
      <th>wagon</th>
      <th>woody</th>
      <th>xe</th>
      <th>yorker</th>
      <th>zephyr</th>
      <th>zx</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>1.452785</td>
      <td>2.426007</td>
      <td>2.916388</td>
      <td>1.580639</td>
      <td>-2.320642</td>
      <td>-1.611836</td>
      <td>56.750000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>352</th>
      <td>-0.874316</td>
      <td>-0.933437</td>
      <td>-1.034011</td>
      <td>-0.720703</td>
      <td>1.862364</td>
      <td>1.351615</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>0.289235</td>
      <td>0.500933</td>
      <td>-0.141986</td>
      <td>0.330873</td>
      <td>-0.175511</td>
      <td>-1.342431</td>
      <td>41.666667</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>1.452785</td>
      <td>1.916429</td>
      <td>1.769498</td>
      <td>1.708880</td>
      <td>-1.426838</td>
      <td>-1.342431</td>
      <td>50.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>304</th>
      <td>-0.874316</td>
      <td>-0.999493</td>
      <td>-0.932065</td>
      <td>-1.012159</td>
      <td>-0.282767</td>
      <td>0.812806</td>
      <td>22.750000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>394</th>
      <td>-0.874316</td>
      <td>-0.942873</td>
      <td>-1.365335</td>
      <td>-1.012159</td>
      <td>3.256700</td>
      <td>1.621020</td>
      <td>24.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>258</th>
      <td>0.289235</td>
      <td>0.321637</td>
      <td>-0.014553</td>
      <td>0.445124</td>
      <td>0.110507</td>
      <td>0.543401</td>
      <td>38.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>297</th>
      <td>-0.292540</td>
      <td>-0.131322</td>
      <td>-0.728174</td>
      <td>0.619998</td>
      <td>1.647851</td>
      <td>0.812806</td>
      <td>36.600000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>-0.874316</td>
      <td>-0.716394</td>
      <td>0.189338</td>
      <td>-0.890913</td>
      <td>-1.069316</td>
      <td>-1.611836</td>
      <td>30.250000</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>-0.874316</td>
      <td>-0.933437</td>
      <td>-0.651714</td>
      <td>-0.972521</td>
      <td>-0.175511</td>
      <td>-1.073026</td>
      <td>24.500000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>352 rows × 294 columns</p>
</div>




```python
from sklearn.linear_model import RidgeCV
```


```python
RidgeCV?
```


```python
# 5-fold CV
models['quant+dc+o+n-RidgeCV-5fold'] = (name_design_matrix_std, RidgeCV(alphas = np.arange(0.1,1,10),cv = 5))
```


```python
fig = compare_models(models)
fig.update_yaxes(range = [0, 4], title = "RMSE")
```


<div>                            <div id="c849ea9f-ea0c-42a9-9e24-dcc40ccc456f" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("c849ea9f-ea0c-42a9-9e24-dcc40ccc456f")) {                    Plotly.newPlot(                        "c849ea9f-ea0c-42a9-9e24-dcc40ccc456f",                        [{"name":"Training RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o","quant+dc+o+n-RidgeCV-5fold"],"y":[3.3745826999424584,3.033309344625912,2.8664339999878297,3.012941172853171,1.361429699934418],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o","quant+dc+o+n-RidgeCV-5fold"],"y":[3.4559015156162536,3.111315976504573,3.1849476048477237,3.1207285180151905,3.31785241963314],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('c849ea9f-ea0c-42a9-9e24-dcc40ccc456f');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


### Lasso Regression

Lasso regression combines the absolute (L1) regularization function with the least squares loss.  

$$
\hat{\theta}_\alpha = \arg \min_\theta \left(\frac{1}{n} \sum_{i=1}^n \left(Y_i -  f_\theta(X_i)\right)^2 \right) + \alpha \sum_{k=1}^d |\theta_k|
$$

Lasso is actually an acronym (and a cool name) which stands for Least Absolute Shrinkage and Selection Operator.  It is an absolute operator because it is the absolute value.  It is a shrinkage operator because it favors smaller parameter values.  It is a selection operator because it has the peculiar property of pushing parameter values all the way to zero thereby selecting the remaining features.  It is this last property that makes Lasso regression so useful. By using Lasso regression and setting sufficiently large value of $\alpha$ you can eliminate features that are not informative. 

Unfortunately, there is no closed form solution for Lasso regression and so iterative optimization algorithms like gradient descent are typically used. 


```python
from sklearn.linear_model import Lasso, LassoCV
```


```python
LassoCV?
```


```python
models['quant+dc+o+n-LassoCV'] = (name_design_matrix_std,  LassoCV(alphas = np.arange(0.1,1,0.1), cv = 5))
```


```python
fig = compare_models(models)
fig.update_yaxes(range = [0, 4], title = "RMSE")
```


<div>                            <div id="f1ac23ff-6901-4e57-9a9f-bed31c503aa7" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("f1ac23ff-6901-4e57-9a9f-bed31c503aa7")) {                    Plotly.newPlot(                        "f1ac23ff-6901-4e57-9a9f-bed31c503aa7",                        [{"name":"Training RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o","quant+dc+o+n-RidgeCV-5fold","quant+dc+o+n-LassoCV"],"y":[3.3745826999424584,3.033309344625912,2.8664339999878297,3.012941172853171,1.361429699934418,3.168824941431058],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc","quant+dc+o+b","quant+dc+o","quant+dc+o+n-RidgeCV-5fold","quant+dc+o+n-LassoCV"],"y":[3.4559015156162536,3.111315976504573,3.1849476048477237,3.1207285180151905,3.31785241963314,3.3056111838502],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('f1ac23ff-6901-4e57-9a9f-bed31c503aa7');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


Let's compare the distribution of the parameters for both the `RidgeCV` and `LassoCV` models.


```python
model = RidgeCV()
model.fit(name_design_matrix_std(tr), tr['mpg'])
ridge_coef = model.coef_

model = LassoCV()
model.fit(name_design_matrix_std(tr), tr['mpg'])
lasso_coef = model.coef_
```


```python
ff.create_distplot([ridge_coef, lasso_coef], ["Ridge", "Lasso"], bin_size = 0.1)
```


<div>                            <div id="394b4b1f-19a3-4c6b-97c6-f31058a00a4f" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("394b4b1f-19a3-4c6b-97c6-f31058a00a4f")) {                    Plotly.newPlot(                        "394b4b1f-19a3-4c6b-97c6-f31058a00a4f",                        [{"autobinx":false,"histnorm":"probability density","legendgroup":"Ridge","marker":{"color":"rgb(31, 119, 180)"},"name":"Ridge","opacity":0.7,"x":[-3.99306919368233,5.037703251896069,-0.8618254501203131,-3.518143500093341,-0.4246938571387098,2.681282201468191,-0.30531458316843896,0.225470866298231,-0.10313995513768215,-0.12233091116054062,0.1980254740367647,-0.12096923597827285,-1.0307349960082024,0.16054616663688848,0.18853639551109955,-0.5453464132844311,2.5605928944992438,0.5680348391887868,-0.08841057029679074,1.2472505317253375,-2.160230765395618,-1.0677409849345936,-0.7364849429177451,-0.28112098997789636,-0.4882475060999198,-0.1425576133235897,0.1691084509360443,-2.0529875860314046,-0.22818313515560246,1.6303535359653587,0.8247284958343394,0.6917671103465695,0.6339733263643443,2.786627284213715,1.6999498733488676,0.2176394169838952,-0.4585414989724577,-1.8837289958894594,1.7836060122605069,-1.7389733928317812,-0.40243166247786455,0.6134325242990762,2.004331221154762,0.9351900064124458,0.6522049111168239,-2.4074597277499925,-0.39265252407870394,-0.005285919488866073,1.3906261964441549,-1.1616037424271637,0.8189254155613295,1.0215379890426113,-2.637221932716584,0.9361208196448293,-0.04223649969157739,-1.9565464961934331,0.24985779224650795,-2.315030515160257,1.6026187321074647,-2.329852832342274,-0.01831941436676659,1.2373129436137094,-2.1630547161835643,0.3874297846724441,0.4948673663634461,0.4341785024692798,0.3968312310257145,-1.1540100751195967,-1.0653725203822604,-0.4275049160295889,-1.3657494493721067,-0.368479476200124,-1.3560032393828272,1.916141048296885,0.4341785024692798,0.5744090048161632,-0.7771061917846339,0.40558274892243196,0.23064206609333193,-1.8974790844937957,0.46121366395995816,1.3590820283499632,-0.11806189831151974,-0.062336117496393395,-0.07435451646712286,-2.8553645595291415,0.3873635587264386,1.0392987593975593,-0.1614882993239033,-0.48985938741573953,-0.9368997009385195,0.15097206177047623,2.1509718272368006,2.381501788404273,0.729890873878227,0.4611998508370523,-0.5850812205330833,-0.5766478514315909,-0.0842736723450091,-0.7326296025054808,0.779962075729646,0.10732084989935053,0.5339684840239793,0.33179740827534043,0.9623797379288901,-1.409136254108555,-1.2291494337633997,0.14425910823946358,0.4331713596424655,0.5838555717902595,0.3158534049890076,-0.3478909774726338,0.6189045066996242,-1.0726914056625207,-0.741705924962981,-0.12408193154471454,-0.1106003528374088,-0.39265252407870394,-0.5487481018650975,1.9467143014388553,0.8742526670258126,-2.098105545298266,0.9757650198915024,-0.698037888742613,-0.8464642645194409,1.685698860552264,-0.01831941436676659,-0.10760176154622614,7.682175323566998,0.16796990200654802,0.4482517885924341,-0.1999958575078007,1.7942833919555785,1.226615287265604,0.8071214607482923,1.169760812638818,0.6339733263643443,0.41649375308346515,-0.30428774746211307,-1.68166757656904,1.0989302571807134,-0.6205092991725667,1.1145049284259971,2.3325865177493905,0.215452013264411,-0.6986593516108979,1.0936996724139487,0.9974315786160914,-1.407430307520337,1.235917856700818,0.47996983491565054,-1.426249199291498,4.00672085831785,-0.3223283046640506,-1.4404328017367907,-0.19442500937051288,0.3417978238286872,-2.107840844595967,-0.48985938741573953,1.9572274502485816,2.1115971524615564,-0.7683885279644251,2.012642208218853,0.5680348391887868,1.192123079471266,1.878765026912756,-0.05006793217813388,-1.1465662192600896,0.30000372094512257,1.6319378655424295,0.5095374822855244,-1.5520388924207411,0.26364822358941364,-1.2075031029262813,-2.1400776378362782,0.8045344667769887,-2.098181170511385,0.15322260147561373,-1.8095174186696794,1.2933493524940836,0.34760805945348366,0.3263719150808219,1.8022382923921754,-0.7846170533599903,-0.04833304101051134,-1.0333405344985171,0.25887210309773856,0.08418350533031038,0.11381657692545072,-0.27840102209206696,-2.914878994851995,-0.716222869866457,-1.0989167937252406,-0.3371975377973157,0.5744090048161632,-0.7661721021388503,0.9965650814252371,0.16054616663688848,0.2857242185743487,0.3063430634915238,0.3873635587264386,0.641516813490248,0.6917671103465695,-0.5604835780016102,0.6486327923859554,0.6145561347053797,0.8915657414661364,-0.6494825002619433,0.2853938064384929,-1.5958345515656993,-0.3546946012769488,-0.9939621593370583,0.005548225269753182,0.2483080155452836,3.817646637803243,-1.3797561092144521,0.3817767514389901,0.6194056372609968,1.0699011290624454,0.16328722908384036,-1.0166920313011634,0.8394235955607138,-0.1073065030302659,0.12140768004437781,-0.6919093726359291,0.5071910575635769,-0.04472434566119249,-0.3343042673219773,-1.6159508819679478,0.344140052029557,0.6145561347053797,-0.01831941436676659,-0.7623030730024267,-3.357188263702384,-2.6385357025435616,-3.6274114127566066,-0.5383119878974132,1.2766053960082964,-1.5397432817498722,-1.4006379765015193,0.3082487478987024,-0.02310303361718085,0.2710413648330612,-0.4911880484914574,-0.14113324828185445,0.18932121571114557,-0.5967101997756155,-0.22992584158215473,-0.20156557368954608,-0.3398644620897863,-0.06048041883928153,-0.13313491595798324,-0.1693695354620947,-0.65647741704421,1.5843929484363597,-0.3343042673219773,0.8915657414661364,0.06343382376951158,1.982622177115232,2.397016722370968,0.37362588932361024,0.6405990301821536,-0.40043755851746404,-0.8376852920110558,0.7497945288486347,-1.9895537622618933,0.4734198938575302,2.9866868034966405,0.351794301521462,1.2866775739017517,0.3269821109588186,0.2873304519747448,-0.5196881893484727,2.099416771356489,2.099416771356489,-2.0012708418546246,-0.9832916621767517,-0.37683229797854784,-1.0166920313011634,-0.8746832953429918,-0.26718391737856995,-0.5967101997756155,-0.1106003528374088,-2.0222122025762053,-1.3282205088683336,-0.22915228605732274,-2.6730265939249294,3.559972706403369,-1.666849415271121,-1.5409088940630198,0.8915657414661364,0.6486327923859554,-2.0060305527460764,1.7836060122605069],"xaxis":"x","xbins":{"end":7.682175323566998,"size":0.1,"start":-3.99306919368233},"yaxis":"y","type":"histogram"},{"autobinx":false,"histnorm":"probability density","legendgroup":"Lasso","marker":{"color":"rgb(255, 127, 14)"},"name":"Lasso","opacity":0.7,"x":[-2.047619873490006,3.2237420957398473,-0.22808811219082387,-4.424263598198713,-0.0,2.6754583974503543,-0.23827509751446085,-0.0,0.1933492848197241,-0.6878399125175547,0.0,0.0,-0.0,-0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,0.0,0.0,0.0,-0.3983334666124017,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.6021573559342094,0.0,0.0,5.588974057521393,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.2307513818617175,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,0.1860925703855788,0.6622835325725703,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,-0.0,1.8088480904729822,-0.0,-0.0,0.0,0.0,-0.0,0.0],"xaxis":"x","xbins":{"end":5.588974057521393,"size":0.1,"start":-4.424263598198713},"yaxis":"y","type":"histogram"},{"legendgroup":"Ridge","marker":{"color":"rgb(31, 119, 180)"},"mode":"lines","name":"Ridge","showlegend":false,"x":[-3.99306919368233,-3.969718704647831,-3.9463682156133326,-3.9230177265788337,-3.8996672375443353,-3.8763167485098364,-3.852966259475338,-3.829615770440839,-3.8062652814063407,-3.782914792371842,-3.7595643033373434,-3.736213814302845,-3.712863325268346,-3.689512836233847,-3.6661623471993487,-3.64281185816485,-3.6194613691303514,-3.5961108800958526,-3.572760391061354,-3.5494099020268557,-3.526059412992357,-3.502708923957858,-3.4793584349233595,-3.456007945888861,-3.432657456854362,-3.4093069678198633,-3.385956478785365,-3.362605989750866,-3.3392555007163676,-3.3159050116818687,-3.2925545226473703,-3.2692040336128714,-3.245853544578373,-3.222503055543874,-3.1991525665093756,-3.175802077474877,-3.1524515884403783,-3.1291010994058794,-3.105750610371381,-3.0824001213368826,-3.0590496323023837,-3.035699143267885,-3.0123486542333864,-2.9889981651988875,-2.965647676164389,-2.94229718712989,-2.9189466980953918,-2.8955962090608933,-2.8722457200263944,-2.8488952309918956,-2.8255447419573967,-2.8021942529228983,-2.7788437638884,-2.755493274853901,-2.732142785819402,-2.7087922967849036,-2.685441807750405,-2.6620913187159063,-2.6387408296814074,-2.615390340646909,-2.5920398516124106,-2.5686893625779117,-2.545338873543413,-2.5219883845089144,-2.498637895474416,-2.475287406439917,-2.4519369174054186,-2.42858642837092,-2.4052359393364213,-2.3818854503019224,-2.358534961267424,-2.3351844722329256,-2.3118339831984267,-2.288483494163928,-2.2651330051294294,-2.241782516094931,-2.218432027060432,-2.195081538025933,-2.1717310489914348,-2.1483805599569363,-2.1250300709224375,-2.1016795818879386,-2.0783290928534397,-2.0549786038189413,-2.031628114784443,-2.008277625749944,-1.984927136715445,-1.9615766476809466,-1.9382261586464482,-1.9148756696119493,-1.891525180577451,-1.868174691542952,-1.8448242025084536,-1.8214737134739547,-1.7981232244394563,-1.7747727354049574,-1.7514222463704585,-1.72807175733596,-1.7047212683014612,-1.6813707792669628,-1.658020290232464,-1.6346698011979655,-1.6113193121634666,-1.5879688231289681,-1.5646183340944693,-1.5412678450599708,-1.517917356025472,-1.4945668669909735,-1.4712163779564746,-1.4478658889219762,-1.4245153998874773,-1.401164910852979,-1.37781442181848,-1.3544639327839816,-1.3311134437494827,-1.3077629547149843,-1.2844124656804854,-1.261061976645987,-1.237711487611488,-1.2143609985769896,-1.1910105095424908,-1.1676600205079923,-1.1443095314734935,-1.120959042438995,-1.0976085534044961,-1.0742580643699977,-1.0509075753354988,-1.0275570863010004,-1.0042065972665015,-0.9808561082320026,-0.9575056191975047,-0.9341551301630058,-0.9108046411285073,-0.8874541520940085,-0.86410366305951,-0.8407531740250112,-0.8174026849905127,-0.7940521959560138,-0.7707017069215154,-0.7473512178870165,-0.7240007288525181,-0.7006502398180192,-0.6772997507835208,-0.6539492617490219,-0.6305987727145235,-0.6072482836800246,-0.5838977946455262,-0.5605473056110273,-0.5371968165765288,-0.51384632754203,-0.49049583850753153,-0.46714534947303266,-0.4437948604385342,-0.42044437140403534,-0.3970938823695369,-0.37374339333503803,-0.3503929043005396,-0.3270424152660407,-0.3036919262315423,-0.2803414371970434,-0.256990948162545,-0.2336404591280461,-0.21028997009354722,-0.18693948105904878,-0.1635889920245499,-0.14023850299005147,-0.1168880139555526,-0.09353752492105416,-0.07018703588655528,-0.04683654685205685,-0.02348605781755797,-0.00013556878305953646,0.023214920251439786,0.046565409285937776,0.06991589832043665,0.09326638735493464,0.11661687638943352,0.1399673654239324,0.16331785445843128,0.18666834349292927,0.21001883252742815,0.23336932156192702,0.2567198105964259,0.2800702996309239,0.30342078866542277,0.32677127769992165,0.3501217667344205,0.3734722557689185,0.3968227448034174,0.42017323383791627,0.44352372287241515,0.46687421190691314,0.4902247009414129,0.5135751899759109,0.5369256790104098,0.5602761680449078,0.5836266570794075,0.6069771461139055,0.6303276351484044,0.6536781241829024,0.6770286132174022,0.7003791022519001,0.723729591286399,0.747080080320897,0.7704305693553968,0.7937810583898948,0.8171315474243936,0.8404820364588916,0.8638325254933914,0.8871830145278894,0.9105335035623883,0.9338839925968863,0.957234481631386,0.980584970665884,1.003935459700383,1.0272859487348809,1.0506364377693806,1.0739869268038786,1.0973374158383775,1.1206879048728755,1.1440383939073753,1.1673888829418733,1.1907393719763721,1.2140898610108701,1.23744035004537,1.2607908390798679,1.2841413281143668,1.3074918171488656,1.3308423061833645,1.3541927952178625,1.3775432842523614,1.4008937732868603,1.4242442623213591,1.4475947513558571,1.470945240390356,1.494295729424855,1.5176462184593538,1.5409967074938518,1.5643471965283506,1.5876976855628495,1.6110481745973484,1.6343986636318464,1.6577491526663453,1.6810996417008441,1.704450130735343,1.727800619769841,1.7511511088043399,1.7745015978388388,1.7978520868733376,1.8212025759078356,1.8445530649423345,1.8679035539768334,1.8912540430113323,1.9146045320458303,1.9379550210803291,1.961305510114828,1.9846559991493269,2.008006488183825,2.0313569772183246,2.0547074662528226,2.0780579552873206,2.1014084443218195,2.1247589333563184,2.1481094223908173,2.1714599114253152,2.194810400459814,2.218160889494313,2.241511378528812,2.26486186756331,2.2882123565978087,2.3115628456323076,2.3349133346668065,2.3582638237013045,2.3816143127358034,2.4049648017703023,2.428315290804801,2.451665779839299,2.475016268873798,2.498366757908297,2.5217172469427958,2.5450677359772937,2.5684182250117926,2.5917687140462915,2.6151192030807904,2.6384696921152884,2.6618201811497872,2.685170670184286,2.708521159218785,2.731871648253283,2.7552221372877828,2.7785726263222807,2.8019231153567796,2.8252736043912776,2.8486240934257774,2.8719745824602754,2.8953250714947742,2.9186755605292722,2.942026049563772,2.96537653859827,2.988727027632769,3.012077516667267,3.0354280057017666,3.0587784947362646,3.0821289837707635,3.1054794728052615,3.1288299618397613,3.1521804508742592,3.175530939908758,3.198881428943256,3.222231917977756,3.245582407012254,3.2689328960467527,3.2922833850812507,3.3156338741157505,3.3389843631502485,3.3623348521847474,3.3856853412192454,3.409035830253745,3.432386319288243,3.455736808322742,3.47908729735724,3.5024377863917397,3.5257882754262377,3.5491387644607366,3.5724892534952355,3.5958397425297344,3.6191902315642324,3.6425407205987312,3.66589120963323,3.689241698667729,3.712592187702227,3.735942676736726,3.7592931657712247,3.7826436548057236,3.8059941438402216,3.8293446328747205,3.8526951219092194,3.8760456109437182,3.8993960999782162,3.922746589012715,3.946097078047214,3.969447567081713,3.992798056116211,4.016148545150709,4.0394990341852095,4.062849523219707,4.0862000122542055,4.109550501288704,4.132900990323203,4.156251479357702,4.179601968392199,4.2029524574267,4.226302946461197,4.249653435495696,4.273003924530195,4.296354413564694,4.3197049025991925,4.343055391633691,4.3664058806681885,4.389756369702689,4.413106858737186,4.436457347771685,4.459807836806184,4.483158325840683,4.506508814875182,4.529859303909681,4.553209792944178,4.576560281978678,4.5999107710131755,4.623261260047674,4.646611749082173,4.669962238116672,4.693312727151171,4.71666321618567,4.740013705220167,4.763364194254668,4.786714683289165,4.810065172323664,4.8334156613581625,4.856766150392661,4.88011663942716,4.903467128461659,4.926817617496156,4.950168106530657,4.973518595565156,4.996869084599653,5.020219573634152,5.043570062668651,5.0669205517031495,5.090271040737648,5.1136215297721455,5.136972018806646,5.160322507841145,5.183672996875642,5.207023485910141,5.23037397494464,5.253724463979139,5.277074953013638,5.300425442048135,5.323775931082635,5.347126420117134,5.370476909151631,5.39382739818613,5.417177887220629,5.440528376255128,5.463878865289627,5.487229354324124,5.510579843358625,5.5339303323931235,5.557280821427621,5.5806313104621195,5.603981799496618,5.627332288531117,5.650682777565616,5.674033266600113,5.697383755634614,5.720734244669113,5.74408473370361,5.767435222738109,5.790785711772609,5.8141362008071065,5.837486689841605,5.8608371788761024,5.884187667910603,5.907538156945102,5.930888645979599,5.954239135014098,5.977589624048599,6.000940113083096,6.024290602117595,6.047641091152092,6.070991580186591,6.094342069221091,6.117692558255588,6.141043047290087,6.164393536324586,6.187744025359085,6.211094514393584,6.234445003428081,6.25779549246258,6.2811459814970805,6.304496470531578,6.3278469595660765,6.351197448600575,6.374547937635074,6.397898426669573,6.42124891570407,6.444599404738569,6.46794989377307,6.491300382807567,6.514650871842066,6.538001360876565,6.5613518499110635,6.584702338945562,6.608052827980061,6.631403317014558,6.654753806049059,6.678104295083556,6.701454784118055,6.724805273152554,6.748155762187053,6.771506251221552,6.7948567402560505,6.818207229290548,6.841557718325048,6.864908207359545,6.888258696394044,6.911609185428543,6.934959674463042,6.958310163497541,6.98166065253204,7.005011141566537,7.0283616306010375,7.051712119635535,7.0750626086700334,7.098413097704532,7.121763586739031,7.14511407577353,7.168464564808029,7.191815053842526,7.215165542877027,7.238516031911526,7.261866520946023,7.285217009980522,7.3085674990150205,7.331917988049519,7.355268477084018,7.378618966118515,7.401969455153016,7.425319944187515,7.448670433222012,7.472020922256511,7.49537141129101,7.518721900325509,7.5420723893600075,7.565422878394505,7.588773367429005,7.612123856463504,7.635474345498001,7.6588248345325],"xaxis":"x","y":[0.00843784074154678,0.008769082774297025,0.009099560948369586,0.009428622228230536,0.009755662845954298,0.010080138863440146,0.010401576693451122,0.010719583437323666,0.011033856889257045,0.011344195051578028,0.011650505002708715,0.01195281096012119,0.012251261384638105,0.012546134980248357,0.01283784545524607,0.013126944925945419,0.01341412586331027,0.013700221505261805,0.013986204682741749,0.014273185035233433,0.014562404620668372,0.01485523195466622,0.015153154543978272,0.015457770007892634,0.01577077590825874,0.01609395843277144,0.016429180096351192,0.016778366641103125,0.017143493325803824,0.017526570800698534,0.017929630762335398,0.018354711576186917,0.018803844042113608,0.019279037459751108,0.019782266128323473,0.02031545638909194,0.020880474289714717,0.021479113919451173,0.022113086433728425,0.022784009757490828,0.02349339893036261,0.02424265703429686,0.025033066627264365,0.025865781595674927,0.026741819334410354,0.02766205316708826,0.02862720493065791,0.029637837667504628,0.030694348394395887,0.03179696094999462,0.03294571896009788,0.03414047900075709,0.03538090408226229,0.03666645761970817,0.03799639809646581,0.03936977466328558,0.040785423945929294,0.04224196835627851,0.04373781621412659,0.045271163987962326,0.04684000095199629,0.04844211653290753,0.05007511058319685,0.051736406769047005,0.05342326920010388,0.055132822358038264,0.05686207430195933,0.05860794304402007,0.06036728590045332,0.0621369315346554,0.06391371432275668,0.06569451059139259,0.06747627620503922,0.06925608491901408,0.07103116686650236,0.07279894651574055,0.07455707941831495,0.07630348707235819,0.07803638924562446,0.0797543331427171,0.0814562188572305,0.08314132062176434,0.084809303454596,0.08646023489874433,0.08809459165427373,0.08971326101476121,0.0913175371305043,0.09290911223082997,0.09449006304244309,0.09606283273696176,0.09763020882579565,0.09919529749191669,0.10076149490391872,0.10233245609672084,0.10391206202456715,0.10550438539550246,0.10711365588271263,0.10874422527809563,0.11040053310875059,0.11208707317979277,0.11380836143944202,0.11556890548737923,0.1173731759677773,0.11922558000709997,0.1211304367765774,0.12309195518291002,0.125114213620689,0.12720114165834157,0.12935650347789543,0.1315838828487377,0.13388666938771965,0.13626804584270336,0.13873097613392413,0.14127819389673407,0.14391219128949162,0.14663520786026366,0.14944921930401558,0.15235592598633113,0.15535674115847692,0.1584527788398307,0.1616448413953515,0.1649334068859803,0.16831861631683998,0.17180026095029166,0.17537776988690656,0.17905019814616063,0.1828162154992782,0.1866740963186356,0.19062171071119194,0.19465651719756807,0.19877555718392106,0.2029754514511621,0.2072523988560836,0.21160217740249238,0.21602014779857542,0.22050125957062475,0.22504005975424102,0.2296307041335285,0.2342669709480263,0.23894227693753647,0.24364969554804605,0.24838197707887186,0.2531315705132884,0.25789064674338774,0.2626511228757982,0.26740468728908484,0.2721428251068536,0.2768568437533766,0.2815378982711604,0.28617701610246676,0.2907651210690518,0.2952930563258941,0.2997516061146484,0.304131516199856,0.30842351293428905,0.3126183209674693,0.3167066796815331,0.32067935850911355,0.3245271713564442,0.32824099041915705,0.3318117597357376,0.33523050887201317,0.3384883671670849,0.34157657899473753,0.3444865205028418,0.34720971828522584,0.3497378704150528,0.3520628702255051,0.35417683316275905,0.3560721269586506,0.3577414052774707,0.3591776448850855,0.36037418627158446,0.3613247775341255,0.36202362119799447,0.3624654235251672,0.362645445734752,0.3625595564429061,0.3622042845251324,0.3615768715151516,0.36067532258531476,0.35949845510670814,0.358045943765045,0.3563183612128034,0.3543172132695649,0.35204496774111615,0.34950507601265407,0.3467019866804935,0.343641150617427,0.3403290170158967,0.33677302011638593,0.33298155650136335,0.3289639530128383,0.32473042552903053,0.32029202900771164,0.3156605993655984,0.3108486879101013,0.30586948916780365,0.3007367630597999,0.29546475245484627,0.2900680971853668,0.28456174563788295,0.27896086502842954,0.27328075144600195,0.26753674069487743,0.2617441208924646,0.2559180476864606,0.2500734628474349,0.24422501687480255,0.23838699612996547,0.23257325488476613,0.22679715255077154,0.22107149623934358,0.21540848869778523,0.20981968157607545,0.2043159339043843,0.19890737560529229,0.1936033758273461,0.18841251586828622,0.1833425664562293,0.17840046917371635,0.17359232184068943,0.1689233677152321,0.16439798842217965,0.16001970057575693,0.15579115611963018,0.15171414646231665,0.14778961053429673,0.14401764693201832,0.14039753034052238,0.13692773243826714,0.13360594748325155,0.13042912275778346,0.12739349400997554,0.12449462597384378,0.12172745797800341,0.11908635456736649,0.11656516096553722,0.11415726310085339,0.11185565180972704,0.10965299072085384,0.10754168721685811,0.10551396576989339,0.10356194285831319,0.10167770259619627,0.09985337214921129,0.09808119597155325,0.0963536078812927,0.09466329999666998,0.09300328758410298,0.09136696891970446,0.08974817933897357,0.08814123874238179,0.08654099193556572,0.08494284130896793,0.08334277149978414,0.0817373658254051,0.08012381442839893,0.07849991422454229,0.0768640608936508,0.07521523329421317,0.07355297081367385,0.07187734428348101,0.07018892118907245,0.06848872598762598,0.06677819640904205,0.06505913665722488,0.06333366844886495,0.06160418082575347,0.05987327965491496,0.058143737689787485,0.05641844600702251,0.05470036755936661,0.05299249349795536,0.05129780281991493,0.04961922579226157,0.04795961149365585,0.046321699704501736,0.04470809726601079,0.04312125892281698,0.04156347256396258,0.04003684868570422,0.03854331381842938,0.03708460759047176,0.03566228304485091,0.03427770978161005,0.03293207946880902,0.031626413249260514,0.030361570567385008,0.029138258950360582,0.027957044299057026,0.026818361275826364,0.0257225234166386,0.024669732642722368,0.02366008790013206,0.022693592712786922,0.021770161493812286,0.020889624519766,0.020051731530982272,0.019256153977319748,0.01850248598074921,0.017790244133288148,0.017118866289833543,0.016487709549683923,0.015896047647433267,0.015343067993109458,0.014827868612791222,0.0143494552445226,0.013906738840409523,0.013498533714738695,0.013123556560380466,0.012780426532314516,0.012467666568660746,0.012183706086984613,0.011926885157822953,0.01169546021931312,0.011487611357487678,0.011301451137185418,0.011135034929560802,0.010986372644723935,0.010853441742923698,0.010734201365617585,0.010626607399386107,0.010528628261468406,0.010438261176138162,0.010353548696504506,0.010272595216804258,0.010193583215925901,0.010114788973744683,0.010034597507720991,0.009951516487897456,0.009864188903612979,0.009771404274550905,0.009672108221703016,0.00956541023995935,0.00945058954278124,0.009327098880207557,0.00919456626368994,0.009052794564352427,0.008901758984629778,0.008741602436276181,0.008572628889895042,0.00839529479189737,0.008210198673666406,0.00801806910425264,0.007819751161760662,0.007616191619388888,0.007408423059577212,0.007197547143695018,0.006984717275022052,0.006771120899348773,0.0065579616903305915,0.0063464418658044615,0.006137744876704639,0.005933018702139179,0.00573335997279041,0.005539799130313002,0.005353286813081753,0.0051746816387833825,0.005004739532273058,0.004844104723168604,0.0046933025121913404,0.00455273387865588,0.004422671974138143,0.004303260519600406,0.004194514095507515,0.004096320287116405,0.004008443620540658,0.003930531199755578,0.0038621199307761127,0.00380264519715693,0.003751450831053727,0.0037078002066519636,0.0036708882680847412,0.0036398542922659745,0.003613795178558517,0.0035917790520353867,0.003572858965382087,0.0035560864862813077,0.0035405249624104094,0.003525262264898576,0.003509422823100461,0.0034921787786482044,0.0034727601046812217,0.003450463556598958,0.0034246603432549296,0.0033948024317792375,0.0033604274247080812,0.0033211619743065022,0.003276723725368947,0.0032269218038362586,0.003171655893748565,0.003110913968850746,0.003044768767102379,0.0029733731159848754,0.0028969542334680654,0.0028158071434880353,0.0027302873555636316,0.0026408029655878413,0.002547806338804408,0.0024517855365375554,0.0023532556454844223,0.0022527501624883765,0.0021508125789392522,0.002047988297612909,0.0019448170012383748,0.0018418255767783896,0.0017395216827691858,0.0016383880295435275,0.0015388774242124416,0.0014414086143522647,0.0013463629468529515,0.0012540818417182513,0.001164865065109792,0.0010789697718854565,0.0009966102755317571,0.0009179584929042916,0.0008431450026816801,0.0007722606499604994,0.0007053586249647307,0.0006424569413555875,0.0005835412389990769,0.0005285678371318765,0.0004774669664787618,0.00043014611281053653,0.00038649340946356013,0.00034638102223640075,0.00030966847659689225,0.0002762058840411307,0.00024583703152142853,0.0002184023048958097,0.00019374142415973475,0.00017169597463802453,0.00015211172420249498,0.00013484072182772344,0.00011974317731969458,0.00010668912579300555,9.555988340195766e-05,8.62493029434737e-05,7.86648392632113e-05,7.272843494896037e-05,6.837723664448921e-05,6.556415153567612e-05,6.425825223583804e-05,6.444503652658897e-05,6.612654630115232e-05,6.93213477218771e-05,7.406437216006753e-05,8.040661505323148e-05,8.841468751128977e-05,9.817021344538049e-05,0.00010976906329202304,0.0001233204141659969,0.00013894562559209974,0.00015677691992210902,0.00017695585720747817,0.00019963159572261664,0.00022495893155082146,0.0002530961136669334,0.00028420243476521737,0.0003184356026516781,0.00035594890228320586,0.00039688816440199324,0.0004413885630653264,0.0004895712710652114,0.0005415400091015531,0.0005973775314283206,0.0006571420973258197,0.000720863983944744,0.000788542101589144,0.0008601407771268723,0.0009355867747126931,0.0010147666251704034,0.001097524336015894,0.0011836595530534382,0.0012729262416174018,0.0013650319507831046,0.0014596377172019892,0.0015563586566540286,0.0016547652810370412,0.0017543855664718935,0.0018547077846969929,0.0019551840952156743,0.002055234880057502,0.00215425378687831,0.0022516134298491983,0.002346671681792742,0.002438778475752407,0.0025272830200654935,0.002611541318475177,0.0026909238762619927,0.00276482346515488,0.0028326628142013367,0.002893902091072167,0.00294804603861143,0.002994650634896636,0.0030333291516398877,0.003063757495340016,0.0030856787280031184,0.0030989066792128203],"yaxis":"y","type":"scatter"},{"legendgroup":"Lasso","marker":{"color":"rgb(255, 127, 14)"},"mode":"lines","name":"Lasso","showlegend":false,"x":[-4.424263598198713,-4.404237122887272,-4.3842106475758325,-4.364184172264392,-4.344157696952951,-4.324131221641512,-4.304104746330071,-4.284078271018631,-4.264051795707191,-4.2440253203957505,-4.223998845084311,-4.20397236977287,-4.18394589446143,-4.16391941914999,-4.14389294383855,-4.123866468527109,-4.1038399932156695,-4.083813517904229,-4.0637870425927884,-4.043760567281349,-4.023734091969908,-4.003707616658469,-3.983681141347028,-3.9636546660355876,-3.9436281907241475,-3.9236017154127074,-3.903575240101267,-3.883548764789827,-3.8635222894783867,-3.843495814166946,-3.823469338855506,-3.803442863544066,-3.783416388232626,-3.763389912921186,-3.7433634376097453,-3.7233369622983052,-3.703310486986865,-3.6832840116754246,-3.6632575363639845,-3.6432310610525445,-3.623204585741104,-3.603178110429664,-3.5831516351182238,-3.5631251598067837,-3.5430986844953436,-3.523072209183903,-3.503045733872463,-3.483019258561023,-3.4629927832495824,-3.4429663079381423,-3.422939832626702,-3.4029133573152617,-3.3828868820038216,-3.3628604066923815,-3.342833931380941,-3.322807456069501,-3.302780980758061,-3.2827545054466203,-3.26272803013518,-3.24270155482374,-3.2226750795122996,-3.20264860420086,-3.1826221288894194,-3.1625956535779793,-3.1425691782665393,-3.1225427029550987,-3.1025162276436586,-3.0824897523322186,-3.062463277020778,-3.042436801709338,-3.022410326397898,-3.0023838510864573,-2.9823573757750177,-2.962330900463577,-2.942304425152137,-2.922277949840697,-2.9022514745292565,-2.8822249992178164,-2.8621985239063763,-2.8421720485949358,-2.8221455732834957,-2.8021190979720556,-2.782092622660615,-2.762066147349175,-2.742039672037735,-2.7220131967262944,-2.7019867214148547,-2.681960246103414,-2.661933770791974,-2.641907295480534,-2.6218808201690935,-2.6018543448576534,-2.5818278695462133,-2.561801394234773,-2.5417749189233327,-2.5217484436118927,-2.501721968300452,-2.481695492989012,-2.461669017677572,-2.4416425423661314,-2.4216160670546913,-2.4015895917432513,-2.3815631164318107,-2.3615366411203706,-2.3415101658089306,-2.3214836904974905,-2.30145721518605,-2.28143073987461,-2.26140426456317,-2.2413777892517293,-2.221351313940289,-2.201324838628849,-2.181298363317409,-2.1612718880059685,-2.1412454126945284,-2.1212189373830883,-2.101192462071648,-2.0811659867602077,-2.0611395114487676,-2.0411130361373275,-2.021086560825887,-2.001060085514447,-1.9810336102030068,-1.9610071348915667,-1.9409806595801262,-1.9209541842686861,-1.900927708957246,-1.8809012336458055,-1.8608747583343654,-1.8408482830229254,-1.8208218077114853,-1.8007953324000447,-1.7807688570886047,-1.7607423817771646,-1.740715906465724,-1.720689431154284,-1.7006629558428439,-1.6806364805314038,-1.6606100052199633,-1.6405835299085232,-1.620557054597083,-1.6005305792856426,-1.5805041039742025,-1.5604776286627624,-1.5404511533513223,-1.5204246780398818,-1.5003982027284417,-1.4803717274170016,-1.4603452521055615,-1.440318776794121,-1.420292301482681,-1.4002658261712408,-1.3802393508598003,-1.3602128755483602,-1.3401864002369202,-1.32015992492548,-1.3001334496140395,-1.2801069743025995,-1.2600804989911594,-1.2400540236797188,-1.2200275483682788,-1.2000010730568387,-1.1799745977453986,-1.159948122433958,-1.139921647122518,-1.119895171811078,-1.0998686964996374,-1.0798422211881973,-1.0598157458767572,-1.0397892705653171,-1.0197627952538766,-0.9997363199424365,-0.9797098446309964,-0.9596833693195563,-0.9396568940081158,-0.9196304186966757,-0.8996039433852356,-0.8795774680737951,-0.859550992762355,-0.8395245174509149,-0.8194980421394749,-0.7994715668280343,-0.7794450915165942,-0.7594186162051542,-0.7393921408937136,-0.7193656655822736,-0.6993391902708335,-0.6793127149593934,-0.6592862396479529,-0.6392597643365128,-0.6192332890250727,-0.5992068137136322,-0.5791803384021916,-0.5591538630907515,-0.5391273877793115,-0.5191009124678709,-0.49907443715643085,-0.47904796184499077,-0.4590214865335507,-0.43899501122211015,-0.41896853591067007,-0.39894206059922954,-0.3789155852877899,-0.3588891099763494,-0.33886263466490885,-0.3188361593534692,-0.2988096840420287,-0.27878320873058904,-0.2587567334191485,-0.23873025810770887,-0.21870378279626834,-0.19867730748482781,-0.1786508321733873,-0.15862435686194765,-0.13859788155050712,-0.11857140623906748,-0.09854493092762695,-0.07851845561618731,-0.058491980304745894,-0.038465504993306254,-0.018439029681865726,0.0015874456295739137,0.02161392094101444,0.04164039625245408,0.06166687156389461,0.08169334687533514,0.10171982218677567,0.1217462974982153,0.14177277280965583,0.16179924812109547,0.181825723432536,0.20185219874397564,0.22187867405541706,0.2419051493668567,0.2619316246782972,0.28195809998973687,0.3019845753011774,0.32201105061261703,0.34203752592405756,0.3620640012354972,0.3820904765469386,0.40211695185837826,0.4221434271698188,0.4421699024812584,0.46219637779269895,0.4822228531041386,0.5022493284155791,0.5222758037270196,0.5423022790384602,0.5623287543498998,0.5823552296613403,0.60238170497278,0.6224081802842205,0.6424346555956602,0.6624611309071016,0.6824876062185412,0.7025140815299817,0.7225405568414223,0.7425670321528619,0.7625935074643024,0.7826199827757421,0.8026464580871835,0.8226729333986231,0.8426994087100637,0.8627258840215033,0.8827523593329438,0.9027788346443835,0.922805309955824,0.9428317852672645,0.962858260578705,0.9828847358901447,1.0029112112015852,1.0229376865130249,1.0429641618244654,1.062990637135905,1.0830171124473464,1.103043587758786,1.1230700630702266,1.1430965383816662,1.1631230136931068,1.1831494890045464,1.203175964315987,1.2232024396274275,1.243228914938868,1.2632553902503076,1.2832818655617482,1.3033083408731878,1.3233348161846283,1.343361291496068,1.3633877668075085,1.383414242118949,1.4034407174303896,1.4234671927418292,1.4434936680532697,1.4635201433647094,1.48354661867615,1.5035730939875895,1.523599569299031,1.5436260446104706,1.5636525199219111,1.5836789952333508,1.6037054705447913,1.623731945856231,1.6437584211676715,1.663784896479112,1.6838113717905525,1.7038378471019922,1.7238643224134327,1.7438907977248723,1.7639172730363128,1.7839437483477525,1.803970223659194,1.8239966989706335,1.844023174282074,1.8640496495935137,1.8840761249049542,1.9041026002163939,1.9241290755278344,1.944155550839275,1.9641820261507155,1.984208501462155,2.0042349767735956,2.0242614520850353,2.044287927396476,2.0643144027079154,2.084340878019357,2.1043673533307965,2.124393828642237,2.1444203039536767,2.164446779265117,2.184473254576557,2.2044997298879974,2.224526205199438,2.2445526805108784,2.264579155822318,2.2846056311337586,2.3046321064451982,2.3246585817566388,2.3446850570680784,2.364711532379519,2.3847380076909594,2.4047644830024,2.4247909583138396,2.44481743362528,2.46484390893672,2.4848703842481603,2.5048968595596,2.5249233348710414,2.544949810182481,2.5649762854939215,2.585002760805361,2.6050292361168017,2.6250557114282413,2.645082186739682,2.6651086620511224,2.685135137362563,2.7051616126740026,2.725188087985443,2.7452145632968827,2.7652410386083233,2.785267513919763,2.8052939892312043,2.825320464542644,2.8453469398540845,2.865373415165524,2.8853998904769647,2.9054263657884043,2.925452841099845,2.9454793164112854,2.965505791722726,2.9855322670341655,3.005558742345606,3.0255852176570457,3.045611692968486,3.065638168279926,3.0856646435913673,3.105691118902807,3.1257175942142474,3.145744069525687,3.1657705448371276,3.1857970201485672,3.2058234954600078,3.2258499707714483,3.245876446082889,3.2659029213943294,3.285929396705769,3.3059558720172095,3.325982347328649,3.3460088226400897,3.3660352979515293,3.3860617732629708,3.4060882485744104,3.426114723885851,3.4461411991972906,3.466167674508731,3.4861941498201707,3.5062206251316113,3.526247100443052,3.5462735757544923,3.566300051065932,3.5863265263773725,3.606353001688812,3.6263794770002535,3.646405952311693,3.666432427623133,3.6864589029345725,3.706485378246014,3.7265118535574535,3.746538328868895,3.7665648041803346,3.786591279491774,3.806617754803214,3.8266442301146553,3.846670705426095,3.8666971807375345,3.886723656048976,3.9067501313604156,3.926776606671857,3.946803081983295,3.9668295572947363,3.986856032606176,4.006882507917617,4.026908983229057,4.046935458540497,4.066961933851938,4.086988409163378,4.107014884474817,4.127041359786257,4.147067835097698,4.16709431040914,4.187120785720578,4.207147261032019,4.227173736343459,4.2472002116549,4.267226686966338,4.287253162277779,4.307279637589221,4.3273061129006605,4.3473325882121,4.36735906352354,4.387385538834981,4.407412014146421,4.4274384894578604,4.447464964769302,4.4674914400807415,4.487517915392183,4.507544390703621,4.527570866015062,4.547597341326502,4.567623816637943,4.587650291949383,4.6076767672608225,4.627703242572264,4.647729717883704,4.667756193195143,4.687782668506583,4.707809143818024,4.727835619129466,4.747862094440904,4.767888569752345,4.787915045063785,4.807941520375226,4.827967995686664,4.847994470998105,4.868020946309547,4.888047421620986,4.908073896932426,4.928100372243866,4.948126847555307,4.968153322866747,4.988179798178186,5.008206273489626,5.028232748801067,5.048259224112509,5.068285699423947,5.088312174735388,5.108338650046828,5.128365125358269,5.148391600669707,5.168418075981148,5.18844455129259,5.2084710266040295,5.228497501915469,5.248523977226909,5.26855045253835,5.28857692784979,5.3086034031612295,5.328629878472671,5.3486563537841105,5.368682829095552,5.38870930440699,5.408735779718431,5.428762255029871,5.448788730341312,5.468815205652752,5.488841680964192,5.508868156275633,5.528894631587073,5.548921106898512,5.568947582209952],"xaxis":"x","y":[0.008231159467868654,0.008170648324910304,0.007991770915025639,0.007702301941591469,0.007314574341882726,0.0068446080257981825,0.00631101353305774,0.00573377499114613,0.0051330227130815765,0.00452789900378611,0.003935602989373106,0.003370674671964368,0.0028445488662282577,0.0023653802450996175,0.00193811497534809,0.0015647649675472643,0.0012448289990796553,0.0009758010582115731,0.0007537093066617672,0.000573637423315129,0.0004301917526689571,0.0003178906023459913,0.0002314644528408489,0.0001660664582543181,0.0001174006627298054,8.178057860886605e-05,5.61333310328203e-05,3.7964917082407645e-05,2.530084942943564e-05,1.6614173970756624e-05,1.0750122440602652e-05,6.853920664790626e-06,4.30581871193383e-06,2.6654062622091536e-06,1.6257811806413936e-06,9.771287139296682e-07,5.786719943928667e-07,3.376790822991341e-07,1.9416317205253974e-07,1.1000706134552885e-07,6.14137014777473e-08,3.378321594004035e-08,1.8311659748884297e-08,9.780148211361574e-09,5.146999994628272e-09,2.669032761553128e-09,1.3637810352518455e-09,6.866357232408948e-10,3.4064274843649807e-10,1.6651866146836828e-10,8.020800291765592e-11,3.806831334360753e-11,1.7803334499709787e-11,8.204168290370762e-12,3.7255005186481254e-12,1.6675337536490249e-12,7.369065385697773e-13,3.2451272774417093e-13,1.4975396858388469e-13,8.953041896211749e-14,1.0035392135931061e-13,1.900962762096767e-13,4.2314161054981975e-13,9.619267545533054e-13,2.168559822567057e-12,4.822555457332015e-12,1.05695957896815e-11,2.2826807082198894e-11,4.85764198152375e-11,1.0185850183015251e-10,2.1045543548666856e-10,4.284636944417173e-10,8.595257998138592e-10,1.6990056058615914e-09,3.309190065718266e-09,6.350963507455256e-09,1.201015266849504e-08,2.2379400274273867e-08,4.109030505180558e-08,7.433978353078926e-08,1.3252390490138242e-07,2.3278669878401917e-07,4.029146922293108e-07,6.871618688511741e-07,1.1547713633208257e-06,1.912158833388989e-06,3.1199161919966083e-06,5.015946519045343e-06,7.946097176073335e-06,1.2403545720592936e-05,1.907782396211991e-05,2.8913643879473497e-05,4.317852708766648e-05,6.353657861087442e-05,9.21235852194753e-05,0.00013161604706535049,0.0001852839754269091,0.00025701465219416674,0.0003512925265394551,0.00047311960410616373,0.000627861686471779,0.0008210092043556758,0.0010578475270763064,0.0013430405629811279,0.0016801427773682858,0.0020710675038939715,0.0025155521482086974,0.003010671701940893,0.003550458834247778,0.004125689767523771,0.004723888733130511,0.005329589462422772,0.005924870453633501,0.00649015347237546,0.007005224850747955,0.0074504104304224964,0.007807811531316143,0.008062494855446708,0.008203526489736827,0.00822475034868181,0.008125233853275828,0.00790933589363661,0.007586390175101028,0.007170035996267453,0.006677263305991819,0.006127265141849875,0.005540205200122756,0.004936010021399383,0.0043332846682745734,0.0037484300695752506,0.003195012865373412,0.0026834086465971547,0.0022207108983891173,0.0018108740230193294,0.0014550417686131113,0.0011520032148249625,0.0008987169592812399,0.0006908491318455138,0.0005232805296822473,0.0003905504526225505,0.00028721775181877855,0.0002081315586119696,0.0001486140053193526,0.00010456439301928127,7.249859858681566e-05,4.9539316902301467e-05,3.337251736346988e-05,2.2183874821416928e-05,1.4586524827622102e-05,9.548816604955674e-06,6.328190291074175e-06,4.415142273502666e-06,3.489587282406465e-06,3.39079386108159e-06,4.101396258598995e-06,5.745652225762506e-06,8.60197224263576e-06,1.3129626043434137e-05,2.000927054128994e-05,3.0196385414366217e-05,4.498572319387748e-05,6.608340331274058e-05,9.568130233722511e-05,0.00013652601573138713,0.00019197211683099962,0.0002660070830891956,0.00036323359780901743,0.0004887945633179402,0.0006482276987153547,0.0008472405788835172,0.0010914037230422106,0.0013857688288836355,0.0017344309718682308,0.0021400665226966,0.002603491162721327,0.0031232928412149833,0.003695600898472202,0.004314053264410741,0.00497001776599427,0.005653111425525775,0.0063520449499276715,0.007055801700781674,0.007755145979726512,0.008444450030852455,0.009123838382549907,0.009801676629453372,0.010497481792107431,0.011245401659344676,0.012098494832096185,0.013134129565760162,0.014460889721355303,0.016227405993163888,0.018633491239180625,0.021943819335032377,0.026504118828121963,0.0327594352191452,0.04127344391458809,0.0527470885869785,0.06803402740534877,0.0881495802662067,0.11426920994043262,0.14771219709503183,0.18990625804182767,0.2423295704105526,0.30642813836733207,0.3835086866242017,0.4746102445463664,0.5803610479544702,0.7008309775730249,0.8353929735015158,0.9826091451520349,1.1401580750860782,1.3048186422937464,1.4725223286505993,1.6384804838781104,1.7973858170075583,1.94367919872091,2.071864702058055,2.1768488087452877,2.254274947363425,2.300822857505464,2.314444146498714,2.2945107794981,2.2418615567585785,2.1587418689332813,2.0486428662186706,1.9160562184457735,1.7661685971565113,1.6045249212359967,1.4366907854338082,1.2679423685198379,1.1030070137100203,0.9458704795091232,0.7996586709496765,0.6665935964040949,0.548016321989699,0.444464508473758,0.3557890702755723,0.2812936082995854,0.21988126610070244,0.17019607205472287,0.13074909422773923,0.10002328946366607,0.07655429646741171,0.05898725851679661,0.04611186857032731,0.036879152426562076,0.030404101926626747,0.02595827357959998,0.022956049366969686,0.020937590634747226,0.01955075693432644,0.01853352814946615,0.017697838432533457,0.016915244050636755,0.016104512164358004,0.015221019110101172,0.014247756880286693,0.013187732034405887,0.01205757029144172,0.010882186004255816,0.00969041955591951,0.00851157630205422,0.007372813902067462,0.006297322019036603,0.005303224127771199,0.004403111748573936,0.003604102885566699,0.0029083035796824814,0.0023135471738892147,0.0018142909881345972,0.0014025636992060833,0.001068876639561242,0.000803035642017884,0.0005948140709726241,0.0004344698007687793,0.0003131073245254134,0.00022289990334954624,0.00015719546037082043,0.00011053416160178506,7.860608396021323e-05,5.8175013825769405e-05,4.699021123931266e-05,4.3702746745227905e-05,4.7797398618096996e-05,5.954550270133476e-05,7.99788129931504e-05,0.00011087948670251409,0.00015477685240316617,0.00021493780095323075,0.00029533470451199666,0.0004005730892827858,0.0005357613302775312,0.0007063068966244758,0.0009176285647564034,0.0011747817226913004,0.0014820042362757913,0.0018422026862309415,0.00225641193606142,0.0027232732967127577,0.0032385860293095573,0.003794991525447876,0.004381847462552148,0.004985339446533842,0.005588860015265558,0.006173660481238535,0.006719752272104725,0.0072070045530699504,0.007616357973263949,0.007931054386474876,0.008137772736517297,0.008227564096096703,0.008196494530075262,0.008045931564794781,0.007782445395129935,0.007417335080765977,0.0069658278122832415,0.006446031012652843,0.00587773869387003,0.0052812027715360785,0.004675976457688804,0.004079921728826202,0.0035084490161932215,0.002974028438924388,0.0024859821218034474,0.00205054006610764,0.0016711204578183012,0.0013487808117781067,0.0010827793346722193,0.0008711856309466875,0.0007114848902451615,0.0006011281248055988,0.000537991035778479,0.0005207141940450353,0.0005489064972265501,0.0006232020072489497,0.000745167529802434,0.0009170652805246286,0.0011414824116689484,0.0014208475948471206,0.0017568644011355765,0.0021499014415842705,0.0025983890609678566,0.0030982802275346315,0.0036426372626745477,0.0042214044055115365,0.004821417577326228,0.00542668662078439,0.006018962392105081,0.006578573266892565,0.007085485878253043,0.007520516987262711,0.007866601241791336,0.008110006708904346,0.008241388874763092,0.00825658511114329,0.008157074395389678,0.007950058575009699,0.007648157575348913,0.00726874686135924,0.00683299650487831,0.006364693608613695,0.005888941357140439,0.005430828219667875,0.0050141512637405595,0.004660261053711385,0.004387075920197305,0.004208294260205003,0.004132818025860066,0.004164390476339933,0.004301446843339512,0.004537176538555179,0.00485979753481235,0.005253044696449929,0.005696871449631754,0.006168356489799262,0.0066427938196565,0.007094926466626213,0.00750026433897658,0.007836408403188283,0.008084290532834564,0.00822923431513826,0.00826174891040911,0.008177986132196264,0.007979818753004903,0.007674532438053456,0.007274160270759528,0.006794522705278519,0.006254062472035329,0.0056725800822221015,0.005069979363331207,0.004465123991762862,0.003874887086219524,0.0033134497373169683,0.0027918747662614386,0.002317952998942789,0.0018962943537695865,0.0015286175369672982,0.0012141813722685592,0.0009502978010690473,0.0007328703846533139,0.0005569110241197561,0.0004169995530296587,0.0003076638383127473,0.0002236703307582794,0.00016022539432018987,0.00011309550616475054,7.86593530788683e-05,5.390715454849112e-05,3.640268850826614e-05,2.4222084833022513e-05,1.5881100379725666e-05,1.02598418954027e-05,6.53118149694021e-06,4.09669699504602e-06,2.5320188816213963e-06,1.5420236777551947e-06,9.253502579657752e-07,5.471573832673379e-07,3.1879344500389695e-07,1.830195601600413e-07,1.0353248475137204e-07,5.770942833322171e-08,3.169625212198529e-08,1.7153788795283186e-08,9.147516672687914e-09,4.806593183509911e-09,2.4886425831331787e-09,1.269634442117103e-09,6.382427174494105e-10,3.16143347638442e-10,1.5430259909012506e-10,7.420847218476384e-11,3.516616663981199e-11,1.6420606867347444e-11,7.555334408643224e-12,3.4258028711624626e-12,1.5316719734931007e-12,6.774695641872511e-13,3.019278513344427e-13,1.4879306348885892e-13,1.1019823458265587e-13,1.5844083417603283e-13,3.281094430027449e-13,7.383735290403488e-13,1.6681231812550846e-12,3.725733820984465e-12,8.20425926000957e-12,1.780336944316093e-11,3.8068326566611915e-11,8.0208007847036e-11,1.6651866327868043e-10,3.4064274909147524e-10,6.866357234743323e-10,1.3637810353337924e-09,2.669032761581381e-09,5.146999994637936e-09,9.780148211364992e-09,1.8311659748884718e-08,3.3783215940040696e-08,6.141370147774742e-08,1.1000706134553064e-07,1.9416317205253013e-07,3.3767908229912873e-07,5.78671994392876e-07,9.771287139296682e-07,1.6257811806413936e-06,2.6654062622090778e-06,4.30581871193383e-06,6.853920664790534e-06,1.0750122440602518e-05,1.6614173970756197e-05,2.530084942943564e-05,3.7964917082408086e-05,5.613333103281906e-05,8.178057860886519e-05,0.00011740066272980413,0.00016606645825431975,0.00023146445284084234,0.00031789060234598546,0.0004301917526689607,0.0005736374233151243,0.0007537093066617672,0.0009758010582115588,0.0012448289990796553,0.0015647649675472643,0.0019381149753480667,0.0023653802450996175,0.0028445488662282577,0.0033706746719643996,0.003935602989373037,0.004527899003786092,0.005133022713081524,0.005733774991146146,0.006311013533057724,0.006844608025798168,0.007314574341882726,0.007702301941591469,0.007991770915025625,0.008170648324910297],"yaxis":"y","type":"scatter"},{"legendgroup":"Ridge","marker":{"color":"rgb(31, 119, 180)","symbol":"line-ns-open"},"mode":"markers","name":"Ridge","showlegend":false,"x":[-3.99306919368233,5.037703251896069,-0.8618254501203131,-3.518143500093341,-0.4246938571387098,2.681282201468191,-0.30531458316843896,0.225470866298231,-0.10313995513768215,-0.12233091116054062,0.1980254740367647,-0.12096923597827285,-1.0307349960082024,0.16054616663688848,0.18853639551109955,-0.5453464132844311,2.5605928944992438,0.5680348391887868,-0.08841057029679074,1.2472505317253375,-2.160230765395618,-1.0677409849345936,-0.7364849429177451,-0.28112098997789636,-0.4882475060999198,-0.1425576133235897,0.1691084509360443,-2.0529875860314046,-0.22818313515560246,1.6303535359653587,0.8247284958343394,0.6917671103465695,0.6339733263643443,2.786627284213715,1.6999498733488676,0.2176394169838952,-0.4585414989724577,-1.8837289958894594,1.7836060122605069,-1.7389733928317812,-0.40243166247786455,0.6134325242990762,2.004331221154762,0.9351900064124458,0.6522049111168239,-2.4074597277499925,-0.39265252407870394,-0.005285919488866073,1.3906261964441549,-1.1616037424271637,0.8189254155613295,1.0215379890426113,-2.637221932716584,0.9361208196448293,-0.04223649969157739,-1.9565464961934331,0.24985779224650795,-2.315030515160257,1.6026187321074647,-2.329852832342274,-0.01831941436676659,1.2373129436137094,-2.1630547161835643,0.3874297846724441,0.4948673663634461,0.4341785024692798,0.3968312310257145,-1.1540100751195967,-1.0653725203822604,-0.4275049160295889,-1.3657494493721067,-0.368479476200124,-1.3560032393828272,1.916141048296885,0.4341785024692798,0.5744090048161632,-0.7771061917846339,0.40558274892243196,0.23064206609333193,-1.8974790844937957,0.46121366395995816,1.3590820283499632,-0.11806189831151974,-0.062336117496393395,-0.07435451646712286,-2.8553645595291415,0.3873635587264386,1.0392987593975593,-0.1614882993239033,-0.48985938741573953,-0.9368997009385195,0.15097206177047623,2.1509718272368006,2.381501788404273,0.729890873878227,0.4611998508370523,-0.5850812205330833,-0.5766478514315909,-0.0842736723450091,-0.7326296025054808,0.779962075729646,0.10732084989935053,0.5339684840239793,0.33179740827534043,0.9623797379288901,-1.409136254108555,-1.2291494337633997,0.14425910823946358,0.4331713596424655,0.5838555717902595,0.3158534049890076,-0.3478909774726338,0.6189045066996242,-1.0726914056625207,-0.741705924962981,-0.12408193154471454,-0.1106003528374088,-0.39265252407870394,-0.5487481018650975,1.9467143014388553,0.8742526670258126,-2.098105545298266,0.9757650198915024,-0.698037888742613,-0.8464642645194409,1.685698860552264,-0.01831941436676659,-0.10760176154622614,7.682175323566998,0.16796990200654802,0.4482517885924341,-0.1999958575078007,1.7942833919555785,1.226615287265604,0.8071214607482923,1.169760812638818,0.6339733263643443,0.41649375308346515,-0.30428774746211307,-1.68166757656904,1.0989302571807134,-0.6205092991725667,1.1145049284259971,2.3325865177493905,0.215452013264411,-0.6986593516108979,1.0936996724139487,0.9974315786160914,-1.407430307520337,1.235917856700818,0.47996983491565054,-1.426249199291498,4.00672085831785,-0.3223283046640506,-1.4404328017367907,-0.19442500937051288,0.3417978238286872,-2.107840844595967,-0.48985938741573953,1.9572274502485816,2.1115971524615564,-0.7683885279644251,2.012642208218853,0.5680348391887868,1.192123079471266,1.878765026912756,-0.05006793217813388,-1.1465662192600896,0.30000372094512257,1.6319378655424295,0.5095374822855244,-1.5520388924207411,0.26364822358941364,-1.2075031029262813,-2.1400776378362782,0.8045344667769887,-2.098181170511385,0.15322260147561373,-1.8095174186696794,1.2933493524940836,0.34760805945348366,0.3263719150808219,1.8022382923921754,-0.7846170533599903,-0.04833304101051134,-1.0333405344985171,0.25887210309773856,0.08418350533031038,0.11381657692545072,-0.27840102209206696,-2.914878994851995,-0.716222869866457,-1.0989167937252406,-0.3371975377973157,0.5744090048161632,-0.7661721021388503,0.9965650814252371,0.16054616663688848,0.2857242185743487,0.3063430634915238,0.3873635587264386,0.641516813490248,0.6917671103465695,-0.5604835780016102,0.6486327923859554,0.6145561347053797,0.8915657414661364,-0.6494825002619433,0.2853938064384929,-1.5958345515656993,-0.3546946012769488,-0.9939621593370583,0.005548225269753182,0.2483080155452836,3.817646637803243,-1.3797561092144521,0.3817767514389901,0.6194056372609968,1.0699011290624454,0.16328722908384036,-1.0166920313011634,0.8394235955607138,-0.1073065030302659,0.12140768004437781,-0.6919093726359291,0.5071910575635769,-0.04472434566119249,-0.3343042673219773,-1.6159508819679478,0.344140052029557,0.6145561347053797,-0.01831941436676659,-0.7623030730024267,-3.357188263702384,-2.6385357025435616,-3.6274114127566066,-0.5383119878974132,1.2766053960082964,-1.5397432817498722,-1.4006379765015193,0.3082487478987024,-0.02310303361718085,0.2710413648330612,-0.4911880484914574,-0.14113324828185445,0.18932121571114557,-0.5967101997756155,-0.22992584158215473,-0.20156557368954608,-0.3398644620897863,-0.06048041883928153,-0.13313491595798324,-0.1693695354620947,-0.65647741704421,1.5843929484363597,-0.3343042673219773,0.8915657414661364,0.06343382376951158,1.982622177115232,2.397016722370968,0.37362588932361024,0.6405990301821536,-0.40043755851746404,-0.8376852920110558,0.7497945288486347,-1.9895537622618933,0.4734198938575302,2.9866868034966405,0.351794301521462,1.2866775739017517,0.3269821109588186,0.2873304519747448,-0.5196881893484727,2.099416771356489,2.099416771356489,-2.0012708418546246,-0.9832916621767517,-0.37683229797854784,-1.0166920313011634,-0.8746832953429918,-0.26718391737856995,-0.5967101997756155,-0.1106003528374088,-2.0222122025762053,-1.3282205088683336,-0.22915228605732274,-2.6730265939249294,3.559972706403369,-1.666849415271121,-1.5409088940630198,0.8915657414661364,0.6486327923859554,-2.0060305527460764,1.7836060122605069],"xaxis":"x","y":["Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge","Ridge"],"yaxis":"y2","type":"scatter"},{"legendgroup":"Lasso","marker":{"color":"rgb(255, 127, 14)","symbol":"line-ns-open"},"mode":"markers","name":"Lasso","showlegend":false,"x":[-2.047619873490006,3.2237420957398473,-0.22808811219082387,-4.424263598198713,-0.0,2.6754583974503543,-0.23827509751446085,-0.0,0.1933492848197241,-0.6878399125175547,0.0,0.0,-0.0,-0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,0.0,0.0,0.0,-0.3983334666124017,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.6021573559342094,0.0,0.0,5.588974057521393,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.2307513818617175,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,0.1860925703855788,0.6622835325725703,0.0,-0.0,0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,0.0,0.0,-0.0,0.0,-0.0,-0.0,0.0,-0.0,0.0,0.0,0.0,0.0,-0.0,-0.0,-0.0,0.0,0.0,-0.0,-0.0,-0.0,-0.0,-0.0,0.0,-0.0,0.0,-0.0,-0.0,-0.0,-0.0,1.8088480904729822,-0.0,-0.0,0.0,0.0,-0.0,0.0],"xaxis":"x","y":["Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso","Lasso"],"yaxis":"y2","type":"scatter"}],                        {"barmode":"overlay","hovermode":"closest","legend":{"traceorder":"reversed"},"xaxis":{"anchor":"y2","domain":[0.0,1.0],"zeroline":false},"yaxis":{"anchor":"free","domain":[0.35,1],"position":0.0},"yaxis2":{"anchor":"x","domain":[0,0.25],"dtick":1,"showticklabels":false},"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('394b4b1f-19a3-4c6b-97c6-f31058a00a4f');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>



```python
name_design_matrix_std(tr).columns[lasso_coef != 0]
```




    Index(['cylinders', 'displacement', 'horsepower', 'weight', 'model_year',
           'displacement/cylinder', 'origin_japan', 'origin_usa', 'amc', 'datsun',
           'diesel', 'ford', 'plymouth', 'pontiac', 'vw'],
          dtype='object')




```python
name_design_matrix_std(tr).columns[ridge_coef != 0]
```




    Index(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration',
           'model_year', 'displacement/cylinder', 'origin_europe', 'origin_japan',
           'origin_usa',
           ...
           'volare', 'volkswagen', 'volvo', 'vw', 'wagon', 'woody', 'xe', 'yorker',
           'zephyr', 'zx'],
          dtype='object', length=294)




```python

```