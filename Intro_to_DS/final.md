# YSC2239 Final Examination Spring 2023

### This exam consists of 3 questions.

### Time: April 28th (Friday) 2:45pm - 5:15pm (No submission will be accepted after the deadline)

### Venue: Tan Chin Tuan Lecture Theatre at Yale-NUS College


## Table of Contents

### [1 Basic Data Science (40 points) ](#q1)

### [2 Basic Mathematics (22 points)](#q2)

### [3 Logistic Regression vs Decision Tree (38 points)](#q3)



```python
# Run this cell to set up your notebook
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
from scipy.optimize import minimize

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import tree

# you may get a warning from importing ensemble. It is OK to ignore said warning
from sklearn import ensemble
plt.style.use('fivethirtyeight')
```

## 1 Basic Data Science (40 points) <a id='q1'></a>

Our module is called the introduction to data science, so at the end of the module, it's worthy to have some brief review in restrospect. We spend quite some time on getting ourselves familiar with coding tool i.e. Python and some useful packages(for example datascience, pandas). As the saying goes, good tools are prerequisite to the success of a job. So then what is the "job" of the course? Definitely not the tool, as tools may differ from time to time. Instead, the key lies in the word `model`.



### Question 1.1 (2 points) Define the notation of model in data science.


```python
# Simply write your answer to Question 1.1 below and no need to Run this cell

```

Recall that there are four steps basic step when we talk about the modeling process:

A. Define a model.

B. Define a loss function.

C. Find the parameters that minimizes the loss.

D. Evaluate the model performance

We'll go through the `first three steps` on some example dataset from online repository loaded by using `load_dataset` command of `seaborn` package. The description of `load_dataset` is available at https://seaborn.pydata.org/generated/seaborn.load_dataset.html and the list of datasets is avaiable at https://github.com/mwaskom/seaborn-data. 

Note since we are not going to evaluate the model performance, we are not going to split the dataset into train set and test test. Instead, we use the full dataset to train various models for this part.

### Question 1.2 (3 points) Load the dataset named `tips` into our notebook and give the dataset the same name (i.e. tips) and show the last 15 rows of the dataset.


```python
# Write your codes to Question 1.2 below and then Run this cell

```

Throughout the rest of questions (for part 1 Basic Data Science), we try to predict restaurant tips in **absolute amounts**.

`y_tips`: Each actual tip in our dataset is $y$, which is what we call the **observed value** or **dependent variable**. We want to predict each observed value as $\hat{y}$.


```python
# No further action needed, just Run this cell to define y_tips array, the array of observed tips.
y_tips = np.array(tips['tip'])              
```

### Question 1.3 (in total 6 points) Use a **constant model $\hat{y} = \theta_0$ with $L_2$ loss** to predict the tip $\hat{y}$. In other words, regardless of any other details (i.e., features) about the meals, we will always predict our tip $\hat{y}$ as one single value: $\theta_0$. 

Remark on **$L_2$ loss** (also **squared loss**): for an observed tip value $y$ (i.e., the real tip), our prediction of the tip $\hat{y}$ would give an $L_2$ loss of:

$$\large L_2(y, \hat{y}) = \large (y - \hat{y})^2 = \large (y - \theta_0)^2 $$

We just defined loss for a single datapoint. Let's extend the above function to our entire dataset by taking the **average loss** across the dataset.

### Question 1.3a (3 points) Define the `mse_tips_constant` function which computes the **average $L_2$ error** on the tips dataset for the constant model with parameter $\theta_0$.

**Hint:** 
* You should use the array `y_tips` defined before.



```python
#Complete the definition of the function and then Run the cell
def mse_tips_constant(theta0):
    """
    Calculate the average squared loss on the tips data for a constant model.
    
    Parameters
    ------------
    theta0 : fitted constant model
    
    Returns
    ------------
    The mean square error on the tips data for a constant model.
    """
    ...

mse_tips_constant(5.3) # Arbitrarily pick theta0 = 5.3
```

### Question 1.3b (3 points) Find the value of $\theta_0$ that minimizes the mean squared error for our `tips` dataset by using the `minimize` function. 

Note the function `minimize` from [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) will attempt to minimize any function you throw at it.

**Hints:** 
* You should use the function you defined earlier: `mse_tips_constant`.
* Assign `min_scipy_constant` to the result of the `minimize` function which is called with initial `x0 = 0.0`.


```python
# Complete the ... part and then Run this cell.
min_scipy_constant = ...
theta0_hat_constant = min_scipy_constant['x'][0]
theta0_hat_constant
```

### Question 1.4 (in total 11 points) Instead of using the constant model, we assume that tip depends on the total amount of the bill of the meal and furthermore we assume **a linear model with $L_2$ loss** to predict the tip $\hat{y}$.

We define our model as the **linear model** that takes a single input feature, `total_bill`, $x$, and predicts the dependent variable, $\hat{y}$:

$$\large
\hat{y} = \theta_0 + \theta_1 x
$$

Our modeling goal is to find optimal parameter(s) $\hat{\theta_0}$ and $\hat{\theta_1}$ that **best fit our data**. We use **$L_2$ loss**, therefore for an observed tip value $y$ (i.e., the real tip), our prediction of the tip $\hat{y}$ would give an $L_2$ loss of:

$$\large L_2(y, \hat{y}) = \large (y - \hat{y})^2 = \large (y - (\theta_0 + \theta_1 x))^2 $$


```python
# No further action needed, just Run this cell to define x_total_bills, the feature of our model.
x_total_bills = np.array(tips['total_bill'])
```

### Question 1.4a (3 points) Define the `mse_tips_linear` function which computes the mean squared error on the tips dataset for the linear model with parameters $\theta_0$ and $\theta_1$.

**Hints:** 
* This function takes in two parameters `theta0` and `theta1`.
* You should use the arrays `x_total_bills` and `y_tips` defined before.


```python
#Complete the definition of the function and then Run the cell
def mse_tips_linear(theta0, theta1):
    """
    Calculate the mean squared error on the tips data for a linear model.
    
    Parameters
    ------------
    theta0 : intercept of the fitted linear model
    theta1 : slope of the fitted linear model
    
    Returns
    ------------
    The mean square error on the tips data for a linear model.
    """
    ...
mse_tips_linear(0.9, 0.1) # Arbitrarily pick theta0 = 0.9, theta1 = 0.1
```

### Question 1.4b (8 points) As we learn in linear regression, the optimal parameter(s) $\hat{\theta_0}$ and $\hat{\theta_1}$ are just the intercept and slope of the regression line between `x_total_bills` and `y_tips`. Write down the expression for $\hat{\theta_0}$ and $\hat{\theta_1}$ explicitely, denoted by `theta0_hat_analytic` and `theta1_hat_analytic` respectively.


```python
# Write out the slope and intercept of the regression line and then Run the Cell
theta1_hat_analytic = ...
theta0_hat_analytic = ...
theta0_hat_analytic, theta1_hat_analytic
```

### Question 1.5 (3 points) For predicting tip on the `tips` dataset, would you rather use the constant model or the linear model assuming an $L_2$ loss function for both and why?  


```python
# Simply write your answer to Question 1.5 below and no need to Run this cell

```

### Question 1.6 (in total 9 points) Now we assume **a linear model with $L_1$ loss** (also known as the absolute loss) to predict the tip $\hat{y}$. For an observed tip value $y$, our prediction of the tip $\hat{y}$ would give an $L_1$ loss of:

$$\large L_1(y, \hat{y}) = |y - \hat{y}| = |y - (\theta_0 + \theta_1 x)|$$

### Question 1.6a (3 points) Define the `mae_tips_linear` function which computes the **Mean Absolute Error (MAE)** on the dataset for the linear model with parameters $\theta_0$ and $\theta_1$.

**Hint**: 
* You should use the arrays `x_total_bills` and `y_tips` defined before.


```python
#Complete the definition of the function and then Run the cell
def mae_tips_linear(theta0, theta1):
    """
    Calculate the mean absolute error on the tips data for a linear model.
    
    Parameters
    ------------
    theta0 : intercept of the fitted linear model
    theta1 : slope of the fitted linear model
    
    Returns
    ------------
    The mean absolute error on the tips data for a linear model.
    """
    ...
mae_tips_linear(5.3, 2) # Arbitrarily pick theta0 = 5.3 and theta1 = 2
```

### Question 1.6b (3 points) In this case, unlike in Question 1.4, we do not have explicit analytical solution. So we are going to use the `minimize` function to find the value for $\hat{\theta_0}$ and $\hat{\theta_1}$. But there is a small technical issue. The `minimize` function can minimize functions of multiple variables. There's one quirk, however, which is that functions have to accept its parameters as a single list, so we will define $\vec{\theta} = \begin{bmatrix}\theta_0\\ \theta_1 \end{bmatrix}$, as a single list input to the function.


Implement the `mae_tips_linear_list` function, which is exactly like `mae_tips_linear` defined previously except that it takes in a single list of 2 variables rather than two separate variables.


```python
#Complete the definition of the function and then Run the cell
def mae_tips_linear_list(theta):
    """
    Calculate the mean absolute error on the tips data for a linear model.
    
    Parameters
    ------------
    theta : a list containg [theta0, theta1]
    
    Returns
    ------------
    The mean absolute error on the tips data for a linear model.
    """
    ...
mae_tips_linear_list([5.3, 2]) # Arbitrarily pick theta = [5.3, 2]
```

### Question 1.6c (3 points) Compute the optimal value for $\hat{\theta_0}$ and $\hat{\theta_1}$ denoted by `theta0_hat_mae` and `theta1_hat_mae` respectively.

**Hint:**
* Assign `min_linear_mae` to the result of the `minimize` function which is called with initial `x0 = [0.0, 0.0]`.


```python
# Complete the ... part and then Run this cell.
min_linear_mae = ...
theta0_hat_mae = min_linear_mae['x'][0]
theta1_hat_mae = min_linear_mae['x'][1]
theta0_hat_mae, theta1_hat_mae
```

### Question 1.7 (6 points) Identify some key differences you observe between the **$L_1$ loss** and **$L_2$ loss**. Which one you prefer and why?

**Hint:**
* You can try ploting `mae_tips_linear` and `mse_tips_linear` to get some idea


```python
# Simply write your answer to Question 1.7 below and no need to Run this cell

```

## 2 Basic Mathematics (22 points) <a id='q2'></a>

Recall that for the Regression Line we learned in the first half of this semester, it is written as follows:

$$\hat{y} = \theta_0 + \theta_1 x,$$

where $\hat{y}$ denotes the predicted value of $y$ for the input value of $x$, $\theta_0$ is the intercept term and $\theta_1$ is the slope. 

In the second-half of this semester, we generalize the above simple linear regression (SLR) by including more varialbes or features so that the formulation of our multiple linear regression model is:

$$\hat{y} = \theta_0 + \theta_1 x_1 + \dots + \theta_p x_p$$

We can rewrite our multiple linear regression model using matrix notation. Let $\mathbb{Y}$ be the (column) vector of all $n$ observations in our sample. Then our prediction vector $\hat{\mathbb{Y}}$ is

$$\Large \hat{\mathbb{Y}} = \mathbb{X} \theta$$

meaning the prediction vector $\hat{\mathbb{Y}}$ is just the matrix multiplication between $\mathbb{X}$ and $\theta$, where $\mathbb{X}$ is the **design matrix** representing the $p$ features for all $n$ datapoints in our sample and $\theta$ is the parameter vector. You can refer to basic rules on the matrix multiplicaiton at wiki link (https://en.wikipedia.org/wiki/Matrix_multiplication) if need.

Note that for our SLR model, $p = 1$ and therefore the matrix notation seems rather silly. Nevertheless it is valuable to start small and build on our intuition.

Because we have an intercept term $\theta_0$ in our parameter vector $\theta$, our design matrix $\mathbb{X}$ for $p$ features actually has dimension

$$ \Large \mathbb{X} \in \mathbb{R}^{n \times (p + 1)}$$

Therefore, the resulting matrix expression $\hat{\mathbb{Y}} = \mathbb{X} \theta$ represents $n$ linear equations, where for $i$-th observation, 
$$\hat{y_i} = \theta_0 + \theta_1 x_1^i + \dots + \theta_p x_p^i = [1, x_1^i, \dots,x_p^i] \begin{bmatrix}\theta_0\\ \theta_1 \\ \dots \\ \theta_p \end{bmatrix}$$.

The constant all-ones column of $\mathbb{X}$ is sometimes called the **bias feature**; $\theta_0$ is frequently called the **bias or intercept term**.

### Question 2.1 (3 points) As the example dataset for this part (i.e  2 Basic Mathematics), load the dataset named `mpg` into our notebook, denote the dataset by the same name (i.e. `mpg`) and drop any rows that have missing data.


```python
# Write your codes to Question 2.1 below and then Run this cell

```

### Question 2.2 (3 points) Implement `add_intercept` which computes a design matrix such that the first (left-most) column is all ones. 

Note that once we have contruct the all-ones column `bias_feature` by using the `np.ones` function (NumPy [documentation](https://numpy.org/doc/stable/reference/generated/numpy.ones.html?highlight=ones)) properly, we then call `np.concatenate` ([documentation](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)) function to generate `design matrix`. This part of code is already written.

**Hint:**
* `bias_feature` should be a (column) vector of dimension `(n,1)`, not a vector of dimension `(n,)`.


```python
# Complete the ... part of the definition and then Run this cell.
def add_intercept(X):
    """
    Return X with a bias feature.
    
    Parameters
    -----------
    X: a 2D dataframe of p numeric features
    (may also be a 2D numpy array) of shape n x p
    
    Returns
    -----------
    A 2D matrix of shape n x (p + 1), where the leftmost
    column is a column vector of 1's
    """
    ...
    bias_feature = ...
    return np.concatenate([bias_feature, X], axis=1)
X = add_intercept(mpg[['horsepower']])
X.shape
```

### Question 2.3 (3 points) Define the model by implementing the `linear_model` function.

The predictions for all $n$ points in our data are (note $\theta = (\theta_0, \theta_1, \dots, \theta_p)$) :
$$ \Large \hat{\mathbb{Y}} = \mathbb{X} \theta. $$


**Hint**: 
* You can use [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html), [pd.DataFrame.dot](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dot.html), or the `@` operator to multiply matrices/vectors. However, while the `@` operator can be used to multiply `numpy` arrays, it generally will not work between two `pandas` dataframe objects, so keep that in mind when computing matrix-vector products!



```python
# Complete the definition of the function and then Run the cell
def linear_model(thetas, X):
    """
    Return the linear combination of thetas and features as defined above.
    
    Parameters
    -----------
    thetas: a 1D vector representing the parameters of our model ([theta1, theta2, ...])
    X: a 2D dataframe of numeric features (may also be a 2D numpy array)
    
    Returns
    -----------
    A 1D vector representing the linear combination of thetas and features as defined above.
    """
    ...
```

### Question 2.4 (5 points) When we fit a linear model with mean squared error, it is equivalent to the following optimization problem:

$$\Large \min_{\theta} ||\Bbb{X}\theta - \Bbb{Y}||^2$$

And when $X^T X$ is invertible, there is an analytic solution which is given by the equation (if you are interested, there is a geometric argument with the detail in the [link provided](https://learningds.org/ch/15/linear_multi_fit.html) but not related to this quesiton):

$$ \Large \hat{\theta} = (\Bbb{X}^T\Bbb{X})^{-1}\Bbb{X}^T\Bbb{Y}$$

So please implement the analytic solution $\hat{\theta}$ using `np.linalg.inv` ([link](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)) to compute the inverse of $\Bbb{X}^T\Bbb{X}$. Note: You can also consider using `np.linalg.solve` ([link](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)) instead of `np.linalg.inv` because it is more robust (more on StackOverflow [here](https://stackoverflow.com/questions/31256252/why-does-numpy-linalg-solve-offer-more-precise-matrix-inversions-than-numpy-li)). 


**Hint**: 
* To compute the transpose of a matrix, you can use `X.T` or `X.transpose()` ([link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T)).




```python
#Complete the definition of the function and then Run the cell
def get_analytical_sol(X, y):
    """
    Computes the analytical solution to our
    least squares problem
    
    Parameters
    -----------
    X: a 2D dataframe (or numpy array) of numeric features
    y: a 1D vector of tip amounts
    
    Returns
    -----------
    The estimate for theta (a 1D vector) computed using the
    equation mentioned above.
    """
    ...
Y = mpg['mpg']
analytical_thetas = get_analytical_sol(X, Y)
analytical_thetas
```

### Question 2.5 (in total 8 points) It's great we can have analytic solution for the optimization problems. But unfortunately it's not always the case in reality. For such cases, as we have seen in part 1, we are going to use `minimize` command.

### Question 2.5a (3 points) The cell below plots some arbitrary 4th degree polynomial function


```python
# No further action is needed, just Run the cell.
w_values = np.linspace(-4, 2.5, 100)

def fx(w):
    return 0.1 * w**4 + 0.2*w**3 + 0.2 * w **2 + 1 * w + 10

plt.plot(w_values, fx(w_values));
plt.title("Arbitrary 4th degree polynomial");
```


    
![png](final_files/final_47_0.png)
    


Compute the minimum value for the function `fx` and the optimal value of `x` which minimizes the function `fx` in the following cell, denoted by `min_of_fx` and `x_which_minimizes_fx` respectively.

**Hint:**
* Assign `min_result` to the result of `minimize` command.

**Initial guess**: The parameter `x0` that we passed to the `minimize` function is where it starts looking for the minimum. For the function above, it doesn't really matter what x we start at because the function is nice. Note that no matter what your actual variable is called in your function (`w` in this case), the `minimize` routine still expects a starting point parameter called `x0`.


```python
#Complete the ... part and then Run the cell
min_result = minimize(...)
min_of_fx = min_result['fun']
x_which_minimizes_fx = min_result['x'][0]
min_of_fx, x_which_minimizes_fx
```

### Question 2.5b (5 points) The `minimize` function can minimize functions of multiple variables. But `minimize` isn't perfect. The reason is that if the function we are given has many valleys (also known as local minima), `minimize` can get stuck when trying to minimize the function. So it's useful to have `initial guess` around the true minimum. Provide one suggestion on how we can have a good initial guess.


```python
# Simply write your answer to Question 2.5b below and no need to Run this cell

```

## 3 Logistic Regression vs Decision Tree (38 points) <a id='q3'></a>

**Backgroud:** In our module, we have covered quite a few basic models and if you are interested, you can pursue further with more advanced data science related modules. A common concern may arise is about how to choose from those models. In fact, with the same data, we can follow different models. In this question, you are going to train a multi-class classifier with two different models (one-vs-rest logistic regression and decision trees) and compare the accuracies and decision boundaries created by each.

**Data and Task:** We'll be looking at a dataset of per-game stats for all NBA players in the 2021-22 season. This dataset comes from [basketball-reference.com](https://www.basketball-reference.com/). Our goal will be to predict a player's **position** given several other features.


```python
# just run this cell
nba_data = pd.read_csv("nba21-22.csv")
```

There are several features we could use to predict about position. For our purpose, we will restrict our exploration to two inputs: Rebounds (TRB) and Assists (AST). The main reason is that two-input features models will make our 2-D visualizations more straightforward.

The 5 most common positions in basketball are PG, SG, SF, PF, and C (which stand for point guard, shooting guard, small forward, power forward, and center; [Wikipedia](https://en.wikipedia.org/wiki/Basketball_positions)). This information is contained in the `Pos` column of the dataset. While we could set out to try and perform 5-class classification, the results (and visualizations) are slightly more interesting if we try and categorize players into 1 of 3 categories: **Guard**, **Forward**, and **Center** by using the `basic_position` function defined as follows:


```python
# just run this cell
def basic_position(pos):
    if 'F' in pos:
        return 'F'
    elif 'G' in pos:
        return 'G'
    return 'C'
```

### Question 3.1 (2 points)  Take the `Pos` column of our dataframe and use it to create a new column `Pos3` that consist of values `'G'`, `'F'`, and `'C'` (which stand for Guard, Forward, and Center).


```python
# Complete ... part below and then Run this cell
nba_data['Pos3'] = ...
nba_data['Pos3']
```

### Question 3.2 (3 points) Since there are many players in the NBA (in the 2021-22 season there were over 600 unique players), our visualizations may get noisy and messy. Let's restrict our data to only contain rows for players that averaged 10 or more points (as shown in the `PTS` column) per game. The new dataset is still named as `nba_data`.


```python
# Complete ... part below and then Run this cell
nba_data = ...
nba_data
```

Let's have a look what the whole dataset look like with different values in features and their corrsponding positions.


```python
# just run this cell
sns.scatterplot(data = nba_data, x = 'AST', y = 'TRB', hue = 'Pos3');
```

### Question 3.3 (2 points) Before fitting any models, let's first split nba_data into a training set and test set. 

**Hint:**
* Using `train_test_split` command by setting `random_state=100` and `test_size = 0.25`.


```python
# Complete ... part below and then Run this cell
nba_train, nba_test = ...
nba_test
```

### One-vs-rest Logistic Regression

We only discussed binary logistic regression in class, but there is a natural extension of binary logistic regression called one-vs-rest logistic regression for multiclass classification. In essence, one-vs-rest logistic regression simply builds one binary logistic regression classifier for each of the `N` classes (in this scenario  𝑁=3). We then predict the class corresponding to the classifier that gives the highest probability among the `N` classes.

### Question 3.4 (5 points) In the cell below, set `logistic_regression_model` to be a one-vs-rest logistic regression model. Then, fit that model using the `AST` and `TRB` columns (in that order) from `nba_train` as our features, and `Pos3` as our response variable.

**Hint:**
* `sklearn.linear_model.LogisticRegression` ([documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)) has already been imported for you. There is an optional parameter **`multi_class`** you need to specify in order to make your model a multi-class one-vs-rest classifier. See the documentation for more details.



```python
# Complete ... part below and then Run this cell
logistic_regression_model = ...
```

### Decision Tree

Let's now create a decision tree classifier on the same training data `nba_train`. In lecture we define the entropy of a node and use it to evaluate split quality for classification and regression trees. Another metric for determining the quality of a split is **Gini impurity**. This is defined as the chance that a randomly chosen element of a set would be incorrectly labeled if it was labeled randomly and independently according to the distribution of labels in the set. Gini impurity is a popular alternative to entropy for determining the best split at a node, and it is in fact the default criterion for scikit-learn's `DecisionTreeClassifier`.

### Question 3.5 (5 points) We can calculate the Gini impurity of a node with the formula ($p_C$ is the proportion of data points in a node with label/class $C$):

$$ G = 1 - \sum_{C} {p_C}^2 $$

Implement the `gini_impurity` function, which outputs the Gini impurity of a node with a given set of labels. The `labels` parameter is a list of labels in our dataset. For example, `labels` could be `['G', 'G', 'F', 'F', 'C', 'C']`


```python
# Complete the definition of the function gini_impurity and then Run this cell
def gini_impurity(labels):
    ...

gini_impurity(nba_data['Pos3'])
```

### Question 3.6 (5 points) Use `tree.DecisionTreeClassifier` ([documentation](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)) to fit a model using the same features and response as above, and call this model `decision_tree_model`. 

**Hint:**
* Set the `random_state` and `criterion` parameters to 42 and `gini`, respectively.


```python
# Complete ... part below and then Run this cell
decision_tree_model = ...
```

### Question 3.7 (5 points) Show performance by accuracy of both models in one plot. 

**Hints:**
* We can compute the accuracy by using `model.score()` function. Note `model.score()` is used the same way as `model.fit()` or `model.predict()` for classification or regression problems. The resulting scores are between 0 and 1, with a larger score indicating a better fit.
* The training accuracy and testing accuracy should be displayed seperately.


```python
# Write your codes to Question 3.7 below and then Run this cell

```

To enable better comparision between two classifiers, we want to visualize the decision boundary for them classifier, and see how the classifiers perform on both the training and test data.

### Question 3.8 (5 points) Draw the decision boundaries for two classifers on training and testing sets in one plot using the `plot_decision_boundaries` function defined below.
**Hint:**
* 2 by 2 subplot is recommended.


```python
# Just run this cell to define the function plot_decision_boundaries
def plot_decision_boundaries(model, nba_dataset, title=None, ax=None):
    sns_cmap = ListedColormap(np.array(sns.color_palette())[0:3, :])
    xx, yy = np.meshgrid(np.arange(0, 12, 0.02), np.arange(0, 16, 0.02))
    Z_string = model.predict(np.c_[xx.ravel(), yy.ravel()])
    categories, Z_int = np.unique(Z_string, return_inverse = True)
    Z_int = Z_int.reshape(xx.shape)
    
    if ax is None:
        plt.figure()
        ax = plt.gca()
        
    ax.contourf(xx, yy, Z_int, cmap = sns_cmap)
    
    sns.scatterplot(data = nba_dataset, x = 'AST', y = 'TRB', hue = 'Pos3', ax=ax)

    if title is not None:
        ax.set_title(title)
```


```python
# Write your codes to Question 3.8 below and then Run this cell

```

### Question 3.9 (6 points) Looking at the two models:
* Which model performes better on the training set?
* Which model performes better on the test set?
* How do the decision boundaries generated for each of the two models relate to the model's performance?


```python
# Simply write your answer to Question 3.9 below and no need to Run this cell

```

## Final Words  (0 point)

If there was any question that you thought was ambiguous and required clarification to be answerable, please identify the question and state your assumptions. Be warned: We only plan to consider this information if we agree that the question was erroneous or ambiguous and we consider your assumption reasonable. (0 point)


```python
# Simply write your comment below and no need to Run this cell

```

### Submission

To submit your answer, please download your notebook as a .ipynb and .html file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as ... > Notebook (.ipynb) or HTML (.html). Then, upload **both files** under "Final_Eaxm" in the Assignments on Canvas.
