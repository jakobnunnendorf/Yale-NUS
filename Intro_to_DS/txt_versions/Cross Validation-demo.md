# Lecture 17

## Train Test Split and Cross Validation

In this section we will work through the train test-split and the process of cross validation.  

## Imports

As with other notebooks we will use the same set of standard imports.


```python
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
#import cufflinks as cf
#cf.set_config_file(offline=True, sharing=False, theme='ggplot');
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

## Train Test Split

The first thing we will want to do with this data is construct a train/test split. Constructing a train test split before EDA and data cleaning can often be helpful.  This allows us to see if our data cleaning and any conclusions we draw from visualizations generalize to new data. This can be done by re-running the data cleaning and EDA process on the test dataset.

### Using Pandas Operations

We can sample the entire dataset to get a permutation and then select a range of rows.


```python
data.sample?
```


```python
shuffled_data = data.sample(frac = 1,random_state=19)
shuffled_data
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
      <th>208</th>
      <td>13.0</td>
      <td>8</td>
      <td>318.0</td>
      <td>150.0</td>
      <td>3940</td>
      <td>13.2</td>
      <td>76</td>
      <td>usa</td>
      <td>plymouth volare premier v8</td>
    </tr>
    <tr>
      <th>84</th>
      <td>27.0</td>
      <td>4</td>
      <td>97.0</td>
      <td>88.0</td>
      <td>2100</td>
      <td>16.5</td>
      <td>72</td>
      <td>japan</td>
      <td>toyota corolla 1600 (sw)</td>
    </tr>
    <tr>
      <th>236</th>
      <td>25.5</td>
      <td>4</td>
      <td>140.0</td>
      <td>89.0</td>
      <td>2755</td>
      <td>15.8</td>
      <td>77</td>
      <td>usa</td>
      <td>ford mustang ii 2+2</td>
    </tr>
    <tr>
      <th>288</th>
      <td>18.2</td>
      <td>8</td>
      <td>318.0</td>
      <td>135.0</td>
      <td>3830</td>
      <td>15.2</td>
      <td>79</td>
      <td>usa</td>
      <td>dodge st. regis</td>
    </tr>
    <tr>
      <th>76</th>
      <td>18.0</td>
      <td>4</td>
      <td>121.0</td>
      <td>112.0</td>
      <td>2933</td>
      <td>14.5</td>
      <td>72</td>
      <td>europe</td>
      <td>volvo 145e (sw)</td>
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
      <th>19</th>
      <td>26.0</td>
      <td>4</td>
      <td>97.0</td>
      <td>46.0</td>
      <td>1835</td>
      <td>20.5</td>
      <td>70</td>
      <td>europe</td>
      <td>volkswagen 1131 deluxe sedan</td>
    </tr>
    <tr>
      <th>359</th>
      <td>28.1</td>
      <td>4</td>
      <td>141.0</td>
      <td>80.0</td>
      <td>3230</td>
      <td>20.4</td>
      <td>81</td>
      <td>europe</td>
      <td>peugeot 505s turbo diesel</td>
    </tr>
    <tr>
      <th>247</th>
      <td>39.4</td>
      <td>4</td>
      <td>85.0</td>
      <td>70.0</td>
      <td>2070</td>
      <td>18.6</td>
      <td>78</td>
      <td>japan</td>
      <td>datsun b210 gx</td>
    </tr>
    <tr>
      <th>111</th>
      <td>18.0</td>
      <td>3</td>
      <td>70.0</td>
      <td>90.0</td>
      <td>2124</td>
      <td>13.5</td>
      <td>73</td>
      <td>japan</td>
      <td>maxda rx3</td>
    </tr>
    <tr>
      <th>94</th>
      <td>13.0</td>
      <td>8</td>
      <td>440.0</td>
      <td>215.0</td>
      <td>4735</td>
      <td>11.0</td>
      <td>73</td>
      <td>usa</td>
      <td>chrysler new yorker brougham</td>
    </tr>
  </tbody>
</table>
<p>392 rows × 9 columns</p>
</div>



Selecting a range of rows for training and test.


```python
split_point = int(shuffled_data.shape[0] * 0.90)
split_point
```




    352




```python
tr = shuffled_data.iloc[:split_point]
te = shuffled_data.iloc[split_point:]
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
      <th>79</th>
      <td>26.0</td>
      <td>4</td>
      <td>96.0</td>
      <td>69.0</td>
      <td>2189</td>
      <td>18.0</td>
      <td>72</td>
      <td>europe</td>
      <td>renault 12 (sw)</td>
    </tr>
    <tr>
      <th>276</th>
      <td>21.6</td>
      <td>4</td>
      <td>121.0</td>
      <td>115.0</td>
      <td>2795</td>
      <td>15.7</td>
      <td>78</td>
      <td>europe</td>
      <td>saab 99gle</td>
    </tr>
    <tr>
      <th>248</th>
      <td>36.1</td>
      <td>4</td>
      <td>91.0</td>
      <td>60.0</td>
      <td>1800</td>
      <td>16.4</td>
      <td>78</td>
      <td>japan</td>
      <td>honda civic cvcc</td>
    </tr>
    <tr>
      <th>56</th>
      <td>26.0</td>
      <td>4</td>
      <td>91.0</td>
      <td>70.0</td>
      <td>1955</td>
      <td>20.5</td>
      <td>71</td>
      <td>usa</td>
      <td>plymouth cricket</td>
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
      <th>245</th>
      <td>36.1</td>
      <td>4</td>
      <td>98.0</td>
      <td>66.0</td>
      <td>1800</td>
      <td>14.4</td>
      <td>78</td>
      <td>usa</td>
      <td>ford fiesta</td>
    </tr>
    <tr>
      <th>55</th>
      <td>27.0</td>
      <td>4</td>
      <td>97.0</td>
      <td>60.0</td>
      <td>1834</td>
      <td>19.0</td>
      <td>71</td>
      <td>europe</td>
      <td>volkswagen model 111</td>
    </tr>
    <tr>
      <th>51</th>
      <td>30.0</td>
      <td>4</td>
      <td>79.0</td>
      <td>70.0</td>
      <td>2074</td>
      <td>19.5</td>
      <td>71</td>
      <td>europe</td>
      <td>peugeot 304</td>
    </tr>
    <tr>
      <th>176</th>
      <td>19.0</td>
      <td>6</td>
      <td>232.0</td>
      <td>90.0</td>
      <td>3211</td>
      <td>17.0</td>
      <td>75</td>
      <td>usa</td>
      <td>amc pacer</td>
    </tr>
    <tr>
      <th>191</th>
      <td>22.0</td>
      <td>6</td>
      <td>225.0</td>
      <td>100.0</td>
      <td>3233</td>
      <td>15.4</td>
      <td>76</td>
      <td>usa</td>
      <td>plymouth valiant</td>
    </tr>
  </tbody>
</table>
</div>



Checking that they add up.


```python
len(tr) + len(te) == len(data)
```




    True



### Shuffling with Numpy

We can directly shuffle the data with `numpy`, and then select the corresponding rows from our original DataFrame.


```python
np.random.seed(100) #Seting the RandomState
shuffled_indices = np.random.permutation(np.arange(len(data)))
shuffled_indices
```




    array([124, 140, 276, 252, 326, 136, 369, 132, 387, 174, 225, 356, 257,
           239, 231, 267,   7, 129, 258, 234,  43, 190, 227, 368,  75, 149,
           201, 288,  78, 163, 347, 284, 152,   1, 246, 213,  21, 110, 161,
            69,  56, 198, 160, 134,  97, 195, 255,  98,  54, 118, 361,  18,
           311,  64, 272, 295, 298, 127, 191,   5, 103, 377, 266, 346,  90,
           385, 188, 293,  96,  46,  50, 282, 248, 120, 233, 209, 187,  27,
           235, 338, 328, 352, 372, 304, 308,   6, 153, 219, 279, 121,   3,
            20, 125, 166, 307, 309,  60,  84, 342,  80, 147, 133,  31, 345,
            45,  47, 260, 150, 391,  59, 334,  23,  88, 332,  15,  33, 171,
           355, 169, 265, 386, 241, 249, 178, 362,  19,  26, 297,  35, 157,
            39, 244, 375,  10, 199, 184, 208, 367,  65, 259, 285,  41, 378,
           203, 104, 128, 216, 151, 142, 158,  40, 217,  32,  48, 327, 197,
           123, 173, 204,  61,  71, 305, 330, 126, 115, 271,  85, 159, 164,
            52, 321, 154, 205, 315,  29, 358, 139, 302, 319, 162, 111, 296,
           177, 371, 300, 175, 331, 324, 281, 339,  62, 247,  99, 269, 112,
            37, 189, 206, 374,  83, 373, 314,  51, 263, 341, 370,  42, 357,
           229, 236, 318, 179,  87, 268,  55,  22, 379, 313, 101,  11, 291,
           108, 376, 194,  25, 117,  81, 366, 275, 242, 230,  82, 292, 156,
           278, 333, 329,  74, 224, 254, 218, 306, 145, 320, 130, 113, 349,
           351, 287, 388, 353, 210,  28, 344, 221,  24, 168, 148, 380, 322,
            77, 340,  34, 144, 182, 232,  73, 301,  57, 365,  44,  92, 146,
           200, 264, 138, 223, 220,  67, 109,  12,  16,  89, 337, 243, 382,
           286, 222, 107, 186, 116, 122, 165, 262, 277,   9, 253, 196, 310,
           384, 250, 256, 102, 289,  76, 119, 237, 114,  95, 170, 381,  94,
           214,  38, 261,  36, 299, 180, 176, 360, 215, 207, 212, 325,  70,
           131, 185, 335,   0, 348,  68, 383,  17,  30, 106,  13,  72, 273,
           202, 192, 274, 172, 294, 167, 303, 238, 312, 283, 181,  63, 105,
             2, 336, 251, 183, 270, 317, 193,  49, 135, 389,  91,   4, 100,
           211, 245, 141, 364, 155,  86,  93, 137,  58, 316, 363, 228, 143,
           390, 240, 290,  14, 226,  66,  53, 354, 350,  79, 343, 359, 323,
           280,   8])




```python
data.iloc[shuffled_indices].head()
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
      <th>125</th>
      <td>20.0</td>
      <td>6</td>
      <td>198.0</td>
      <td>95.0</td>
      <td>3102</td>
      <td>16.5</td>
      <td>74</td>
      <td>usa</td>
      <td>plymouth duster</td>
    </tr>
    <tr>
      <th>142</th>
      <td>26.0</td>
      <td>4</td>
      <td>79.0</td>
      <td>67.0</td>
      <td>1963</td>
      <td>15.5</td>
      <td>74</td>
      <td>europe</td>
      <td>volkswagen dasher</td>
    </tr>
    <tr>
      <th>278</th>
      <td>31.5</td>
      <td>4</td>
      <td>89.0</td>
      <td>71.0</td>
      <td>1990</td>
      <td>14.9</td>
      <td>78</td>
      <td>europe</td>
      <td>volkswagen scirocco</td>
    </tr>
    <tr>
      <th>254</th>
      <td>20.2</td>
      <td>6</td>
      <td>200.0</td>
      <td>85.0</td>
      <td>2965</td>
      <td>15.8</td>
      <td>78</td>
      <td>usa</td>
      <td>ford fairmont (auto)</td>
    </tr>
    <tr>
      <th>328</th>
      <td>30.0</td>
      <td>4</td>
      <td>146.0</td>
      <td>67.0</td>
      <td>3250</td>
      <td>21.8</td>
      <td>80</td>
      <td>europe</td>
      <td>mercedes-benz 240d</td>
    </tr>
  </tbody>
</table>
</div>




```python
tr = data.iloc[shuffled_indices[:split_point]]
te = data.iloc[shuffled_indices[split_point:]]
```


```python
len(tr), len(te)
```




    (352, 40)



### Using SKLearn

We can use the `train_test_split` function from `sklearn.model_selection` to do this easily.


```python
from sklearn.model_selection import train_test_split
```


```python
train_test_split?
```


```python
tr, te = train_test_split(data, test_size = 0.1, random_state=83)
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



```python
Y_hat = model.predict(basic_design_matrix(te))
Y = te['mpg']
print("Test Error (RMSE):", rmse(Y, Y_hat))
```

    Test Error (RMSE): 3.6898289520141385


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

    Training Error (RMSE): 3.0333093446259105


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
KFold?
```

    Object `KFold` not found.



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




    3.1113159765045704



The following helper function generates a plot comparing all the models in the `transformations` dictionary.


```python
def compare_models(models):
    
    # Compute the training error for each model
    training_rmse = []
    for transformation, model in models.values():
        model = clone(model) #construct a clone of the model
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


<div>                            <div id="a5c3b8c0-ade1-4be3-acec-65f220dc6f3e" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("a5c3b8c0-ade1-4be3-acec-65f220dc6f3e")) {                    Plotly.newPlot(                        "a5c3b8c0-ade1-4be3-acec-65f220dc6f3e",                        [{"name":"Training RMSE","x":["quant","quant+dc"],"y":[3.3745826999424584,3.033309344625912],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc"],"y":[3.4559015156162536,3.111315976504573],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('a5c3b8c0-ade1-4be3-acec-65f220dc6f3e');
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
                           columns = oh_enc.get_feature_names(),
                           index = df.index)
    return X.join(ohe_cols)

models['quant+dc+o'] = (origin_design_matrix, LinearRegression())

origin_design_matrix(tr)
```

    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    





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
      <th>x0_europe</th>
      <th>x0_japan</th>
      <th>x0_usa</th>
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

    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    



<div>                            <div id="64bd0b1f-b5dd-47e7-a5b4-1fc443e3afae" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("64bd0b1f-b5dd-47e7-a5b4-1fc443e3afae")) {                    Plotly.newPlot(                        "64bd0b1f-b5dd-47e7-a5b4-1fc443e3afae",                        [{"name":"Training RMSE","x":["quant","quant+dc","quant+dc+o"],"y":[3.3745826999424584,3.033309344625912,3.012941172853171],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc","quant+dc+o"],"y":[3.4559015156162536,3.111315976504573,3.1207285180151905],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('64bd0b1f-b5dd-47e7-a5b4-1fc443e3afae');
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

Let's try if we can gain any information from the `name` column. This column contains the maker and model of each car. The models are fairly unique, so let's try to extract information about the brand (e.g. `ford`). The following cell shows the top 20 words that appear in this column.


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

    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    





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
      <th>x0_europe</th>
      <th>x0_japan</th>
      <th>x0_usa</th>
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

    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    
    /opt/homebrew/lib/python3.10/site-packages/sklearn/utils/deprecation.py:87: FutureWarning:
    
    Function get_feature_names is deprecated; get_feature_names is deprecated in 1.0 and will be removed in 1.2. Please use get_feature_names_out instead.
    



<div>                            <div id="6f146198-df61-446e-b77a-7f190cb96f46" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("6f146198-df61-446e-b77a-7f190cb96f46")) {                    Plotly.newPlot(                        "6f146198-df61-446e-b77a-7f190cb96f46",                        [{"name":"Training RMSE","x":["quant","quant+dc","quant+dc+o","quant+dc+o+b"],"y":[3.3745826999424584,3.033309344625912,3.012941172853171,2.8664339999878297],"type":"bar"},{"name":"CV RMSE","x":["quant","quant+dc","quant+dc+o","quant+dc+o+b"],"y":[3.4559015156162536,3.111315976504573,3.1207285180151905,3.1849476048477237],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"yaxis":{"range":[0,4],"title":{"text":"RMSE"}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('6f146198-df61-446e-b77a-7f190cb96f46');
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
