```python
from datascience import *
import numpy as np
import warnings
warnings.filterwarnings("ignore")

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
plots.rcParams["patch.force_edgecolor"] = True
```

## Lecture 5##

## Functions ##


```python
def triple(x):
    """multiply 3 to x"""
    return 3 * x
```


```python
triple(3)
```




    9




```python
num = 4
```


```python
triple(num)
```




    12




```python
triple(num * 5)
```




    60



### Multiple Arguments

$ h^2 = x^2 + y^2 \hspace{20 pt} => \hspace{20 pt} h = \sqrt{ x^2 + y^2 } $


```python
def hypotenuse(x,y):
    hypot_squared = (x ** 2 + y ** 2)
    return hypot_squared ** 0.5
```


```python
hypotenuse(9, 12)
```




    15.0




```python
hypotenuse(2, 2)
```




    2.8284271247461903



## Apply


```python
ages = Table().with_columns(
    'Person', make_array('Jim', 'Pam', 'Michael', 'Creed'),
    'Birth Year', make_array(1985, 1988, 1967, 1904)
)
ages
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Person</th> <th>Birth Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Jim    </td> <td>1985      </td>
        </tr>
        <tr>
            <td>Pam    </td> <td>1988      </td>
        </tr>
        <tr>
            <td>Michael</td> <td>1967      </td>
        </tr>
        <tr>
            <td>Creed  </td> <td>1904      </td>
        </tr>
    </tbody>
</table>




```python
def cap_at_1980(x):
    return min(x, 1980)
```


```python
cap_at_1980(1975)
```




    1975




```python
cap_at_1980(1991)
```




    1980




```python
ages.apply(cap_at_1980, 'Birth Year')
```




    array([1980, 1980, 1967, 1904], dtype=int64)




```python
def name_and_age(name, year):
    age = 2022 - year
    return name + ' is ' + str(age)
```


```python
ages.apply(name_and_age, 'Person', 'Birth Year')
```




    array(['Jim is 34', 'Pam is 31', 'Michael is 52', 'Creed is 115'],
          dtype='<U13')




```python

```

## Grouping by One Column ##


```python
cones = Table.read_table('cones.csv')
```


```python
cones
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
cones.group('Flavor')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bubblegum </td> <td>1    </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>3    </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>2    </td>
        </tr>
    </tbody>
</table>




```python
cones.drop('Color').group('Flavor', np.average)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Price average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bubblegum </td> <td>4.75         </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>5.08333      </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>4.4          </td>
        </tr>
    </tbody>
</table>




```python
cones.drop('Color').group('Flavor', min)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Price min</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>bubblegum </td> <td>4.75     </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>4.75     </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>3.55     </td>
        </tr>
    </tbody>
</table>



## Grouping By One Column: Welcome Survey ##


```python
survey = Table.read_table('welcome_survey_v1.csv')
survey
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Extraversion</th> <th>Number of textees</th> <th>Hours of sleep</th> <th>Handedness</th> <th>Pant leg</th> <th>Sleep position</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8           </td> <td>10               </td> <td>6             </td> <td>Left-handed </td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>7           </td> <td>4                </td> <td>7             </td> <td>Left-handed </td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>3           </td> <td>6                </td> <td>7             </td> <td>Left-handed </td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>3           </td> <td>8                </td> <td>7             </td> <td>Left-handed </td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>3           </td> <td>3                </td> <td>9             </td> <td>Left-handed </td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>3           </td> <td>1                </td> <td>5             </td> <td>Right-handed</td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>4           </td> <td>6                </td> <td>5             </td> <td>Right-handed</td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>4           </td> <td>1                </td> <td>6             </td> <td>Right-handed</td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>3           </td> <td>3                </td> <td>6             </td> <td>Right-handed</td> <td>I don't know</td> <td>On your back  </td>
        </tr>
        <tr>
            <td>5           </td> <td>3                </td> <td>6             </td> <td>Right-handed</td> <td>I don't know</td> <td>On your back  </td>
        </tr>
    </tbody>
</table>
<p>... (1281 rows omitted)</p>




```python
by_extra = survey.group('Extraversion', np.average)
by_extra
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Extraversion</th> <th>Number of textees average</th> <th>Hours of sleep average</th> <th>Handedness average</th> <th>Pant leg average</th> <th>Sleep position average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1           </td> <td>2.57895                  </td> <td>7.21053               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>2           </td> <td>4.30612                  </td> <td>7.10204               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>3           </td> <td>5.43529                  </td> <td>7.12941               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>4           </td> <td>5.75                     </td> <td>7.09398               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>5           </td> <td>5.92216                  </td> <td>7.1488                </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>6           </td> <td>6.52121                  </td> <td>7.07576               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>7           </td> <td>7.79039                  </td> <td>7.1441                </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>8           </td> <td>8.6036                   </td> <td>7.26577               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>9           </td> <td>10.8889                  </td> <td>7.48889               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
        <tr>
            <td>10          </td> <td>18.6667                  </td> <td>7.77778               </td> <td>                  </td> <td>                </td> <td>                      </td>
        </tr>
    </tbody>
</table>




```python
by_extra.select(0,1,2).plot('Extraversion') # Drop the categorical columns
```


    
![png](Lec5-demo_files/Lec5-demo_30_0.png)
    



```python
by_extra.select(0,2).plot('Extraversion')
```


    
![png](Lec5-demo_files/Lec5-demo_31_0.png)
    


## Grouping by Two Columns ##


```python
survey.group(['Handedness','Sleep position']).show()
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Handedness</th> <th>Sleep position</th> <th>count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Both        </td> <td>On your back      </td> <td>4    </td>
        </tr>
        <tr>
            <td>Both        </td> <td>On your left side </td> <td>6    </td>
        </tr>
        <tr>
            <td>Both        </td> <td>On your right side</td> <td>1    </td>
        </tr>
        <tr>
            <td>Both        </td> <td>On your stomach   </td> <td>1    </td>
        </tr>
        <tr>
            <td>Left-handed </td> <td>On your back      </td> <td>30   </td>
        </tr>
        <tr>
            <td>Left-handed </td> <td>On your left side </td> <td>28   </td>
        </tr>
        <tr>
            <td>Left-handed </td> <td>On your right side</td> <td>28   </td>
        </tr>
        <tr>
            <td>Left-handed </td> <td>On your stomach   </td> <td>13   </td>
        </tr>
        <tr>
            <td>Right-handed</td> <td>On your back      </td> <td>288  </td>
        </tr>
        <tr>
            <td>Right-handed</td> <td>On your left side </td> <td>310  </td>
        </tr>
        <tr>
            <td>Right-handed</td> <td>On your right side</td> <td>394  </td>
        </tr>
        <tr>
            <td>Right-handed</td> <td>On your stomach   </td> <td>188  </td>
        </tr>
    </tbody>
</table>


## Pivot Tables


```python
survey.pivot('Sleep position', 'Handedness')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Handedness</th> <th>On your back</th> <th>On your left side</th> <th>On your right side</th> <th>On your stomach</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Both        </td> <td>4           </td> <td>6                </td> <td>1                 </td> <td>1              </td>
        </tr>
        <tr>
            <td>Left-handed </td> <td>30          </td> <td>28               </td> <td>28                </td> <td>13             </td>
        </tr>
        <tr>
            <td>Right-handed</td> <td>288         </td> <td>310              </td> <td>394               </td> <td>188            </td>
        </tr>
    </tbody>
</table>




```python
survey.pivot('Sleep position', 'Handedness', values='Extraversion', collect=np.average)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Handedness</th> <th>On your back</th> <th>On your left side</th> <th>On your right side</th> <th>On your stomach</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Both        </td> <td>2.75        </td> <td>5.16667          </td> <td>9                 </td> <td>8              </td>
        </tr>
        <tr>
            <td>Left-handed </td> <td>5.66667     </td> <td>5.25             </td> <td>5.03571           </td> <td>5.69231        </td>
        </tr>
        <tr>
            <td>Right-handed</td> <td>5.31597     </td> <td>5.57742          </td> <td>5.67766           </td> <td>5.8617         </td>
        </tr>
    </tbody>
</table>



## Challenge Question ##


```python
sky = Table.read_table('skyscrapers_v2.csv')
sky = (sky.with_column('age', 2020 - sky.column('completed'))
          .drop('completed'))
sky.show(3)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>name</th> <th>material</th> <th>city</th> <th>height</th> <th>age</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>One World Trade Center</td> <td>mixed/composite</td> <td>New York City</td> <td>541.3 </td> <td>6   </td>
        </tr>
        <tr>
            <td>Willis Tower          </td> <td>steel          </td> <td>Chicago      </td> <td>442.14</td> <td>46  </td>
        </tr>
        <tr>
            <td>432 Park Avenue       </td> <td>concrete       </td> <td>New York City</td> <td>425.5 </td> <td>5   </td>
        </tr>
    </tbody>
</table>
<p>... (1778 rows omitted)</p>



```python
# 1. For each city, what’s the tallest building for each material?









```


```python
# 2. For each city, what’s the height difference between the tallest 
#    steel building and the tallest concrete building?











```

Don't read ahead until you try the challenge questions yourself first!


```python

```


```python

```


```python

```

## Joins ##


```python
drinks = Table(['Drink', 'Cafe', 'Price'])

drinks = drinks.with_rows([
    ['Milk Tea', 'Toastbox', 5.5],
    ['Espresso', 'Starbucks',  1.75],
    ['Latte',    'Starbucks',  3.25],
    ['Espresso', "Tiong Hoe",   2]
])
drinks
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Drink</th> <th>Cafe</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Milk Tea</td> <td>Toastbox </td> <td>5.5  </td>
        </tr>
        <tr>
            <td>Espresso</td> <td>Starbucks</td> <td>1.75 </td>
        </tr>
        <tr>
            <td>Latte   </td> <td>Starbucks</td> <td>3.25 </td>
        </tr>
        <tr>
            <td>Espresso</td> <td>Tiong Hoe</td> <td>2    </td>
        </tr>
    </tbody>
</table>




```python
discounts = Table().with_columns(
    'Coupon % off', make_array(10, 25, 5),
    'Location', make_array('Toastbox', 'Starbucks', 'Tiong Hoe')
)
discounts
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Coupon % off</th> <th>Location</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>10          </td> <td>Toastbox </td>
        </tr>
        <tr>
            <td>25          </td> <td>Starbucks</td>
        </tr>
        <tr>
            <td>5           </td> <td>Tiong Hoe</td>
        </tr>
    </tbody>
</table>




```python
combined = drinks.join('Cafe', discounts, 'Location')
combined
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Cafe</th> <th>Drink</th> <th>Price</th> <th>Coupon % off</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Starbucks</td> <td>Espresso</td> <td>1.75 </td> <td>25          </td>
        </tr>
        <tr>
            <td>Starbucks</td> <td>Latte   </td> <td>3.25 </td> <td>25          </td>
        </tr>
        <tr>
            <td>Tiong Hoe</td> <td>Espresso</td> <td>2    </td> <td>5           </td>
        </tr>
        <tr>
            <td>Toastbox </td> <td>Milk Tea</td> <td>5.5  </td> <td>10          </td>
        </tr>
    </tbody>
</table>




```python
discounted_frac = 1 - combined.column('Coupon % off') / 100
combined.with_column(
    'Discounted Price', 
    combined.column('Price') * discounted_frac
)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Cafe</th> <th>Drink</th> <th>Price</th> <th>Coupon % off</th> <th>Discounted Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Starbucks</td> <td>Espresso</td> <td>1.75 </td> <td>25          </td> <td>1.3125          </td>
        </tr>
        <tr>
            <td>Starbucks</td> <td>Latte   </td> <td>3.25 </td> <td>25          </td> <td>2.4375          </td>
        </tr>
        <tr>
            <td>Tiong Hoe</td> <td>Espresso</td> <td>2    </td> <td>5           </td> <td>1.9             </td>
        </tr>
        <tr>
            <td>Toastbox </td> <td>Milk Tea</td> <td>5.5  </td> <td>10          </td> <td>4.95            </td>
        </tr>
    </tbody>
</table>




```python
drinks.join('Cafe', drinks, 'Cafe')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Cafe</th> <th>Drink</th> <th>Price</th> <th>Drink_2</th> <th>Price_2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Starbucks</td> <td>Espresso</td> <td>1.75 </td> <td>Espresso</td> <td>1.75   </td>
        </tr>
        <tr>
            <td>Starbucks</td> <td>Espresso</td> <td>1.75 </td> <td>Latte   </td> <td>3.25   </td>
        </tr>
        <tr>
            <td>Starbucks</td> <td>Latte   </td> <td>3.25 </td> <td>Espresso</td> <td>1.75   </td>
        </tr>
        <tr>
            <td>Starbucks</td> <td>Latte   </td> <td>3.25 </td> <td>Latte   </td> <td>3.25   </td>
        </tr>
        <tr>
            <td>Tiong Hoe</td> <td>Espresso</td> <td>2    </td> <td>Espresso</td> <td>2      </td>
        </tr>
        <tr>
            <td>Toastbox </td> <td>Milk Tea</td> <td>5.5  </td> <td>Milk Tea</td> <td>5.5    </td>
        </tr>
    </tbody>
</table>


