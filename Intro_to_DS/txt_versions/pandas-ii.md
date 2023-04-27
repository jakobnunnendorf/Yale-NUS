```python
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.style.use('fivethirtyeight')
sns.set_context("notebook")
```

Let's start by loading the California baby names again.


```python
import urllib.request
import os.path
import zipfile

data_url = "https://www.ssa.gov/oact/babynames/state/namesbystate.zip"
local_filename = "babynamesbystate.zip"
if not os.path.exists(local_filename): # if the data exists don't download again
    with urllib.request.urlopen(data_url) as resp, open(local_filename, 'wb') as f:
        f.write(resp.read())

zf = zipfile.ZipFile(local_filename, 'r')

ca_name = 'CA.TXT'
field_names = ['State', 'Sex', 'Year', 'Name', 'Count']
with zf.open(ca_name) as fh:
    babynames = pd.read_csv(fh, header=None, names=field_names)

babynames.sample(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>87941</th>
      <td>CA</td>
      <td>F</td>
      <td>1981</td>
      <td>Genelle</td>
      <td>6</td>
    </tr>
    <tr>
      <th>258383</th>
      <td>CA</td>
      <td>M</td>
      <td>1954</td>
      <td>German</td>
      <td>7</td>
    </tr>
    <tr>
      <th>253144</th>
      <td>CA</td>
      <td>M</td>
      <td>1948</td>
      <td>Maury</td>
      <td>5</td>
    </tr>
    <tr>
      <th>330873</th>
      <td>CA</td>
      <td>M</td>
      <td>1998</td>
      <td>Eloy</td>
      <td>24</td>
    </tr>
    <tr>
      <th>17440</th>
      <td>CA</td>
      <td>F</td>
      <td>1940</td>
      <td>Veronica</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



## Goal 1: Find the most popular baby name in California in 2018


```python
babynames[babynames["Year"] == 2018].sort_values(by = "Count", ascending = False).head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>221160</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Emma</td>
      <td>2743</td>
    </tr>
    <tr>
      <th>385701</th>
      <td>CA</td>
      <td>M</td>
      <td>2018</td>
      <td>Noah</td>
      <td>2569</td>
    </tr>
    <tr>
      <th>221161</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Mia</td>
      <td>2499</td>
    </tr>
    <tr>
      <th>221162</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Olivia</td>
      <td>2465</td>
    </tr>
    <tr>
      <th>385702</th>
      <td>CA</td>
      <td>M</td>
      <td>2018</td>
      <td>Liam</td>
      <td>2413</td>
    </tr>
  </tbody>
</table>
</div>



## Goal 2: Find baby names that start with j. 

### Approach 1: Combine syntax from Pandas I lecture with CS61A/CS88 ideas.


```python
babynames["Name"].head(10)
```




    0         Mary
    1        Helen
    2      Dorothy
    3     Margaret
    4      Frances
    5         Ruth
    6       Evelyn
    7        Alice
    8     Virginia
    9    Elizabeth
    Name: Name, dtype: object




```python
starts_with_j = [x[0] == 'J' for x in babynames["Name"]]
babynames[starts_with_j].sample(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>340593</th>
      <td>CA</td>
      <td>M</td>
      <td>2002</td>
      <td>Jon</td>
      <td>47</td>
    </tr>
    <tr>
      <th>222332</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Jaylee</td>
      <td>24</td>
    </tr>
    <tr>
      <th>308352</th>
      <td>CA</td>
      <td>M</td>
      <td>1989</td>
      <td>Josef</td>
      <td>21</td>
    </tr>
    <tr>
      <th>182970</th>
      <td>CA</td>
      <td>F</td>
      <td>2008</td>
      <td>Josephina</td>
      <td>13</td>
    </tr>
    <tr>
      <th>363936</th>
      <td>CA</td>
      <td>M</td>
      <td>2010</td>
      <td>Jaykob</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
j_names = babynames[[x[0] == 'J' for x in babynames["Name"]]]
```

### Approach 2: Use the Series.str methods.


```python
babynames["Name"].str.startswith('J').head(10)
```




    0    False
    1    False
    2    False
    3    False
    4    False
    5    False
    6    False
    7    False
    8    False
    9    False
    Name: Name, dtype: bool




```python
babynames["Name"].str.startswith('J')
```




    0         False
    1         False
    2         False
    3         False
    4         False
              ...  
    394174    False
    394175    False
    394176    False
    394177    False
    394178    False
    Name: Name, Length: 394179, dtype: bool




```python
starts_with_j = babynames["Name"].str.startswith('J')
starts_with_j.head(10)
```




    0    False
    1    False
    2    False
    3    False
    4    False
    5    False
    6    False
    7    False
    8    False
    9    False
    Name: Name, dtype: bool




```python
babynames[babynames["Name"].str.startswith('J')].sample(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34091</th>
      <td>CA</td>
      <td>F</td>
      <td>1954</td>
      <td>Julee</td>
      <td>5</td>
    </tr>
    <tr>
      <th>286137</th>
      <td>CA</td>
      <td>M</td>
      <td>1977</td>
      <td>Jerald</td>
      <td>17</td>
    </tr>
    <tr>
      <th>296754</th>
      <td>CA</td>
      <td>M</td>
      <td>1983</td>
      <td>Job</td>
      <td>7</td>
    </tr>
    <tr>
      <th>38712</th>
      <td>CA</td>
      <td>F</td>
      <td>1957</td>
      <td>Jesus</td>
      <td>5</td>
    </tr>
    <tr>
      <th>390888</th>
      <td>CA</td>
      <td>M</td>
      <td>2019</td>
      <td>Jaziah</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
babynames[babynames["Name"].str.contains('ad')].sample(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>77636</th>
      <td>CA</td>
      <td>F</td>
      <td>1977</td>
      <td>Madeleine</td>
      <td>7</td>
    </tr>
    <tr>
      <th>380468</th>
      <td>CA</td>
      <td>M</td>
      <td>2016</td>
      <td>Conrad</td>
      <td>51</td>
    </tr>
    <tr>
      <th>365963</th>
      <td>CA</td>
      <td>M</td>
      <td>2011</td>
      <td>Aaden</td>
      <td>39</td>
    </tr>
    <tr>
      <th>170096</th>
      <td>CA</td>
      <td>F</td>
      <td>2005</td>
      <td>Madysen</td>
      <td>15</td>
    </tr>
    <tr>
      <th>338429</th>
      <td>CA</td>
      <td>M</td>
      <td>2001</td>
      <td>Vladimir</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
babynames["Name"].str.split('a').to_frame().head(5)
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
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[M, ry]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[Helen]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[Dorothy]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[M, rg, ret]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[Fr, nces]</td>
    </tr>
  </tbody>
</table>
</div>



In-lecture challenge: Try to write a line of code that creates a list (or Series or array) of all names that end with “ert”.

## Goal 3: Sort names by their length.

Suppose we want to sort all baby names in California by their length.

As before, there are ways to do this using only lecture 5 content. For example, the montrosity below was concocted during the Sp19 version of this class.


```python
babynames.iloc[[i for i, m in sorted(enumerate(babynames['Name']), key=lambda x: -len(x[1]))]].head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>102490</th>
      <td>CA</td>
      <td>F</td>
      <td>1986</td>
      <td>Mariadelosangel</td>
      <td>5</td>
    </tr>
    <tr>
      <th>305111</th>
      <td>CA</td>
      <td>M</td>
      <td>1987</td>
      <td>Franciscojavier</td>
      <td>5</td>
    </tr>
    <tr>
      <th>306544</th>
      <td>CA</td>
      <td>M</td>
      <td>1988</td>
      <td>Franciscojavier</td>
      <td>10</td>
    </tr>
    <tr>
      <th>309451</th>
      <td>CA</td>
      <td>M</td>
      <td>1989</td>
      <td>Franciscojavier</td>
      <td>6</td>
    </tr>
    <tr>
      <th>314358</th>
      <td>CA</td>
      <td>M</td>
      <td>1991</td>
      <td>Ryanchristopher</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



### Approach 1: Create a temporary column.

Create a new series of only the lengths. Then add that series to the dataframe as a column. Then sort by that column. Then drop that column.


```python
#create a new series of only the lengths
babyname_lengths = babynames["Name"].str.len()

#add that series to the dataframe as a column
babynames["name_lengths"] = babyname_lengths
babynames.head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
      <th>name_lengths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CA</td>
      <td>F</td>
      <td>1910</td>
      <td>Mary</td>
      <td>295</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CA</td>
      <td>F</td>
      <td>1910</td>
      <td>Helen</td>
      <td>239</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CA</td>
      <td>F</td>
      <td>1910</td>
      <td>Dorothy</td>
      <td>220</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CA</td>
      <td>F</td>
      <td>1910</td>
      <td>Margaret</td>
      <td>163</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CA</td>
      <td>F</td>
      <td>1910</td>
      <td>Frances</td>
      <td>134</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
#sort by the temporary column
babynames = babynames.sort_values(by = "name_lengths", ascending=False)
babynames.head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
      <th>name_lengths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>332035</th>
      <td>CA</td>
      <td>M</td>
      <td>1998</td>
      <td>Franciscojavier</td>
      <td>6</td>
      <td>15</td>
    </tr>
    <tr>
      <th>329864</th>
      <td>CA</td>
      <td>M</td>
      <td>1997</td>
      <td>Franciscojavier</td>
      <td>5</td>
      <td>15</td>
    </tr>
    <tr>
      <th>320036</th>
      <td>CA</td>
      <td>M</td>
      <td>1993</td>
      <td>Ryanchristopher</td>
      <td>5</td>
      <td>15</td>
    </tr>
    <tr>
      <th>314358</th>
      <td>CA</td>
      <td>M</td>
      <td>1991</td>
      <td>Ryanchristopher</td>
      <td>7</td>
      <td>15</td>
    </tr>
    <tr>
      <th>319923</th>
      <td>CA</td>
      <td>M</td>
      <td>1993</td>
      <td>Johnchristopher</td>
      <td>5</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
#drop the temporary column
babynames = babynames.drop("name_lengths", axis = 1)
babynames.head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>332035</th>
      <td>CA</td>
      <td>M</td>
      <td>1998</td>
      <td>Franciscojavier</td>
      <td>6</td>
    </tr>
    <tr>
      <th>329864</th>
      <td>CA</td>
      <td>M</td>
      <td>1997</td>
      <td>Franciscojavier</td>
      <td>5</td>
    </tr>
    <tr>
      <th>320036</th>
      <td>CA</td>
      <td>M</td>
      <td>1993</td>
      <td>Ryanchristopher</td>
      <td>5</td>
    </tr>
    <tr>
      <th>314358</th>
      <td>CA</td>
      <td>M</td>
      <td>1991</td>
      <td>Ryanchristopher</td>
      <td>7</td>
    </tr>
    <tr>
      <th>319923</th>
      <td>CA</td>
      <td>M</td>
      <td>1993</td>
      <td>Johnchristopher</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



We can also use the Python map function if we want to use an arbitrarily defined function. Suppose we want to sort by the number of occurrences of "dr" plus the number of occurences of "ea".


```python
def dr_ea_count(string):
    return string.count('dr') + string.count('ea')

#create the temporary column
babynames["dr_ea_count"] = babynames["Name"].map(dr_ea_count)

#sort by the temporary column
babynames = babynames.sort_values(by = "dr_ea_count", ascending=False)

#drop that column
babynames = babynames.drop("dr_ea_count", 1)
babynames.head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>131013</th>
      <td>CA</td>
      <td>F</td>
      <td>1994</td>
      <td>Leandrea</td>
      <td>5</td>
    </tr>
    <tr>
      <th>101962</th>
      <td>CA</td>
      <td>F</td>
      <td>1986</td>
      <td>Deandrea</td>
      <td>6</td>
    </tr>
    <tr>
      <th>115942</th>
      <td>CA</td>
      <td>F</td>
      <td>1990</td>
      <td>Deandrea</td>
      <td>5</td>
    </tr>
    <tr>
      <th>300700</th>
      <td>CA</td>
      <td>M</td>
      <td>1985</td>
      <td>Deandrea</td>
      <td>6</td>
    </tr>
    <tr>
      <th>108715</th>
      <td>CA</td>
      <td>F</td>
      <td>1988</td>
      <td>Deandrea</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# anything else you all want to try?
```

### Approach 2: Generate an index sorted in the desired order.


```python
#let's start over by first scrambling the order of babynames
babynames = babynames.sample(frac=1)
babynames.head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>312445</th>
      <td>CA</td>
      <td>M</td>
      <td>1990</td>
      <td>Werner</td>
      <td>5</td>
    </tr>
    <tr>
      <th>280473</th>
      <td>CA</td>
      <td>M</td>
      <td>1973</td>
      <td>Rory</td>
      <td>16</td>
    </tr>
    <tr>
      <th>134170</th>
      <td>CA</td>
      <td>F</td>
      <td>1995</td>
      <td>Lindy</td>
      <td>6</td>
    </tr>
    <tr>
      <th>250270</th>
      <td>CA</td>
      <td>M</td>
      <td>1945</td>
      <td>Ignacio</td>
      <td>26</td>
    </tr>
    <tr>
      <th>78541</th>
      <td>CA</td>
      <td>F</td>
      <td>1978</td>
      <td>Bernadette</td>
      <td>99</td>
    </tr>
  </tbody>
</table>
</div>



Another approach is to take advantage of the fact that .loc can accept an index. That is:
 + df.loc[idx] returns df with its rows in the same order as the given index.
 + Only works if the index exactly matches the DataFrame.

The first step was to create a sequence of the lengths of the names.


```python
name_lengths = babynames["Name"].str.len()
name_lengths.head(5)
```




    312445     6
    280473     4
    134170     5
    250270     7
    78541     10
    Name: Name, dtype: int64



The next step is to sort the new series we just created.


```python
name_lengths_sorted_by_length = name_lengths.sort_values()
name_lengths_sorted_by_length.head(5)
```




    329914    2
    111253    2
    247513    2
    309363    2
    373212    2
    Name: Name, dtype: int64



Next, we pass the index of the sorted series to the loc method of the original dataframe.


```python
index_sorted_by_length = name_lengths_sorted_by_length.index
index_sorted_by_length
```




    Int64Index([329914, 111253, 247513, 309363, 373212,  90042,  45983, 334976,
                 87768, 316852,
                ...
                320036, 306544, 314479, 309451, 319923, 332035, 305111, 329864,
                330040, 314358],
               dtype='int64', length=394179)




```python
babynames.loc[index_sorted_by_length].head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>329914</th>
      <td>CA</td>
      <td>M</td>
      <td>1997</td>
      <td>Jc</td>
      <td>5</td>
    </tr>
    <tr>
      <th>111253</th>
      <td>CA</td>
      <td>F</td>
      <td>1989</td>
      <td>An</td>
      <td>8</td>
    </tr>
    <tr>
      <th>247513</th>
      <td>CA</td>
      <td>M</td>
      <td>1941</td>
      <td>Al</td>
      <td>21</td>
    </tr>
    <tr>
      <th>309363</th>
      <td>CA</td>
      <td>M</td>
      <td>1989</td>
      <td>Aj</td>
      <td>6</td>
    </tr>
    <tr>
      <th>373212</th>
      <td>CA</td>
      <td>M</td>
      <td>2013</td>
      <td>Jr</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



Note we can also do this all in one line:


```python
babynames.loc[babynames["Name"].str.len().sort_values().index].head(5)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>329914</th>
      <td>CA</td>
      <td>M</td>
      <td>1997</td>
      <td>Jc</td>
      <td>5</td>
    </tr>
    <tr>
      <th>111253</th>
      <td>CA</td>
      <td>F</td>
      <td>1989</td>
      <td>An</td>
      <td>8</td>
    </tr>
    <tr>
      <th>247513</th>
      <td>CA</td>
      <td>M</td>
      <td>1941</td>
      <td>Al</td>
      <td>21</td>
    </tr>
    <tr>
      <th>309363</th>
      <td>CA</td>
      <td>M</td>
      <td>1989</td>
      <td>Aj</td>
      <td>6</td>
    </tr>
    <tr>
      <th>373212</th>
      <td>CA</td>
      <td>M</td>
      <td>2013</td>
      <td>Jr</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



### Goal 4: Name whose popularity has changed the most. 

First we need to define change in popularity. 

For the purposes of lecture, let’s stay simple and use the AMMD (absolute max/min difference): max(count) - min(count). 

To make sure we understand this quantity, let's consider the name Jennifer.


```python
jennifer_counts = babynames.query("Name == 'Jennifer'")["Count"]
jennifer_counts.head(5)
```




    176727    1035
    63084     5457
    38858      738
    85805     5628
    49399     1516
    Name: Count, dtype: int64



The AMMD for Jennifer is 6,061, as seen below:


```python
max(jennifer_counts) - min(jennifer_counts)
```




    6059




```python
def ammd(series):
    return max(series) - min(series)
```


```python
ammd(jennifer_counts)
```




    6059



### Approach 1: Naive For Loop

As a first approach, we can try to use a for loop.


```python
#build dictionary where entry i is the ammd for the given name
#e.g. ammd["jennifer"] should be 6061
#ammd_of_babyname_counts = {}
#for name in ??:
#    counts_of_current_name = babynames[??]["Count"]
#    ammd_of_babyname_counts[name] = ammd(counts_of_current_name)
    
#convert to series
#ammd_of_babyname_counts = pd.Series(ammd_of_babyname_counts) 
```

Answer below. Note that we only used the first 100 names because otherwise the code takes ages to complete running.


```python
#build dictionary where entry i is the ammd for the given name
#e.g. ammd["jennifer"] should be 6061
ammd_of_babyname_counts = {}
for name in sorted(babynames["Name"].unique())[0:100]:
    counts_of_current_name = babynames[babynames["Name"] == name]["Count"]
    ammd_of_babyname_counts[name] = ammd(counts_of_current_name)
    
#convert to series
ammd_of_babyname_counts = pd.Series(ammd_of_babyname_counts) 
ammd_of_babyname_counts.head(5)
```




    Aadan        2
    Aadarsh      0
    Aaden      148
    Aadhav       2
    Aadhira      4
    dtype: int64



### Approach 2: Use groupby.agg

Instead, we can use the very powerful groupby.agg operation, which allows us to simply and efficiently compute what we want.


```python
babynames.groupby("Name").agg(ammd).head(5)
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
      <th>Year</th>
      <th>Count</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Aadan</th>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Aadarsh</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Aaden</th>
      <td>13</td>
      <td>148</td>
    </tr>
    <tr>
      <th>Aadhav</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Aadhira</th>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



Note that the result includes both a Year and Count column. The Count column is what we want, namely the AMMD for the name in that row. To check your understanding, try to figure out what the Year column represents.

To understand how groupby works, consider the visual diagram below. The `groupby` function clusters rows from the original dataframe into groups (which I call subframes). The `agg` function then condenses each subframe into a single representative row using the provided function f.

![groupby_picture.png](attachment:groupby_picture.png)

## Some Additional Groupby Puzzles

#### Groupby puzzle #1: To test your understanding, try to interpret the result of the code below.


```python
babynames.groupby("Year").agg(ammd).plot()
```




    <AxesSubplot:xlabel='Year'>




    
![png](pandas-ii_files/pandas-ii_61_1.png)
    


For reference, the first 5 values from the plot above are:


```python
babynames.groupby("Year").agg(ammd).head(5)
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
      <th>Count</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1910</th>
      <td>290</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>385</td>
    </tr>
    <tr>
      <th>1912</th>
      <td>529</td>
    </tr>
    <tr>
      <th>1913</th>
      <td>609</td>
    </tr>
    <tr>
      <th>1914</th>
      <td>768</td>
    </tr>
  </tbody>
</table>
</div>



#### groupby Puzzle #2


```python
elections = pd.read_csv("elections.csv")
elections.sample(5)
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1824</td>
      <td>Andrew Jackson</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>loss</td>
      <td>57.210122</td>
    </tr>
    <tr>
      <th>99</th>
      <td>1948</td>
      <td>Claude A. Watson</td>
      <td>Prohibition</td>
      <td>103708</td>
      <td>loss</td>
      <td>0.212747</td>
    </tr>
    <tr>
      <th>173</th>
      <td>2016</td>
      <td>Donald Trump</td>
      <td>Republican</td>
      <td>62984828</td>
      <td>win</td>
      <td>46.407862</td>
    </tr>
    <tr>
      <th>53</th>
      <td>1896</td>
      <td>William McKinley</td>
      <td>Republican</td>
      <td>7112138</td>
      <td>win</td>
      <td>51.213817</td>
    </tr>
    <tr>
      <th>38</th>
      <td>1884</td>
      <td>Benjamin Butler</td>
      <td>Anti-Monopoly</td>
      <td>134294</td>
      <td>loss</td>
      <td>1.335838</td>
    </tr>
  </tbody>
</table>
</div>



We have to be careful when using aggregation functions. For example, the code below might be misinterpreted to say that Woodrow Wilson ran for election in 2016. Why is this happening?


```python
elections.groupby("Party").agg(max).head(10)
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
    </tr>
    <tr>
      <th>Party</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>American</th>
      <td>1976</td>
      <td>Thomas J. Anderson</td>
      <td>873053</td>
      <td>loss</td>
      <td>21.554001</td>
    </tr>
    <tr>
      <th>American Independent</th>
      <td>1976</td>
      <td>Lester Maddox</td>
      <td>9901118</td>
      <td>loss</td>
      <td>13.571218</td>
    </tr>
    <tr>
      <th>Anti-Masonic</th>
      <td>1832</td>
      <td>William Wirt</td>
      <td>100715</td>
      <td>loss</td>
      <td>7.821583</td>
    </tr>
    <tr>
      <th>Anti-Monopoly</th>
      <td>1884</td>
      <td>Benjamin Butler</td>
      <td>134294</td>
      <td>loss</td>
      <td>1.335838</td>
    </tr>
    <tr>
      <th>Citizens</th>
      <td>1980</td>
      <td>Barry Commoner</td>
      <td>233052</td>
      <td>loss</td>
      <td>0.270182</td>
    </tr>
    <tr>
      <th>Communist</th>
      <td>1932</td>
      <td>William Z. Foster</td>
      <td>103307</td>
      <td>loss</td>
      <td>0.261069</td>
    </tr>
    <tr>
      <th>Constitution</th>
      <td>2016</td>
      <td>Michael Peroutka</td>
      <td>203091</td>
      <td>loss</td>
      <td>0.152398</td>
    </tr>
    <tr>
      <th>Constitutional Union</th>
      <td>1860</td>
      <td>John Bell</td>
      <td>590901</td>
      <td>loss</td>
      <td>12.639283</td>
    </tr>
    <tr>
      <th>Democratic</th>
      <td>2016</td>
      <td>Woodrow Wilson</td>
      <td>69498516</td>
      <td>win</td>
      <td>61.344703</td>
    </tr>
    <tr>
      <th>Democratic-Republican</th>
      <td>1824</td>
      <td>John Quincy Adams</td>
      <td>151271</td>
      <td>win</td>
      <td>57.210122</td>
    </tr>
  </tbody>
</table>
</div>



#### groupby puzzle #3

Inspired by above, try to predict the results of the groupby operation shown. The answer is below the image.

![groupby_puzzle.png](attachment:groupby_puzzle.png)

The top ?? will be "hi", the second ?? will be "tx", and the third ?? will be "sd". 

#### groupby puzzle #4

Next we'll write code that properly returns the best result by each party. That is, each row should show the Year, Candidate, Popular Vote, Result, and % for the election in which that party saw its best results (rather than mixing them as in the example above).


```python
#def get_first(s):
#    return s.iloc[0]
    
#elections_sorted_by_percent = elections.sort_values("%", ascending=False)
#elections_sorted_by_percent.groupby("Party").agg(lambda x : x.iloc[0])
```

#### groupby puzzle #5: Total Male and Female babies born

Suppose we want to find the total number of male and female babies born each year in California.

Try to figure out how we'd do this using groupby.


```python

```

## Other groupby Features

It is possible to group a DataFrame by multiple features. For example, if we group by Year and Sex we get back a DataFrame with the total number of babies of each sex born in each year.


```python
babynames.groupby(["Year", "Sex"]).agg(sum).head(6)
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
      <th></th>
      <th>Count</th>
    </tr>
    <tr>
      <th>Year</th>
      <th>Sex</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1910</th>
      <th>F</th>
      <td>5950</td>
    </tr>
    <tr>
      <th>M</th>
      <td>3213</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1911</th>
      <th>F</th>
      <td>6602</td>
    </tr>
    <tr>
      <th>M</th>
      <td>3381</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1912</th>
      <th>F</th>
      <td>9804</td>
    </tr>
    <tr>
      <th>M</th>
      <td>8142</td>
    </tr>
  </tbody>
</table>
</div>



The DataFrame resulting from the aggregation operation is now multi-indexed. That is, it has more than one dimension to its index. We will explore this in next week's exercises.

### groupby.size()


```python
#size returns a Series giving the size of each group
elections.groupby("Party").size().head(15)
```




    Party
    American                  2
    American Independent      3
    Anti-Masonic              1
    Anti-Monopoly             1
    Citizens                  1
    Communist                 1
    Constitution              3
    Constitutional Union      1
    Democratic               46
    Democratic-Republican     2
    Dixiecrat                 1
    Farmer–Labor              1
    Free Soil                 2
    Green                     6
    Greenback                 1
    dtype: int64



### groupby.filter()


```python
# filter gives a copy of the original DataFrame where row r is included
# if its group obeys the given condition
#
# Note: Filtering is done per GROUP, not per ROW.
elections.groupby("Year").filter(lambda sf: sf["%"].max() < 45)
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23</th>
      <td>1860</td>
      <td>Abraham Lincoln</td>
      <td>Republican</td>
      <td>1855993</td>
      <td>win</td>
      <td>39.699408</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1860</td>
      <td>John Bell</td>
      <td>Constitutional Union</td>
      <td>590901</td>
      <td>loss</td>
      <td>12.639283</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1860</td>
      <td>John C. Breckinridge</td>
      <td>Southern Democratic</td>
      <td>848019</td>
      <td>loss</td>
      <td>18.138998</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1860</td>
      <td>Stephen A. Douglas</td>
      <td>Northern Democratic</td>
      <td>1380202</td>
      <td>loss</td>
      <td>29.522311</td>
    </tr>
    <tr>
      <th>66</th>
      <td>1912</td>
      <td>Eugene V. Debs</td>
      <td>Socialist</td>
      <td>901551</td>
      <td>loss</td>
      <td>6.004354</td>
    </tr>
    <tr>
      <th>67</th>
      <td>1912</td>
      <td>Eugene W. Chafin</td>
      <td>Prohibition</td>
      <td>208156</td>
      <td>loss</td>
      <td>1.386325</td>
    </tr>
    <tr>
      <th>68</th>
      <td>1912</td>
      <td>Theodore Roosevelt</td>
      <td>Progressive</td>
      <td>4122721</td>
      <td>loss</td>
      <td>27.457433</td>
    </tr>
    <tr>
      <th>69</th>
      <td>1912</td>
      <td>William Taft</td>
      <td>Republican</td>
      <td>3486242</td>
      <td>loss</td>
      <td>23.218466</td>
    </tr>
    <tr>
      <th>70</th>
      <td>1912</td>
      <td>Woodrow Wilson</td>
      <td>Democratic</td>
      <td>6296284</td>
      <td>win</td>
      <td>41.933422</td>
    </tr>
    <tr>
      <th>115</th>
      <td>1968</td>
      <td>George Wallace</td>
      <td>American Independent</td>
      <td>9901118</td>
      <td>loss</td>
      <td>13.571218</td>
    </tr>
    <tr>
      <th>116</th>
      <td>1968</td>
      <td>Hubert Humphrey</td>
      <td>Democratic</td>
      <td>31271839</td>
      <td>loss</td>
      <td>42.863537</td>
    </tr>
    <tr>
      <th>117</th>
      <td>1968</td>
      <td>Richard Nixon</td>
      <td>Republican</td>
      <td>31783783</td>
      <td>win</td>
      <td>43.565246</td>
    </tr>
    <tr>
      <th>139</th>
      <td>1992</td>
      <td>Andre Marrou</td>
      <td>Libertarian</td>
      <td>290087</td>
      <td>loss</td>
      <td>0.278516</td>
    </tr>
    <tr>
      <th>140</th>
      <td>1992</td>
      <td>Bill Clinton</td>
      <td>Democratic</td>
      <td>44909806</td>
      <td>win</td>
      <td>43.118485</td>
    </tr>
    <tr>
      <th>141</th>
      <td>1992</td>
      <td>Bo Gritz</td>
      <td>Populist</td>
      <td>106152</td>
      <td>loss</td>
      <td>0.101918</td>
    </tr>
    <tr>
      <th>142</th>
      <td>1992</td>
      <td>George H. W. Bush</td>
      <td>Republican</td>
      <td>39104550</td>
      <td>loss</td>
      <td>37.544784</td>
    </tr>
    <tr>
      <th>143</th>
      <td>1992</td>
      <td>Ross Perot</td>
      <td>Independent</td>
      <td>19743821</td>
      <td>loss</td>
      <td>18.956298</td>
    </tr>
  </tbody>
</table>
</div>



### groupby.sum(), groupby.mean(), etc.

As an alternative to groupby.agg(sum), we can also simply do groupby.sum().


```python
elections.groupby("Year").agg(sum).head()
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
      <th>Popular vote</th>
      <th>%</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1824</th>
      <td>264413</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1828</th>
      <td>1143703</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1832</th>
      <td>1287655</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>1460216</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1840</th>
      <td>2404437</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
elections.groupby("Year").sum().head()
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
      <th>Popular vote</th>
      <th>%</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1824</th>
      <td>264413</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1828</th>
      <td>1143703</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1832</th>
      <td>1287655</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>1460216</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1840</th>
      <td>2404437</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>



The same applies for many other common operations.


```python
elections.groupby("Year").agg(max).head()
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
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1824</th>
      <td>John Quincy Adams</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>win</td>
      <td>57.210122</td>
    </tr>
    <tr>
      <th>1828</th>
      <td>John Quincy Adams</td>
      <td>National Republican</td>
      <td>642806</td>
      <td>win</td>
      <td>56.203927</td>
    </tr>
    <tr>
      <th>1832</th>
      <td>William Wirt</td>
      <td>National Republican</td>
      <td>702735</td>
      <td>win</td>
      <td>54.574789</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>763291</td>
      <td>win</td>
      <td>52.272472</td>
    </tr>
    <tr>
      <th>1840</th>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>1275583</td>
      <td>win</td>
      <td>53.051213</td>
    </tr>
  </tbody>
</table>
</div>




```python
elections.groupby("Year").max().head()
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
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1824</th>
      <td>John Quincy Adams</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>win</td>
      <td>57.210122</td>
    </tr>
    <tr>
      <th>1828</th>
      <td>John Quincy Adams</td>
      <td>National Republican</td>
      <td>642806</td>
      <td>win</td>
      <td>56.203927</td>
    </tr>
    <tr>
      <th>1832</th>
      <td>William Wirt</td>
      <td>National Republican</td>
      <td>702735</td>
      <td>win</td>
      <td>54.574789</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>763291</td>
      <td>win</td>
      <td>52.272472</td>
    </tr>
    <tr>
      <th>1840</th>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>1275583</td>
      <td>win</td>
      <td>53.051213</td>
    </tr>
  </tbody>
</table>
</div>




```python
#elections.groupby("Year").mean().head()
#elections.groupby("Year").median().head()
elections.groupby("Year").max().head()
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
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1824</th>
      <td>John Quincy Adams</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>win</td>
      <td>57.210122</td>
    </tr>
    <tr>
      <th>1828</th>
      <td>John Quincy Adams</td>
      <td>National Republican</td>
      <td>642806</td>
      <td>win</td>
      <td>56.203927</td>
    </tr>
    <tr>
      <th>1832</th>
      <td>William Wirt</td>
      <td>National Republican</td>
      <td>702735</td>
      <td>win</td>
      <td>54.574789</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>763291</td>
      <td>win</td>
      <td>52.272472</td>
    </tr>
    <tr>
      <th>1840</th>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>1275583</td>
      <td>win</td>
      <td>53.051213</td>
    </tr>
  </tbody>
</table>
</div>



## Pivot Tables

### Goal 5: Finding the number of babies born in each year of each sex.

Suppose we want to build a table showing the total number of babies born of each sex in each year. One way is to groupby using both columns of interest.


```python
babynames.groupby(["Year", "Sex"]).agg(sum).head(6)
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
      <th></th>
      <th>Count</th>
    </tr>
    <tr>
      <th>Year</th>
      <th>Sex</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1910</th>
      <th>F</th>
      <td>5950</td>
    </tr>
    <tr>
      <th>M</th>
      <td>3213</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1911</th>
      <th>F</th>
      <td>6602</td>
    </tr>
    <tr>
      <th>M</th>
      <td>3381</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1912</th>
      <th>F</th>
      <td>9804</td>
    </tr>
    <tr>
      <th>M</th>
      <td>8142</td>
    </tr>
  </tbody>
</table>
</div>



A more natural approach is to use a pivot table (like we saw in data 8).


```python
babynames_pivot = babynames.pivot_table(
    index='Year', # the rows (turned into index)
    columns='Sex', # the column values
    values='Count', # the field(s) to processed in each group
    aggfunc=np.max, # group operation
)
babynames_pivot.head(6)
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
      <th>Sex</th>
      <th>F</th>
      <th>M</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1910</th>
      <td>295</td>
      <td>237</td>
    </tr>
    <tr>
      <th>1911</th>
      <td>390</td>
      <td>214</td>
    </tr>
    <tr>
      <th>1912</th>
      <td>534</td>
      <td>501</td>
    </tr>
    <tr>
      <th>1913</th>
      <td>584</td>
      <td>614</td>
    </tr>
    <tr>
      <th>1914</th>
      <td>773</td>
      <td>769</td>
    </tr>
    <tr>
      <th>1915</th>
      <td>998</td>
      <td>1033</td>
    </tr>
  </tbody>
</table>
</div>



The basic idea behind pivot tables is shown in the image below.

![pivot_picture.png](attachment:pivot_picture.png)

### Extra Groupby Puzzle

### groupby puzzle #5:  More careful look at the most popular 2018 name in California.

In goal 1, we didn't take into account the unlikely possibility that the most popular name was actually spread across both birth sexes. For example, what if in the table below it turns out that there were 300 female Noahs born in CA in 2018. In that case, Noah would actually be the most popular.

Since our queries are getting pretty long, I've stuck them inside parentheses which allows us to spread them over many lines.


```python
(
babynames[babynames["Year"] == 2018]
    .sort_values(by = "Count", ascending = False)
    .head(5)
)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>221160</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Emma</td>
      <td>2743</td>
    </tr>
    <tr>
      <th>385701</th>
      <td>CA</td>
      <td>M</td>
      <td>2018</td>
      <td>Noah</td>
      <td>2569</td>
    </tr>
    <tr>
      <th>221161</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Mia</td>
      <td>2499</td>
    </tr>
    <tr>
      <th>221162</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Olivia</td>
      <td>2465</td>
    </tr>
    <tr>
      <th>385702</th>
      <td>CA</td>
      <td>M</td>
      <td>2018</td>
      <td>Liam</td>
      <td>2413</td>
    </tr>
  </tbody>
</table>
</div>



Try to add a single line to the operation above so that each row represents the sum of male and female babies born in 2018 with that name. To do this, fill in the ??? below.


```python
(
babynames[babynames["Year"] == 2018]
    #.???
    .sort_values(by = "Count", ascending = False)
    .head(5)
)
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
      <th>Sex</th>
      <th>Year</th>
      <th>Name</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>221160</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Emma</td>
      <td>2743</td>
    </tr>
    <tr>
      <th>385701</th>
      <td>CA</td>
      <td>M</td>
      <td>2018</td>
      <td>Noah</td>
      <td>2569</td>
    </tr>
    <tr>
      <th>221161</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Mia</td>
      <td>2499</td>
    </tr>
    <tr>
      <th>221162</th>
      <td>CA</td>
      <td>F</td>
      <td>2018</td>
      <td>Olivia</td>
      <td>2465</td>
    </tr>
    <tr>
      <th>385702</th>
      <td>CA</td>
      <td>M</td>
      <td>2018</td>
      <td>Liam</td>
      <td>2413</td>
    </tr>
  </tbody>
</table>
</div>


