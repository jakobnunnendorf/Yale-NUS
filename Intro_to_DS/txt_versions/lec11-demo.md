## Lecture 11 ##


```python
from datascience import *
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```


```python
# Some functions for plotting. 

def resize_window(lim=3.5):
    plots.xlim(-lim, lim)
    plots.ylim(-lim, lim)
    
def draw_line(slope=0, intercept=0, x=make_array(-4, 4), color='r'):
    y = x*slope + intercept
    plots.plot(x, y, color=color)
    
def draw_vertical_line(x_position, color='black'):
    x = make_array(x_position, x_position)
    y = make_array(-4, 4)
    plots.plot(x, y, color=color)
    
def make_correlated_data(r):
    x = np.random.normal(0, 1, 1000)
    z = np.random.normal(0, 1, 1000)
    y = r*x + (np.sqrt(1-r**2))*z
    return x, y

def r_scatter(r):
    """Generate a scatter plot with a correlation approximately r"""
    plots.figure(figsize=(5,5))
    x, y = make_correlated_data(r)
    plots.scatter(x, y, color='darkblue', s=20)
    plots.xlim(-4, 4)
    plots.ylim(-4, 4)
    
def r_table(r):
    """
    Generate a table of 1000 data points with a correlation approximately r
    """
    np.random.seed(8)
    x, y = make_correlated_data(r)
    return Table().with_columns('x', x, 'y', y)
```

## Linear regression: defining the line


```python
# Copy-pasted from above
def standard_units(x):
    """ Converts an array x to standard units """
    return (x - np.mean(x)) / np.std(x)

def correlation(t, x, y):
    """ Computes correlation: t is a table, and x and y are column names """
    x_su = standard_units(t.column(x))
    y_su = standard_units(t.column(y))
    return np.mean(x_su * y_su)

```


```python
def slope(t, x, y):
    """ Computes the slope of the regression line, like correlation above """
    r = correlation(t, x, y)
    y_sd = np.std(t.column(y))
    x_sd = np.std(t.column(x))
    return r * y_sd / x_sd

def intercept(t, x, y):
    """ Computes the intercept of the regression line, like slope above """
    x_mean = np.mean(t.column(x))
    y_mean = np.mean(t.column(y))
    return y_mean - slope(t, x, y)*x_mean
```


```python
example = r_table(0.5)
slope(example, 'x', 'y')
```




    0.5022638281625915




```python
intercept(example,'x','y')
```




    0.03801479544542581



## Regression line vs other lines

Now we'll work with another dataset, illustrating the relationship between median income and education level across US.


```python
def demographics_errors(slope, intercept):
    # Use four convenient points from the original data
    sample = [[14.7, 33995], [19.1, 61454], [50.7, 71183], [59.5, 105918]]
    demographics.scatter('College%', 'Median Income', alpha=0.5)
    xlims = make_array(5, 75)
    # Plot a line with the slope and intercept you specified:
    plots.plot(xlims, slope * xlims + intercept, lw=4)
    # Plot red lines from each of the four points to the line
    for x, y in sample:
        plots.plot([x, x], [y, slope * x + intercept], color='r', lw=4)
```


```python
def fitted_values(t, x, y):
    """Return an array of the regression estimates at all the x values"""
    a = slope(t, x, y)
    b = intercept(t, x, y)
    return a*t.column(x) + b
```


```python
demographics = Table.read_table('district_demographics2016.csv')
demographics.show(5)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>State</th> <th>District</th> <th>Median Income</th> <th>Percent voting for Clinton</th> <th>College%</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alabama</td> <td>Congressional District 1 (115th Congress), Alabama</td> <td>47083        </td> <td>34.1                      </td> <td>24      </td>
        </tr>
        <tr>
            <td>Alabama</td> <td>Congressional District 2 (115th Congress), Alabama</td> <td>42035        </td> <td>33                        </td> <td>21.8    </td>
        </tr>
        <tr>
            <td>Alabama</td> <td>Congressional District 3 (115th Congress), Alabama</td> <td>46544        </td> <td>32.3                      </td> <td>22.8    </td>
        </tr>
        <tr>
            <td>Alabama</td> <td>Congressional District 4 (115th Congress), Alabama</td> <td>41110        </td> <td>17.4                      </td> <td>17      </td>
        </tr>
        <tr>
            <td>Alabama</td> <td>Congressional District 5 (115th Congress), Alabama</td> <td>51690        </td> <td>31.3                      </td> <td>30.3    </td>
        </tr>
    </tbody>
</table>
<p>... (430 rows omitted)</p>



```python
demographics = demographics.select('Median Income', 'College%')
demographics.show(5)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Median Income</th> <th>College%</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>47083        </td> <td>24      </td>
        </tr>
        <tr>
            <td>42035        </td> <td>21.8    </td>
        </tr>
        <tr>
            <td>46544        </td> <td>22.8    </td>
        </tr>
        <tr>
            <td>41110        </td> <td>17      </td>
        </tr>
        <tr>
            <td>51690        </td> <td>30.3    </td>
        </tr>
    </tbody>
</table>
<p>... (430 rows omitted)</p>



```python
demographics.scatter('College%', 'Median Income')
```


    
![png](lec11-demo_files/lec11-demo_14_0.png)
    


Let's pause here for a moment to see what we can infer from this scatter plot.

We can use linear regression to infer a linear model to help us predict the median income of a congressional district, given the percentage of people with a college education.


```python
correlation(demographics, 'College%', 'Median Income')
```




    0.8184648517141335




```python
regression_slope = slope(demographics, 'College%', 'Median Income')
regression_intercept = intercept(demographics, 'College%', 'Median Income')
regression_slope, regression_intercept
```




    (1270.70168946388, 20802.577766677925)




```python
predicted = fitted_values(demographics, 'College%', 'Median Income')
```


```python
demographics = demographics.with_column(
    'Linear Prediction', predicted)
demographics.scatter('College%')
```


    
![png](lec11-demo_files/lec11-demo_20_0.png)
    


Of course the linear model is not perfect; there will typically be some errors in the predictions.  Let's measure how large those errors are, and visualize them.


```python
actual = demographics.column('Median Income')
errors = actual - predicted
```


```python
demographics.with_column('Error', errors)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Median Income</th> <th>College%</th> <th>Linear Prediction</th> <th>Error</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>47083        </td> <td>24      </td> <td>51299.4          </td> <td>-4216.42</td>
        </tr>
        <tr>
            <td>42035        </td> <td>21.8    </td> <td>48503.9          </td> <td>-6468.87</td>
        </tr>
        <tr>
            <td>46544        </td> <td>22.8    </td> <td>49774.6          </td> <td>-3230.58</td>
        </tr>
        <tr>
            <td>41110        </td> <td>17      </td> <td>42404.5          </td> <td>-1294.51</td>
        </tr>
        <tr>
            <td>51690        </td> <td>30.3    </td> <td>59304.8          </td> <td>-7614.84</td>
        </tr>
        <tr>
            <td>61413        </td> <td>36.7    </td> <td>67437.3          </td> <td>-6024.33</td>
        </tr>
        <tr>
            <td>34664        </td> <td>19.4    </td> <td>45454.2          </td> <td>-10790.2</td>
        </tr>
        <tr>
            <td>76440        </td> <td>29.6    </td> <td>58415.3          </td> <td>18024.7 </td>
        </tr>
        <tr>
            <td>50537        </td> <td>24.5    </td> <td>51934.8          </td> <td>-1397.77</td>
        </tr>
        <tr>
            <td>49072        </td> <td>34      </td> <td>64006.4          </td> <td>-14934.4</td>
        </tr>
    </tbody>
</table>
<p>... (425 rows omitted)</p>



It's tempting to measure the quality of a linear regression model by taking the average error.  However, this doesn't work: the average works out to zero, because the points above the line (where error is positive) are cancelled out by points below the line (where error is negative).


```python
np.mean(errors)
```




    6.356008950321154e-13



Side question: It looks like the average was a very small number, not exactly zero.  Can you guess why that happened?

Intuitively, if your prediction is too large, that's as bad as if the prediction is too small.  So, it'd be natural to take the absolute value of the errors (to make them all positive, so they don't cancel each other out) and take the average of that.  But, for various reasons, instead we're going to take the square of the errors; that will also all make them positive and eliminate squaring.  (This might remind you of how we define the standard deviation.)


```python
np.mean(errors ** 2) ** 0.5
```




    9398.515588571281



Let's visualize the errors.


```python
demographics_errors(regression_slope, regression_intercept)
```


    
![png](lec11-demo_files/lec11-demo_30_0.png)
    


What if we tried a different line?  Then the errors would look different:


```python
demographics_errors(1500, 20000)
```


    
![png](lec11-demo_files/lec11-demo_32_0.png)
    



```python
demographics_errors(-1000, 75000)
```


    
![png](lec11-demo_files/lec11-demo_33_0.png)
    


Ugh.  That last line looked like a terrible fit to the data; the prediction errors it would make are huge.

## Root Mean Square Error ##

Let's quantify that, by measuring the root-mean-square error.  A prediction line with a smaller root-mean-square error will tend to have a smaller prediction error, so smaller is better.


```python
def show_demographics_rmse(slope, intercept):
    demographics_errors(slope, intercept)
    x = demographics.column('College%')
    y = demographics.column('Median Income')
    prediction = slope * x + intercept
    mse = np.mean((y - prediction) ** 2)
    print("Root mean squared error:", round(mse ** 0.5, 2))
```


```python
show_demographics_rmse(-1000, 75000)
```

    Root mean squared error: 30247.88



    
![png](lec11-demo_files/lec11-demo_38_1.png)
    



```python
show_demographics_rmse(1500, 20000)
```

    Root mean squared error: 11559.09



    
![png](lec11-demo_files/lec11-demo_39_1.png)
    



```python
show_demographics_rmse(regression_slope, regression_intercept)
```

    Root mean squared error: 9398.52



    
![png](lec11-demo_files/lec11-demo_40_1.png)
    


Which of those lines had the lowest root-mean-square error?

## Numerical Optimization ##

Let's take a bit of an aside.  We'll show you how to do numerical optimization.  In particular, if you have a function that computes how good a particular set of values are, numerical optimization will find the best values.  It will find inputs to the function that make the output of that function as small as possible.

How does it work?  Magic.  OK, it's not really magic -- you can take more advanced classes where you learn how to do this -- but that's beyond the scope of this class.  For our purposes, we'll take it for granted that someone else has figured out how to do this, and we'll use it for our needs.


```python
x = np.arange(1, 3, 0.1)
y = (x-2)**2 + 3
Table().with_columns('x', x, 'y', y).plot('x')
```


    
![png](lec11-demo_files/lec11-demo_44_0.png)
    



```python
def f(x):
    return ((x-2)**2) + 3
```


```python
minimize(f)
```




    1.9999999946252267




```python
x = np.arange(-1.5, 1.5, 0.05)
y2 = 2 * np.sin(x*np.pi) + x ** 3 + x ** 4 
Table().with_columns('x', x, 'y', y2).plot('x')
```


    
![png](lec11-demo_files/lec11-demo_47_0.png)
    



```python
def complicated_function(x):
    return 2 * np.sin(x*np.pi) + x ** 3 + x ** 4 
```


```python
minimize(complicated_function)
```




    -0.5126437620940081



## Minimizing RMSE ##

Now let's use numerical optimization to find the line (the slope and intercept) that minimize the root-mean-square prediction error.


```python
def demographics_rmse(any_slope, any_intercept):
    x = demographics.column('College%')
    y = demographics.column('Median Income')
    estimate = any_slope*x + any_intercept
    return (np.mean((y - estimate) ** 2)) ** 0.5
```


```python
demographics_rmse(1500, 20000)
```




    11559.086490075999




```python
demographics_rmse(-1000, 75000)
```




    30247.883767944502




```python
minimize(demographics_rmse)
```




    array([ 1270.70168805, 20802.57933807])




```python
make_array(regression_slope, regression_intercept)
```




    array([ 1270.70168946, 20802.57776668])




```python

```
