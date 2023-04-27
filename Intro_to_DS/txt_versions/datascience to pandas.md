# Mapping from `datascience` to Pandas

It serves as an introduction to working with Python's widely used Pandas library. The functions introduced will be analogous to those in  `datascience` module, with examples provided for each.

We will cover the following topics in this notebook:
1. [Basics of Pandas](#basics)
    - [Importing and Loading Packages](#import)
<br>
<br>
2. [Dataframes: Working with Tabular Data](#dataframes)
    - [Creating a Dataframe](#creating)
    - [Accessing Values in Dataframe](#accessing)
    - [Manipulating Data](#manipulating)
<br>
<br>
3. [Visualizing Data](#visualizing)
    - [Histograms](#histograms)
    - [Line Plots](#line)
    - [Scatter Plots](#scatter)
    - [Bar Plots](#bar)

## 1. Basics <a id='basics'></a>

This notebook assumes familiarity with Python concepts, syntax and data structures at the level of Data 8. For a brief refresher on some Python concepts, refer to this [Python Basics Guide on Github](https://github.com/TiesdeKok/LearnPythonforResearch/blob/master/0_python_basics.ipynb)

Python has a great ecosystem of data-centric packages which makes it excellent for data analysis. Pandas is one of those packages, and makes importing and analyzing data much easier. Pandas builds on packages like NumPy and matplotlib to give us a single, convenient, place to do most of our data analysis and visualization work.

### 1.1 Importing and Loading Packages <a id='import'></a>


```python
# run this cell to import the following packages
from datascience import * # import the datascience package
import pandas as pd # import the pandas library. pd is a common shorthand for pandas
import numpy as np # import numpy for working with numbers
```

## 2. Dataframes: Working with Tabular Data <a id='dataframes'></a>

In Python's `datascience` module, we used `Table` to build our dataframes and used commands such as `select()`, `where()`, `group()`, `column()` etc. In this section, we will go over some basic commands to work with tabular data in Pandas

### 2.1 Creating a Dataframe <a id='creating'> </a>

Pandas introduces a data structure (i.e. dataframe) that represents data as a table with columns and rows. 

In Python's `datascience` module, this is how we created tables from scratch by extending an empty table:


```python
t = Table().with_columns([
     'letter', ['a', 'b', 'c', 'z'],
     'count',  [  9,   3,   3,   1],
     'points', [  1,   2,   2,  10],
 ])
t
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>count</th> <th>points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>a     </td> <td>9    </td> <td>1     </td>
        </tr>
        <tr>
            <td>b     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>c     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>z     </td> <td>1    </td> <td>10    </td>
        </tr>
    </tbody>
</table>



In Pandas, we can use the function `pd.DataFrame` to initialize a dataframe from a dictionary or a list-like object. Refer to the [documentation](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) for more information


```python
# example: creating a dataframe from a dictionary
df_from_dict = pd.DataFrame({ 'letter' : ['a', 'b', 'c', 'z'],
                      'count' : [  9,   3,   3,   1],
                      'points' : [  1,   2,   2,  10]
                      })
df_from_dict
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
      <th>letter</th>
      <th>count</th>
      <th>points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>z</td>
      <td>1</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



More often, we will need to create a dataframe by importing data from a .csv file. In `datascience`, this is how we read data from a csv:


```python
datascience_baby = Table.read_table('baby.csv')
datascience_baby
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Unnamed: 0</th> <th>Birth.Weight</th> <th>Gestational.Days</th> <th>Maternal.Age</th> <th>Maternal.Height</th> <th>Maternal.Pregnancy.Weight</th> <th>Maternal.Smoker</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1         </td> <td>120         </td> <td>284             </td> <td>27          </td> <td>62             </td> <td>100                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>2         </td> <td>113         </td> <td>282             </td> <td>33          </td> <td>64             </td> <td>135                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>3         </td> <td>128         </td> <td>279             </td> <td>28          </td> <td>64             </td> <td>115                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>4         </td> <td>108         </td> <td>282             </td> <td>23          </td> <td>67             </td> <td>125                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>5         </td> <td>136         </td> <td>286             </td> <td>25          </td> <td>62             </td> <td>93                       </td> <td>False          </td>
        </tr>
        <tr>
            <td>6         </td> <td>138         </td> <td>244             </td> <td>33          </td> <td>62             </td> <td>178                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>7         </td> <td>132         </td> <td>245             </td> <td>23          </td> <td>65             </td> <td>140                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>8         </td> <td>120         </td> <td>289             </td> <td>25          </td> <td>62             </td> <td>125                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>9         </td> <td>143         </td> <td>299             </td> <td>30          </td> <td>66             </td> <td>136                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>10        </td> <td>140         </td> <td>351             </td> <td>27          </td> <td>68             </td> <td>120                      </td> <td>False          </td>
        </tr>
    </tbody>
</table>
<p>... (1164 rows omitted)</p>



In Pandas, we use `pd.read.csv()` to read data from a csv file. Sometimes, depending on the data file, we may need to specify the parameters `sep`, `header` or `encoding` as well. For a full list of parameters, refer to [this guide](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)


```python
# reading baby.csv (located in current working directory)
baby = pd.read_csv('baby.csv')
baby.head() # display first few rows of dataframe
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
      <th>Unnamed: 0</th>
      <th>Birth.Weight</th>
      <th>Gestational.Days</th>
      <th>Maternal.Age</th>
      <th>Maternal.Height</th>
      <th>Maternal.Pregnancy.Weight</th>
      <th>Maternal.Smoker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>120</td>
      <td>284</td>
      <td>27</td>
      <td>62</td>
      <td>100</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>113</td>
      <td>282</td>
      <td>33</td>
      <td>64</td>
      <td>135</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>128</td>
      <td>279</td>
      <td>28</td>
      <td>64</td>
      <td>115</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>108</td>
      <td>282</td>
      <td>23</td>
      <td>67</td>
      <td>125</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>136</td>
      <td>286</td>
      <td>25</td>
      <td>62</td>
      <td>93</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv?
```


```python
# view summary of data
baby.describe()
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
      <th>Unnamed: 0</th>
      <th>Birth.Weight</th>
      <th>Gestational.Days</th>
      <th>Maternal.Age</th>
      <th>Maternal.Height</th>
      <th>Maternal.Pregnancy.Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1174.000000</td>
      <td>1174.000000</td>
      <td>1174.000000</td>
      <td>1174.000000</td>
      <td>1174.000000</td>
      <td>1174.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>587.500000</td>
      <td>119.462521</td>
      <td>279.101363</td>
      <td>27.228279</td>
      <td>64.049404</td>
      <td>128.478705</td>
    </tr>
    <tr>
      <th>std</th>
      <td>339.048915</td>
      <td>18.328671</td>
      <td>16.010305</td>
      <td>5.817839</td>
      <td>2.526102</td>
      <td>20.734282</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>55.000000</td>
      <td>148.000000</td>
      <td>15.000000</td>
      <td>53.000000</td>
      <td>87.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>294.250000</td>
      <td>108.000000</td>
      <td>272.000000</td>
      <td>23.000000</td>
      <td>62.000000</td>
      <td>114.250000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>587.500000</td>
      <td>120.000000</td>
      <td>280.000000</td>
      <td>26.000000</td>
      <td>64.000000</td>
      <td>125.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>880.750000</td>
      <td>131.000000</td>
      <td>288.000000</td>
      <td>31.000000</td>
      <td>66.000000</td>
      <td>139.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1174.000000</td>
      <td>176.000000</td>
      <td>353.000000</td>
      <td>45.000000</td>
      <td>72.000000</td>
      <td>250.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# example: loading csv from URL
sat = pd.read_csv('https://raw.githubusercontent.com/data-8/materials-sp18/master/lec/sat2014.csv')
sat.head()
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
      <th>State</th>
      <th>Participation Rate</th>
      <th>Critical Reading</th>
      <th>Math</th>
      <th>Writing</th>
      <th>Combined</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>North Dakota</td>
      <td>2.3</td>
      <td>612</td>
      <td>620</td>
      <td>584</td>
      <td>1816</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Illinois</td>
      <td>4.6</td>
      <td>599</td>
      <td>616</td>
      <td>587</td>
      <td>1802</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Iowa</td>
      <td>3.1</td>
      <td>605</td>
      <td>611</td>
      <td>578</td>
      <td>1794</td>
    </tr>
    <tr>
      <th>3</th>
      <td>South Dakota</td>
      <td>2.9</td>
      <td>604</td>
      <td>609</td>
      <td>579</td>
      <td>1792</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Minnesota</td>
      <td>5.9</td>
      <td>598</td>
      <td>610</td>
      <td>578</td>
      <td>1786</td>
    </tr>
  </tbody>
</table>
</div>




```python
# view information about dataframe
print(sat.shape) # view dimensions (rows, cols)
print(sat.columns.values) # view column names
```

    (51, 6)
    ['State' 'Participation Rate' 'Critical Reading' 'Math' 'Writing'
     'Combined']


### 2.2 Accessing Values in Dataframe <a id='accessing'> </a>

In `datascience`, we can use `column()` to access values in a particular column as follows:


```python
# access column 'letter'. returns array
t.column('letter')
```




    array(['a', 'b', 'c', 'z'], dtype='<U1')



In Pandas, columns are also known as Series. We can access a Pandas series by using the square bracket notation.


```python
# returns Series object
sat['State'].describe()
```




    count           51
    unique          51
    top       Michigan
    freq             1
    Name: State, dtype: object




```python

```

If we want a numpy array of column values, we can call the method `values` on a Series object:


```python
sat['State'].values
```




    array(['North Dakota', 'Illinois', 'Iowa', 'South Dakota', 'Minnesota',
           'Michigan', 'Wisconsin', 'Missouri', 'Wyoming', 'Kansas',
           'Kentucky', 'Nebraska', 'Colorado', 'Mississippi', 'Tennessee',
           'Arkansas', 'Oklahoma', 'Utah', 'Louisiana', 'Ohio', 'Montana',
           'Alabama', 'New Mexico', 'New Hampshire', 'Massachusetts',
           'Vermont', 'Arizona', 'Oregon', 'Virginia', 'New Jersey',
           'Connecticut', 'West Virginia', 'Washington', 'California',
           'Alaska', 'North Carolina', 'Pennsylvania', 'Rhode Island',
           'Indiana', 'Maryland', 'New York', 'Hawaii', 'Nevada', 'Florida',
           'Georgia', 'South Carolina', 'Texas', 'Maine', 'Idaho', 'Delaware',
           'District of Columbia'], dtype=object)



In `datascience`, we used `take()` to access a row in the Table:


```python
# selecting first two rows using Python's slicing notation
t.take[0:2]
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>count</th> <th>points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>a     </td> <td>9    </td> <td>1     </td>
        </tr>
        <tr>
            <td>b     </td> <td>3    </td> <td>2     </td>
        </tr>
    </tbody>
</table>



In Pandas, we can access rows and column by their position using the `iloc` method. We need to specify the rows and columns we want in the following syntax: `df.iloc[<rows>, <columns>]`. For more information on indexing, refer to [this guide](https://pandas.pydata.org/pandas-docs/stable/indexing.html)


```python
# selecting first two rows using iloc
baby.iloc[0:2, :] 
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
      <th>Unnamed: 0</th>
      <th>Birth.Weight</th>
      <th>Gestational.Days</th>
      <th>Maternal.Age</th>
      <th>Maternal.Height</th>
      <th>Maternal.Pregnancy.Weight</th>
      <th>Maternal.Smoker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>120</td>
      <td>284</td>
      <td>27</td>
      <td>62</td>
      <td>100</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>113</td>
      <td>282</td>
      <td>33</td>
      <td>64</td>
      <td>135</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
# specifying row indices
baby.iloc[[1, 4, 6], :]
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
      <th>Unnamed: 0</th>
      <th>Birth.Weight</th>
      <th>Gestational.Days</th>
      <th>Maternal.Age</th>
      <th>Maternal.Height</th>
      <th>Maternal.Pregnancy.Weight</th>
      <th>Maternal.Smoker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>113</td>
      <td>282</td>
      <td>33</td>
      <td>64</td>
      <td>135</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>136</td>
      <td>286</td>
      <td>25</td>
      <td>62</td>
      <td>93</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>132</td>
      <td>245</td>
      <td>23</td>
      <td>65</td>
      <td>140</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



We can also access a specific value in the dataframe by passing in the row and column indices:


```python
# get value in second row, third column
baby.iloc[1, 2]
```




    282



### 2.3 Manipulating Data <a id='manipulating'></a>

**Adding Columns**

Adding a new column in `datascience` is done by the `with_column()` function as follows:


```python
t.with_column('vowel', ['yes', 'no', 'no', 'no'])
t
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>count</th> <th>points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>a     </td> <td>9    </td> <td>1     </td>
        </tr>
        <tr>
            <td>b     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>c     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>z     </td> <td>1    </td> <td>10    </td>
        </tr>
    </tbody>
</table>



In Pandas, we can use the bracket notation and assign a list to add to the dataframe as follows:


```python
# adding a new column
df_from_dict['newcol'] = [5, 6, 7, 8]
df_from_dict
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
      <th>letter</th>
      <th>count</th>
      <th>points</th>
      <th>newcol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>9</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>3</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>z</td>
      <td>1</td>
      <td>10</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



We can also add an existing column to the new dataframe as a new column by performing an operation on it:


```python
# adding count * 2 to the dataframe
df_from_dict['doublecount'] = df_from_dict['count'] * 2
df_from_dict
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
      <th>letter</th>
      <th>count</th>
      <th>points</th>
      <th>newcol</th>
      <th>doublecount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>9</td>
      <td>1</td>
      <td>5</td>
      <td>18</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>3</td>
      <td>2</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>z</td>
      <td>1</td>
      <td>10</td>
      <td>8</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



**Selecting Columns**

In `datascience`, we used `select()` to subset the dataframe by selecting columns:


```python
t.select(['letter', 'points'])
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>a     </td> <td>1     </td>
        </tr>
        <tr>
            <td>b     </td> <td>2     </td>
        </tr>
        <tr>
            <td>c     </td> <td>2     </td>
        </tr>
        <tr>
            <td>z     </td> <td>10    </td>
        </tr>
    </tbody>
</table>



In Pandas, we use a double bracket notation to select columns. This returns a dataframe, unlike a Series object when we only use single bracket notation


```python
# double bracket notation for new dataframe
df_from_dict[['count', 'doublecount']]
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
      <th>count</th>
      <th>doublecount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>18</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



**Filtering Rows Conditionally**

In `datascience`, we used `where()` to select rows according to a given condition:


```python
t.where('points', 2) # rows where points == 2
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>count</th> <th>points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>b     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>c     </td> <td>3    </td> <td>2     </td>
        </tr>
    </tbody>
</table>




```python
t.where(t['count'] < 8) # rows where count < 8
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>count</th> <th>points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>b     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>c     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>z     </td> <td>1    </td> <td>10    </td>
        </tr>
    </tbody>
</table>



In Pandas, we can use the bracket notation to subset the dataframe based on a condition. We first specify a condition and then subset using the bracket notation:


```python
# array of booleans
baby['Maternal.Smoker'] == True
```




    0       False
    1       False
    2        True
    3        True
    4       False
            ...  
    1169    False
    1170    False
    1171     True
    1172    False
    1173    False
    Name: Maternal.Smoker, Length: 1174, dtype: bool




```python
# filter rows by condition Maternal.Smoker == True
baby[baby['Maternal.Smoker'] == True]
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
      <th>Unnamed: 0</th>
      <th>Birth.Weight</th>
      <th>Gestational.Days</th>
      <th>Maternal.Age</th>
      <th>Maternal.Height</th>
      <th>Maternal.Pregnancy.Weight</th>
      <th>Maternal.Smoker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>128</td>
      <td>279</td>
      <td>28</td>
      <td>64</td>
      <td>115</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>108</td>
      <td>282</td>
      <td>23</td>
      <td>67</td>
      <td>125</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>143</td>
      <td>299</td>
      <td>30</td>
      <td>66</td>
      <td>136</td>
      <td>True</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>144</td>
      <td>282</td>
      <td>32</td>
      <td>64</td>
      <td>124</td>
      <td>True</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>141</td>
      <td>279</td>
      <td>23</td>
      <td>63</td>
      <td>128</td>
      <td>True</td>
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
      <th>1162</th>
      <td>1163</td>
      <td>143</td>
      <td>281</td>
      <td>28</td>
      <td>65</td>
      <td>135</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1163</th>
      <td>1164</td>
      <td>113</td>
      <td>287</td>
      <td>29</td>
      <td>70</td>
      <td>145</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1164</th>
      <td>1165</td>
      <td>109</td>
      <td>244</td>
      <td>21</td>
      <td>63</td>
      <td>102</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1165</th>
      <td>1166</td>
      <td>103</td>
      <td>278</td>
      <td>30</td>
      <td>60</td>
      <td>87</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1171</th>
      <td>1172</td>
      <td>130</td>
      <td>291</td>
      <td>30</td>
      <td>65</td>
      <td>150</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>459 rows × 7 columns</p>
</div>




```python
# filtering with multiple conditions
baby[(baby['Maternal.Smoker'] == True) & (baby['Birth.Weight'] > 120)]
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
      <th>Unnamed: 0</th>
      <th>Birth.Weight</th>
      <th>Gestational.Days</th>
      <th>Maternal.Age</th>
      <th>Maternal.Height</th>
      <th>Maternal.Pregnancy.Weight</th>
      <th>Maternal.Smoker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>128</td>
      <td>279</td>
      <td>28</td>
      <td>64</td>
      <td>115</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>143</td>
      <td>299</td>
      <td>30</td>
      <td>66</td>
      <td>136</td>
      <td>True</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>144</td>
      <td>282</td>
      <td>32</td>
      <td>64</td>
      <td>124</td>
      <td>True</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>141</td>
      <td>279</td>
      <td>23</td>
      <td>63</td>
      <td>128</td>
      <td>True</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>134</td>
      <td>288</td>
      <td>23</td>
      <td>63</td>
      <td>92</td>
      <td>True</td>
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
      <th>1145</th>
      <td>1146</td>
      <td>127</td>
      <td>242</td>
      <td>17</td>
      <td>61</td>
      <td>135</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1147</th>
      <td>1148</td>
      <td>141</td>
      <td>281</td>
      <td>29</td>
      <td>54</td>
      <td>156</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1160</th>
      <td>1161</td>
      <td>124</td>
      <td>288</td>
      <td>21</td>
      <td>64</td>
      <td>116</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1162</th>
      <td>1163</td>
      <td>143</td>
      <td>281</td>
      <td>28</td>
      <td>65</td>
      <td>135</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1171</th>
      <td>1172</td>
      <td>130</td>
      <td>291</td>
      <td>30</td>
      <td>65</td>
      <td>150</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>162 rows × 7 columns</p>
</div>



**Renaming Columns**

In `datascience`, we used `relabeled()` to rename columns:


```python
# rename 'points' to 'other name'
t.relabeled('points', 'other name')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>count</th> <th>other name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>a     </td> <td>9    </td> <td>1         </td>
        </tr>
        <tr>
            <td>b     </td> <td>3    </td> <td>2         </td>
        </tr>
        <tr>
            <td>c     </td> <td>3    </td> <td>2         </td>
        </tr>
        <tr>
            <td>z     </td> <td>1    </td> <td>10        </td>
        </tr>
    </tbody>
</table>



Pandas uses `rename()`, which has an `index` parameter that needs to be set to `str` and a `columns` parameter that needs to be set to a dictionary of the names to be replaced with their replacements:


```python
# rename 'points' to 'other name'
df_from_dict.rename(index = str, columns = {"points" : "other name"})
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
      <th>letter</th>
      <th>count</th>
      <th>other name</th>
      <th>newcol</th>
      <th>doublecount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>9</td>
      <td>1</td>
      <td>5</td>
      <td>18</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>3</td>
      <td>2</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>z</td>
      <td>1</td>
      <td>10</td>
      <td>8</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



**Sorting Dataframe by Column**

In `datascience` we used `sort()` to sort a Table according to the values in a column:


```python
# sort by count
t.sort('count')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>letter</th> <th>count</th> <th>points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>z     </td> <td>1    </td> <td>10    </td>
        </tr>
        <tr>
            <td>b     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>c     </td> <td>3    </td> <td>2     </td>
        </tr>
        <tr>
            <td>a     </td> <td>9    </td> <td>1     </td>
        </tr>
    </tbody>
</table>



In Pandas, we use the `sort_values()` to sort by column. We need the `by` parameter to specify the row we want to sort by and the optional parameter `ascending = False` if we want to sort in descending order:


```python
# sort by count, descending
df_from_dict.sort_values(by = ['count'], ascending = False)
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
      <th>letter</th>
      <th>count</th>
      <th>points</th>
      <th>newcol</th>
      <th>doublecount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>9</td>
      <td>1</td>
      <td>5</td>
      <td>18</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>3</td>
      <td>2</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>z</td>
      <td>1</td>
      <td>10</td>
      <td>8</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



**Grouping and Aggregating**

In `datascience`, we used `group()` and the `collect` argument to group a Table by a column and aggregrate values in another column:


```python
baby['Maternal.Smoker'].unique()
```




    array([False,  True])




```python
# group by count and aggregate by sum
t.select(['count', 'points']).group('count', collect=sum)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>count</th> <th>points sum</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1    </td> <td>10        </td>
        </tr>
        <tr>
            <td>3    </td> <td>4         </td>
        </tr>
        <tr>
            <td>9    </td> <td>1         </td>
        </tr>
    </tbody>
</table>



In Pandas, we use `groupby()` to group the dataframe. This function returns a groupby object, on which we can then call an aggregation function to return a dataframe with aggregated values for other columns. For more information, refer to the [documentation](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html)


```python
# selecting two columns for brevity
df_subset = df_from_dict[['count', 'points']]
df_subset
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
      <th>count</th>
      <th>points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
count_sums_df = df_subset.groupby(['count']).sum()
count_sums_df
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
      <th>points</th>
    </tr>
    <tr>
      <th>count</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



For Series, the `value_counts` method is often quite handy.


```python
baby['Maternal.Age'].value_counts()
```




    23    90
    24    83
    26    82
    27    80
    22    77
    25    75
    21    65
    28    64
    30    61
    29    61
    20    57
    19    49
    33    42
    31    41
    32    36
    34    31
    35    29
    37    27
    36    24
    39    22
    38    18
    18    15
    41    14
    40    11
    17     7
    43     6
    42     4
    45     1
    44     1
    15     1
    Name: Maternal.Age, dtype: int64



Also commonly used is the `unique` method, which returns all unique values as a numpy array.


```python
baby['Maternal.Age'].unique()
```




    array([27, 33, 28, 23, 25, 30, 32, 36, 38, 43, 22, 26, 20, 34, 24, 37, 31,
           21, 39, 35, 29, 19, 42, 40, 18, 17, 41, 15, 44, 45], dtype=int64)




```python

```


```python

```

**Pivot Tables**

In `datascience`, we used the `pivot()` function to build contingency tables:


```python
# creating new Table
cones_tbl = Table().with_columns(
    'Flavor', make_array('strawberry', 'chocolate', 'chocolate', 'strawberry', 'chocolate', 'bubblegum'),
    'Color', make_array('pink', 'light brown', 'dark brown', 'pink', 'dark brown', 'pink'),
    'Price', make_array(3.55, 4.75, 5.25, 5.25, 5.25, 4.75)
)

cones_tbl
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>3.55 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td> <td>4.75 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>bubblegum </td> <td>pink       </td> <td>4.75 </td>
        </tr>
    </tbody>
</table>




```python
# pivoting on color and flavor
cones_tbl.pivot("Flavor", "Color")
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Color</th> <th>bubblegum</th> <th>chocolate</th> <th>strawberry</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>dark brown </td> <td>0        </td> <td>2        </td> <td>0         </td>
        </tr>
        <tr>
            <td>light brown</td> <td>0        </td> <td>1        </td> <td>0         </td>
        </tr>
        <tr>
            <td>pink       </td> <td>1        </td> <td>0        </td> <td>2         </td>
        </tr>
    </tbody>
</table>



We can also pass in the parameters `values` to specify the values in the table and `collect` to specify the aggregration function.


```python
# setting parameters values and collect
cones_tbl.pivot("Flavor", "Color", values = "Price", collect = np.sum)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Color</th> <th>bubblegum</th> <th>chocolate</th> <th>strawberry</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>dark brown </td> <td>0        </td> <td>10.5     </td> <td>0         </td>
        </tr>
        <tr>
            <td>light brown</td> <td>0        </td> <td>4.75     </td> <td>0         </td>
        </tr>
        <tr>
            <td>pink       </td> <td>4.75     </td> <td>0        </td> <td>8.8       </td>
        </tr>
    </tbody>
</table>



In Pandas, we use `pd.pivot_table()` to create a contingency table. The argument `columns` is similar to the first argument in `datascience`'s `pivot` function and sets the column names of the pivot table. The argument `index` is similar to the second argument in `datascience`'s `pivot` function and sets the first column of the pivot table or the keys to group on. For more information, refer to the [documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html)


```python
# creating new dataframe
cones_df = pd.DataFrame({"Flavor" : ['strawberry', 'chocolate', 'chocolate', 'strawberry', 'chocolate', 'bubblegum'],
                         "Color" : ['pink', 'light brown', 'dark brown', 'pink', 'dark brown', 'pink'],
                         "Price" : [3.55, 4.75, 5.25, 5.25, 5.25, 4.75]})
cones_df
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
      <th>Flavor</th>
      <th>Color</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>strawberry</td>
      <td>pink</td>
      <td>3.55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chocolate</td>
      <td>light brown</td>
      <td>4.75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>chocolate</td>
      <td>dark brown</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>strawberry</td>
      <td>pink</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chocolate</td>
      <td>dark brown</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bubblegum</td>
      <td>pink</td>
      <td>4.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
# creating the pivot table
pd.pivot_table(cones_df, columns = ["Flavor"], index = ["Color"])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">Price</th>
    </tr>
    <tr>
      <th>Flavor</th>
      <th>bubblegum</th>
      <th>chocolate</th>
      <th>strawberry</th>
    </tr>
    <tr>
      <th>Color</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>dark brown</th>
      <td>NaN</td>
      <td>5.25</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>light brown</th>
      <td>NaN</td>
      <td>4.75</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>pink</th>
      <td>4.75</td>
      <td>NaN</td>
      <td>4.4</td>
    </tr>
  </tbody>
</table>
</div>



If there is no data in the groups, then Pandas will output `NaN` values. 

We can also specify the parameters like `values` (equivalent to `values` in `datascience`'s `pivot`) and `aggfunc` (equivalent to `collect` in `datascience`'s `pivot`)


```python
# additional arguments
pd.pivot_table(cones_df, columns = ["Flavor"], index = ["Color"], values = "Price", aggfunc=np.sum)
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
      <th>Flavor</th>
      <th>bubblegum</th>
      <th>chocolate</th>
      <th>strawberry</th>
    </tr>
    <tr>
      <th>Color</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>dark brown</th>
      <td>NaN</td>
      <td>10.50</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>light brown</th>
      <td>NaN</td>
      <td>4.75</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>pink</th>
      <td>4.75</td>
      <td>NaN</td>
      <td>8.8</td>
    </tr>
  </tbody>
</table>
</div>



**Joining/Merging**

In `datascience`, we used `join()` to join two tables based on shared values in columns. We specify the column name in the first table to match on, the name of the second table and the column name in the second table to match on.


```python
# creating new table
ratings_tbl = Table().with_columns(
    'Kind', make_array('strawberry', 'chocolate', 'vanilla'),
    'Stars', make_array(2.5, 3.5, 4)
)
ratings_tbl
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Kind</th> <th>Stars</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td> <td>2.5  </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>3.5  </td>
        </tr>
        <tr>
            <td>vanilla   </td> <td>4    </td>
        </tr>
    </tbody>
</table>




```python
# joining cones and ratings
cones_tbl.join("Flavor", ratings_tbl, "Kind")
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>Price</th> <th>Stars</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate </td> <td>light brown</td> <td>4.75 </td> <td>3.5  </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>5.25 </td> <td>3.5  </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td> <td>5.25 </td> <td>3.5  </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>3.55 </td> <td>2.5  </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>5.25 </td> <td>2.5  </td>
        </tr>
    </tbody>
</table>



In Pandas, we can use the `merge()` function to join two tables together. The first parameter is the name of the second table to join on. The parameters `left_on` and `right_on` specify the columns to use in the left and right tables respectively. There are more parameters such as `how` which specify what kind of join to perform (Inner (Default), Outer, Left, Right). For more information, refer to this [Kaggle Tutorial](https://www.kaggle.com/crawford/python-merge-tutorial/notebook)


```python
# creating new ratings df
ratings_df = pd.DataFrame({"Kind" : ['strawberry', 'chocolate', 'vanilla'],
                           "Stars" : [2.5, 3.5, 4]})
ratings_df
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
      <th>Kind</th>
      <th>Stars</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>strawberry</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chocolate</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>vanilla</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# merging cones and ratings
cones_df.merge(ratings_df, left_on = "Flavor", right_on = "Kind")
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
      <th>Flavor</th>
      <th>Color</th>
      <th>Price</th>
      <th>Kind</th>
      <th>Stars</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>strawberry</td>
      <td>pink</td>
      <td>3.55</td>
      <td>strawberry</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>strawberry</td>
      <td>pink</td>
      <td>5.25</td>
      <td>strawberry</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>chocolate</td>
      <td>light brown</td>
      <td>4.75</td>
      <td>chocolate</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>chocolate</td>
      <td>dark brown</td>
      <td>5.25</td>
      <td>chocolate</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chocolate</td>
      <td>dark brown</td>
      <td>5.25</td>
      <td>chocolate</td>
      <td>3.5</td>
    </tr>
  </tbody>
</table>
</div>



## 3. Visualizing Data <a id='visualizing'> </a>

In `datascience`, we learned to plot data using histograms, line plots, scatter plots and histograms. The corresponding functions were `hist()`, `plot()`, `scatter()` and `barh()`. Plotting methods in Pandas are nearly identical to `datascience` since both build on the library `matplotlib`

In this section we will go through examples of such plots in Pandas

<a id='histograms'></a>**3.1 Histograms**

In `datascience`, we used `hist()` to create a histogram. In this example, we will be using data from `baby.csv`. Recall that the baby data set contains data on a random sample of 1,174 mothers and their newborn babies. The column `Birth.Weight` contains the birth weight of the baby, in ounces; `Gestational.Days` is the number of gestational days, that is, the number of days the baby was in the womb. There is also data on maternal age, maternal height, maternal pregnancy weight, and whether or not the mother was a smoker.


```python
# importing matplotlib for plotting
import matplotlib
matplotlib.use('Agg', warn=False)
%matplotlib inline
```

    <ipython-input-46-1dd03428a63c>:3: MatplotlibDeprecationWarning: The 'warn' parameter of use() is deprecated since Matplotlib 3.1 and will be removed in 3.3.  If any parameter follows 'warn', they should be pass as keyword, not positionally.
      matplotlib.use('Agg', warn=False)



```python
# reading in the data
datascience_baby = Table.read_table('baby.csv')
datascience_baby
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Unnamed: 0</th> <th>Birth.Weight</th> <th>Gestational.Days</th> <th>Maternal.Age</th> <th>Maternal.Height</th> <th>Maternal.Pregnancy.Weight</th> <th>Maternal.Smoker</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1         </td> <td>120         </td> <td>284             </td> <td>27          </td> <td>62             </td> <td>100                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>2         </td> <td>113         </td> <td>282             </td> <td>33          </td> <td>64             </td> <td>135                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>3         </td> <td>128         </td> <td>279             </td> <td>28          </td> <td>64             </td> <td>115                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>4         </td> <td>108         </td> <td>282             </td> <td>23          </td> <td>67             </td> <td>125                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>5         </td> <td>136         </td> <td>286             </td> <td>25          </td> <td>62             </td> <td>93                       </td> <td>False          </td>
        </tr>
        <tr>
            <td>6         </td> <td>138         </td> <td>244             </td> <td>33          </td> <td>62             </td> <td>178                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>7         </td> <td>132         </td> <td>245             </td> <td>23          </td> <td>65             </td> <td>140                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>8         </td> <td>120         </td> <td>289             </td> <td>25          </td> <td>62             </td> <td>125                      </td> <td>False          </td>
        </tr>
        <tr>
            <td>9         </td> <td>143         </td> <td>299             </td> <td>30          </td> <td>66             </td> <td>136                      </td> <td>True           </td>
        </tr>
        <tr>
            <td>10        </td> <td>140         </td> <td>351             </td> <td>27          </td> <td>68             </td> <td>120                      </td> <td>False          </td>
        </tr>
    </tbody>
</table>
<p>... (1164 rows omitted)</p>




```python
# creating a histogram
datascience_baby.hist('Birth.Weight')
```


    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_95_0.png)
    


In Pandas, we use `hist()` to create histograms, just like `datascience`. Refer to the [documentation](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.hist.html) for a full list of parameters


```python
# creating a histogram
baby.hist('Birth.Weight')
```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x0000027B61C2F9D0>]],
          dtype=object)




    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_97_1.png)
    


<a id='line'></a>**3.2 Line Plots**

In `datascience`, we used `plot()` to create a line plot of numerical values. In this example, we will be using census data and plot variables such as Age in a line plot


```python
# line plot in datascience
census_tbl = Table.read_table("https://raw.githubusercontent.com/data-8/materials-x18/master/lec/x18/1/census.csv").select(['SEX', 'AGE', 'POPESTIMATE2014'])
children_tbl = census_tbl.where('SEX', are.equal_to(0)).where('AGE', are.below(19)).drop('SEX')
children_tbl.plot('AGE')
```


    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_99_0.png)
    


In Pandas, we can use `plot.line()` to create line plots. For a full list of parameters, refer to the [documentation](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.plot.line.html)


```python
#Pandas
census_df = pd.read_csv("https://raw.githubusercontent.com/data-8/materials-x18/master/lec/x18/1/census.csv")[["SEX", "AGE", "POPESTIMATE2014"]]
children_df = census_df[(census_df.SEX == 0) & (census_df.AGE < 19)].drop("SEX", axis=1)
children_df.plot.line(x="AGE", y="POPESTIMATE2014")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x27b61d588b0>




    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_101_1.png)
    


<a id='scatter'></a>**3.3 Scatter Plots**

In `datascience`, we used `scatter()` to create a scatter plot of two numerical columns


```python
football_tbl = Table.read_table('https://raw.githubusercontent.com/data-8/materials-sp18/master/lec/deflategate.csv')
football_tbl
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Team</th> <th>Blakeman</th> <th>Prioleau</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Patriots</td> <td>11.5    </td> <td>11.8    </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>10.85   </td> <td>11.2    </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>11.15   </td> <td>11.5    </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>10.7    </td> <td>11      </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>11.1    </td> <td>11.45   </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>11.6    </td> <td>11.95   </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>11.85   </td> <td>12.3    </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>11.1    </td> <td>11.55   </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>10.95   </td> <td>11.35   </td>
        </tr>
        <tr>
            <td>Patriots</td> <td>10.5    </td> <td>10.9    </td>
        </tr>
    </tbody>
</table>
<p>... (5 rows omitted)</p>




```python
football_tbl.scatter('Blakeman', 'Prioleau')
```


    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_104_0.png)
    


In Pandas, we use `plot.scatter()` to create a scatter plot. For a full list of parameters, refer to the [documentation](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.plot.scatter.html)


```python
football_df = pd.read_csv('https://raw.githubusercontent.com/data-8/materials-sp18/master/lec/deflategate.csv')
football_df.plot.scatter(x="Blakeman", y="Prioleau")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x27b61e04100>




    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_106_1.png)
    


<a id='bar'></a>**3.4 Bar Plots**

In `datascience`, we used `barh()` to create a horizontal bar plot


```python
t.barh("letter", "points")
```


    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_108_0.png)
    


In Pandas, we use `plot.barh()` to create a bar chart. For a full list of parameters, refer to the [documentation](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.plot.barh.html)


```python
df_from_dict.plot.barh(x='letter', y='points')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x27b61eab400>




    
![png](datascience%20to%20pandas_files/datascience%20to%20pandas_110_1.png)
    


---

## Further Reading

Here is a list of useful Pandas resources:

- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Dataquest Pandas Tutorial](https://www.dataquest.io/blog/pandas-python-tutorial/)
- [Pandas Cookbook](http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/tree/master/cookbook/)
