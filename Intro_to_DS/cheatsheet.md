# Data Science Cheat sheet

1. **Introduction of Python for data science**
   - Tables
   - Data types
   - Charts
   - Histograms
   - Functions
   - Groups
   - Joins
   - Iteration
2. **Statistics**
   - Chance
   - Sampling
   - Models
   - Distributions
   - A/B testing
   - Confidence intervals
   - Central limit theorem
   - Correlation
   - P-values
3. **Machine learning**
   - Linear regression
   - Multiple linear regression
   - Regression diagnostics
   - Feature engineering
   - Logistic regression
   - Classification
   - Clustering
   - Decision tree


# Cheatsheet

## 1. Introduction of Python for data science
### 1.1 Tables
- `Table.read_table(filename)`: reads a table from a spreadsheet
- `Table()`: creates an empty table

### 1.2 Data types
- Arrays
- Ranges
- Lists

### 1.3 Charts
- Line graph: `plot`
- Scatter plot: `scatter`
- Bar chart: distribution of categorical data
- Histogram: distribution of numerical data

### 1.4 Histograms
- Histogram: distribution of numerical data

### 1.5 Functions
- Apply method: `table_name.apply(function, 'column_label')`
- Group method: `t.group(column)` or `t.group(column, function)`

### 1.6 Groups
- Group by one column: `t.group(column)` or `t.group(column, function)`
- Group by multiple columns: `t.group([column, …])` or `t.group([column, …], function)`

### 1.7 Joins
- `t.join(column, other_table, other_table_column)`

### 1.8 Iteration
- Random selection: `np.random.choice(some_array, sample_size)`

## 2. Statistics
### 2.1 Chance
- Law of averages

### 2.2 Sampling
- Probability samples
- Sample of convenience

### 2.3 Models
- Assessing models
- Summary of the method

### 2.4 Distributions
- Probability distribution
- Empirical distribution

### 2.5 A/B testing
- Comparing empirical distribution of simulated test statistic values to actual test statistic from the sample in the study

### 2.6 Confidence intervals
- Interval estimate of a population parameter

### 2.7 Central limit theorem
- Distribution of the sample mean approaches a normal distribution as sample size increases

### 2.8 Correlation
- Scatter plot: relation between numerical variables

### 2.9 P-values
- Probability of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true

## 3. Machine learning
### 3.1 Linear regression
- Model for predicting a continuous dependent variable based on one or more independent variables

### 3.2 Multiple linear regression
- Model for predicting a continuous dependent variable based on multiple independent variables

### 3.3 Regression diagnostics
- Techniques to evaluate the quality of a regression model

### 3.4 Feature engineering
- Process of selecting, transforming, or creating features to improve the performance of a machine learning model

### 3.5 Logistic regression
- Model for predicting the probability of a binary outcome based on one or more independent variables

### 3.6 Classification
- Categorizing input data into one of several predefined classes or labels

### 3.7 Clustering
- Unsupervised learning technique for grouping similar data points based on their features

### 3.8 Decision tree
- Hierarchical model for making decisions or predictions based on the input features
