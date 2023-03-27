# Lab 10: Logistic Regression

In this lab you will build a logistic regression model and evaluate the performance of your model.


```python
# Run this cell to set up your notebook
import numpy as np
import pandas as pd
import sklearn
import sklearn.datasets
import sklearn.linear_model
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
#import cufflinks as cf


%matplotlib inline
sns.set()
sns.set_context("talk")
#py.init_notebook_mode(connected=False)
#cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
```

In this lab we will be working with the breast cancer dataset. This dataset can be loaded using the `sklearn.datasets.load_breast_cancer()` method.  


```python
data = sklearn.datasets.load_breast_cancer()
# data is actually a dictionnary
print(data.keys())
print(data.DESCR)
```

The data format is not a `pandas.DataFrame` so we will need to do some preprocessing to create a new DataFrame from it.


```python
df = pd.DataFrame(data.data, columns=data.feature_names)
df.head()
```

Let us try to fit a simple model with only one feature.


```python
# Define our features/target
X = df[["mean radius"]]
# Target data['target'] = 0 is malignant, 1 is benign
Y = (data.target == 0)

```


```python
# Create a 75-25 train-test split
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(X,Y, test_size=0.25, random_state=42)

print(f"Training Data Size: {len(x_train)}")
print(f"Test Data Size: {len(x_test)}")
```

### Question 1

Let's first fit a logistic regression model using the training set. 

For this problem, we will use the existing `LogisticRegression` implementation in sklearn.

Fill in the code below to compute the training and testing accuracy, defined as:

$$
\text{Training Accuracy} = \frac{1}{n_{train\_set}} \sum_{i \in {train\_set}} {\mathbb{1}_{y_i == \hat{y_i}}}
$$

$$
\text{Testing Accuracy} = \frac{1}{n_{test\_set}} \sum_{i \in {test\_set}} {\mathbb{1}_{y_i == \hat{y_i}}}
$$

where $\hat{y_i}$ is the prediction of our model, $y_i$ the true value, and $\mathbb{1}_{y_i == \hat{y_i}}$ an indicator function where $\mathbb{1}_{y_i == \hat{y_i}} = 1$ if ${y_i} = \hat{y_i}$, and $\mathbb{1}_{y_i == \hat{y_i}} = 0$ if ${y_i} \neq \hat{y_i}$

<!--
BEGIN QUESTION
name: q1
-->


```python
lr = sklearn.linear_model.LogisticRegression(fit_intercept=True, solver = 'lbfgs')

lr.fit(x_train,y_train) 
train_accuracy = ...
test_accuracy = ...

print(f"Train accuracy: {train_accuracy:.4f}")
print(f"Test accuracy: {test_accuracy:.4f}")
```

### Question 2
It seems we can get a very high test accuracy. How about precision and recall?  
- Precision (also called positive predictive value) is the fraction of true positives among the total number of data points predicted as positive.  
- Recall (also known as sensitivity) is the fraction of true positives among the total number of data points with positive labels.

Precision measures the ability of our classifier to not predict negative samples as positive, while recall is the ability of the classifier to find all the positive samples.

To understand the link between precision and recall, it's useful to create a confusion matrix of our predictions. Luckily, `sklearn.metrics` provides us with such a function!


```python
from sklearn.metrics import confusion_matrix

cnf_matrix = confusion_matrix(y_test, lr.predict(x_test))

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import itertools
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
class_names = ['False', 'True']
# Plot non-normalized confusion matrix
plt.figure()
plt.grid(False)
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plt.grid(False)
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')
```

Mathematically, Precision and Recall are defined as:
$$
\text{Precision} = \frac{n_{true\_positives}}{n_{true\_positives} + n_{false\_positives}}
$$

$$
\text{Recall} = \frac{n_{true\_positives}}{n_{true\_positives} + n_{false\_negatives}}
$$

Below is a graphical illustration of precision and recall:
![precision_recall](precision_recall.png)

Now let's compute the precision and recall for the test set using the model we got from Question 1.  

**Do not** use `sklearn.metrics` for this computation.

<!--
BEGIN QUESTION
name: q2
-->


```python
y_pred = lr.predict(x_test) 

...

precision = ...
recall = ...

print(f'precision = {precision:.4f}')
print(f'recall = {recall:.4f}')
```

Our precision is fairly high while our recall is a bit lower. Why might we observe these results? Please consider the following plots, which display the distribution of the target variable in the training and testing sets. 


```python
fig, axes = plt.subplots(1, 2)
sns.countplot(x=y_train, ax=axes[0]);
sns.countplot(x=y_test, ax=axes[1]);

axes[0].set_title('Train')
axes[1].set_title('Test')
plt.tight_layout();
```

_Type your answer here, replacing this text._

## Submission

To submit your assignment, please download your notebook as a .ipynb file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as... > Notebook (.ipynb) or HTML (.html). Then, upload both files under "Lab #10".

 
