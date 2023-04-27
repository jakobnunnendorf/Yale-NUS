# Lab 7: Regression Inference

**Reading**: 
* [Inference for Regression](https://www.inferentialthinking.com/chapters/16/Inference_for_Regression.html)


```python
# Don't change this cell; just run it. 

import numpy as np
from datascience import *

# These lines do some fancy plotting magic.",
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)
```

## Part 1: Regression Inference for the NFL Draft

In this homework, we will be analyzing the relationship between draft position and success in the NFL. The NFL draft is an annual event in which every NFL team takes turns choosing players that they will add to their team. There are around 200 selections, called "picks" made every year, although this number has changed over the years.

The `nfl_data` table has five columns, the name of the `Player`, the `Salary` that player made for the 2019 season, the year that player was drafted (`Year Drafted`), the number of the draft pick that was used when the player was drafted (`Pick Number`), and the `Position` in football that player plays.

Each row in `nfl_data` corresponds to one player who played in the **2019 season**.


```python
# Just run this cell!
nfl_data = Table.read_table("nfl.csv")
nfl_data.show(5)
```

#### Question 1

Take the `nfl_data` table and add a column called `Career Length` that corresponds to how long a player has been in the NFL to create a new table called `nfl`. `Career Length` is from when they were drafted to this year, 2021. So, if a player was drafted in 2015, their career length is 6:
$$2021-2015=6$$

<!--
BEGIN QUESTION
name: q1_1
manual: false
-->


```python
nfl = ...
nfl.show(5)
```

As usual, let's investigate our data visually before analyzing it numerically. The first relationship we will analyze is the relationship between a player's `Pick Number` and their `Career Length`. Run the following cell to see a scatter diagram with the line of best fit plotted for you in red.


```python
# Just run this cell
nfl.scatter("Pick Number", "Career Length")
m, b = np.polyfit(nfl.column(3), nfl.column(5), 1)
plt.plot(nfl.column(3), m*nfl.column(3)+b, color='r');
```

#### Question 2

Use the functions given to assign the correlation between `Pick Number` and `Career Length` to `pick_length_correlation`. `correlation` takes in three arguments, a table `tbl` and the labels of the columns you are finding the correlation between, `col1` and `col2`.

<!--
BEGIN QUESTION
name: q1_2
manual: false
-->


```python
def standard_units(arr):
    return (arr- np.mean(arr)) / np.std(arr)

def correlation(tbl, col1, col2):
    r = np.mean(standard_units(tbl.column(col1)) * standard_units(tbl.column(col2)))
    return r

pick_length_correlation = ...
pick_length_correlation
```

We can see that there is a negative association between `Pick Number` and `Career Length`! If in the sample, we found a linear relation between the two variables, would the same be true for the population? Would it be exactly the same linear relation? Could we predict the response of a new individual who is not in our sample? 

Let's find out the answers to these questions by investigating whether there is a true linear relation or correlation in the population between `Pick Number` and `Career Length`!

#### Question 3

Michael thinks that the slope of the true line of best fit for `Pick Number` and `Career Length` is not zero: that is, there is some correlation/association between `Pick Number` and `Career Length`. To test this claim, we can run a hypothesis test! Define the null and alternative hypothesis for this test.

<!--
BEGIN QUESTION
name: q1_3
manual: true
-->
<!-- EXPORT TO PDF -->

*Write your answer here, replacing this text.*

#### Question 4

Saurav says that instead of finding the slope for each resample, we can find the correlation instead, and that we will get the same result for the hypothesis test. Why is he correct? What is the relationship between slope and correlation?

*Hint: This [section](https://www.inferentialthinking.com/chapters/15/2/Regression_Line.html) of the textbook describes the relationship between slope and correlation.*

<!--
BEGIN QUESTION
name: q1_4
manual: true
-->
<!-- EXPORT TO PDF -->

*Write your answer here, replacing this text.*

#### Question 5
Define the function `one_resample_r` that performs a bootstrap and finds the correlation between `Pick Number` and `Career Length` in the resample. `one_resample_r` should take three arguments, a table `tbl` and the labels of the columns you are finding the correlation between, `col1` and `col2`.

*Hint: You can use previously defined functions to help you.*

<!--
BEGIN QUESTION
name: q1_5
manual: false
-->


```python
def one_resample_r(tbl, col1, col2):
    ...

# Don't change this line below!
one_resample = one_resample_r(nfl, "Pick Number", "Career Length")
one_resample
```

#### Question 6

Generate 1000 bootstrapped correlations for `Pick Number` and `Career Length`, store your results in the array `resampled_correlations_pc`, and plot a histogram of your results.

<!--
BEGIN QUESTION
name: q1_6
manual: true
-->
<!-- EXPORT TO PDF -->


```python
resampled_correlations_pc = ...
...

# Don't change the following line of code. It will plot your histogram.
Table().with_column("Resampled Correlations, Pick Number vs Career Length", resampled_correlations_pc).hist()
```

#### Question 7

Calculate a 95% confidence interval for the resampled correlations and then assign either `True` or `False` to `reject` if we can reject the null hypothesis or if we cannot reject the null hypothesis using a 5% p-value cutoff.

*Note: Feel free to calculate the CI first, then fill in the `reject` variable after.*

<!--
BEGIN QUESTION
name: q1_7
manual: false
-->


```python
lower_bound_pc = ...
upper_bound_pc = ...
reject = ...

# Don't change this!
print(f"95% CI: [{lower_bound_pc}, {upper_bound_pc}] , Reject the null: {reject}")
```

Now let's investigate the relationship between `Pick Number` and `Salary`. As usual, let's inspect our data visually first. A line of best fit is plotted for you in red.


```python
# Just run this cell!
nfl.scatter("Pick Number", "Salary")
c, d = np.polyfit(nfl.column(3), nfl.column(1), 1)
plt.plot(nfl.column(3), c*nfl.column(3)+d, color='r');
```

#### Question 8

Using the function `correlation`, find the correlation between `Pick Number` and `Salary` and assign it to `pick_salary_correlation`.


<!--
BEGIN QUESTION
name: q1_8
manual: false
-->


```python
pick_salary_correlation = ...
pick_salary_correlation
```

We can see that there is a negative association between `Pick Number` and `Salary`! 

#### Question 9

Once again, Michael thinks that the slope of the true line of best fit for `Pick Number` and `Salary` is not zero: that is, there is some correlation/association between `Pick Number` and `Salary`. To test this claim, we can run a hypothesis test! Define the null and alternative hypothesis for this test.


<!--
BEGIN QUESTION
name: q1_9
manual: true
-->
<!-- EXPORT TO PDF -->

*Write your answer here, replacing this text.*

#### Question 10

Generate 1000 bootstrapped correlations for `Pick Number` and `Salary`, append them to the array `resampled_correlations_salary`, and then plot a histogram of your results.

*Hint: Your code for this question will be similar to Question 6.*

<!--
BEGIN QUESTION
name: q1_10
manual: true
-->
<!-- EXPORT TO PDF -->


```python
resampled_correlations_salary = ...
...

for i in np.arange(1000):
    resampled_correlations_pc = np.append(resampled_correlations_pc,one_resample_r(nfl, "Pick Number", "Career Length"))

# Don't change the following line of code. It will plot your histogram.
Table().with_column("Resampled Correlations for Salary", resampled_correlations_salary).hist()
```

#### Question 11

Calculate a 95% confidence interval for the resampled correlations and then assign either `True` or `False` to `reject_sal` if we can reject the null hypothesis or if we cannot reject the null hypothesis using a 5% p-value cutoff.

*Note: Feel free to calculate the CI first, then fill in the `reject_sal` variable after.*


<!--
BEGIN QUESTION
name: q1_11
manual: false
-->


```python
lower_bound_sal = ...
upper_bound_sal = ...
reject_sal = ...

# Don't change this!
print(f"95% CI: [{lower_bound_sal}, {upper_bound_sal}], Reject the null: {reject_sal}")
```

## Part 2: Analyzing Residuals

Next, Evan wants to predict his Career Length and Salary based on his Pick Number. To understand what his Career Length and Salary might be, Evan wants to generate confidence intervals of possible values for both career length and salary. First, let's investigate how effective our predictions for career length and salary based on pick number are.

#### Question 12

Calculate the slope and intercept for the line of best fit for `Pick Number` vs `Career Length` and for `Pick Number` vs `Salary`. Assign these values to `career_length_slope`, `career_length_intercept`, `salary_slope`, and `salary_intercept` respectively. The function `parameters` returns a two-item array containing the slope and intercept of a linear regression line.

*Hint 1: Use the `parameters` function with the arguments specified!*

*Hint 2: Remember we're predicting career length and salary **based off** a pick number. That should tell you what the `colx` and `coly` arguments you should specify when calling `parameters`.*

<!--
BEGIN QUESTION
name: q1_12
manual: false
-->


```python
# DON'T EDIT THE PARAMETERS FUNCTION
def parameters(tbl, colx, coly):
    x = tbl.column(colx)
    y = tbl.column(coly)
    
    r = correlation(tbl, colx, coly)
    
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_sd = np.std(x)
    y_sd = np.std(y)
    
    slope = (y_sd / x_sd) * r
    intercept = y_mean - (slope * x_mean)
    return make_array(slope, intercept)

career_length_slope = ...
career_length_intercept = ...

salary_slope = ...
salary_intercept = ...

print(career_length_slope)
print(career_length_intercept)

print(salary_slope)
print(salary_intercept)
```

#### Question 13

Draw a scatter plot of the residuals (i.e. actual - predicted) for each line of best fit for `Pick Number` vs `Career Length` and for `Pick Number` vs `Salary`. 

*Hint: We want to get the predictions for every player in the dataset*

*Hint 2: This question is really involved, try to follow the skeleton code! This [section](https://www.inferentialthinking.com/chapters/15/5/Visual_Diagnostics.html) of the textbook will be helpful for the next two questions.*

<!--
BEGIN QUESTION
name: q1_13
manual: true
-->
<!-- EXPORT TO PDF -->


```python
predicted_career_lengths = ...
predicted_salaries = ...

career_length_residuals = ...
salary_residuals = ...

nfl_with_residuals = nfl.with_columns("Career Length Residuals", career_length_residuals, "Salary Residuals", salary_residuals)

# Now generate two scatter plots!
nfl_with_residuals.scatter("Pick Number", "Career Length Residuals")
nfl_with_residuals.scatter("Pick Number", "Salary Residuals")
```

Here's a [link](https://www.inferentialthinking.com/chapters/15/6/Numerical_Diagnostics.html) to properties of residuals in the textbook that could help out with some questions.

#### Question 14

Based on these plots of residuals, do you think linear regression is a good model for `Pick Number` vs `Career Length` and for `Pick Number` vs `Salary`? Explain for both.


<!--
BEGIN QUESTION
name: q1_14
manual: true
-->
<!-- EXPORT TO PDF -->

*Write your answer here, replacing this text.*

#### Question 15

Assign `career_length_residual_corr` and `salary_residual_corr` to either 1, 2 or 3 corresponding to whether or not the correlation between `Pick Number` and `Career Length Residuals` is zero, positive, or negative, and to whether or not the correlation between `Pick Number` and `Salary Residuals` is zero, positive, or negative respectively.

*Hint: This [section](https://www.inferentialthinking.com/chapters/15/6/Numerical_Diagnostics.html) of the textbook will be helpful.*

1. Zero
2. Positive
3. Negative

<!--
BEGIN QUESTION
name: q1_15
manual: false
-->


```python
career_length_residual_corr = ...
salary_residual_corr = ...
```

It looks like the largest residuals are positive residuals, so let's investigate those more closely.

#### Question 16

Let's investigate where our regression line is making errors. Using the `nfl_with_residuals` table, assign `greatest_career_length_residual` to the string that is the name of the player with the largest positive residual for `Pick Number` vs `Career Length`.

*Hint: We would recommend running `nfl_with_residuals` in a separate cell to see what the table looks like.*


<!--
BEGIN QUESTION
name: q1_16
manual: false
-->


```python
greatest_career_length_residual = ...
greatest_career_length_residual
```

Now let's investigate the residuals for salary. Run the cell below to see the players with the largest residuals for `Pick Number` vs `Salary`.


```python
# Just run this cell!
nfl_with_residuals.sort("Salary Residuals", descending=True).take(np.arange(10)).drop(2,6)
```

#### Question 17

What patterns do you notice with these large residuals for salary? How could this affect our analysis?


<!--
BEGIN QUESTION
name: q1_17
manual: true
-->
<!-- EXPORT TO PDF -->

*Write your answer here, replacing this text.*

## Part 3: Prediction Intervals

Now, Evan wants to predict his career length based on his specific pick number, which is 169. Instead of using the best fit line generated from the sample, Evan wants to generate an interval for his predicted career length.

#### Question 18

Define the function `one_resample_prediction` that generates a bootstrapped sample from the `tbl` argument, calculates the line of best fit for `coly` vs `colx` for that resample, and predicts a value based on `xvalue`.

*Hint: The standard form of the line of best fit is y = mx+b, with a unique slope (m) and intercept (b) for our data. Remember, the `parameters` function was defined earlier to help find that slope and intercept!*


<!--
BEGIN QUESTION
name: q1_18
manual: false
-->


```python
def one_resample_prediction(tbl, colx, coly, xvalue):
    ...

evans_career_length_pred = one_resample_prediction(nfl, "Pick Number", "Career Length", 169)
evans_career_length_pred
```

#### Question 19

Assign `resampled_predictions` to be an array that will contain 1000 resampled predictions for Evan's career length based on his pick number 169, and then generate a histogram of it.


<!--
BEGIN QUESTION
name: q1_19
manual: true
-->
<!-- EXPORT TO PDF -->


```python
resampled_predictions = ...

...

# Don't change/delete the code below in this cell
Table().with_column("Resampled Career Length Predictions", resampled_predictions).hist()
```

#### Question 20

Using `resampled_predictions` from Question 19, generate a 99% confidence interval for Evan's predicted career lengths.


<!--
BEGIN QUESTION
name: q1_20
manual: false
-->


```python
lower_bound_evan = ...
upper_bound_evan = ...

# Don't delete/modify the code below in this cell
print(f"99% CI: [{lower_bound_evan}, {upper_bound_evan}]")
```

Run the following cell to see a few bootstrapped regression lines, and the predictions they make for a career length from a pick number of 169.


```python
# Just run this cell! 
# You don't need to understand all of what it is doing but you should recognize a lot of the code!
lines = Table(['slope','intercept'])
x=169
for i in np.arange(20):
    resamp = nfl.sample(with_replacement=True)
    resample_pars = parameters(resamp, "Pick Number", "Career Length") 
    slope = resample_pars.item(0)
    intercept = resample_pars.item(1)
    lines.append([slope, intercept])
    
lines['prediction at x='+str(x)] = lines.column('slope')*x + lines.column('intercept')
xlims = [min(nfl.column("Pick Number")), max(nfl.column("Pick Number"))]
left = xlims[0]*lines[0] + lines[1]
right = xlims[1]*lines[0] + lines[1]
fit_x = x*lines['slope'] + lines['intercept']
for i in range(20):
    plt.plot(xlims, np.array([left[i], right[i]]), lw=1)
    plt.scatter(x, fit_x[i], s=30)
plt.ylabel("Career Length");
plt.xlabel("Pick Number");
plt.title("Resampled Regression Lines");
```

## Nonlinear regression

Just run the cells/explore if you're interested.

In the past few weeks you have learned one of the most powerful tools in a data scientist's arsenal: regression. At this point you may be wondering: what do we do when our data is not linear? You have learned that you shouldn't try and force models when they are bad fits: for example, if we detect heteroscedasticity in our residuals plot, we know that linear regression is a bad fit.

How can we fit data that is not linear then?

Let's increase our data's complexity a little: instead of linear data, let's look at data that you would naturally model with a parabola instead:


```python
def parabola(x, a=1, b=0, c=0):
    random_noise = np.random.normal(size=len(x)) * 3
    return  a*(x**2) + b*(x) + c + random_noise

size = 500
x_values = np.random.uniform(-5, 10, size=size)
y_values = parabola(x_values, a=2, b=-3, c=5)

Table().with_columns("X", x_values, "Y", y_values).scatter("X","Y", fit_line=True)
```

You can see that our line of best fit is a poor match for this data. Let's look at the residual plot:


```python
def mse(slope, intercept):
    predicted_y = slope * x_values + intercept
    errors = y_values - predicted_y
    return np.mean(errors**2)


slope_and_intercept = minimize(mse, smooth=True)
predicted_y = slope_and_intercept.item(0) * x_values + slope_and_intercept.item(1)
residuals = y_values - predicted_y

Table().with_columns("X", x_values, "Residuals",residuals).scatter("X", "Residuals")
```

Our residuals clearly have a pattern, confirming that linear regression is a bad fit for this data! In fact, our residuals actually look like our original data.

Linear regression generates a line that minimizes mean squared error. Using the `minimize` function on the `mse` function does all the work of finding values for us! Can we use `minimize` for more complicated models? Yes! In future data science classes, you will learn how to find these values yourself using the mathematical fields of Linear Algebra (note that it involves lines!) and calculus!

Let's take a look at the equation for a line:

$$y = ax +b$$

There are two parameters here that we can change: $a$, which is the slope, and $b$, which is the intercept.

How about the equation for a parabola?

$$y = ax^2 + bx + c$$

Now there are three parameters, $a,b,c$.

Let's change our mse function to incorporate these three parameters!


```python
def mse_parabola(a, b, c):
    predicted_y = a * (x_values**2) + b * (x_values) + c
    errors = y_values - predicted_y
    return np.mean(errors**2)
```

The function still returns the mean squared error of our predicted curve, just our curve is now a parabola with the parameters `a`, `b`, and `c`. Let's try and minimize this function!


```python
params = minimize(mse_parabola, smooth=True)
a = params.item(0)
b = params.item(1)
c = params.item(2)
a, b, c
```

Let's plot our new curve with these values!


```python
x_values_range = np.linspace(-5, 10, 1000)
predicted_y = a * (x_values_range**2) + b * (x_values_range) + c

Table().with_columns("X", x_values, "Y", y_values).scatter("X", "Y")
plt.plot(x_values_range, predicted_y, color='gold', markersize=1);
```

Our curve looks like a much better fit now! Let's double check the residuals plot to be sure.


```python
residuals = y_values - (a * (x_values**2) + b * (x_values) + c)
Table().with_columns("X", x_values, "Residuals", residuals).scatter("X", "Residuals")
```

A formless cloud, excellent!

What else can the method of least squares do?

Can we predict a single variable based on the values of two other variables? Right now, we don't have a way of doing that. 

If you look at the previous example, you could say that the $x^2$ term is actually a second variable.

Let's generate a dataset to work with. We are going to try and predict `z` based on `x` and `y`.


```python
x_values_range = np.linspace(-5, 10, 1000)

x = 0.5 * np.random.uniform(-5, 10, size=size) + 3
y = np.random.uniform(-5, 10, size=size) - 1
z = 3*x  + (-2*y) -4 + np.random.normal(size=size)

data = Table().with_columns("x", x, "y", y, "z", z)
data.scatter("x", "y")
data.scatter("x", "z")
data.scatter("y", "z")
```

We can see that `x` and `y` would both be very helpful to predict `z` by themselves! However, if we combined them we could predict `z` even better. Since our goal is to minimize mean squared error, let's find the mean squared error of the models that only use `x` and `y` by themselves (using an intercept).


```python
from scipy import stats
def su(x):
    return (x-np.mean(x)) / np.std(x)
def r(x, y):
    return np.mean(su(x) * su(y))

def mse_x(slope, intercept):
    predicted_z = slope * x + intercept
    errors = z - predicted_z
    return np.mean(errors**2)

def mse_y(slope, intercept):
    predicted_z = slope * y + intercept
    errors = z - predicted_z
    return np.mean(errors**2)


slope_and_intercept_x = minimize(mse_x, smooth=True)
predicted_z_x = slope_and_intercept_x.item(0) * x + slope_and_intercept_x.item(1)
residuals_x = z - predicted_z_x

Table().with_columns("X", x, "Residuals for X Model", residuals_x).scatter("X", "Residuals for X Model")

slope_and_intercept_y = minimize(mse_y, smooth=True)
predicted_z_y = slope_and_intercept_y.item(0) * y + slope_and_intercept_y.item(1)
residuals_y = z - predicted_z_y

Table().with_columns("Y", y, "Residuals for Y Model", residuals_y).scatter("Y", "Residuals for Y Model")
```

Both of the residual plots show no trend, so using these `x` or `y` by themselves would work, but how good are these models? Let's calculate their actual mse.


```python
x_only_mse = mse_x(slope_and_intercept_x.item(0), slope_and_intercept_x.item(1))
y_only_mse = mse_y(slope_and_intercept_y.item(0), slope_and_intercept_y.item(1))

print(f"X only model MSE: {x_only_mse}, Y only model MSE: {y_only_mse}")
```

Looks like the y only model has lower MSE, so we should try and use that if we can only use `x` or `y`. 

Instead, let's try to build a model that is a combination of `x`, `y` and an intercept `c` to predict `z`!

$$z = ax + by +c$$


```python
def mse_both(a, b, c):
    predicted_z = (a * x) + (b * y) + c
    errors = z - predicted_z
    return np.mean(errors**2)

slope_and_intercept_both = minimize(mse_both, smooth=True)
predicted_z = (slope_and_intercept_both.item(0) * x) + (slope_and_intercept_both.item(1) * y) + slope_and_intercept_both.item(2)
residuals = z - predicted_z

Table().with_columns("X", x, "Residuals for Full Model", residuals).scatter("X", "Residuals for Full Model")
Table().with_columns("Y", x, "Residuals for Full Model", residuals).scatter("Y", "Residuals for Full Model")
```

This model is also a good fit looking at the residuals with respect to both `x` and `y`! What is this model's mse?


```python
full_model_mse = mse_both(slope_and_intercept_both.item(0), slope_and_intercept_both.item(1), slope_and_intercept_both.item(2))

print(f"X only model MSE: {x_only_mse}, Y only model MSE: {y_only_mse}, Both X and Y MSE: {full_model_mse}")
```

That MSE is much lower! We should definitely use this model instead of either the x only or y only model independently!
Let's try and visualize what this model looks like with a 3D graph!


```python
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
sns.set_style("whitegrid", {'axes.grid' : False})

fig = plt.figure(figsize=(10,7));
ax = fig.add_subplot(111, projection='3d');
ax.scatter(x, y, z);
ax.set_xlabel('X');
ax.set_ylabel('Y');
ax.set_zlabel('Z');

ax.scatter(x,y,predicted_z)
ax.view_init(elev=20, azim=70);
```

Once we start working in more dimensions, visualization becomes increasingly difficult and useless. Instead of predicting a line, our prediction is actually a plane of values (the red values)!

## 2. Submission


To submit your assignment, please download your notebook as a .ipynb file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as... > Notebook (.ipynb) or HTML (.html). Then, upload both files under "Lab #07".
