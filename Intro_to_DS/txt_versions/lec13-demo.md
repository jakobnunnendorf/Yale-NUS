# Pandas Basics

A high-level overview of the [Pandas](https://pandas.pydata.org) library.


```python
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.style.use('fivethirtyeight')
sns.set_context("notebook")
```

## Reading in DataFrames from Files

Pandas has a number of very useful file reading tools. You can see them enumerated by typing "pd.re" and pressing tab. We'll be using read_csv today. 


```python
elections = pd.read_csv("elections.csv")
elections 
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Year</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Clinton</td>
      <td>Democratic</td>
      <td>43.0</td>
      <td>1992</td>
      <td>win</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>37.4</td>
      <td>1992</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Perot</td>
      <td>Independent</td>
      <td>18.9</td>
      <td>1992</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Clinton</td>
      <td>Democratic</td>
      <td>49.2</td>
      <td>1996</td>
      <td>win</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Dole</td>
      <td>Republican</td>
      <td>40.7</td>
      <td>1996</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Perot</td>
      <td>Independent</td>
      <td>8.4</td>
      <td>1996</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Gore</td>
      <td>Democratic</td>
      <td>48.4</td>
      <td>2000</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>47.9</td>
      <td>2000</td>
      <td>win</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Kerry</td>
      <td>Democratic</td>
      <td>48.3</td>
      <td>2004</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>2004</td>
      <td>win</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Obama</td>
      <td>Democratic</td>
      <td>52.9</td>
      <td>2008</td>
      <td>win</td>
    </tr>
    <tr>
      <th>18</th>
      <td>McCain</td>
      <td>Republican</td>
      <td>45.7</td>
      <td>2008</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Obama</td>
      <td>Democratic</td>
      <td>51.1</td>
      <td>2012</td>
      <td>win</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Romney</td>
      <td>Republican</td>
      <td>47.2</td>
      <td>2012</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Clinton</td>
      <td>Democratic</td>
      <td>48.2</td>
      <td>2016</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Trump</td>
      <td>Republican</td>
      <td>46.1</td>
      <td>2016</td>
      <td>win</td>
    </tr>
  </tbody>
</table>
</div>



We can use the head command to return only a few rows of a dataframe.


```python
elections.head(10)
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Year</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Clinton</td>
      <td>Democratic</td>
      <td>43.0</td>
      <td>1992</td>
      <td>win</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>37.4</td>
      <td>1992</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Perot</td>
      <td>Independent</td>
      <td>18.9</td>
      <td>1992</td>
      <td>loss</td>
    </tr>
  </tbody>
</table>
</div>



There is also a tail command.


```python
elections.tail(7)
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Year</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>2004</td>
      <td>win</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Obama</td>
      <td>Democratic</td>
      <td>52.9</td>
      <td>2008</td>
      <td>win</td>
    </tr>
    <tr>
      <th>18</th>
      <td>McCain</td>
      <td>Republican</td>
      <td>45.7</td>
      <td>2008</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Obama</td>
      <td>Democratic</td>
      <td>51.1</td>
      <td>2012</td>
      <td>win</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Romney</td>
      <td>Republican</td>
      <td>47.2</td>
      <td>2012</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Clinton</td>
      <td>Democratic</td>
      <td>48.2</td>
      <td>2016</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Trump</td>
      <td>Republican</td>
      <td>46.1</td>
      <td>2016</td>
      <td>win</td>
    </tr>
  </tbody>
</table>
</div>



The read_csv command lets us specify a column to use an index. For example, we could have used Year as the index.


```python
elections_year_index = pd.read_csv("elections.csv", index_col = "Year")
elections_year_index.head(5)
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Result</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1984</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1984</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>loss</td>
    </tr>
  </tbody>
</table>
</div>



Alternately, we could have used the set_index commmand.


```python
elections_party_index = elections.set_index("Party")
elections_party_index.head(5)
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
      <th>Candidate</th>
      <th>%</th>
      <th>Year</th>
      <th>Result</th>
    </tr>
    <tr>
      <th>Party</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Republican</th>
      <td>Reagan</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>Democratic</th>
      <td>Carter</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>Independent</th>
      <td>Anderson</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>Republican</th>
      <td>Reagan</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>Democratic</th>
      <td>Mondale</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
  </tbody>
</table>
</div>



The set_index command (along with all other data frame methods) does not modify the dataframe. That is, the original "elections" is untouched. Note: There is a flag called "inplace" which does modify the calling dataframe.


```python
elections.head() #the index remains unchanged
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Year</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
  </tbody>
</table>
</div>



By contrast, column names are ideally unique. For example, if we try to read in a file for which column names are not unique, Pandas will automatically rename any duplicates.


```python
dups = pd.read_csv("duplicate_columns.csv")
dups
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
      <th>name</th>
      <th>name.1</th>
      <th>flavor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>john</td>
      <td>smith</td>
      <td>vanilla</td>
    </tr>
    <tr>
      <th>1</th>
      <td>zhang</td>
      <td>shan</td>
      <td>chocolate</td>
    </tr>
    <tr>
      <th>2</th>
      <td>fulan</td>
      <td>alfulani</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>hong</td>
      <td>gildong</td>
      <td>banana</td>
    </tr>
  </tbody>
</table>
</div>



## The [] Operator

The DataFrame class has an indexing operator [] that lets you do a variety of different things. If your provide a String to the [] operator, you get back a Series corresponding to the requested label.


```python
elections_year_index.head(6)
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Result</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1984</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1984</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1988</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>win</td>
    </tr>
  </tbody>
</table>
</div>




```python
elections_year_index["Candidate"].head(6)
```




    Year
    1980      Reagan
    1980      Carter
    1980    Anderson
    1984      Reagan
    1984     Mondale
    1988        Bush
    Name: Candidate, dtype: object



The [] operator also accepts a list of strings. In this case, you get back a DataFrame corresponding to the requested strings.


```python
elections_year_index[["Candidate", "Party"]].head()
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
      <th>Candidate</th>
      <th>Party</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980</th>
      <td>Reagan</td>
      <td>Republican</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>Carter</td>
      <td>Democratic</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>Anderson</td>
      <td>Independent</td>
    </tr>
    <tr>
      <th>1984</th>
      <td>Reagan</td>
      <td>Republican</td>
    </tr>
    <tr>
      <th>1984</th>
      <td>Mondale</td>
      <td>Democratic</td>
    </tr>
  </tbody>
</table>
</div>



A list of one label also returns a DataFrame. This can be handy if you want your results as a DataFrame, not a series.


```python
elections_year_index[["Candidate"]].head()
```

Note that we can also use the to_frame method to turn a Series into a DataFrame.


```python
elections_year_index["Candidate"].to_frame().head()
```

The [] operator also accepts numerical slices as arguments. In this case, we are indexing by row, not column!


```python
elections_year_index[0:3]
```

If you provide a single argument to the [] operator, it tries to use it as a name. This is true even if the argument passed to [] is an integer. 


```python
#elections_year_index[0] #this does not work, try uncommenting this to see it fail in action, woo
```

The following cells allow you to test your understanding.


```python
weird = pd.DataFrame({
    1:["topdog","botdog"], 
    "1":["topcat","botcat"]
})
weird
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
      <th>1</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>topdog</td>
      <td>topcat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>botdog</td>
      <td>botcat</td>
    </tr>
  </tbody>
</table>
</div>




```python
weird[1] #try to predict the output
```




    0    topdog
    1    botdog
    Name: 1, dtype: object




```python
weird["1"] #try to predict the output
```




    0    topcat
    1    botcat
    Name: 1, dtype: object




```python
weird[1:] #try to predict the output
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
      <th>1</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>botdog</td>
      <td>botcat</td>
    </tr>
  </tbody>
</table>
</div>



## Boolean Array Selection

The `[]` operator also supports array of booleans as an input. In this case, the array must be exactly as long as the number of rows. The result is a filtered version of the data frame, where only rows corresponding to True appear.


```python
elections_year_index
```


```python
elections_year_index[[False, False, False, False, False, 
          False, False, True, False, False,
          True, False, False, False, True,
          False, False, False, False, False,
          False, False, True]]
```

One very common task in Data Science is filtering. Boolean Array Selection is one way to achieve this in Pandas. We start by observing logical operators like the equality operator can be applied to Pandas Series data to generate a Boolean Array. For example, we can compare the 'Result' column to the String 'win':


```python
elections_year_index.head(5)
```


```python
iswin = elections_year_index['Result'] == 'win'
iswin#.head(5)
```

The output of the logical operator applied to the Series is another Series with the same name and index, but of datatype boolean. The entry at row #i represents the result of the application of that operator to the entry of the original Series at row #i.

Such a boolean Series can be used as an argument to the [] operator. For example, the following code creates a DataFrame of all election winners since 1980.


```python
elections_year_index[iswin]
```

Above, we've assigned the result of the logical operator to a new variable called `iswin`. This is uncommon. Usually, the series is created and used on the same line. Such code is a little tricky to read at first, but you'll get used to it quickly.


```python
elections_year_index[elections_year_index['Result'] == 'win']
```

We can select multiple criteria by creating multiple boolean Series and combining them using the `&` operator.


```python
win50plus = (elections_year_index['Result'] == 'win') & (elections_year_index['%'] < 50)
```


```python
win50plus.head(5)
```


```python
elections_year_index[(elections_year_index['Result'] == 'win')
          & (elections_year_index['%'] < 50)]

# Note for Python experts: The reason we use the & symbol and not the word "and" is because the Python __and__ 
# method overrides the "&" operator, not the "and" operator.
```

The | operator is the symbol for or.


```python
elections_year_index[(elections_year_index['Party'] == 'Republican')
          | (elections_year_index['Party'] == "Democratic")]
```

If we have multiple conditions (say Republican or Democratic), we can use the isin operator to simplify our code.


```python
elections_year_index['Party'].isin(["Republican", "Democratic"])
```


```python
elections_year_index[elections_year_index['Party'].isin(["Republican", "Democratic"])]
```

An alternate simpler way to get back a specific set of rows is to use the `query` command.


```python
elections_year_index.query?
```


```python
elections_year_index.query("Result == 'win' and Year < 2000")
```

## Label-based access with `loc`


```python
elections.head(5)
```


```python
elections.loc[[0, 1, 2, 3, 4], ['Candidate','Party', 'Year']]
```

Note: The `loc` command won't work with numeric arguments if we're using the elections DataFrame that was indexed by year.


```python
elections_year_index.head(5)
```


```python
#causes error
elections_year_index.loc[[0, 1, 2, 3, 4], ['Candidate','Party']]#
```


```python
elections_year_index.loc[[1980, 1984], ['Candidate','Party']]
```

Loc also supports slicing (for all types, including numeric and string labels!). Note that the slicing for loc is **inclusive**, even for numeric slices.


```python
elections.loc[0:4, 'Candidate':'Year']
```


```python
elections_year_index.loc[1980:1984, 'Candidate':'Party']
```

If we provide only a single label for the column argument, we get back a Series.


```python
elections.loc[0:4, 'Candidate']
```

If we want a data frame instead and don't want to use to_frame, we can provde a list containing the column name.


```python
elections.loc[0:4, ['Candidate']]
```

If we give only one row but many column labels, we'll get back a Series corresponding to a row of the table. This new Series has a neat index, where each entry is the name of the column that the data came from.


```python
elections.head(1)
```


```python
elections.loc[0, 'Candidate':'Year']
```


```python
elections.loc[[0], 'Candidate':'Year']
```

If we omit the column argument altogether, the default behavior is to retrieve all columns. 


```python
elections.loc[[2, 4, 5]]
```

Loc also supports boolean array inputs instead of labels. The Boolean arrays _must_ be of the same length as the row/column shape of the dataframe, respectively (in versions prior to 0.25, Pandas used to allow size mismatches and would assume the missing values were all False, [this was changed in 2019](https://github.com/pandas-dev/pandas/pull/26911)).


```python
elections.loc[[True, False, False, True, False, False, True, True, True, False, False, True, 
               True, True, False, True, True, False, False, False, True, False, False], # row mask
              [True, False, False, True, True] # column mask
             ]
```


```python
elections.loc[[0, 3], ['Candidate', 'Year']]
```

We can use boolean array arguments for one axis of the data, and labels for the other.


```python
elections.loc[[True, False, False, True, False, False, True, True, True, False, False, True, 
               True, True, False, True, True, False, False, False, True, False, False], # row mask
              
              'Candidate':'%' # column label slice
             ]
```

A student asks what happens if you give scalar arguments for the requested rows AND columns. The answer is that you get back just a single value.


```python
elections.loc[15, '%']
```

## Positional access with `iloc`

loc's cousin iloc is very similar, but is used to access based on numerical position instead of label. For example, to access to the top 3 rows and top 3 columns of a table, we can use [0:3, 0:3]. iloc slicing is **exclusive**, just like standard Python slicing of numerical values.


```python
elections.head(5)
```


```python
elections.iloc[:3, 2:]
```

We will use both loc and iloc in the course. Loc is generally preferred for a number of reasons, for example: 

1. It is harder to make mistakes since you have to literally write out what you want to get.
2. Code is easier to read, because the reader doesn't have to know e.g. what column #31 represents.
3. It is robust against permutations of the data, e.g. the social security administration switches the order of two columns.

However, iloc is sometimes more convenient. We'll provide examples of when iloc is the superior choice.

## Quick Challenge

Which of the following expressions return DataFrame of the first 3 Candidate and Year for candidates that won with more than 50% of the vote.


```python
elections.head(10)
```


```python
elections.iloc[[0, 3, 5], [0, 3]]
```


```python
elections.loc[[0, 3, 5], "Candidate":"Year"]
```


```python
elections.loc[elections["%"] > 50, ["Candidate", "Year"]].head(3)
```


```python
elections.loc[elections["%"] > 50, ["Candidate", "Year"]].iloc[0:2, :]
```

## Sampling

Pandas dataframes also make it easy to get a sample. We simply use the `sample` method and provide the number of samples that we'd like as the arugment. Sampling is done without replacement by default. Set `replace=True` if you want replacement.


```python
elections.sample(10)
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Year</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Obama</td>
      <td>Democratic</td>
      <td>52.9</td>
      <td>2008</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Perot</td>
      <td>Independent</td>
      <td>8.4</td>
      <td>1996</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>2004</td>
      <td>win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Trump</td>
      <td>Republican</td>
      <td>46.1</td>
      <td>2016</td>
      <td>win</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Gore</td>
      <td>Democratic</td>
      <td>48.4</td>
      <td>2000</td>
      <td>loss</td>
    </tr>
  </tbody>
</table>
</div>




```python
elections.query("Year < 1992").sample(50, replace=True)
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
      <th>Candidate</th>
      <th>Party</th>
      <th>%</th>
      <th>Year</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bush</td>
      <td>Republican</td>
      <td>53.4</td>
      <td>1988</td>
      <td>win</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>58.8</td>
      <td>1984</td>
      <td>win</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anderson</td>
      <td>Independent</td>
      <td>6.6</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Reagan</td>
      <td>Republican</td>
      <td>50.7</td>
      <td>1980</td>
      <td>win</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dukakis</td>
      <td>Democratic</td>
      <td>45.6</td>
      <td>1988</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Carter</td>
      <td>Democratic</td>
      <td>41.0</td>
      <td>1980</td>
      <td>loss</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mondale</td>
      <td>Democratic</td>
      <td>37.6</td>
      <td>1984</td>
      <td>loss</td>
    </tr>
  </tbody>
</table>
</div>



## Handy Properties and Utility Functions for Series and DataFrames

#### Python Operations on Numerical DataFrames and Series

Consider a series of only the vote percentages of election winners.


```python
winners = elections.query("Result == 'win'")["%"]
winners
```

We can perform various Python operations (including numpy operations) to DataFrames and Series.


```python
max(winners)
```


```python
np.mean(winners)
```

We can also do more complicated operations like computing the mean squared error, i.e. the average L2 loss. (This will mean more in the next few weeks.)


```python
c = 50.38
mse = np.mean((c - winners)**2)
mse
```


```python
c2 = 50.35
mse2 = np.mean((c2 - winners)**2)
mse2
```

We can also apply mathematical operations to a DataFrame so long as it has only numerical data.


```python
(elections[["%", "Year"]] + 3).head(5)
```

#### Handy Utility Methods

The head, shape, size, and describe methods can be used to quickly get a good sense of the data we're working with. For example:


```python
mottos = pd.read_csv("mottos.csv", index_col="State")
```


```python
mottos.head(20)
```


```python
mottos.size
```

The fact that the size is 200 means our data file is relatively small, with only 200 total entries.


```python
mottos.shape
```

Since we're looking at data for states, and we see the number 50, it looks like we've mostly likely got a complete dataset that omits Washington D.C. and U.S. territories like Guam and Puerto Rico.


```python
mottos.describe()
```

Above, we see a quick summary of all the data. For example, the most common language for mottos is Latin, which covers 23 different states. Does anything else seem surprising?

We can get a direct reference to the index using .index.


```python
mottos.index
```

We can also access individual properties of the index, for example, `mottos.index.name`.


```python
mottos.index.name
```

This reflects the fact that in our data frame, the index IS the state name!


```python
mottos.head(2)
```

It turns out the columns also have an Index. We can access this index by using `.columns`.


```python
mottos.head(2)
```

There are also a ton of useful utility methods we can use with Data Frames and Series. For example, we can create a copy of a data frame sorted by a specific column using `sort_values`.


```python
elections.sort_values('%', ascending=False)
```

As mentioned before, all Data Frame methods return a copy and do **not** modify the original data structure, unless you set inplace to True.


```python
elections.head(5)
```

If we want to sort in reverse order, we can set `ascending=False`.


```python
elections.sort_values('%', ascending=False)
```

We can also use `sort_values` on Series objects.


```python
mottos['Language'].sort_values(ascending=False).head(10)
```

For Series, the `value_counts` method is often quite handy.


```python
elections['Party'].value_counts()
```


```python
mottos['Language'].value_counts()
```

Also commonly used is the `unique` method, which returns all unique values as a numpy array.


```python
mottos['Language'].unique()
```
