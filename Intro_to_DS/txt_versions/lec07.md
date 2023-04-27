```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Lecture 7 ##

## Random Sampling ##


```python
united = Table.read_table('united.csv')
united
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Date</th> <th>Flight Number</th> <th>Destination</th> <th>Delay</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>6/1/15</td> <td>73           </td> <td>HNL        </td> <td>257  </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>217          </td> <td>EWR        </td> <td>28   </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>237          </td> <td>STL        </td> <td>-3   </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>250          </td> <td>SAN        </td> <td>0    </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>267          </td> <td>PHL        </td> <td>64   </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>273          </td> <td>SEA        </td> <td>-6   </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>278          </td> <td>SEA        </td> <td>-8   </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>292          </td> <td>EWR        </td> <td>12   </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>300          </td> <td>HNL        </td> <td>20   </td>
        </tr>
        <tr>
            <td>6/1/15</td> <td>317          </td> <td>IND        </td> <td>-10  </td>
        </tr>
    </tbody>
</table>
<p>... (13815 rows omitted)</p>




```python
united.sample(100)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Date</th> <th>Flight Number</th> <th>Destination</th> <th>Delay</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8/20/15</td> <td>1655         </td> <td>DEN        </td> <td>-4   </td>
        </tr>
        <tr>
            <td>6/29/15</td> <td>1946         </td> <td>BOS        </td> <td>4    </td>
        </tr>
        <tr>
            <td>8/29/15</td> <td>1984         </td> <td>PDX        </td> <td>-5   </td>
        </tr>
        <tr>
            <td>7/29/15</td> <td>1120         </td> <td>IAH        </td> <td>2    </td>
        </tr>
        <tr>
            <td>8/24/15</td> <td>708          </td> <td>BOS        </td> <td>-3   </td>
        </tr>
        <tr>
            <td>7/14/15</td> <td>522          </td> <td>PDX        </td> <td>5    </td>
        </tr>
        <tr>
            <td>7/23/15</td> <td>205          </td> <td>PDX        </td> <td>77   </td>
        </tr>
        <tr>
            <td>7/29/15</td> <td>1670         </td> <td>HNL        </td> <td>0    </td>
        </tr>
        <tr>
            <td>6/29/15</td> <td>1721         </td> <td>KOA        </td> <td>4    </td>
        </tr>
        <tr>
            <td>6/29/15</td> <td>1743         </td> <td>LAX        </td> <td>-4   </td>
        </tr>
    </tbody>
</table>
<p>... (90 rows omitted)</p>



## Large Random Samples ##


```python
united 
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Row</th> <th>Date</th> <th>Flight Number</th> <th>Destination</th> <th>Delay</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0   </td> <td>6/1/15</td> <td>73           </td> <td>HNL        </td> <td>257  </td>
        </tr>
        <tr>
            <td>1   </td> <td>6/1/15</td> <td>217          </td> <td>EWR        </td> <td>28   </td>
        </tr>
        <tr>
            <td>2   </td> <td>6/1/15</td> <td>237          </td> <td>STL        </td> <td>-3   </td>
        </tr>
        <tr>
            <td>3   </td> <td>6/1/15</td> <td>250          </td> <td>SAN        </td> <td>0    </td>
        </tr>
        <tr>
            <td>4   </td> <td>6/1/15</td> <td>267          </td> <td>PHL        </td> <td>64   </td>
        </tr>
        <tr>
            <td>5   </td> <td>6/1/15</td> <td>273          </td> <td>SEA        </td> <td>-6   </td>
        </tr>
        <tr>
            <td>6   </td> <td>6/1/15</td> <td>278          </td> <td>SEA        </td> <td>-8   </td>
        </tr>
        <tr>
            <td>7   </td> <td>6/1/15</td> <td>292          </td> <td>EWR        </td> <td>12   </td>
        </tr>
        <tr>
            <td>8   </td> <td>6/1/15</td> <td>300          </td> <td>HNL        </td> <td>20   </td>
        </tr>
        <tr>
            <td>9   </td> <td>6/1/15</td> <td>317          </td> <td>IND        </td> <td>-10  </td>
        </tr>
    </tbody>
</table>
<p>... (13815 rows omitted)</p>




```python
# Population Distribution
united_bins = np.arange(-20, 201, 5)
united.hist('Delay', bins = united_bins)
```


    
![png](lec07_files/lec07_7_0.png)
    



```python
# (Sample) Empirical Distribution
united.sample(10).hist('Delay', bins = united_bins)
```


    
![png](lec07_files/lec07_8_0.png)
    



```python
# (Sample) Empirical Distribution
united.sample(1000).hist('Delay', bins = united_bins)
```


    
![png](lec07_files/lec07_9_0.png)
    


## Simulating Statistics ##


```python
# (Population) parameter # Usually unknown 
np.median(united.column('Delay'))
```




    2.0




```python
# (Sample) Statistic
np.median(united.sample(10).column('Delay'))
```




    -2.0




```python
def sample_median(size):
    return np.median(united.sample(size).column('Delay'))
```


```python
sample_median(10)
```




    -1.0




```python
sample_median(100)
```




    4.5




```python
sample_medians = make_array()

for i in np.arange(1000):
    new_median = sample_median(10)
    sample_medians = np.append(sample_medians, new_median)
```


```python
Table().with_column('Sample medians', sample_medians).hist(bins = np.arange(-10,31))
```


    
![png](lec07_files/lec07_17_0.png)
    



```python
sample_medians = make_array()

for i in np.arange(1000):
    new_median = sample_median(1000)
    sample_medians = np.append(sample_medians, new_median)
```


```python
Table().with_column(
    'Sample medians', sample_medians).hist(bins = np.arange(-10,31))
```


    
![png](lec07_files/lec07_19_0.png)
    


## Alameda County Jury Panels ##


```python
jury = Table().with_columns(
    'Ethnicity', make_array('Asian', 'Black', 'Latino', 'White', 'Other'),
    'Eligible', make_array(0.15, 0.18, 0.12, 0.54, 0.01),
    'Panels', make_array(0.26, 0.08, 0.08, 0.54, 0.04)
)

jury
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Ethnicity</th> <th>Eligible</th> <th>Panels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Asian    </td> <td>0.15    </td> <td>0.26  </td>
        </tr>
        <tr>
            <td>Black    </td> <td>0.18    </td> <td>0.08  </td>
        </tr>
        <tr>
            <td>Latino   </td> <td>0.12    </td> <td>0.08  </td>
        </tr>
        <tr>
            <td>White    </td> <td>0.54    </td> <td>0.54  </td>
        </tr>
        <tr>
            <td>Other    </td> <td>0.01    </td> <td>0.04  </td>
        </tr>
    </tbody>
</table>




```python
jury.barh('Ethnicity')
```


    
![png](lec07_files/lec07_22_0.png)
    



```python
# Under the model, this is the true distribution of people
# from which the jurors are randomly sampled
model = make_array(0.15, 0.18, 0.12, 0.54, 0.01)
```


```python
# Let's simulate a random draw of 1423 jurors from this distribution
simulated = sample_proportions(1423, model)
simulated
```




    array([0.1658468 , 0.17427969, 0.11243851, 0.53759663, 0.00983837])




```python
# The actual observed distribution (Panels) looks quite different
# from the simulation -- try running this several times to confirm!
jury_with_simulated = jury.with_column('Simulated', simulated)
jury_with_simulated
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Ethnicity</th> <th>Eligible</th> <th>Panels</th> <th>Simulated</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Asian    </td> <td>0.15    </td> <td>0.26  </td> <td>0.165847  </td>
        </tr>
        <tr>
            <td>Black    </td> <td>0.18    </td> <td>0.08  </td> <td>0.17428   </td>
        </tr>
        <tr>
            <td>Latino   </td> <td>0.12    </td> <td>0.08  </td> <td>0.112439  </td>
        </tr>
        <tr>
            <td>White    </td> <td>0.54    </td> <td>0.54  </td> <td>0.537597  </td>
        </tr>
        <tr>
            <td>Other    </td> <td>0.01    </td> <td>0.04  </td> <td>0.00983837</td>
        </tr>
    </tbody>
</table>




```python
jury_with_simulated.barh('Ethnicity')
```


    
![png](lec07_files/lec07_26_0.png)
    


## Distance Between Distributions


```python
# In this case, we need to understand how each of the 5 categories
# differ from their expected values according to the model.

diffs = jury.column('Panels') - jury.column('Eligible')
jury_with_difference = jury.with_column('Difference', diffs)
jury_with_difference
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Ethnicity</th> <th>Eligible</th> <th>Panels</th> <th>Difference</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Asian    </td> <td>0.15    </td> <td>0.26  </td> <td>0.11      </td>
        </tr>
        <tr>
            <td>Black    </td> <td>0.18    </td> <td>0.08  </td> <td>-0.1      </td>
        </tr>
        <tr>
            <td>Latino   </td> <td>0.12    </td> <td>0.08  </td> <td>-0.04     </td>
        </tr>
        <tr>
            <td>White    </td> <td>0.54    </td> <td>0.54  </td> <td>0         </td>
        </tr>
        <tr>
            <td>Other    </td> <td>0.01    </td> <td>0.04  </td> <td>0.03      </td>
        </tr>
    </tbody>
</table>




```python
sum(abs(jury_with_difference.column("Difference")))/2
```




    0.14



## Total Variation Distance


```python
def tvd(dist1, dist2):
    return sum(abs(dist1 - dist2))/2
```


```python
# The TVD of our observed data (Panels) from their expected values
# assuming the model is true (Eligbible)
obsvd_tvd = tvd(jury.column('Panels'), jury.column('Eligible'))
obsvd_tvd
```




    0.14




```python
# The TVD of a model simluation from its expected values
tvd(sample_proportions(1423, model), jury.column('Eligible'))
```




    0.02234012649332397




```python
def simulated_tvd():
    return tvd(sample_proportions(1423, model), model)

tvds = make_array()

num_simulations = 10000
for i in np.arange(num_simulations):
    new_tvd = simulated_tvd()
    tvds = np.append(tvds, new_tvd)
```


```python
title = 'Simulated TVDs (if model is true)'
bins = np.arange(0, .05, .005)

Table().with_column(title, tvds).hist(bins = bins)
print('Observed TVD: ' + str(obsvd_tvd))
```

    Observed TVD: 0.14



    
![png](lec07_files/lec07_35_1.png)
    

