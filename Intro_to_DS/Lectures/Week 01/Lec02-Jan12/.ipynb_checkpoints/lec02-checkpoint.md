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
```


```python
a
```


```python
a * 3
```


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


```python
a = 10
```


```python
total
```


```python
total = a + b
```


```python
total
```


```python
'total'
```


```python
c * a
```


```python
a = 7
a
```

### Why Names?


```python
hours_per_week = 40
weeks_per_year = 52
```


```python
hours_per_year = hours_per_week * weeks_per_year
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


```python
yearly_wages = hours_per_year * hk_hourly_minimum_wage
yearly_wages
```


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


```python
abs(1 - 3)
```


```python
day_temp = 52
night_temp = 47
abs(night_temp - day_temp)
```


```python
min(14, 15)
```


```python
round(123.456)
```


```python
round(123.456, 1)
```


```python
round(123.456, 2)
```


```python
round(123.456, 0)
```


```python
round(123.456, ndigits=1)
```


```python
ndigits
```

## Tables ##
Documentation of Table: http://data8.org/datascience/tables.html


```python
cones = Table.read_table('cones.csv')
cones
```


```python
cones.show(3)
```


```python
cones.show()
```


```python
cones.select('Flavor')
```


```python
cones.select('Flavor', 'Price')
```


```python
cones.select(Flavor, 'Price')
```


```python
cones.drop('Price')
```


```python
cones
```


```python
cones_without_price = cones.drop('Price')
cones_without_price
```


```python
cones.where('Flavor', 'chocolate')
```


```python
cones.sort('Price')
```


```python
cones.sort('Price', descending=True)
```


```python
cones.sort('Price', descending=False)
```


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


```python
skyscrapers.where('city', 'Los Angeles')
```


```python
skyscrapers.where('name', 'Empire State Building')
```


```python
skyscrapers.where('city', 'New York City').sort('completed')
```


```python
skyscrapers.where('city', 'New York City').sort('completed', descending=True)
```


```python
skyscrapers.where('city', 'New York City').sort('completed', descending=True).show(3)
```

## Numbers ##


```python
30
```


```python
10 * 3    # int
```


```python
10 / 3    # float
```


```python
10 / 2
```


```python
10 ** 3
```


```python
10 ** 0.5
```


```python
1234567 ** 890
```


```python
10 / 3
```


```python
75892745.215489247589274985712
```


```python
75892745.215489247589274985712 - 75892745.21548925
```


```python
(13 ** 0.5) ** 2
```


```python
int(10 / 5)
```


```python
int(10 / 4)
```


```python
float(3)
```


```python
6 / 4
```


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


```python
x = 5
```


```python
2x
```


```python
2 * x
```


```python
round(3.7)
```


```python
round(2.00000052345324, 2)
```


```python
10 * 3.0
```

## Strings ##


```python
'Flavor'
```


```python
Flavor
```


```python
"Flavor"
```


```python
"Don't always use single quotes"
```


```python
'Don't always use single quotes'
```


```python
'straw' + 'berry' # concatenation
```


```python
'Chris' + 'Paul' # spaces aren't added for you
```


```python
'Chris' + ' ' + 'Paul'
```


```python
'ha' * 100
```


```python
'ha' * 5.5
```


```python
'ha' + 10
```


```python
int('3')
```




    3




```python
int('3.0')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-2-90ae876cd031> in <module>
    ----> 1 int('3.0')
    

    ValueError: invalid literal for int() with base 10: '3.0'



```python
float('3.0')
```




    3.0




```python
str(3)
```


```python
str(4.5)
```

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


```python
type(True)
```


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


