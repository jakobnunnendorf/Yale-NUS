```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Arrays


```python
my_array = make_array(1, 2, 3, 4)
```


```python
my_array
```




    array([1, 2, 3, 4])




```python
my_array * 2
```




    array([2, 4, 6, 8])




```python
my_array ** 2
```




    array([ 1,  4,  9, 16])




```python
my_array + 1
```




    array([2, 3, 4, 5])




```python
my_array # array is unchanged
```




    array([1, 2, 3, 4])




```python
len(my_array)
```




    4




```python
sum(my_array)
```




    10




```python
sum(my_array) / len(my_array)
```




    2.5




```python
np.average(my_array)
```




    2.5




```python
another = make_array(70, 60, 90, 80)
```


```python
my_array + another
```




    array([71, 62, 93, 84])




```python
yet_another = make_array(5, 6, 7)
```


```python
my_array + yet_another
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-21-a4a5e45ad569> in <module>
    ----> 1 my_array + yet_another
    

    ValueError: operands could not be broadcast together with shapes (4,) (3,) 



```python
tunas = make_array('bluefin', 'albacore', 'jim')
tunas
```




    array(['bluefin', 'albacore', 'jim'], dtype='<U8')




```python
tunas * 4
```


    ---------------------------------------------------------------------------

    UFuncTypeError                            Traceback (most recent call last)

    <ipython-input-23-f8fd22639529> in <module>
          1 # HOWEVER, can NOT use multiplication on string arrays
          2 
    ----> 3 tunas * 4
          4 
          5 # SOME OPERTIONS you can do on an array are LIMITED


    UFuncTypeError: ufunc 'multiply' did not contain a loop with signature matching types (dtype('<U8'), dtype('<U8')) -> dtype('<U8')



```python
tunas.item(0) # NOTE: indexing starts at 0!
```




    'bluefin'




```python
tunas.item(2)
```




    'jim'




```python
tunas.item(3)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-26-6d89581c3231> in <module>
          1 # [Q] what do you think will happen if I do .item(3) ?
          2 
    ----> 3 tunas.item(3)
    

    IndexError: index 3 is out of bounds for axis 0 with size 3


## Columns of Tables are Arrays ##


```python
nba = Table.read_table('nba_salaries.csv').relabeled(3, 'SALARY')
warriors = nba.where('TEAM', 'Golden State Warriors')
```


```python
warriors
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>TEAM</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Klay Thompson    </td> <td>SG      </td> <td>Golden State Warriors</td> <td>15.501 </td>
        </tr>
        <tr>
            <td>Draymond Green   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>14.2609</td>
        </tr>
        <tr>
            <td>Andrew Bogut     </td> <td>C       </td> <td>Golden State Warriors</td> <td>13.8   </td>
        </tr>
        <tr>
            <td>Andre Iguodala   </td> <td>SF      </td> <td>Golden State Warriors</td> <td>11.7105</td>
        </tr>
        <tr>
            <td>Stephen Curry    </td> <td>PG      </td> <td>Golden State Warriors</td> <td>11.3708</td>
        </tr>
        <tr>
            <td>Jason Thompson   </td> <td>PF      </td> <td>Golden State Warriors</td> <td>7.00847</td>
        </tr>
        <tr>
            <td>Shaun Livingston </td> <td>PG      </td> <td>Golden State Warriors</td> <td>5.54373</td>
        </tr>
        <tr>
            <td>Harrison Barnes  </td> <td>SF      </td> <td>Golden State Warriors</td> <td>3.8734 </td>
        </tr>
        <tr>
            <td>Marreese Speights</td> <td>C       </td> <td>Golden State Warriors</td> <td>3.815  </td>
        </tr>
        <tr>
            <td>Leandro Barbosa  </td> <td>SG      </td> <td>Golden State Warriors</td> <td>2.5    </td>
        </tr>
    </tbody>
</table>
<p>... (4 rows omitted)</p>




```python
warriors.select('SALARY')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>15.501 </td>
        </tr>
        <tr>
            <td>14.2609</td>
        </tr>
        <tr>
            <td>13.8   </td>
        </tr>
        <tr>
            <td>11.7105</td>
        </tr>
        <tr>
            <td>11.3708</td>
        </tr>
        <tr>
            <td>7.00847</td>
        </tr>
        <tr>
            <td>5.54373</td>
        </tr>
        <tr>
            <td>3.8734 </td>
        </tr>
        <tr>
            <td>3.815  </td>
        </tr>
        <tr>
            <td>2.5    </td>
        </tr>
    </tbody>
</table>
<p>... (4 rows omitted)</p>




```python
warriors.column('SALARY')
```




    array([15.501   , 14.26087 , 13.8     , 11.710456, 11.370786,  7.008475,
            5.543725,  3.873398,  3.815   ,  2.5     ,  2.008748,  1.270964,
            1.13196 ,  0.289755])




```python
np.average(warriors.column('SALARY'))
```




    6.72036692857143




```python
raptors = nba.where('TEAM', 'Toronto Raptors')
```


```python
np.average(warriors.column('SALARY')) - np.average(raptors.column('SALARY'))
```




    2.3278598697479005



## Ranges ##


```python
make_array(0, 1, 2, 3, 4, 5, 6)
```




    array([0, 1, 2, 3, 4, 5, 6])




```python
np.arange(7)
```




    array([0, 1, 2, 3, 4, 5, 6])




```python
np.arange(5, 11)
```




    array([ 5,  6,  7,  8,  9, 10])




```python
np.arange(0, 20, 2)
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])




```python
np.arange(0, 21, 2)
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20])




```python
np.arange(0, 1, 0.1)
```




    array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])



## Python list can hold heterogeneous data types ##


```python
l = [True, "HelloWorld",1,2.3]
print(l)
```

    [True, 'HelloWorld', 1, 2.3]


## Creating array from scratch via numpy ##


```python
# Create an array from a list
np.array([1,2,3,4])
```




    array([1, 2, 3, 4])




```python
# Create a length-10 array filled with zeros
np.zeros(10)
```




    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])




```python
# Create a length-10 array filled with ones
np.ones(10)
```




    array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])



## Array indexing ##


```python
a1 = np.array([5,0,9,8])
a1
```




    array([5, 0, 9, 8])




```python
# first element
a1[0]
```




    5




```python
# third element
a1[2]
```




    9




```python
# last elemeent
a1[-1]
```




    8



## Array slicing ##


```python
x1 = np.arange(0,10)
x1
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
# from index 1 onwards
x1[1:]
```




    array([1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
# first 5 elements
x1[:5]
```




    array([0, 1, 2, 3, 4])




```python
# from index 4 to index 6
x1[4:7]
```




    array([4, 5, 6])




```python

```

# Ways to Create a Table #

## Creating a Table from Scratch ##


```python
rcs = make_array('Elm', 'Saga', 'Cendana')
rcs
```




    array(['Elm', 'Saga', 'Cendana'], dtype='<U7')




```python
Table()
```




<table border="1" class="dataframe">
    <thead>
        <tr>

        </tr>
    </thead>
    <tbody>
    </tbody>
</table>




```python
yalenus = Table().with_column('Residential Colleges', rcs)
yalenus
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Residential Colleges</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Elm                 </td>
        </tr>
        <tr>
            <td>Saga                </td>
        </tr>
        <tr>
            <td>Cendana             </td>
        </tr>
    </tbody>
</table>




```python
yalenus.with_column('Number of students', np.arange(100,130,10))
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Residential Colleges</th> <th>Number of students</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Elm                 </td> <td>100               </td>
        </tr>
        <tr>
            <td>Saga                </td> <td>110               </td>
        </tr>
        <tr>
            <td>Cendana             </td> <td>120               </td>
        </tr>
    </tbody>
</table>




```python
yalenus
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Residential Colleges</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Elm                 </td>
        </tr>
        <tr>
            <td>Saga                </td>
        </tr>
        <tr>
            <td>Cendana             </td>
        </tr>
    </tbody>
</table>




```python
yalenus = yalenus.with_column('Number of students', np.arange(100,130,10))
yalenus
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Residential Colleges</th> <th>Number of students</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Elm                 </td> <td>100               </td>
        </tr>
        <tr>
            <td>Saga                </td> <td>110               </td>
        </tr>
        <tr>
            <td>Cendana             </td> <td>120               </td>
        </tr>
    </tbody>
</table>




```python
Table().with_columns(
    'Residential Colleges', rcs,
    'Number of students', np.arange(100,130,10)
)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Residential Colleges</th> <th>Number of students</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Elm                 </td> <td>100               </td>
        </tr>
        <tr>
            <td>Saga                </td> <td>110               </td>
        </tr>
        <tr>
            <td>Cendana             </td> <td>120               </td>
        </tr>
    </tbody>
</table>



## Reading a Table from a File  ##


```python
du_bois = Table.read_table('du_bois.csv')
du_bois
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>CLASS</th> <th>ACTUAL AVERAGE</th> <th>RENT</th> <th>FOOD</th> <th>CLOTHES</th> <th>TAXES</th> <th>OTHER</th> <th>STATUS</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>100-200      </td> <td>139.1         </td> <td>0.19</td> <td>0.43</td> <td>0.28   </td> <td>0.001</td> <td>0.099</td> <td>POOR       </td>
        </tr>
        <tr>
            <td>200-300      </td> <td>249.45        </td> <td>0.22</td> <td>0.47</td> <td>0.23   </td> <td>0.04 </td> <td>0.04 </td> <td>POOR       </td>
        </tr>
        <tr>
            <td>300-400      </td> <td>335.66        </td> <td>0.23</td> <td>0.43</td> <td>0.18   </td> <td>0.045</td> <td>0.115</td> <td>FAIR       </td>
        </tr>
        <tr>
            <td>400-500      </td> <td>433.82        </td> <td>0.18</td> <td>0.37</td> <td>0.15   </td> <td>0.055</td> <td>0.245</td> <td>FAIR       </td>
        </tr>
        <tr>
            <td>500-750      </td> <td>547           </td> <td>0.13</td> <td>0.31</td> <td>0.17   </td> <td>0.05 </td> <td>0.34 </td> <td>COMFORTABLE</td>
        </tr>
        <tr>
            <td>750-1000     </td> <td>880           </td> <td>0   </td> <td>0.37</td> <td>0.19   </td> <td>0.08 </td> <td>0.36 </td> <td>COMFORTABLE</td>
        </tr>
        <tr>
            <td>1000 and over</td> <td>1125          </td> <td>0   </td> <td>0.29</td> <td>0.16   </td> <td>0.045</td> <td>0.505</td> <td>WELL-TO-DO </td>
        </tr>
    </tbody>
</table>




```python
du_bois.column('ACTUAL AVERAGE')
```




    array([ 139.1 ,  249.45,  335.66,  433.82,  547.  ,  880.  , 1125.  ])




```python
du_bois.column('FOOD')
```




    array([0.43, 0.47, 0.43, 0.37, 0.31, 0.37, 0.29])




```python
du_bois.column('ACTUAL AVERAGE') * du_bois.column('FOOD')
```




    array([ 59.813 , 117.2415, 144.3338, 160.5134, 169.57  , 325.6   ,
           326.25  ])




```python
food_dollars = du_bois.column('ACTUAL AVERAGE') * du_bois.column('FOOD')
du_bois.with_columns('Food $', food_dollars)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>CLASS</th> <th>ACTUAL AVERAGE</th> <th>RENT</th> <th>FOOD</th> <th>CLOTHES</th> <th>TAXES</th> <th>OTHER</th> <th>STATUS</th> <th>Food $</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>100-200      </td> <td>139.1         </td> <td>0.19</td> <td>0.43</td> <td>0.28   </td> <td>0.001</td> <td>0.099</td> <td>POOR       </td> <td>59.813 </td>
        </tr>
        <tr>
            <td>200-300      </td> <td>249.45        </td> <td>0.22</td> <td>0.47</td> <td>0.23   </td> <td>0.04 </td> <td>0.04 </td> <td>POOR       </td> <td>117.241</td>
        </tr>
        <tr>
            <td>300-400      </td> <td>335.66        </td> <td>0.23</td> <td>0.43</td> <td>0.18   </td> <td>0.045</td> <td>0.115</td> <td>FAIR       </td> <td>144.334</td>
        </tr>
        <tr>
            <td>400-500      </td> <td>433.82        </td> <td>0.18</td> <td>0.37</td> <td>0.15   </td> <td>0.055</td> <td>0.245</td> <td>FAIR       </td> <td>160.513</td>
        </tr>
        <tr>
            <td>500-750      </td> <td>547           </td> <td>0.13</td> <td>0.31</td> <td>0.17   </td> <td>0.05 </td> <td>0.34 </td> <td>COMFORTABLE</td> <td>169.57 </td>
        </tr>
        <tr>
            <td>750-1000     </td> <td>880           </td> <td>0   </td> <td>0.37</td> <td>0.19   </td> <td>0.08 </td> <td>0.36 </td> <td>COMFORTABLE</td> <td>325.6  </td>
        </tr>
        <tr>
            <td>1000 and over</td> <td>1125          </td> <td>0   </td> <td>0.29</td> <td>0.16   </td> <td>0.045</td> <td>0.505</td> <td>WELL-TO-DO </td> <td>326.25 </td>
        </tr>
    </tbody>
</table>




```python
du_bois.select('CLASS', 'ACTUAL AVERAGE', 'FOOD', 'Food $')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-62-15a9d3d2329e> in <module>
          3 # class, average, food proportion, food $
          4 
    ----> 5 du_bois.select('CLASS', 'ACTUAL AVERAGE', 'FOOD', 'Food $')
          6 
          7 # get an error!


    ~/anaconda/lib/python3.6/site-packages/datascience/tables.py in select(self, *column_or_columns)
        648         table = type(self)()
        649         for label in labels:
    --> 650             self._add_column_and_format(table, label, np.copy(self[label]))
        651         return table
        652 


    ~/anaconda/lib/python3.6/site-packages/datascience/tables.py in __getitem__(self, index_or_label)
        167 
        168     def __getitem__(self, index_or_label):
    --> 169         return self.column(index_or_label)
        170 
        171     def __setitem__(self, index_or_label, values):


    ~/anaconda/lib/python3.6/site-packages/datascience/tables.py in column(self, index_or_label)
        275                 'The column "{}" is not in the table. The table contains '
        276                 'these columns: {}'
    --> 277                 .format(index_or_label, ', '.join(self.labels))
        278             )
        279         if (isinstance(index_or_label, int)


    ValueError: The column "Food $" is not in the table. The table contains these columns: CLASS, ACTUAL AVERAGE, RENT, FOOD, CLOTHES, TAXES, OTHER, STATUS



```python
food_dollars = du_bois.column('ACTUAL AVERAGE') * du_bois.column('FOOD')

du_bois = du_bois.with_columns('Food $', food_dollars)

du_bois
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>CLASS</th> <th>ACTUAL AVERAGE</th> <th>RENT</th> <th>FOOD</th> <th>CLOTHES</th> <th>TAXES</th> <th>OTHER</th> <th>STATUS</th> <th>Food $</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>100-200      </td> <td>139.1         </td> <td>0.19</td> <td>0.43</td> <td>0.28   </td> <td>0.001</td> <td>0.099</td> <td>POOR       </td> <td>59.813 </td>
        </tr>
        <tr>
            <td>200-300      </td> <td>249.45        </td> <td>0.22</td> <td>0.47</td> <td>0.23   </td> <td>0.04 </td> <td>0.04 </td> <td>POOR       </td> <td>117.241</td>
        </tr>
        <tr>
            <td>300-400      </td> <td>335.66        </td> <td>0.23</td> <td>0.43</td> <td>0.18   </td> <td>0.045</td> <td>0.115</td> <td>FAIR       </td> <td>144.334</td>
        </tr>
        <tr>
            <td>400-500      </td> <td>433.82        </td> <td>0.18</td> <td>0.37</td> <td>0.15   </td> <td>0.055</td> <td>0.245</td> <td>FAIR       </td> <td>160.513</td>
        </tr>
        <tr>
            <td>500-750      </td> <td>547           </td> <td>0.13</td> <td>0.31</td> <td>0.17   </td> <td>0.05 </td> <td>0.34 </td> <td>COMFORTABLE</td> <td>169.57 </td>
        </tr>
        <tr>
            <td>750-1000     </td> <td>880           </td> <td>0   </td> <td>0.37</td> <td>0.19   </td> <td>0.08 </td> <td>0.36 </td> <td>COMFORTABLE</td> <td>325.6  </td>
        </tr>
        <tr>
            <td>1000 and over</td> <td>1125          </td> <td>0   </td> <td>0.29</td> <td>0.16   </td> <td>0.045</td> <td>0.505</td> <td>WELL-TO-DO </td> <td>326.25 </td>
        </tr>
    </tbody>
</table>




```python
du_bois.select('CLASS', 'ACTUAL AVERAGE', 'FOOD', 'Food $')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>CLASS</th> <th>ACTUAL AVERAGE</th> <th>FOOD</th> <th>Food $</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>100-200      </td> <td>139.1         </td> <td>0.43</td> <td>59.813 </td>
        </tr>
        <tr>
            <td>200-300      </td> <td>249.45        </td> <td>0.47</td> <td>117.241</td>
        </tr>
        <tr>
            <td>300-400      </td> <td>335.66        </td> <td>0.43</td> <td>144.334</td>
        </tr>
        <tr>
            <td>400-500      </td> <td>433.82        </td> <td>0.37</td> <td>160.513</td>
        </tr>
        <tr>
            <td>500-750      </td> <td>547           </td> <td>0.31</td> <td>169.57 </td>
        </tr>
        <tr>
            <td>750-1000     </td> <td>880           </td> <td>0.37</td> <td>325.6  </td>
        </tr>
        <tr>
            <td>1000 and over</td> <td>1125          </td> <td>0.29</td> <td>326.25 </td>
        </tr>
    </tbody>
</table>




```python
du_bois.labels
```




    ('CLASS',
     'ACTUAL AVERAGE',
     'RENT',
     'FOOD',
     'CLOTHES',
     'TAXES',
     'OTHER',
     'STATUS',
     'Food $')




```python
du_bois.num_rows
```




    7




```python
du_bois.num_columns
```




    9



## Discussion Question: NBA Salaries


```python
nba = Table.read_table('nba_salaries.csv')
nba = nba.relabeled(3, 'SALARY').drop('TEAM')
nba.show(3)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Paul Millsap  </td> <td>PF      </td> <td>18.6717</td>
        </tr>
        <tr>
            <td>Al Horford    </td> <td>C       </td> <td>12     </td>
        </tr>
        <tr>
            <td>Tiago Splitter</td> <td>C       </td> <td>9.75625</td>
        </tr>
    </tbody>
</table>
<p>... (414 rows omitted)</p>



```python
# Question (a)
guards = nba.where('POSITION', 'PG')
guards.where('SALARY', are.above(15)).column('PLAYER')
```




    array(['Derrick Rose', 'Kyrie Irving', 'Chris Paul', 'Russell Westbrook',
           'John Wall'], dtype='<U24')




```python
# Question (b)
nba.drop('POSITION')
nba.num_columns
```




    3




```python
nba.where('POSITION','PG').append(nba.where('POSITION','C')).show(100)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>PLAYER</th> <th>POSITION</th> <th>SALARY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Jeff Teague            </td> <td>PG      </td> <td>8       </td>
        </tr>
        <tr>
            <td>Dennis Schroder        </td> <td>PG      </td> <td>1.7634  </td>
        </tr>
        <tr>
            <td>Avery Bradley          </td> <td>PG      </td> <td>7.73034 </td>
        </tr>
        <tr>
            <td>Isaiah Thomas          </td> <td>PG      </td> <td>6.91287 </td>
        </tr>
        <tr>
            <td>Marcus Smart           </td> <td>PG      </td> <td>3.43104 </td>
        </tr>
        <tr>
            <td>Terry Rozier           </td> <td>PG      </td> <td>1.82436 </td>
        </tr>
        <tr>
            <td>Jarrett Jack           </td> <td>PG      </td> <td>6.3     </td>
        </tr>
        <tr>
            <td>Shane Larkin           </td> <td>PG      </td> <td>1.5     </td>
        </tr>
        <tr>
            <td>Kemba Walker           </td> <td>PG      </td> <td>12      </td>
        </tr>
        <tr>
            <td>Brian Roberts          </td> <td>PG      </td> <td>2.85494 </td>
        </tr>
        <tr>
            <td>Jeremy Lin             </td> <td>PG      </td> <td>2.139   </td>
        </tr>
        <tr>
            <td>Jorge Gutierrez        </td> <td>PG      </td> <td>0.947276</td>
        </tr>
        <tr>
            <td>Derrick Rose           </td> <td>PG      </td> <td>20.0931 </td>
        </tr>
        <tr>
            <td>Aaron Brooks           </td> <td>PG      </td> <td>2.25    </td>
        </tr>
        <tr>
            <td>Kyrie Irving           </td> <td>PG      </td> <td>16.4075 </td>
        </tr>
        <tr>
            <td>Mo Williams            </td> <td>PG      </td> <td>2.1     </td>
        </tr>
        <tr>
            <td>Matthew Dellavedova    </td> <td>PG      </td> <td>1.14728 </td>
        </tr>
        <tr>
            <td>Deron Williams         </td> <td>PG      </td> <td>5.37897 </td>
        </tr>
        <tr>
            <td>J.J. Barea             </td> <td>PG      </td> <td>4.29    </td>
        </tr>
        <tr>
            <td>Devin Harris           </td> <td>PG      </td> <td>4.05345 </td>
        </tr>
        <tr>
            <td>Raymond Felton         </td> <td>PG      </td> <td>3.95031 </td>
        </tr>
        <tr>
            <td>Jameer Nelson          </td> <td>PG      </td> <td>4.345   </td>
        </tr>
        <tr>
            <td>Emmanuel Mudiay        </td> <td>PG      </td> <td>3.10224 </td>
        </tr>
        <tr>
            <td>Reggie Jackson         </td> <td>PG      </td> <td>13.913  </td>
        </tr>
        <tr>
            <td>Stephen Curry          </td> <td>PG      </td> <td>11.3708 </td>
        </tr>
        <tr>
            <td>Shaun Livingston       </td> <td>PG      </td> <td>5.54373 </td>
        </tr>
        <tr>
            <td>Ty Lawson              </td> <td>PG      </td> <td>12.4045 </td>
        </tr>
        <tr>
            <td>Patrick Beverley       </td> <td>PG      </td> <td>6.48649 </td>
        </tr>
        <tr>
            <td>Rodney Stuckey         </td> <td>PG      </td> <td>7       </td>
        </tr>
        <tr>
            <td>Joe Young              </td> <td>PG      </td> <td>1.00703 </td>
        </tr>
        <tr>
            <td>Chris Paul             </td> <td>PG      </td> <td>21.4687 </td>
        </tr>
        <tr>
            <td>Austin Rivers          </td> <td>PG      </td> <td>3.1108  </td>
        </tr>
        <tr>
            <td>Pablo Prigioni         </td> <td>PG      </td> <td>0.947726</td>
        </tr>
        <tr>
            <td>D'Angelo Russell       </td> <td>PG      </td> <td>5.10312 </td>
        </tr>
        <tr>
            <td>Mike Conley            </td> <td>PG      </td> <td>9.58843 </td>
        </tr>
        <tr>
            <td>Mario Chalmers         </td> <td>PG      </td> <td>4.3     </td>
        </tr>
        <tr>
            <td>Beno Udrih             </td> <td>PG      </td> <td>2.17047 </td>
        </tr>
        <tr>
            <td>Russ Smith             </td> <td>PG      </td> <td>0.845059</td>
        </tr>
        <tr>
            <td>Goran Dragic           </td> <td>PG      </td> <td>14.783  </td>
        </tr>
        <tr>
            <td>Corey Hawkins          </td> <td>PG      </td> <td>0.525093</td>
        </tr>
        <tr>
            <td>Greivis Vasquez        </td> <td>PG      </td> <td>6.6     </td>
        </tr>
        <tr>
            <td>Jerryd Bayless         </td> <td>PG      </td> <td>3       </td>
        </tr>
        <tr>
            <td>Michael Carter-Williams</td> <td>PG      </td> <td>2.39904 </td>
        </tr>
        <tr>
            <td>Tyler Ennis            </td> <td>PG      </td> <td>1.66236 </td>
        </tr>
        <tr>
            <td>Ricky Rubio            </td> <td>PG      </td> <td>12.7    </td>
        </tr>
        <tr>
            <td>Zach LaVine            </td> <td>PG      </td> <td>2.14836 </td>
        </tr>
        <tr>
            <td>Tyus Jones             </td> <td>PG      </td> <td>1.28208 </td>
        </tr>
        <tr>
            <td>Jrue Holiday           </td> <td>PG      </td> <td>10.5955 </td>
        </tr>
        <tr>
            <td>Norris Cole            </td> <td>PG      </td> <td>3.03693 </td>
        </tr>
        <tr>
            <td>Toney Douglas          </td> <td>PG      </td> <td>1.16486 </td>
        </tr>
        <tr>
            <td>Bo McCalebb            </td> <td>PG      </td> <td>0.525093</td>
        </tr>
        <tr>
            <td>Jose Calderon          </td> <td>PG      </td> <td>7.40281 </td>
        </tr>
        <tr>
            <td>Jerian Grant           </td> <td>PG      </td> <td>1.57236 </td>
        </tr>
        <tr>
            <td>Jimmer Fredette        </td> <td>PG      </td> <td>0.874837</td>
        </tr>
        <tr>
            <td>Russell Westbrook      </td> <td>PG      </td> <td>16.7442 </td>
        </tr>
        <tr>
            <td>D.J. Augustin          </td> <td>PG      </td> <td>3       </td>
        </tr>
        <tr>
            <td>Cameron Payne          </td> <td>PG      </td> <td>2.02152 </td>
        </tr>
        <tr>
            <td>Brandon Jennings       </td> <td>PG      </td> <td>8.3445  </td>
        </tr>
        <tr>
            <td>Elfrid Payton          </td> <td>PG      </td> <td>2.50572 </td>
        </tr>
        <tr>
            <td>Shabazz Napier         </td> <td>PG      </td> <td>1.29444 </td>
        </tr>
        <tr>
            <td>Keith Appling          </td> <td>PG      </td> <td>0.061776</td>
        </tr>
        <tr>
            <td>Kendall Marshall       </td> <td>PG      </td> <td>2.14477 </td>
        </tr>
        <tr>
            <td>Eric Bledsoe           </td> <td>PG      </td> <td>13.5    </td>
        </tr>
        <tr>
            <td>Bryce Cotton           </td> <td>PG      </td> <td>0.700902</td>
        </tr>
        <tr>
            <td>Lorenzo Brown          </td> <td>PG      </td> <td>0.111444</td>
        </tr>
        <tr>
            <td>Phil Pressey           </td> <td>PG      </td> <td>0.055722</td>
        </tr>
        <tr>
            <td>Damian Lillard         </td> <td>PG      </td> <td>4.23629 </td>
        </tr>
        <tr>
            <td>Rajon Rondo            </td> <td>PG      </td> <td>9.5     </td>
        </tr>
        <tr>
            <td>Darren Collison        </td> <td>PG      </td> <td>5.01356 </td>
        </tr>
        <tr>
            <td>Tony Parker            </td> <td>PG      </td> <td>13.4375 </td>
        </tr>
        <tr>
            <td>Patty Mills            </td> <td>PG      </td> <td>3.57895 </td>
        </tr>
        <tr>
            <td>Ray McCallum           </td> <td>PG      </td> <td>0.947276</td>
        </tr>
        <tr>
            <td>Kyle Lowry             </td> <td>PG      </td> <td>12      </td>
        </tr>
        <tr>
            <td>Cory Joseph            </td> <td>PG      </td> <td>7       </td>
        </tr>
        <tr>
            <td>Luke Ridnour           </td> <td>PG      </td> <td>2.75    </td>
        </tr>
        <tr>
            <td>Delon Wright           </td> <td>PG      </td> <td>1.50936 </td>
        </tr>
        <tr>
            <td>Shannon Scott          </td> <td>PG      </td> <td>0.525093</td>
        </tr>
        <tr>
            <td>Dante Exum             </td> <td>PG      </td> <td>3.77772 </td>
        </tr>
        <tr>
            <td>Trey Burke             </td> <td>PG      </td> <td>2.65824 </td>
        </tr>
        <tr>
            <td>Shelvin Mack           </td> <td>PG      </td> <td>2.43333 </td>
        </tr>
        <tr>
            <td>Raul Neto              </td> <td>PG      </td> <td>0.9     </td>
        </tr>
        <tr>
            <td>Erick Green            </td> <td>PG      </td> <td>0.099418</td>
        </tr>
        <tr>
            <td>John Wall              </td> <td>PG      </td> <td>15.852  </td>
        </tr>
        <tr>
            <td>Ramon Sessions         </td> <td>PG      </td> <td>2.17047 </td>
        </tr>
        <tr>
            <td>Gary Neal              </td> <td>PG      </td> <td>2.139   </td>
        </tr>
        <tr>
            <td>Al Horford             </td> <td>C       </td> <td>12      </td>
        </tr>
        <tr>
            <td>Tiago Splitter         </td> <td>C       </td> <td>9.75625 </td>
        </tr>
        <tr>
            <td>Walter Tavares         </td> <td>C       </td> <td>1       </td>
        </tr>
        <tr>
            <td>Tyler Zeller           </td> <td>C       </td> <td>2.61698 </td>
        </tr>
        <tr>
            <td>Jared Sullinger        </td> <td>C       </td> <td>2.56926 </td>
        </tr>
        <tr>
            <td>Kelly Olynyk           </td> <td>C       </td> <td>2.16516 </td>
        </tr>
        <tr>
            <td>Andrea Bargnani        </td> <td>C       </td> <td>1.3629  </td>
        </tr>
        <tr>
            <td>Al Jefferson           </td> <td>C       </td> <td>13.5    </td>
        </tr>
        <tr>
            <td>Cody Zeller            </td> <td>C       </td> <td>4.2042  </td>
        </tr>
        <tr>
            <td>Frank Kaminsky III     </td> <td>C       </td> <td>2.61252 </td>
        </tr>
        <tr>
            <td>Joakim Noah            </td> <td>C       </td> <td>13.4    </td>
        </tr>
        <tr>
            <td>Pau Gasol              </td> <td>C       </td> <td>7.44876 </td>
        </tr>
        <tr>
            <td>Tristan Thompson       </td> <td>C       </td> <td>14.2609 </td>
        </tr>
        <tr>
            <td>Brendan Haywood        </td> <td>C       </td> <td>10.5225 </td>
        </tr>
        <tr>
            <td>Timofey Mozgov         </td> <td>C       </td> <td>4.95    </td>
        </tr>
    </tbody>
</table>
<p>... (54 rows omitted)</p>



```python

```
