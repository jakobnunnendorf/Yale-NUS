```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Words of Caution ##
- Remember to run the cell above. It's for setting up the environment so you can have access to what's needed for this lecture. For now, don't worry about what it means: we'll learn more about what's inside of it in the next few lectures. 

## Names ##


```python
a = 4
a
```




    4




```python
a
```




    4




```python
a * 3
```




    12




```python
b = 9
```


```python
b
```


```python
total = a + b
```


```python
total
```




    13




```python
a = 10
```


```python
total
```




    13




```python
total = a + b
```


```python
total 
```




    19




```python
total = 29
total
```




    29




```python
'total'
```




    'total'




```python
c * a
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In [15], line 1
    ----> 1 c * a


    NameError: name 'c' is not defined



```python
a = 7
a
```




    7



### Why Names?


```python
hours_per_week = 40
weeks_per_year = 52
```


```python
hours_per_year = hours_per_week * weeks_per_year
# hours_per_year =  40*52
```


```python
hours_per_year
```


```python
# Minimum hourly wage in HK
hk_hourly_minimum_wage = 37.5
```


```python
weekly_wages = hours_per_week * hk_hourly_minimum_wage
weekly_wages
```




    1500.0




```python
yearly_wages = hours_per_year * hk_hourly_minimum_wage
yearly_wages 
# nou recommended 
# yearly_wages = 78000
```




    78000.0




```python
40 * 37.5
```


```python
40 * 52 * 37.5
```

## Functions and Call Expressions

Built-in function documentation: https://docs.python.org/3/library/functions.html


```python
abs(-5)
```




    5




```python
abs(1 - 3)
```




    2




```python
day_temp = 52
night_temp = 47
abs(night_temp - day_temp)
```




    5




```python
min(14, 15)
```




    14




```python
round(123.456)
```




    123




```python
round(123.456, 1)
```




    123.5




```python
round(123.456, 2)
```




    123.46




```python
round(123.456, 0)
```




    123.0




```python
round(123.456, ndigits=1)
```




    123.5




```python
ndigits
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In [32], line 1
    ----> 1 ndigits


    NameError: name 'ndigits' is not defined


## Tables ##
Documentation of Table: http://data8.org/datascience/tables.html


```python
cones = Table.read_table('cones.csv')
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
cones.show(3)
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
    </tbody>
</table>
<p>... (3 rows omitted)</p>



```python
cones.show()
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
cones.select('Flavor')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td>
        </tr>
        <tr>
            <td>chocolate </td>
        </tr>
        <tr>
            <td>chocolate </td>
        </tr>
        <tr>
            <td>strawberry</td>
        </tr>
        <tr>
            <td>chocolate </td>
        </tr>
        <tr>
            <td>bubblegum </td>
        </tr>
    </tbody>
</table>




```python
cones.select('Flavor', 'Price')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td> <td>3.55 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>4.75 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>5.25 </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>bubblegum </td> <td>4.75 </td>
        </tr>
    </tbody>
</table>




```python
cones.select(Flavor, 'Price')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In [39], line 1
    ----> 1 cones.select(Flavor, 'Price')


    NameError: name 'Flavor' is not defined



```python
cones.drop('Price')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td> <td>pink       </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td>
        </tr>
        <tr>
            <td>bubblegum </td> <td>pink       </td>
        </tr>
    </tbody>
</table>




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
cones_without_price = cones.drop('Price')
cones_without_price
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>strawberry</td> <td>pink       </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>light brown</td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td>
        </tr>
        <tr>
            <td>chocolate </td> <td>dark brown </td>
        </tr>
        <tr>
            <td>bubblegum </td> <td>pink       </td>
        </tr>
    </tbody>
</table>




```python
cones.where('Flavor', 'chocolate')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>chocolate</td> <td>light brown</td> <td>4.75 </td>
        </tr>
        <tr>
            <td>chocolate</td> <td>dark brown </td> <td>5.25 </td>
        </tr>
        <tr>
            <td>chocolate</td> <td>dark brown </td> <td>5.25 </td>
        </tr>
    </tbody>
</table>




```python
cones.sort('Price')
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
            <td>bubblegum </td> <td>pink       </td> <td>4.75 </td>
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
    </tbody>
</table>




```python
cones.sort('Price', descending=True)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Flavor</th> <th>Color</th> <th>Price</th>
        </tr>
    </thead>
    <tbody>
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
            <td>chocolate </td> <td>light brown</td> <td>4.75 </td>
        </tr>
        <tr>
            <td>bubblegum </td> <td>pink       </td> <td>4.75 </td>
        </tr>
        <tr>
            <td>strawberry</td> <td>pink       </td> <td>3.55 </td>
        </tr>
    </tbody>
</table>




```python
cones.sort('Price', descending=False)
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
            <td>bubblegum </td> <td>pink       </td> <td>4.75 </td>
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
    </tbody>
</table>




```python
# sort string: dictionary order
cones.sort('Flavor', descending=True)
```


```python
cones.sort('Flavor', descending=False)
```

### A more interesting table


```python
skyscrapers = Table.read_table('skyscrapers.csv')
skyscrapers
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>name</th> <th>material</th> <th>city</th> <th>height</th> <th>completed</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>One World Trade Center           </td> <td>composite</td> <td>New York City</td> <td>541.3 </td> <td>2014     </td>
        </tr>
        <tr>
            <td>Willis Tower                     </td> <td>steel    </td> <td>Chicago      </td> <td>442.14</td> <td>1974     </td>
        </tr>
        <tr>
            <td>432 Park Avenue                  </td> <td>concrete </td> <td>New York City</td> <td>425.5 </td> <td>2015     </td>
        </tr>
        <tr>
            <td>Trump International Hotel & Tower</td> <td>concrete </td> <td>Chicago      </td> <td>423.22</td> <td>2009     </td>
        </tr>
        <tr>
            <td>Empire State Building            </td> <td>steel    </td> <td>New York City</td> <td>381   </td> <td>1931     </td>
        </tr>
        <tr>
            <td>Bank of America Tower            </td> <td>composite</td> <td>New York City</td> <td>365.8 </td> <td>2009     </td>
        </tr>
        <tr>
            <td>Stratosphere Tower               </td> <td>concrete </td> <td>Las Vegas    </td> <td>350.22</td> <td>1996     </td>
        </tr>
        <tr>
            <td>Aon Center                       </td> <td>steel    </td> <td>Chicago      </td> <td>346.26</td> <td>1973     </td>
        </tr>
        <tr>
            <td>John Hancock Center              </td> <td>steel    </td> <td>Chicago      </td> <td>343.69</td> <td>1969     </td>
        </tr>
        <tr>
            <td>WITI TV Tower                    </td> <td>steel    </td> <td>Shorewood    </td> <td>329   </td> <td>1962     </td>
        </tr>
    </tbody>
</table>
<p>... (190 rows omitted)</p>




```python
skyscrapers.where('city', 'Los Angeles')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>name</th> <th>material</th> <th>city</th> <th>height</th> <th>completed</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>U.S. Bank Tower      </td> <td>steel   </td> <td>Los Angeles</td> <td>310.29</td> <td>1990     </td>
        </tr>
        <tr>
            <td>Aon Center           </td> <td>steel   </td> <td>Los Angeles</td> <td>261.52</td> <td>1974     </td>
        </tr>
        <tr>
            <td>Two California Plaza </td> <td>steel   </td> <td>Los Angeles</td> <td>228.6 </td> <td>1992     </td>
        </tr>
        <tr>
            <td>Gas Company Tower    </td> <td>steel   </td> <td>Los Angeles</td> <td>228.3 </td> <td>1991     </td>
        </tr>
        <tr>
            <td>Bank of America Plaza</td> <td>steel   </td> <td>Los Angeles</td> <td>224.03</td> <td>1975     </td>
        </tr>
        <tr>
            <td>777 Tower            </td> <td>steel   </td> <td>Los Angeles</td> <td>221   </td> <td>1991     </td>
        </tr>
        <tr>
            <td>Wells Fargo Tower    </td> <td>steel   </td> <td>Los Angeles</td> <td>220.37</td> <td>1983     </td>
        </tr>
        <tr>
            <td>Figueroa at Wilshire </td> <td>steel   </td> <td>Los Angeles</td> <td>218.54</td> <td>1989     </td>
        </tr>
        <tr>
            <td>City National Tower  </td> <td>steel   </td> <td>Los Angeles</td> <td>213.06</td> <td>1971     </td>
        </tr>
        <tr>
            <td>Paul Hastings Tower  </td> <td>steel   </td> <td>Los Angeles</td> <td>213.06</td> <td>1971     </td>
        </tr>
    </tbody>
</table>
<p>... (1 rows omitted)</p>




```python
skyscrapers.where('name', 'Empire State Building')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>name</th> <th>material</th> <th>city</th> <th>height</th> <th>completed</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Empire State Building</td> <td>steel   </td> <td>New York City</td> <td>381   </td> <td>1931     </td>
        </tr>
    </tbody>
</table>




```python
skyscrapers.where('city', 'New York City').sort('completed')
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>name</th> <th>material</th> <th>city</th> <th>height</th> <th>completed</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Metropolitan Life Tower</td> <td>steel   </td> <td>New York City</td> <td>213.36</td> <td>1909     </td>
        </tr>
        <tr>
            <td>Woolworth Building     </td> <td>steel   </td> <td>New York City</td> <td>241.4 </td> <td>1913     </td>
        </tr>
        <tr>
            <td>Chanin Building        </td> <td>steel   </td> <td>New York City</td> <td>197.8 </td> <td>1929     </td>
        </tr>
        <tr>
            <td>Mercantile Building    </td> <td>steel   </td> <td>New York City</td> <td>192.6 </td> <td>1929     </td>
        </tr>
        <tr>
            <td>Chrysler Building      </td> <td>steel   </td> <td>New York City</td> <td>318.9 </td> <td>1930     </td>
        </tr>
        <tr>
            <td>The Trump Building     </td> <td>steel   </td> <td>New York City</td> <td>282.55</td> <td>1930     </td>
        </tr>
        <tr>
            <td>One Grand Central Place</td> <td>steel   </td> <td>New York City</td> <td>205.13</td> <td>1930     </td>
        </tr>
        <tr>
            <td>Empire State Building  </td> <td>steel   </td> <td>New York City</td> <td>381   </td> <td>1931     </td>
        </tr>
        <tr>
            <td>Twenty Exchange        </td> <td>steel   </td> <td>New York City</td> <td>225.86</td> <td>1931     </td>
        </tr>
        <tr>
            <td>500 Fifth Avenue       </td> <td>steel   </td> <td>New York City</td> <td>212.45</td> <td>1931     </td>
        </tr>
    </tbody>
</table>
<p>... (63 rows omitted)</p>




```python
skyscrapers.where('city', 'New York City').sort('completed', descending=True)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>name</th> <th>material</th> <th>city</th> <th>height</th> <th>completed</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>432 Park Avenue                                 </td> <td>concrete      </td> <td>New York City</td> <td>425.5 </td> <td>2015     </td>
        </tr>
        <tr>
            <td>Sky                                             </td> <td>concrete      </td> <td>New York City</td> <td>206   </td> <td>2015     </td>
        </tr>
        <tr>
            <td>One World Trade Center                          </td> <td>composite     </td> <td>New York City</td> <td>541.3 </td> <td>2014     </td>
        </tr>
        <tr>
            <td>One57                                           </td> <td>steel/concrete</td> <td>New York City</td> <td>306.07</td> <td>2014     </td>
        </tr>
        <tr>
            <td>4 World Trade Center                            </td> <td>composite     </td> <td>New York City</td> <td>297.73</td> <td>2014     </td>
        </tr>
        <tr>
            <td>Courtyard & Residence Inn Manhattan/Central Park</td> <td>concrete      </td> <td>New York City</td> <td>229.62</td> <td>2013     </td>
        </tr>
        <tr>
            <td>Eight Spruce Street                             </td> <td>concrete      </td> <td>New York City</td> <td>265.18</td> <td>2011     </td>
        </tr>
        <tr>
            <td>1 MiMA Tower                                    </td> <td>concrete      </td> <td>New York City</td> <td>194.55</td> <td>2011     </td>
        </tr>
        <tr>
            <td>Goldman Sachs Headquarters                      </td> <td>steel         </td> <td>New York City</td> <td>228.3 </td> <td>2010     </td>
        </tr>
        <tr>
            <td>Langham Place                                   </td> <td>concrete      </td> <td>New York City</td> <td>192.58</td> <td>2010     </td>
        </tr>
    </tbody>
</table>
<p>... (63 rows omitted)</p>




```python
skyscrapers.where('city', 'New York City').sort('completed', descending=True).show(3)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>name</th> <th>material</th> <th>city</th> <th>height</th> <th>completed</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>432 Park Avenue       </td> <td>concrete </td> <td>New York City</td> <td>425.5 </td> <td>2015     </td>
        </tr>
        <tr>
            <td>Sky                   </td> <td>concrete </td> <td>New York City</td> <td>206   </td> <td>2015     </td>
        </tr>
        <tr>
            <td>One World Trade Center</td> <td>composite</td> <td>New York City</td> <td>541.3 </td> <td>2014     </td>
        </tr>
    </tbody>
</table>
<p>... (70 rows omitted)</p>


## Numbers ##


```python
30
```




    30




```python
10 * 3    # int
```




    30




```python
10 / 3    # float
```




    3.3333333333333335




```python
10 / 2
```




    5.0




```python
10 ** 3 
```




    1000




```python
10 ** 0.5
```




    3.1622776601683795




```python
1234567 ** 890
```




    2805763342107369230793809808310885724030151698643898788380662816980113897853769505682553341995361840866283163839674938063847465098181599413516030923830315020297429114484842472806037601633183177392342419552281446098882333113360498936060689417981060580169581781517081000887466986920196787365735472976637384790660527656183529108057677628812897898917415727467403873251697100284318113613171090832770107627373429297578100452541331137972394395518879748252497629953169189742546688743838014842998797222488578482742255590278830326264415887042424349338336685586108014796843647297854686632059611017792593114133643766176826645471505135284339608286440790108605114687261446214106703238304626747430320283170505623593598192482183253323227473361217459497593514576103139354263910235117552944853835259328240635891089203247501395301794244132584186874755797831852390704417457044048557568618633160284149583340352686512009611975784239859264336878392387482791049156912854159715516214706166214466230037339823780492774337274675800289580696315819494418004733412855205155027918058344891850668473780787520539851110601937177777258527635476258052342827179765186381834973522303136829852834242679559888371990546547773735142872611383102742753311234958929602179017609453450788021576889968090558526946002867067155433937025164603278496325064732080655085967120552122358643425906339419468088785812576641170399781555198518542228755764090812514788163758877228031474626249982320173230513790766211051807071509018394299594496298553425032888639575233308427922962072691110016410832613254845558533479779137394546533348267260208654147664661662489837722166465535984470300130195361526724657999247737664119545166367970118960539653700728246780841243422865927822029745430687779341494835511048331091708435435810632677284968867671217350609932555531424276428454845446681148799804144451127195396670373733155503688440766376117308145231339204514518114182442669726926958460263504747823171357759585770665369994677944653246927717262087721616975390825217507408220510861018634338133464060418295047933927635868626199925788463191380080935701443847346532746838349449833204183719520425273508461427363268810901816439207520602455792069406367821658839121277649227555623273564677301331404339603368354187279170542954088017099056552277230318062383216542056927422226999811205450549485589246237819874869638917303541644714356081602468616512144027808621669917967523298847733280998188849126660410144516840751121177122218727312917235905337333060556516611924333661893530040067042505379294125436401184352256775565463142705637306783871882313794728831427529583150846149427004802322087788357968992264438692993009809883875465518646172470495839410492599060455716367637440364630131471750106709132465895371670412945256073822697903510522211765697295922053593229276419226531331408317896936830655815873666355197305378708964668209899291344705444276333578719323904170952074328643811404544256843025709425474387814973960542018630128201161272329024792011740745530212579878161378961127918038096648026162029808878747866210894432543002029434565613132355043777385763831238060952363449797871761622541777453653784081456719940419766751192867804269268505636574832199689538986715250742630200523490339094085425178568698903268320220973567490288420919261018482168538171910000711992076873681129307598675285503345960161016391830728260326693428202177160119543736800344297771481079627076988031975978575895647654221558620092991884687091862613605722144271490738163190650508558761186844994717152403269557878581184075275936408939256017646715559306260196259010170427037361073267573147026510628695621128132172515464076418742940103113964611681699407950967774413428184355249041334714765827480675899800235537773385443229622067233523354213261412403375030932576886654499317808172035910623439488923497729990034132955991616175315301110003136655552464696428279778365477406164307525011119783055047664864798818426307604172381073695798688377889193415423645042188927398145864445871680431617772823584658707705057426132797633601281478887542871708884776132993498113629791075212269131263135104211901928478309667400642477145201362433365658578707267018122388906853103264797837550314906826327964589811537800151348078278689526492266541600168152334174087551992509222975658050902151573849522445074588731109036554789680280345720046009120507928152632018078697710120218368147570599141031673300682348326156497244011574817802187099834880327346210624556369660018678859929271654108596951193479453034452114779847850504280525490303492730731848704497321639579545359051407002629069912400518470707512308477494989006390249351273561453957767103749105099486859441823499120103359974562095361878219993785312682108204349115081403854873968693651144816992008787094413654541840750267945428940655147102103776877924495354589674471203663800973702240269677784610346010441824261817763592599870546594987128802020889878623694800247575251661439276157008847529529237192162577463356503617323132760079688627706444510425779441871297035026396768851129501722454220316418777074912838238391162658683371634959415544181384058154251960767217101632139258312150904777623156788937309713540569306765232165671618935868039816292110221657560493742908804867952618200515005539316960724088551539133626302522557345413249384658492371698805093289004717340532810196692880918816862832405941920828302568461913904088702147654713878056218117011839094769918168741678648022940613796829566893389100562532347981860917540264049




```python
10 / 3
```




    3.3333333333333335




```python
75892745.215489247589274985712
```




    75892745.21548925




```python
75892745.215489247589274985712 - 75892745.21548925
```




    0.0




```python
(13 ** 0.5) ** 2
```




    12.999999999999998




```python
int(10 / 5)
```




    2




```python
int(10 / 4)
```




    2




```python
float(3)
```




    3.0




```python
6 / 4
```




    1.5




```python
6 / 4000
```




    0.0015




```python
6 / 400000000000000000000000000000000000000000000000000000000
```




    1.5e-56




```python
400000000000000000000000000000000000000000000000000000000 * 1.5e-56 
```




    6.0




```python
1.5e-56 
```




    1.5e-56




```python
x = 5
```


```python
2*x
```




    10




```python
2 *    x
```




    10




```python
round(3.7)
```




    4




```python
round(2.00000052345324, 2)
```




    2.0




```python
10 * 3.0
```




    30.0



## Strings ##


```python
'Flavor'

```




    'Flavor'




```python
Flavor
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In [79], line 1
    ----> 1 Flavor


    NameError: name 'Flavor' is not defined



```python
"Flavor"
```




    'Flavor'




```python
"Don't always use single quotes"
```




    "Don't always use single quotes"




```python
'Don't always use single quotes'
```


      Cell In [83], line 1
        'Don't always use single quotes'
                                       ^
    SyntaxError: unterminated string literal (detected at line 1)




```python
'straw' + 'berry' # concatenation
```




    'strawberry'




```python
'Chris' + 'Paul' # spaces aren't added for you
```




    'ChrisPaul'




```python
'Chris' + ' ' + 'Paul'
```




    'Chris Paul'




```python
'ha' * 100
```




    'hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha'




```python
'ha' * 5.5
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In [88], line 1
    ----> 1 'ha' * 5.5


    TypeError: can't multiply sequence by non-int of type 'float'



```python
'ha' + 10
```




    'ha10'




```python
int('3')
```




    3




```python
int('3.0')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In [92], line 1
    ----> 1 int('3.0')


    ValueError: invalid literal for int() with base 10: '3.0'



```python
float('3.0')
```




    3.0




```python
str(3)
```




    '3'




```python
str(4.5)
```




    '4.5'



## Dictionary ##


```python
# dictionary with key-value pairs
my_dict = {'name': 'Michael', 'age': 20}
```


```python
# Access the value stored in the key 'name'
# Output: Michael
print(my_dict['name'])
```

    Michael



```python
# No such key exists -> error
my_dict['address']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-4-da7d3eb9ca23> in <module>
          1 # No such key exists -> error
    ----> 2 my_dict['address']
    

    KeyError: 'address'



```python
# Update values
my_dict['age'] = 21
```


```python
print(my_dict['age'])
```

    21



```python
print(my_dict)
```

    {'name': 'Michael', 'age': 21}


## Types ##


```python
type(10)
```


```python
a = 10
```


```python
type(a)
```


```python
type(4.5)
```


```python
type('abc')
```


```python
type(skyscrapers)
```




    datascience.tables.Table




```python
type(True)
```




    bool




```python
type(abs)
```


```python
type(min)
```


```python
type(my_dict)
```




    dict


