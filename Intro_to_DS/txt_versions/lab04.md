# Lab 4: World Progress, Randomization

Welcome to lab 4!  

This lab brings together many of the topics so far, including data table manipulation, visualization, iteration and probability. The first few parts of the lab is based on a series of talks by Hans Rosling, a statistician who advised many world leaders about the changing state of the world's population. 

(Optional) For a video introduction to the topic of Global population change, you can watch Hans Rosling's video, [Don't Panic: The Facts About Population](https://www.gapminder.org/videos/dont-panic-the-facts-about-population/).

First, set up the imports by running the cell below.


```python
# Run this cell to set up the notebook, but please don't change it.

# These lines import the Numpy and Datascience modules.
import numpy as np
from datascience import *

# These lines do some fancy plotting magic.
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
```

The global population of humans reached 1 billion around 1800, 3 billion around 1960, and 7 billion around 2011. The potential impact of exponential population growth has concerned scientists, economists, and politicians alike.

The UN Population Division estimates that the world population will likely continue to grow throughout the 21st century, but at a slower rate, perhaps reaching 11 billion by 2100. However, the UN does not rule out scenarios of more extreme growth.

<a href="http://www.pewresearch.org/fact-tank/2015/06/08/scientists-more-worried-than-public-about-worlds-growing-population/ft_15-06-04_popcount/"> 
 <img src="pew_population_projection.png" alt="Estimated and project annual world population from 1950 to 2100.  Estimates in 1950 start at 2 billion and grow to 6 billion in 2000.  Projects say the population in 2100 will be 10.9 billion people."/>
</a>

In this section, we will examine some of the factors that influence population growth and how they are changing around the world.

The first table we will consider is the total population of each country over time. Run the cell below.


```python
# The population.csv file can also be found online here:
# https://github.com/open-numbers/ddf--gapminder--systema_globalis/raw/master/ddf--datapoints--population_total--by--geo--time.csv
population = Table.read_table('population.csv')
population.show(3)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>geo</th> <th>time</th> <th>population_total</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>abw </td> <td>1800</td> <td>19286           </td>
        </tr>
        <tr>
            <td>abw </td> <td>1801</td> <td>19286           </td>
        </tr>
        <tr>
            <td>abw </td> <td>1802</td> <td>19286           </td>
        </tr>
    </tbody>
</table>
<p>... (87792 rows omitted)</p>


## 1. Bangladesh

In the `population` table, the `geo` column contains three-letter codes established by the [International Organization for Standardization](https://en.wikipedia.org/wiki/International_Organization_for_Standardization) (ISO) in the [Alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Current_codes) standard. We will begin by taking a close look at Bangladesh. Inspect the standard to find the 3-letter code for Bangladesh.

**Question 1.1** <br/>Create a table called `b_pop` that has two columns labeled `time` and `population_total`. The first column should contain the years from 1970 through 2015 (including both 1970 and 2015) and the second should contain the population of Bangladesh in each of those years.


```python
b_pop = population.where('geo', 'bgd').where('time', are.above_or_equal_to(1970)).where('time', are.below_or_equal_to(2015)).drop('geo')
b_pop
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>time</th> <th>population_total</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1970</td> <td>65048701        </td>
        </tr>
        <tr>
            <td>1971</td> <td>66417450        </td>
        </tr>
        <tr>
            <td>1972</td> <td>67578486        </td>
        </tr>
        <tr>
            <td>1973</td> <td>68658472        </td>
        </tr>
        <tr>
            <td>1974</td> <td>69837960        </td>
        </tr>
        <tr>
            <td>1975</td> <td>71247153        </td>
        </tr>
        <tr>
            <td>1976</td> <td>72930206        </td>
        </tr>
        <tr>
            <td>1977</td> <td>74848466        </td>
        </tr>
        <tr>
            <td>1978</td> <td>76948378        </td>
        </tr>
        <tr>
            <td>1979</td> <td>79141947        </td>
        </tr>
    </tbody>
</table>
<p>... (36 rows omitted)</p>



Run the following cell to create a table called `b_five` that has the population of Bangladesh every five years. At a glance, it appears that the population of Bangladesh has been growing quickly indeed!


```python
b_pop.set_format('population_total', NumberFormatter)

fives = np.arange(1970, 2016, 5) # 1970, 1975, 1980, ...
b_five = b_pop.sort('time').where('time', are.contained_in(fives))
b_five
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>time</th> <th>population_total</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1970</td> <td>65,048,701      </td>
        </tr>
        <tr>
            <td>1975</td> <td>71,247,153      </td>
        </tr>
        <tr>
            <td>1980</td> <td>81,364,176      </td>
        </tr>
        <tr>
            <td>1985</td> <td>93,015,182      </td>
        </tr>
        <tr>
            <td>1990</td> <td>105,983,136     </td>
        </tr>
        <tr>
            <td>1995</td> <td>118,427,768     </td>
        </tr>
        <tr>
            <td>2000</td> <td>131,280,739     </td>
        </tr>
        <tr>
            <td>2005</td> <td>142,929,979     </td>
        </tr>
        <tr>
            <td>2010</td> <td>151,616,777     </td>
        </tr>
        <tr>
            <td>2015</td> <td>160,995,642     </td>
        </tr>
    </tbody>
</table>



Run the next cell to create a table called `b_five_growth` which shows the growth rate for each five-year period from 1970 through 2010.


```python
b_1970_through_2010 = b_five.where('time', are.below_or_equal_to(2010))
b_five_growth = b_1970_through_2010.with_column('annual_growth', (b_five.exclude(0).column(1)/b_1970_through_2010.column(1))**0.2-1)
b_five_growth.set_format('annual_growth', PercentFormatter)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>time</th> <th>population_total</th> <th>annual_growth</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1970</td> <td>65,048,701      </td> <td>1.84%        </td>
        </tr>
        <tr>
            <td>1975</td> <td>71,247,153      </td> <td>2.69%        </td>
        </tr>
        <tr>
            <td>1980</td> <td>81,364,176      </td> <td>2.71%        </td>
        </tr>
        <tr>
            <td>1985</td> <td>93,015,182      </td> <td>2.64%        </td>
        </tr>
        <tr>
            <td>1990</td> <td>105,983,136     </td> <td>2.25%        </td>
        </tr>
        <tr>
            <td>1995</td> <td>118,427,768     </td> <td>2.08%        </td>
        </tr>
        <tr>
            <td>2000</td> <td>131,280,739     </td> <td>1.71%        </td>
        </tr>
        <tr>
            <td>2005</td> <td>142,929,979     </td> <td>1.19%        </td>
        </tr>
        <tr>
            <td>2010</td> <td>151,616,777     </td> <td>1.21%        </td>
        </tr>
    </tbody>
</table>



While the population has grown every five years since 1970, the annual growth rate decreased dramatically from 1985 to 2005. Let's look at some other information in order to develop a possible explanation. Run the next cell to load three additional tables of measurements about countries over time.


```python
life_expectancy = Table.read_table('life_expectancy.csv')
child_mortality = Table.read_table('child_mortality.csv').relabeled(2, 'child_mortality_under_5_per_1000_born')
fertility = Table.read_table('fertility.csv')
life_expectancy.show(2)
child_mortality.show(2)
fertility.show(2)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>geo</th> <th>time</th> <th>life_expectancy_years</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>afg </td> <td>1800</td> <td>28.21                </td>
        </tr>
        <tr>
            <td>afg </td> <td>1801</td> <td>28.2                 </td>
        </tr>
    </tbody>
</table>
<p>... (43855 rows omitted)</p>



<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>geo</th> <th>time</th> <th>child_mortality_under_5_per_1000_born</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>afg </td> <td>1800</td> <td>468.6                                </td>
        </tr>
        <tr>
            <td>afg </td> <td>1801</td> <td>468.6                                </td>
        </tr>
    </tbody>
</table>
<p>... (40754 rows omitted)</p>



<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>geo</th> <th>time</th> <th>children_per_woman_total_fertility</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>afg </td> <td>1800</td> <td>7                                 </td>
        </tr>
        <tr>
            <td>afg </td> <td>1801</td> <td>7                                 </td>
        </tr>
    </tbody>
</table>
<p>... (43410 rows omitted)</p>


The `life_expectancy` table contains a statistic that is often used to measure how long people live, called *life expectancy at birth*. This number, for a country in a given year, [does not measure how long babies born in that year are expected to live](http://blogs.worldbank.org/opendata/what-does-life-expectancy-birth-really-mean). Instead, it measures how long someone would live, on average, if the *mortality conditions* in that year persisted throughout their lifetime. These "mortality conditions" describe what fraction of people at each age survived the year. So, it is a way of measuring the proportion of people that are staying alive, aggregated over different age groups in the population.

The `fertility` table contains a statistic that is often used to measure how many babies are being born, the *total fertility rate*. This number describes the [number of children a woman would have in her lifetime](https://www.measureevaluation.org/prh/rh_indicators/specific/fertility/total-fertility-rate), on average, if the current rates of birth by age of the mother persisted throughout her child bearing years, assuming she survived through age 49. 

**Question 1.2.** <br/>Write a function `fertility_over_time` that takes the Alpha-3 code of a `country` and a `start` year. It returns a two-column table with labels "`Year`" and "`Children per woman`" (in that order) that can be used to generate a line chart of the country's fertility rate each year, starting at the `start` year. The plot should include the `start` year and all later years that appear in the `fertility` table. 

Then, in the next cell, call your `fertility_over_time` function on the Alpha-3 code for Bangladesh and the year 1970 in order to plot how Bangladesh's fertility rate has changed since 1970. Note that the function `fertility_over_time` should not return the plot itself **The expression that draws the line plot is provided for you; please don't change it.**


```python
def fertility_over_time(country, start):
    """Create a two-column table that describes a country's total fertility rate each year."""
    country_fertility = fertility.where('geo', country).drop('geo')
    country_fertility_after_start = country_fertility.where('time', are.above_or_equal_to(start))
    return country_fertility_after_start
```


```python
bangladesh_code = 'bgd'
fertility_over_time(bangladesh_code, 1970).plot(0, 1) # You should *not* change this line.
```


    
![png](lab04_files/lab04_17_0.png)
    


**Question 1.3.** <br/>Using both the `fertility` and `child_mortality` tables, draw a scatter diagram with one point for each year, starting with 1970, that has Bangladesh's total fertility on the horizontal axis and its child mortality on the vertical axis. 

**The expression that draws the scatter diagram is provided for you; please don't change it.** Instead, create a table called `post_1969_fertility_and_child_mortality` with the appropriate column labels and data in order to generate the chart correctly. Use the label "`Children per woman`" to describe total fertility and the label "`Child deaths per 1000 born`" to describe child mortality.

The lines `bgd_fertility`, `bgd_child_mortality`, and `fertility_and_child_mortality` are there to help you answer the question. You do not need to use them, but make sure you assign the correct table to `post_1969_fertility_and_child_mortality`.


```python
bgd_fertility = fertility.where('geo', bangladesh_code).drop('geo')
bgd_child_mortality = child_mortality.where('geo', bangladesh_code).drop('geo')
fertility_and_child_mortality = bgd_fertility.with_column('Child deaths per 1000 born', bgd_child_mortality.column(1)).relabel('children_per_woman_total_fertility', 'Children per woman')
post_1969_fertility_and_child_mortality = fertility_and_child_mortality.where('time', are.above_or_equal_to(1970))
post_1969_fertility_and_child_mortality.scatter('Children per woman', 'Child deaths per 1000 born') # You should *not* change this line.
```


    
![png](lab04_files/lab04_19_0.png)
    


## 2. The World

The change observed in Bangladesh since 1970 can also be observed in many other developing countries: health services improve, life expectancy increases, and child mortality decreases. At the same time, the fertility rate often plummets, and so the population growth rate decreases despite increasing longevity.

Run the next cell to see a line plot of the world population from 1800 through 2005.  You might recognize some of the code used!


```python
population.where('time', are.between(1800, 2006)).drop('geo').group('time', sum).plot(0)
```


    
![png](lab04_files/lab04_22_0.png)
    


**Question 2.1.** Create a function `stats_for_year` that takes a `year` and returns a table of statistics. The table it returns should have four columns: `geo`, `population_total`, `children_per_woman_total_fertility`, and `child_mortality_under_5_per_1000_born`. Each row should contain one Alpha-3 country code and three statistics: population, fertility rate, and child mortality for that `year` from the `population`, `fertility` and `child_mortality` tables. Only include rows for which all three statistics are available for the country and year.

In addition, restrict the result to country codes that appears in `big_50`, an array of the 50 most populous countries in 2010. This restriction will speed up computations later in the project.

*Hint*: What is the common column among all of the datasets? 


```python
# We first create a population table that only includes the 
# 50 countries with the largest 2010 populations. We focus on 
# these 50 countries only so that plotting later will run faster.
big_50 = population.where('time', 2010).sort(2, descending=True).take(np.arange(50)).column('geo')
population_of_big_50 = population.where('time', are.above(1959)).where('geo', are.contained_in(big_50))

def stats_for_year(year):
    """Return a table of the stats for each country that year."""
    p = population_of_big_50.where('time', year).drop('time')
    f = fertility.where('time', year).drop('time')
    c = child_mortality.where('time', year).drop('time')
    return p.join('geo', f).join('geo', c)
```

Try calling your function `stats_for_year` on any year between 1960 and 2010 in the cell below.  Try to understand the output of `stats_for_year`.


```python
stats_for_year(1970)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>geo</th> <th>population_total</th> <th>children_per_woman_total_fertility</th> <th>child_mortality_under_5_per_1000_born</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>afg </td> <td>11121097        </td> <td>7.67                              </td> <td>307.8                                </td>
        </tr>
        <tr>
            <td>arg </td> <td>23973062        </td> <td>3.07                              </td> <td>72.4                                 </td>
        </tr>
        <tr>
            <td>bgd </td> <td>65048701        </td> <td>6.95                              </td> <td>224.1                                </td>
        </tr>
        <tr>
            <td>bra </td> <td>95982453        </td> <td>5.02                              </td> <td>133.7                                </td>
        </tr>
        <tr>
            <td>can </td> <td>21439200        </td> <td>2.31                              </td> <td>22                                   </td>
        </tr>
        <tr>
            <td>chn </td> <td>808510713       </td> <td>5.75                              </td> <td>113.3                                </td>
        </tr>
        <tr>
            <td>cod </td> <td>20009902        </td> <td>6.21                              </td> <td>248.1                                </td>
        </tr>
        <tr>
            <td>col </td> <td>22061214        </td> <td>5.6                               </td> <td>97.6                                 </td>
        </tr>
        <tr>
            <td>deu </td> <td>78366605        </td> <td>2.04                              </td> <td>25.7                                 </td>
        </tr>
        <tr>
            <td>dza </td> <td>14550033        </td> <td>7.64                              </td> <td>242.2                                </td>
        </tr>
    </tbody>
</table>
<p>... (40 rows omitted)</p>



**Question 2.2.** <br/>Create a table called `pop_by_decade` with two columns called `decade` and `population`. It has a row for each `year` since 1960 that starts a decade. The `population` column contains the total population of all countries included in the result of `stats_for_year(year)` for the first `year` of the decade. For example, 1960 is the first year of the 1960's decade. You should see that these countries contain most of the world's population.

*Hint:* It may be helpful to use the provided `pop_for_year` that computes this total population, then `apply` it to the `decade` column.


```python
def pop_for_year(year):
    return sum(stats_for_year(year).column('population_total'))
```


```python
decades = Table().with_column('decade', np.arange(1960, 2011, 10))

pop_by_decade = ...
pop_by_decade.set_format(1, NumberFormatter)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[28], line 4
          1 decades = Table().with_column('decade', np.arange(1960, 2011, 10))
          3 pop_by_decade = ...
    ----> 4 pop_by_decade.set_format(1, NumberFormatter)


    AttributeError: 'ellipsis' object has no attribute 'set_format'


The `countries` table describes various characteristics of countries. The `country` column contains the same codes as the `geo` column in each of the other data tables (`population`, `fertility`, and `child_mortality`). The `world_6region` column classifies each country into a region of the world. Run the cell below to inspect the data.


```python
countries = Table.read_table('countries.csv').where('country', are.contained_in(population.group('geo').column(0)))
countries.select('country', 'name', 'world_6region')
```

**Question 2.3.** <br/>Create a table called `region_counts` that has two columns, `region` and `count`. It should describe the count of how many countries in each region appear in the result of `stats_for_year(1960)`. For example, one row would have `south_asia` as its `world_6region` value and an integer as its `count` value: the number of large South Asian countries for which we have population, fertility, and child mortality numbers from 1960.

*Hint:* What table method lets us find and count the number of unique values in a column? 


```python
region_counts = ...
region_counts
```

The following scatter diagram compares total fertility rate and child mortality rate for each country in 1960. The area of each dot represents the population of the country. Run the cell. Do you think you can identify any of the dots?


```python
from functools import lru_cache as cache

# This cache annotation makes sure that if the same year
# is passed as an argument twice, the work of computing
# the result is only carried out once and then saved.
@cache(None)
def stats_relabeled(year):
    """Relabeled and cached version of stats_for_year."""
    return stats_for_year(year).relabeled(2, 'Children per woman').relabeled(3, 'Child deaths per 1000 born')

def fertility_vs_child_mortality(year):
    """Draw a scatter diagram comparing child mortality and fertility with the country's size"""
    with_region = stats_relabeled(year).join('geo', countries.select('country', 'world_6region'), 'country')
    with_region.scatter(2, 3, sizes=1, s=500)
    plots.xlim(0,10)
    plots.ylim(-50, 500)
    plots.title(year)

fertility_vs_child_mortality(1960)
```

The result of the cell below is interactive. It may take several minutes to run because it computers 55 tables (one for each year). When it's done, a scatter plot and a slider should appear.

Drag the slider to the right to see how countries have changed over time. You'll find that the great divide between so-called "Western" and "developing" countries that existed in the 1960's has nearly disappeared. This shift in fertility rates is the reason that the global population is expected to grow more slowly in the 21st century than it did in the 19th and 20th centuries.


```python
import ipywidgets as widgets

# This part takes a few minutes to run because it 
# computes 55 tables in advance: one for each year.
for year in np.arange(1960, 2016):
    stats_relabeled(year)

_ = widgets.interact(fertility_vs_child_mortality, 
                     year=widgets.IntSlider(min=1960, max=2015, value=1960))
```

## 3. Nachos and Conditionals

In Python, Boolean values can either be `True` or `False`. We get Boolean values when using comparison operators such as `<` (less than), `>` (greater than), and `==` (equal to). A list of common comparison operators can be found below!

<img src="comparisons.png">


```python
3 > 1 + 1
```

We can even assign the result of a comparison operation to a variable.


```python
result = 10 / 2 == 5
result
```

Arrays are compatible with comparison operators. The output is an array of boolean values, where the comparison occurs *elementwise*.


```python
make_array(1, 5, 7, 8, 3, -1) > 3
```

Waiting on the dining table just for you is a hot bowl of nachos! Let's say that whenever you take a nacho, it will have cheese, salsa, both, or neither (just a plain tortilla chip). 

Using the function call `np.random.choice(array_name)`, let's simulate taking nachos from the bowl at random. Start by running the cell below several times, and observe how the results change.

If you don't understand how np.random.choice works, remember that you can check the documentation by typing `np.random.choice?`


```python
nachos = make_array('cheese', 'salsa', 'both', 'neither')
np.random.choice(nachos)
```

**Question 3.1** <br/> Assume we took ten nachos at random, and stored the results in an array called `ten_nachos` as done below. Find the number of nachos with only cheese using code (do not hardcode the answer).  

*Hint:* Our solution involves a comparison operator and the `np.count_nonzero` method.


```python
ten_nachos = make_array('neither', 'cheese', 'both', 'both', 'cheese', 'salsa', 'both', 'neither', 'cheese', 'both')
number_cheese = ...
number_cheese
```

**Conditional Statements**

A conditional statement is made up of many lines that allow Python to choose from different alternatives based on whether some condition is true.

Here is a basic example.

```
def sign(x):
    if x > 0:
        return 'Positive'
```

How the function works is if the input `x` is greater than `0`, we get the string `'Positive'` back.

If we want to test multiple conditions at once, we use the following general format.

```
if <if expression>:
    <if body>
elif <elif expression 0>:
    <elif body 0>
elif <elif expression 1>:
    <elif body 1>
...
else:
    <else body>
```

Only one of the bodies will ever be executed. Each `if` and `elif` expression is evaluated and considered in order, starting at the top. As soon as a true value is found, the corresponding body is executed, and the rest of the expression is skipped. If none of the `if` or `elif` expressions are true, then the `else body` is executed.

**Question 3.2** <br/>Complete the following conditional statement so that the string `'More please'` is assigned to `say_please` if the number of nachos with cheese in `ten_nachos` is less than `5`.

*Hint*: You should not have to reference the variable `ten_nachos`.


```python
say_please = '?'

if ...:
    say_please = 'More please'
    
say_please
```

**Question 3.3** <br/>Write a function called `nacho_reaction` that returns a string based on the type of nacho passed in as an argument. From top to bottom, the conditions should correspond to: `'cheese'`, `'salsa'`, `'both'`, `'neither'`.  


```python
def nacho_reaction(nacho):
    if ...:
        return 'Cheesy!'
    # next condition should return 'Spicy!'
    ...
    # next condition should return 'Wow!'
    ...
    # next condition should return 'Meh.'
    ...

spicy_nacho = nacho_reaction('salsa')
spicy_nacho
```

**Question 3.4** <br/>Add a column `'Reactions'` to the table `ten_nachos_reactions` that consists of reactions for each of the nachos in `ten_nachos`. 

*Hint:* What table method should we use?


```python
ten_nachos_reactions = Table().with_column('Nachos', ten_nachos)
...
ten_nachos_reactions
```

**Question 3.5** <br/>Using code, find the number of `'Wow!'` reactions for the nachos in `ten_nachos_reactions`.


```python
number_wow_reactions = ...
number_wow_reactions
```

## 4. Simulations and For Loops
Using a `for` statement, we can perform a task multiple times. This is known as iteration. Here, we'll simulate drawing different suits from a deck of cards. 


```python
suits = make_array("♤", "♡", "♢", "♧")

draws = make_array()

repetitions = 6

for i in np.arange(repetitions):
    draws = np.append(draws, np.random.choice(suits))

draws
```

The unrolled version of this `for` loop can be found below.


```python
draws = make_array()

draws = np.append(draws, np.random.choice(suits))
draws = np.append(draws, np.random.choice(suits))
draws = np.append(draws, np.random.choice(suits))
draws = np.append(draws, np.random.choice(suits))
draws = np.append(draws, np.random.choice(suits))
draws = np.append(draws, np.random.choice(suits))

draws
```

In the example above, the `for` loop appends a random draw to the `draws` array for every number in `np.arange(repetitions)`. 

Here's a nice way to think of what we did above. We had a deck of 4 cards of different suits, we randomly drew one card, saw the suit, kept track of it in `draws`, and put the card back into the deck. We repeated this for a total of 6 times without having to repeat code, thanks to the `for` loop. We simulated this experiment using a `for` loop. 

Another use of iteration is to loop through a set of values. For instance, we can print out all of the colors of the rainbow.



```python
rainbow = make_array("red", "orange", "yellow", "green", "blue", "indigo", "violet")

for color in rainbow:
    print(color)
```

We can see that the indented part of the `for` loop, known as the body, is executed once for each item in `rainbow`. Note that the name `color` is arbitrary; we could easily have named it something else. The important thing is we stay consistent throughout the for loop. 


```python
for another_name in rainbow:
    print(another_name)
```

In general, however, we would like the variable name to be somewhat informative. 

**Question 4.1** <br/>Clay is playing darts. His dartboard contains ten equal-sized zones with point values from 1 to 10. Write code that simulates his total score after 1000 dart tosses. Make sure to use a `for` loop.

*Hint:* There are three steps to this problem (and most simulations): 
1. Deciding the possible values you can take in the experiment (point values in this case)
2. Running through the experiment a certain amount of times (running through 1000 dart tosses, and randomly getting a value per toss in this case)
3. Keeping track of the total information of each time you ran through the experiment (the total score in this case)
   
*Hint 2:* You can "update" a variable by setting it equal to itself because Python evaluates the right side first and then assigns it to the left name. For example:

`
x = 10 # Set the name x to the value 10
x = x + 5 # Take the current value of x, 10, and add it to 5. Then, reassign the name x to the calculated value, 15
`


```python
possible_point_values = ...
tosses = 1000
total_score = ...

for ...:
    ...

total_score
```

**Question 4.2** <br/>In the following cell, we've loaded the text of _Pride and Prejudice_ by Jane Austen, split it into individual words, and stored these words in an array. Using a `for` loop, assign `longer_than_five` to the number of words in the novel that are more than 5 letters long.

*Hint*: You can find the number of letters in a word with the `len` function. Look at the `rainbow` example above for help.


```python
austen_string = open('Austen_PrideAndPrejudice.txt', encoding='utf-8').read()
p_and_p_words = np.array(austen_string.split())

longer_than_five = ...

# a for loop would be useful here


longer_than_five
```

**Question 4.3** <br/>Using simulation with 10,000 trials, assign `chance_of_all_different` to an estimate of the chance that if you pick **three** words from Pride and Prejudice uniformly at random (with replacement), they all have **different lengths.**

*Hint*: Remember that `!=` only checks for non-equality between two items, not three. However, you can use `!=` more than once in the same line. 

For example, `2 != 3 != 4` first checks for non-equality between `2` and `3`, then `3` and `4`, but NOT `2` and `4`.


```python
trials = 10000
different = ...

for ... in ...:
    ...

chance_of_all_different = ...

chance_of_all_different
```

## 5. Finding Probabilities
After a long day of class, Clay decides to go to a food court for dinner. Today's menu has Clay's four favorite foods: enchiladas, hamburgers, pizza, and spaghetti. However, each dish has a 30% chance of running out before Clay can get to the food court.

**Question 5.1** <br/>What is the probability that Clay will be able to eat pizza at the food court?


```python
pizza_prob = ...
```

**Question 5.2** <br/>What is the probability that Clay will be able to eat all four of these foods at the food court?


```python
all_prob = ...
```

**Question 5.3** <br/>What is the probability that the food court will have run out of at least 1 food before Clay can get there?


```python
something_is_out = ...
```

To make up for their unpredictable food supply, the food court decides to hold a contest for some free food. There is a bag with two red marbles, two green marbles, and two blue marbles. Clay has to draw three marbles separately **without replacement**. In order to win, all three of these marbles must be of different colors.

**Question 5.4** <br/>What is the probability of Clay winning the contest?

*Hint:* For the first event, we can pick any marble -- what is that probability? Then, what's the probability of selecting a different marble? Finally, picking the color that hasn't been selected? 


```python
winning_prob = ...
```


```python

```


```python

```

## 6. Submission

To submit your assignment, please download your notebook as a .ipynb file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as... > Notebook (.ipynb) or HTML (.html). Then, upload your file under "Lab 4".

