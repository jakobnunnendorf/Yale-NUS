```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

import warnings
warnings.simplefilter('ignore')
```

## Lecture 6 ##

## Comparison ##


```python
type(3 < 1)
```




    bool




```python
type(3 < 1)
```




    bool




```python
x = 3
y = 4
x == y
```




    False




```python
3 == 3
```




    True




```python
10 != 9
```




    True




```python
12 < x < 20
```




    False




```python
x > 12 and x < 20
```




    False




```python
10 < x-y < 13
```




    False




```python
True + False + True == 2
```




    True



## Comparisons with arrays


```python
pets = make_array('cat', 'cat', 'dog', 'cat', 'dog', 'rabbit')
```


```python
pets == 'cat'
```




    array([ True,  True, False,  True, False, False])




```python
pets == 'cat'
```




    array([ True,  True, False,  True, False, False])




```python
sum(make_array([ True,  True, False,  True, False, False]))
```




    array([1, 1, 0, 1, 0, 0])




```python
sum(make_array(True, True, False, True, False, False))
```




    3




```python
sum(pets == 'dog')
```




    2




```python
np.count_nonzero(pets == 'dog')
```




    2



### Appending Arrays


```python
first = np.arange(4)
second = np.arange(10, 17)
```


```python
first
```




    array([0, 1, 2, 3])




```python
np.append(first, second)
```




    array([ 0,  1,  2,  3, 10, 11, 12, 13, 14, 15, 16])




```python
first = np.append(first,second)
first
```




    array([ 0,  1,  2,  3, 10, 11, 12, 13, 14, 15, 16])




```python

```

## Simulation

Let's play a game: we each roll a die. 

If my number is bigger: you pay me a dollar.

If they're the same: we do nothing.

If your number is bigger: I pay you a dollar.

Steps:
1. Find a way to simulate two dice rolls.
2. Compute how much money we win/lose based on the result.
3. Do steps 1 and 2 10,000 times.

### Conditional Statements


```python
# Work in progress
def one_round(my_roll, your_roll):
    if my_roll > your_roll:
        return 1
    elif my_roll < your_roll:
        return -1
    elif my_roll == your_roll:
        return 0
```


```python
one_round(4, 3)
```




    1




```python
one_round(3,4)
```




    -1




```python
one_round(2, 6)
```

### Random Selection


```python
mornings = make_array('wake up', 'sleep in')
mornings
```




    array(['wake up', 'sleep in'], dtype='<U8')




```python
np.random.choice(mornings)
```




    'sleep in'




```python
np.random.choice(mornings)
```




    'sleep in'




```python
np.random.choice(mornings)
```




    'wake up'




```python
np.random.choice(mornings, 7)
```




    array(['wake up', 'sleep in', 'wake up', 'sleep in', 'wake up',
           'sleep in', 'wake up'], dtype='<U8')




```python
sum(np.random.choice(mornings, 7) == 'wake up')
```




    1




```python
sum(np.random.choice(mornings, 7) == 'sleep in')
```


```python
die_faces = np.arange(1, 7)

die_faces
```




    array([1, 2, 3, 4, 5, 6])




```python
np.random.choice(die_faces)
```




    3




```python
def simulate_one_round():
    my_roll = np.random.choice(die_faces)
    your_roll = np.random.choice(die_faces)
    return one_round(my_roll, your_roll)
```


```python
simulate_one_round()
```




    1



### Repeated Betting ###


```python
results = make_array()
```


```python
results = np.append(results, simulate_one_round())
results
```




    array([ 1., -1.,  1., -1.,  0., -1., -1., -1., -1.,  1.,  1., -1., -1.,
            0., -1.,  1.,  1.,  1., -1.,  0.,  0.,  1.,  1.,  1.,  0.,  0.,
           -1., -1.,  1., -1., -1., -1.,  0.,  1.,  1.,  1.,  1.,  1.,  1.,
            0.,  1.,  1.,  0., -1.])



## `For` Statements (for loops!)


```python
game_outcomes = make_array()

for i in np.arange(5):
    game_outcomes = np.append(game_outcomes, simulate_one_round())
    
game_outcomes
```




    array([-1.,  1.,  0.,  1., -1.])




```python
game_outcomes = make_array()

for i in np.arange(10000):
    game_outcomes = np.append(game_outcomes, simulate_one_round())
    
game_outcomes
```




    array([-1.,  1.,  1., ..., -1.,  0.,  0.])




```python
results = Table().with_column('My winnings', game_outcomes)
```


```python
results
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>My winnings</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0          </td>
        </tr>
        <tr>
            <td>0          </td>
        </tr>
        <tr>
            <td>0          </td>
        </tr>
        <tr>
            <td>-1         </td>
        </tr>
        <tr>
            <td>-1         </td>
        </tr>
        <tr>
            <td>0          </td>
        </tr>
        <tr>
            <td>-1         </td>
        </tr>
        <tr>
            <td>-1         </td>
        </tr>
        <tr>
            <td>-1         </td>
        </tr>
        <tr>
            <td>-1         </td>
        </tr>
    </tbody>
</table>
<p>... (9990 rows omitted)</p>




```python
results.group('My winnings').barh('My winnings')
```


    
![png](Lec6-demo_files/Lec6-demo_54_0.png)
    


### Another example: simulating heads in 100 coin tosses


```python
coin = make_array('heads', 'tails')
coin
```




    array(['heads', 'tails'], dtype='<U5')




```python
np.random.choice(coin,100)
```




    array(['tails', 'heads', 'tails', 'tails', 'tails', 'heads', 'tails',
           'heads', 'tails', 'heads', 'tails', 'tails', 'heads', 'heads',
           'tails', 'heads', 'heads', 'tails', 'tails', 'tails', 'tails',
           'heads', 'heads', 'heads', 'heads', 'tails', 'tails', 'heads',
           'heads', 'tails', 'tails', 'tails', 'heads', 'tails', 'heads',
           'tails', 'heads', 'heads', 'tails', 'tails', 'heads', 'heads',
           'tails', 'heads', 'tails', 'heads', 'heads', 'tails', 'heads',
           'heads', 'tails', 'heads', 'heads', 'tails', 'tails', 'heads',
           'tails', 'heads', 'heads', 'tails', 'tails', 'heads', 'heads',
           'tails', 'tails', 'heads', 'heads', 'heads', 'tails', 'tails',
           'tails', 'heads', 'tails', 'tails', 'tails', 'heads', 'tails',
           'heads', 'tails', 'tails', 'tails', 'tails', 'tails', 'tails',
           'heads', 'tails', 'heads', 'heads', 'heads', 'tails', 'heads',
           'heads', 'tails', 'heads', 'tails', 'tails', 'heads', 'heads',
           'tails', 'heads'], dtype='<U5')




```python

```


```python
sum(np.random.choice(coin, 100) == 'heads')
```




    46




```python
# Simulate one outcome

def num_heads():
    return sum(np.random.choice(coin, 100) == 'heads')
```


```python
# Decide how many times you want to repeat the experiment

repetitions = 10000
```


```python
# Simulate that many outcomes

outcomes = make_array()

for i in np.arange(repetitions):
    outcomes = np.append(outcomes, num_heads())
```


```python
heads = Table().with_column('Heads', outcomes)
heads.hist(bins = np.arange(29.5, 70.6))
```


    
![png](Lec6-demo_files/Lec6-demo_63_0.png)
    


## Probability

Counting rule

Multiplication rule

Addition rule

Complement rule
