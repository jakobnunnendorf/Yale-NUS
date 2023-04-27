# Lab 3: Tables, Functions and Visualizations

Welcome to lab 3!  

This week, we will focus on manipulating tables, functions, the table method `apply` and histogram plotting. 


```python
import numpy as np
from datascience import *

# These lines set up graphing capabilities.
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
```

## 1. Introduction

For a collection of things in the world, an array is useful for describing a single attribute of each thing. For example, among the collection of US States, an array could describe the land area of each. Tables extend this idea by describing multiple attributes for each element of a collection.

In most data science applications, we have data about many entities, but we also have several kinds of data about each entity.

For example, in the cell below we have two arrays. The first one contains the world population in each year (estimated by the US Census Bureau), and the second contains the years themselves. These elements are in order, so the year and the world population for that year have the same index in their corresponding arrays.


```python
population_amounts = Table.read_table("world_population.csv").column("Population")
years = np.arange(1950, 2016)
print("Population column:", population_amounts)
print("Years column:", years)
```

    Population column: [2557628654 2594939877 2636772306 2682053389 2730228104 2782098943
     2835299673 2891349717 2948137248 3000716593 3043001508 3083966929
     3140093217 3209827882 3281201306 3350425793 3420677923 3490333715
     3562313822 3637159050 3712697742 3790326948 3866568653 3942096442
     4016608813 4089083233 4160185010 4232084578 4304105753 4379013942
     4451362735 4534410125 4614566561 4695736743 4774569391 4856462699
     4940571232 5027200492 5114557167 5201440110 5288955934 5371585922
     5456136278 5538268316 5618682132 5699202985 5779440593 5857972543
     5935213248 6012074922 6088571383 6165219247 6242016348 6318590956
     6395699509 6473044732 6551263534 6629913759 6709049780 6788214394
     6866332358 6944055583 7022349283 7101027895 7178722893 7256490011]
    Years column: [1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964
     1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979
     1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994
     1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009
     2010 2011 2012 2013 2014 2015]


Suppose we want to answer this question:

> When did world population cross 6 billion?

You could technically answer this question just from staring at the arrays, but it's a bit convoluted, since you would have to count the position where the population first crossed 6 billion, then find the corresponding element in the years array. In cases like these, it might be easier to put the data into a *`Table`*, a 2-dimensional type of dataset. 

The expression below:

- creates an empty table using the expression `Table()`,
- adds two columns by calling `with_columns` with four arguments,
- assignes the result to the name `population`, and finally
- evaluates `population` so that we can see the table.

The strings `"Year"` and `"Population"` are column labels that we have chosen. Ther names `population_amounts` and `years` were assigned above to two arrays of the same length. The function `with_columns` (you can find the documentation [here](http://data8.org/datascience/tables.html)) takes in alternating strings (to represent column labels) and arrays (representing the data in those columns), which are all separated by commas.


```python
population = Table().with_columns(
    "Population", population_amounts,
    "Year", years
)
population
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Population</th> <th>Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2557628654</td> <td>1950</td>
        </tr>
        <tr>
            <td>2594939877</td> <td>1951</td>
        </tr>
        <tr>
            <td>2636772306</td> <td>1952</td>
        </tr>
        <tr>
            <td>2682053389</td> <td>1953</td>
        </tr>
        <tr>
            <td>2730228104</td> <td>1954</td>
        </tr>
        <tr>
            <td>2782098943</td> <td>1955</td>
        </tr>
        <tr>
            <td>2835299673</td> <td>1956</td>
        </tr>
        <tr>
            <td>2891349717</td> <td>1957</td>
        </tr>
        <tr>
            <td>2948137248</td> <td>1958</td>
        </tr>
        <tr>
            <td>3000716593</td> <td>1959</td>
        </tr>
    </tbody>
</table>
<p>... (56 rows omitted)</p>



Now the data are all together in a single table! It's much easier to parse this data--if you need to know what the population was in 1959, for example, you can tell from a single glance. We'll revisit this table later.

## 2. Creating Tables

**Question 2.1.** <br/> In the cell below, we've created 2 arrays. Using the steps above, assign `top_10_movies` to a table that has two columns called "Rating" and "Name", in that order, which hold `top_10_movie_ratings` and `top_10_movie_names` respectively.


```python
top_10_movie_ratings = make_array(9.2, 9.2, 9., 8.9, 8.9, 8.9, 8.9, 8.9, 8.9, 8.8)
top_10_movie_names = make_array(
        'The Shawshank Redemption (1994)',
        'The Godfather (1972)',
        'The Godfather: Part II (1974)',
        'Pulp Fiction (1994)',
        "Schindler's List (1993)",
        'The Lord of the Rings: The Return of the King (2003)',
        '12 Angry Men (1957)',
        'The Dark Knight (2008)',
        'Il buono, il brutto, il cattivo (1966)',
        'The Lord of the Rings: The Fellowship of the Ring (2001)')

top_10_movies = Table().with_columns(
        "Rating", top_10_movie_ratings,
        "Name", top_10_movie_names
)

top_10_movies
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Rating</th> <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>9.2   </td> <td>The Shawshank Redemption (1994)                         </td>
        </tr>
        <tr>
            <td>9.2   </td> <td>The Godfather (1972)                                    </td>
        </tr>
        <tr>
            <td>9     </td> <td>The Godfather: Part II (1974)                           </td>
        </tr>
        <tr>
            <td>8.9   </td> <td>Pulp Fiction (1994)                                     </td>
        </tr>
        <tr>
            <td>8.9   </td> <td>Schindler's List (1993)                                 </td>
        </tr>
        <tr>
            <td>8.9   </td> <td>The Lord of the Rings: The Return of the King (2003)    </td>
        </tr>
        <tr>
            <td>8.9   </td> <td>12 Angry Men (1957)                                     </td>
        </tr>
        <tr>
            <td>8.9   </td> <td>The Dark Knight (2008)                                  </td>
        </tr>
        <tr>
            <td>8.9   </td> <td>Il buono, il brutto, il cattivo (1966)                  </td>
        </tr>
        <tr>
            <td>8.8   </td> <td>The Lord of the Rings: The Fellowship of the Ring (2001)</td>
        </tr>
    </tbody>
</table>



#### Loading a table from a file
In most cases, we aren't going to go through the trouble of typing in all the data manually. Instead, we can use our `Table` functions.

`Table().read_table` takes one argument, a path to a data file (a string) and returns a table.  There are many formats for data files, but CSV ("comma-separated values") is the most common. 

**Question 2.2.** <br/>The file `imdb.csv` contains a table of information about the 250 highest-rated movies on IMDb.  Load it as a table called `imdb`. In our case, `imdb.csv` is located in the same folder as the notebook, so you only need to input the name of the file instead of the full path.


```python
imdb = Table().read_table("imdb.csv")
imdb
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Votes</th> <th>Rating</th> <th>Title</th> <th>Year</th> <th>Decade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>88355 </td> <td>8.4   </td> <td>M                    </td> <td>1931</td> <td>1930  </td>
        </tr>
        <tr>
            <td>132823</td> <td>8.3   </td> <td>Singin' in the Rain  </td> <td>1952</td> <td>1950  </td>
        </tr>
        <tr>
            <td>74178 </td> <td>8.3   </td> <td>All About Eve        </td> <td>1950</td> <td>1950  </td>
        </tr>
        <tr>
            <td>635139</td> <td>8.6   </td> <td>Léon                 </td> <td>1994</td> <td>1990  </td>
        </tr>
        <tr>
            <td>145514</td> <td>8.2   </td> <td>The Elephant Man     </td> <td>1980</td> <td>1980  </td>
        </tr>
        <tr>
            <td>425461</td> <td>8.3   </td> <td>Full Metal Jacket    </td> <td>1987</td> <td>1980  </td>
        </tr>
        <tr>
            <td>441174</td> <td>8.1   </td> <td>Gone Girl            </td> <td>2014</td> <td>2010  </td>
        </tr>
        <tr>
            <td>850601</td> <td>8.3   </td> <td>Batman Begins        </td> <td>2005</td> <td>2000  </td>
        </tr>
        <tr>
            <td>37664 </td> <td>8.2   </td> <td>Judgment at Nuremberg</td> <td>1961</td> <td>1960  </td>
        </tr>
        <tr>
            <td>46987 </td> <td>8     </td> <td>Relatos salvajes     </td> <td>2014</td> <td>2010  </td>
        </tr>
    </tbody>
</table>
<p>... (240 rows omitted)</p>



Notice the part about "... (240 rows omitted)."  This table is big enough that only a few of its rows are displayed, but the others are still there.  10 are shown, so there are 250 movies total.

Where did `imdb.csv` come from? Take a look at [this lab's folder](./). You should see a file called `imdb.csv`.

Open up the `imdb.csv` file in that folder and look at the format. What do you notice? The `.csv` filename ending says that this file is in the [CSV (comma-separated value) format](http://edoceo.com/utilitas/csv-file-format).

## 3. Using lists

A *list* is another Python sequence type, similar to an array. It's different than an array because the values it contains can all have different types. Furthermore, the properties of lists and arrays differ in their use, which is why we want to specify when to use either one.

A single list can contain `int` values, `float` values, and strings. Elements in a list can even be other lists! A list is created by giving a name to the list of values enclosed in square brackets and separated by commas. For example, `values_with_different_types = ['data', 8, 8.1]`

One example of the difference in list and array properties is below. Run these cells. 


```python
an_array = make_array(1, 2, 3, 4)
an_array * 2
```




    array([2, 4, 6, 8])




```python
a_list = [1, 2, 3, 4]
a_list * 2
```




    [1, 2, 3, 4, 1, 2, 3, 4]



Lists can be useful when working with tables because they can describe the contents of one row in a table, which often  corresponds to a sequence of values with different types. A list of lists can be used to describe multiple rows.

Each column in a table is a collection of values with the same type (an array). If you create a table column from a list, it will automatically be converted to an array. A row, on the ther hand, mixes types.

Here's a table from Chapter 5. (Run the cell below.)


```python
# Run this cell to recreate the table
flowers = Table().with_columns(
    'Number of petals', make_array(8, 34, 5),
    'Name', make_array('lotus', 'sunflower', 'rose')
)
flowers
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Number of petals</th> <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8               </td> <td>lotus    </td>
        </tr>
        <tr>
            <td>34              </td> <td>sunflower</td>
        </tr>
        <tr>
            <td>5               </td> <td>rose     </td>
        </tr>
    </tbody>
</table>



**Question 3.1.** <br/>Create a list that describes a new fourth row of this table. The details can be whatever you want, but the list must contain two values in this order: the number of petals (an `int` value) and the name of the flower (a string). For example, your flower could be "pondweed"! (A flower with zero petals)


```python
my_flower = [17, 'blaue blume']
my_flower
```




    [17, 'blaue blume']



**Question 3.2.** <br/>`my_flower` fits right in to the table from chapter 5. Complete the cell below to create a **table of seven flowers** that includes your flower as the fourth row followed by `other_flowers`. You can use `with_row` to create a new table with one extra row by passing a list of values and `with_rows` to create a table with multiple extra rows by passing a list of lists of values.

*Hint:* Don't forget to use the variables you define! We can build off of tables we've already created by simply using the variable name of the other table. 


```python
# Use the method .with_row(...) to create a new table that includes my_flower 

four_flowers = flowers.with_row(my_flower)
four_flowers

# Use the method .with_rows(...) to create a table that 
# includes four_flowers followed by other_flowers

other_flowers = [[10, 'lavender'], [3, 'birds of paradise'], [6, 'tulip']]

seven_flowers = four_flowers.with_rows(other_flowers)
seven_flowers
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Number of petals</th> <th>Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>8               </td> <td>lotus            </td>
        </tr>
        <tr>
            <td>34              </td> <td>sunflower        </td>
        </tr>
        <tr>
            <td>5               </td> <td>rose             </td>
        </tr>
        <tr>
            <td>17              </td> <td>blaue blume      </td>
        </tr>
        <tr>
            <td>10              </td> <td>lavender         </td>
        </tr>
        <tr>
            <td>3               </td> <td>birds of paradise</td>
        </tr>
        <tr>
            <td>6               </td> <td>tulip            </td>
        </tr>
    </tbody>
</table>



## 4. Analyzing datasets
With just a few table methods, we can answer some interesting questions about the IMDb dataset.

If we want just the ratings of the movies, we can get an array that contains the data in that column:


```python
imdb.column("Rating")
```




    array([ 8.4,  8.3,  8.3,  8.6,  8.2,  8.3,  8.1,  8.3,  8.2,  8. ,  8.1,
            8.2,  8.3,  8.3,  8.1,  8.4,  8.5,  8.2,  8.1,  8.4,  8.1,  8.1,
            9.2,  8. ,  8.2,  8.1,  8.2,  8.5,  8. ,  8.3,  8.1,  8. ,  8. ,
            8.3,  8.1,  8. ,  8. ,  8.3,  8.4,  8.1,  8.1,  8.5,  8.5,  8. ,
            8.3,  8.1,  8. ,  8.6,  8.5,  8.3,  8.3,  8. ,  8.2,  9.2,  8.2,
            8.5,  8. ,  8.9,  8.4,  8.2,  8.1,  8.3,  8.1,  8.1,  8.1,  8.3,
            8.2,  8.3,  8.7,  8.3,  8.6,  8. ,  8.1,  8.2,  8.5,  8.3,  8.9,
            8. ,  8.6,  8.3,  8.1,  8.7,  8.4,  8.1,  8.4,  8. ,  8.5,  8.8,
            8.2,  8.2,  8.5,  9. ,  8. ,  8. ,  8.3,  8.4,  8.6,  8.5,  8.7,
            8.4,  8.1,  8.1,  8.1,  8.7,  8.4,  8.9,  8.1,  8.2,  8. ,  8.5,
            8.5,  8. ,  8. ,  8.4,  8.1,  8.1,  8. ,  8. ,  8.3,  8.1,  8. ,
            8.3,  8. ,  8. ,  8. ,  8. ,  8. ,  8. ,  8. ,  8.7,  8.3,  8. ,
            8. ,  8.5,  8. ,  8.1,  8.1,  8.1,  8.3,  8.2,  8.3,  8.9,  8.2,
            8.2,  8. ,  8.3,  8.2,  8.9,  8.5,  8.5,  8.1,  8.1,  8.5,  8.3,
            8. ,  8.2,  8.7,  8.3,  8.5,  8.1,  8.3,  8.2,  8.4,  8.1,  8.1,
            8.1,  8. ,  8.2,  8. ,  8.6,  8.3,  8.2,  8. ,  8.3,  8. ,  8.2,
            8. ,  8.2,  8.8,  8.1,  8. ,  8.1,  8. ,  8.2,  8.5,  8.1,  8.4,
            8.1,  8.1,  8.7,  8.2,  8. ,  8. ,  8. ,  8.3,  8.4,  8. ,  8.5,
            8.1,  8.1,  8.2,  8.2,  8.4,  8.3,  8.6,  8.2,  8. ,  8.1,  8.2,
            8.1,  8.3,  8.4,  8.5,  8.6,  8. ,  8.3,  8.5,  8.5,  8.3,  8.5,
            8.4,  8. ,  8.1,  8.7,  8.9,  8.3,  8.1,  8.1,  8. ,  8.2,  8.4,
            8.4,  8.1,  8.3,  8.4,  8.2,  8.5,  8. ,  8.2,  8.1,  8.4,  8.1,
            8.6,  8.4,  8.1,  8.7,  8.1,  8.2,  8.1,  8.3])



The value of that expression is an array, exactly the same kind of thing you'd get if you typed in `make_array(8.4, 8.3, 8.3, [etc])`.

**Question 4.1.** <br/> Using a table array, find the rating of the highest-rated movie in the dataset.

*Hint:* Think back to the functions you've learned about for working with arrays of numbers.  Ask for help if you can't remember one that's useful for this.


```python
highest_rating = max(imdb.column("Rating"))
highest_rating
```




    9.1999999999999993



That's not very useful, though.  You'd probably want to know the *name* of the movie whose rating you found!  To do that, we can sort the entire table by rating, which ensures that the ratings and titles will stay together. Note that calling sort creates a copy of the table and leaves the original table unsorted.


```python
imdb.sort("Rating")
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Votes</th> <th>Rating</th> <th>Title</th> <th>Year</th> <th>Decade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>46987 </td> <td>8     </td> <td>Relatos salvajes                    </td> <td>2014</td> <td>2010  </td>
        </tr>
        <tr>
            <td>55382 </td> <td>8     </td> <td>Bom yeoreum gaeul gyeoul geurigo bom</td> <td>2003</td> <td>2000  </td>
        </tr>
        <tr>
            <td>32385 </td> <td>8     </td> <td>La battaglia di Algeri              </td> <td>1966</td> <td>1960  </td>
        </tr>
        <tr>
            <td>364225</td> <td>8     </td> <td>Jaws                                </td> <td>1975</td> <td>1970  </td>
        </tr>
        <tr>
            <td>158867</td> <td>8     </td> <td>Before Sunrise                      </td> <td>1995</td> <td>1990  </td>
        </tr>
        <tr>
            <td>56671 </td> <td>8     </td> <td>The Killing                         </td> <td>1956</td> <td>1950  </td>
        </tr>
        <tr>
            <td>87591 </td> <td>8     </td> <td>Papillon                            </td> <td>1973</td> <td>1970  </td>
        </tr>
        <tr>
            <td>43090 </td> <td>8     </td> <td>Paris, Texas (1984)                 </td> <td>1984</td> <td>1980  </td>
        </tr>
        <tr>
            <td>427099</td> <td>8     </td> <td>X-Men: Days of Future Past          </td> <td>2014</td> <td>2010  </td>
        </tr>
        <tr>
            <td>87437 </td> <td>8     </td> <td>Roman Holiday                       </td> <td>1953</td> <td>1950  </td>
        </tr>
    </tbody>
</table>
<p>... (240 rows omitted)</p>



Well, that actually doesn't help much, either -- we sorted the movies from lowest -> highest ratings.  To look at the highest-rated movies, sort in reverse order:


```python
imdb.sort("Rating", descending=True)
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Votes</th> <th>Rating</th> <th>Title</th> <th>Year</th> <th>Decade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1027398</td> <td>9.2   </td> <td>The Godfather                                </td> <td>1972</td> <td>1970  </td>
        </tr>
        <tr>
            <td>1498733</td> <td>9.2   </td> <td>The Shawshank Redemption                     </td> <td>1994</td> <td>1990  </td>
        </tr>
        <tr>
            <td>692753 </td> <td>9     </td> <td>The Godfather: Part II                       </td> <td>1974</td> <td>1970  </td>
        </tr>
        <tr>
            <td>447875 </td> <td>8.9   </td> <td>Il buono, il brutto, il cattivo (1966)       </td> <td>1966</td> <td>1960  </td>
        </tr>
        <tr>
            <td>1473049</td> <td>8.9   </td> <td>The Dark Knight                              </td> <td>2008</td> <td>2000  </td>
        </tr>
        <tr>
            <td>384187 </td> <td>8.9   </td> <td>12 Angry Men                                 </td> <td>1957</td> <td>1950  </td>
        </tr>
        <tr>
            <td>1074146</td> <td>8.9   </td> <td>The Lord of the Rings: The Return of the King</td> <td>2003</td> <td>2000  </td>
        </tr>
        <tr>
            <td>761224 </td> <td>8.9   </td> <td>Schindler's List                             </td> <td>1993</td> <td>1990  </td>
        </tr>
        <tr>
            <td>1166532</td> <td>8.9   </td> <td>Pulp Fiction                                 </td> <td>1994</td> <td>1990  </td>
        </tr>
        <tr>
            <td>1177098</td> <td>8.8   </td> <td>Fight Club                                   </td> <td>1999</td> <td>1990  </td>
        </tr>
    </tbody>
</table>
<p>... (240 rows omitted)</p>



(The `descending=True` bit is called an *optional argument*. It has a default value of `False`, so when you explicitly tell the function `descending=True`, then the function will sort in descending order.)

So there are actually 2 highest-rated movies in the dataset: *The Shawshank Redemption* and *The Godfather*.

Some details about sort:

1. The first argument to `sort` is the name of a column to sort by.
2. If the column has strings in it, `sort` will sort alphabetically; if the column has numbers, it will sort numerically.
3. The value of `imdb.sort("Rating")` is a *copy of `imdb`*; the `imdb` table doesn't get modified. For example, if we called `imdb.sort("Rating")`, then running `imdb` by itself would still return the unsorted table.
4. Rows always stick together when a table is sorted.  It wouldn't make sense to sort just one column and leave the other columns alone.  For example, in this case, if we sorted just the "Rating" column, the movies would all end up with the wrong ratings.

**Question 4.2.** <br/>Create a version of `imdb` that's sorted chronologically, with the earliest movies first.  Call it `imdb_by_year`.


```python
imdb_by_year = imdb.sort("Year")
imdb_by_year
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Votes</th> <th>Rating</th> <th>Title</th> <th>Year</th> <th>Decade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>55784 </td> <td>8.3   </td> <td>The Kid                     </td> <td>1921</td> <td>1920  </td>
        </tr>
        <tr>
            <td>58506 </td> <td>8.2   </td> <td>The Gold Rush               </td> <td>1925</td> <td>1920  </td>
        </tr>
        <tr>
            <td>46332 </td> <td>8.2   </td> <td>The General                 </td> <td>1926</td> <td>1920  </td>
        </tr>
        <tr>
            <td>98794 </td> <td>8.3   </td> <td>Metropolis                  </td> <td>1927</td> <td>1920  </td>
        </tr>
        <tr>
            <td>88355 </td> <td>8.4   </td> <td>M                           </td> <td>1931</td> <td>1930  </td>
        </tr>
        <tr>
            <td>92375 </td> <td>8.5   </td> <td>City Lights                 </td> <td>1931</td> <td>1930  </td>
        </tr>
        <tr>
            <td>56842 </td> <td>8.1   </td> <td>It Happened One Night       </td> <td>1934</td> <td>1930  </td>
        </tr>
        <tr>
            <td>121668</td> <td>8.5   </td> <td>Modern Times                </td> <td>1936</td> <td>1930  </td>
        </tr>
        <tr>
            <td>69510 </td> <td>8.2   </td> <td>Mr. Smith Goes to Washington</td> <td>1939</td> <td>1930  </td>
        </tr>
        <tr>
            <td>259235</td> <td>8.1   </td> <td>The Wizard of Oz            </td> <td>1939</td> <td>1930  </td>
        </tr>
    </tbody>
</table>
<p>... (240 rows omitted)</p>



**Question 4.3.** <br/>What's the title of the earliest movie in the dataset?  You could just look this up from the output of the previous cell.  Instead, write Python code to find out.

*Hint:* Starting with `imdb_by_year`, extract the Title column to get an array, then use `item` to get its first item. Don't forget about indexing.


```python
earliest_movie_title = imdb_by_year.column("Title").item(0)
earliest_movie_title
```




    'The Kid'



## 5. Finding pieces of a dataset
Suppose you're interested in movies from the 1940s.  Sorting the table by year doesn't help you, because the 1940s are in the middle of the dataset.

Instead, we use the table method `where`.


```python
forties = imdb.where('Decade', are.equal_to(1940))
forties
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Votes</th> <th>Rating</th> <th>Title</th> <th>Year</th> <th>Decade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>55793 </td> <td>8.1   </td> <td>The Grapes of Wrath             </td> <td>1940</td> <td>1940  </td>
        </tr>
        <tr>
            <td>86715 </td> <td>8.3   </td> <td>Double Indemnity                </td> <td>1944</td> <td>1940  </td>
        </tr>
        <tr>
            <td>101754</td> <td>8.1   </td> <td>The Maltese Falcon              </td> <td>1941</td> <td>1940  </td>
        </tr>
        <tr>
            <td>71003 </td> <td>8.3   </td> <td>The Treasure of the Sierra Madre</td> <td>1948</td> <td>1940  </td>
        </tr>
        <tr>
            <td>35983 </td> <td>8.1   </td> <td>The Best Years of Our Lives     </td> <td>1946</td> <td>1940  </td>
        </tr>
        <tr>
            <td>81887 </td> <td>8.3   </td> <td>Ladri di biciclette             </td> <td>1948</td> <td>1940  </td>
        </tr>
        <tr>
            <td>66622 </td> <td>8     </td> <td>Notorious                       </td> <td>1946</td> <td>1940  </td>
        </tr>
        <tr>
            <td>350551</td> <td>8.5   </td> <td>Casablanca                      </td> <td>1942</td> <td>1940  </td>
        </tr>
        <tr>
            <td>59578 </td> <td>8     </td> <td>The Big Sleep                   </td> <td>1946</td> <td>1940  </td>
        </tr>
        <tr>
            <td>78216 </td> <td>8.2   </td> <td>Rebecca                         </td> <td>1940</td> <td>1940  </td>
        </tr>
    </tbody>
</table>
<p>... (4 rows omitted)</p>



Ignore the syntax for the moment.  Instead, try to read that line like this:

> Assign the name **`forties`** to a table whose rows are the rows in the **`imdb`** table **`where`** the **`'Decade'`**s **`are` `equal` `to` `1940`**.

**Question 5.1.** <br/>Compute the average rating of movies from the 1940s.


```python
average_rating_in_forties = np.average(forties.column('Rating'))
average_rating_in_forties
```




    8.2571428571428562



Now let's dive into the details a bit more.  `where` takes 2 arguments:

1. The name of a column.  `where` finds rows where that column's values meet some criterion.
2. Something that describes the criterion that the column needs to meet, called a predicate.

To create our predicate, we called the function `are.equal_to` with the value we wanted, 1940.  We'll see other predicates soon.

`where` returns a table that's a copy of the original table, but with only the rows that meet the given predicate.

**Question 5.2.**<br/> Create a table called `ninety_nine` containing the movies that came out in the year 1999.  Use `where`.


```python
ninety_nine = imdb.where('Year', are.equal_to(1999))
ninety_nine
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Votes</th> <th>Rating</th> <th>Title</th> <th>Year</th> <th>Decade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1177098</td> <td>8.8   </td> <td>Fight Club     </td> <td>1999</td> <td>1990  </td>
        </tr>
        <tr>
            <td>735056 </td> <td>8.4   </td> <td>American Beauty</td> <td>1999</td> <td>1990  </td>
        </tr>
        <tr>
            <td>630994 </td> <td>8.1   </td> <td>The Sixth Sense</td> <td>1999</td> <td>1990  </td>
        </tr>
        <tr>
            <td>1073043</td> <td>8.7   </td> <td>The Matrix     </td> <td>1999</td> <td>1990  </td>
        </tr>
        <tr>
            <td>672878 </td> <td>8.5   </td> <td>The Green Mile </td> <td>1999</td> <td>1990  </td>
        </tr>
    </tbody>
</table>



So far we've only been finding where a column is *exactly* equal to a certain value. However, there are many other predicates.  Here are a few:

|Predicate|Example|Result|
|-|-|-|
|`are.equal_to`|`are.equal_to(50)`|Find rows with values equal to 50|
|`are.not_equal_to`|`are.not_equal_to(50)`|Find rows with values not equal to 50|
|`are.above`|`are.above(50)`|Find rows with values above (and not equal to) 50|
|`are.above_or_equal_to`|`are.above_or_equal_to(50)`|Find rows with values above 50 or equal to 50|
|`are.below`|`are.below(50)`|Find rows with values below 50|
|`are.between`|`are.between(2, 10)`|Find rows with values above or equal to 2 and below 10|

The textbook section on selecting rows has more examples.


**Question 5.3.** <br/>Using `where` and one of the predicates from the table above, find all the movies with a rating higher than 8.5.  Put their data in a table called `really_highly_rated`.


```python
really_highly_rated = ninety_nine.where('Rating', are.above(8.5))
really_highly_rated
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Votes</th> <th>Rating</th> <th>Title</th> <th>Year</th> <th>Decade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1177098</td> <td>8.8   </td> <td>Fight Club</td> <td>1999</td> <td>1990  </td>
        </tr>
        <tr>
            <td>1073043</td> <td>8.7   </td> <td>The Matrix</td> <td>1999</td> <td>1990  </td>
        </tr>
    </tbody>
</table>



**Question 5.4.** <br/>Find the average rating for movies released in the 20th century (defined in this question as 1900-1999) and the average rating for movies released in the 21st century (as 2000-now) for the movies in `imdb`.

*Hint*: Think of the steps you need to do (take the average, find the ratings, find movies released in 20th/21st centuries), and try to put them in an order that makes sense.


```python
average_20th_century_rating = np.average(imdb.where('Year', are.below(2000)).column('Rating'))
average_21st_century_rating = np.average(imdb.where('Year', are.above_or_equal_to(2000)).column('Rating'))
print("Average 20th century rating:", average_20th_century_rating)
print("Average 21st century rating:", average_21st_century_rating)
```

    Average 20th century rating: 8.2783625731
    Average 21st century rating: 8.23797468354


The property `num_rows` tells you how many rows are in a table.  (A "property" is just a method that doesn't need to be called by adding parentheses.)


```python
num_movies_in_dataset = imdb.num_rows
num_movies_in_dataset
```




    250



**Question 5.5.** <br/>Use `num_rows` (and arithmetic) to find the *proportion* of movies in the dataset that were released in the 20th century (1900-1999), and the proportion from the 21st century (2000-now).

*Hint:* The *proportion* of movies released in the 20th century is the *number* of movies released in the 20th century, divided by the *total number* of movies.


```python
proportion_in_20th_century = imdb.where('Year', are.below(2000)).num_rows / num_movies_in_dataset
proportion_in_21st_century = imdb.where('Year', are.above_or_equal_to(2000)).num_rows / num_movies_in_dataset
print("Proportion in 20th century:", proportion_in_20th_century)
print("Proportion in 21st century:", proportion_in_21st_century)
```

    Proportion in 20th century: 0.684
    Proportion in 21st century: 0.316


**Question 5.6.** <br/>Here's a challenge: Find the number of movies that came out in *even* years.

*Hint:* The operator `%` computes the remainder when dividing by a number.  So `5 % 2` is 1 and `6 % 2` is 0.  A number is even if the remainder is 0 when you divide by 2.

*Hint 2:* `%` can be used on arrays, operating elementwise like `+` or `*`.  So `make_array(5, 6, 7) % 2` is `array([1, 0, 1])`.

*Hint 3:* Create a column called "Year Remainder" that's the remainder when each movie's release year is divided by 2.  Make a copy of `imdb` that includes that column.  Then use `where` to find rows where that new column is equal to 0.  Then use `num_rows` to count the number of such rows.


```python
num_even_year_movies = imdb.with_column('Year Remainder', imdb.column('Year') % 2).where('Year Remainder', are.equal_to(0)).num_rows
num_even_year_movies
```




    127



**Question 5.7.** <br/>Check out the `population` table from the introduction to this lab.  Compute the year when the world population first went above 6 billion.


```python
year_population_crossed_6_billion = population.where('Population', are.above(6e9)).column('Year').item(0)
year_population_crossed_6_billion
```




    1999



## 6. Miscellanea
There are a few more table methods you'll need to fill out your toolbox.  The first 3 have to do with manipulating the columns in a table.

The table `farmers_markets.csv` contains data on farmers' markets in the United States  (data collected [by the USDA]([dataset](https://apps.ams.usda.gov/FarmersMarketsExport/ExcelExport.aspx)) \).  Each row represents one such market.

**Question 6.1.** <br/>Load the dataset into a table.  Call it `farmers_markets`.


```python
farmers_markets = Table.read_table("farmers_markets.csv")
farmers_markets
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>FMID</th> <th>MarketName</th> <th>Website</th> <th>Facebook</th> <th>Twitter</th> <th>Youtube</th> <th>OtherMedia</th> <th>street</th> <th>city</th> <th>County</th> <th>State</th> <th>zip</th> <th>Season1Date</th> <th>Season1Time</th> <th>Season2Date</th> <th>Season2Time</th> <th>Season3Date</th> <th>Season3Time</th> <th>Season4Date</th> <th>Season4Time</th> <th>x</th> <th>y</th> <th>Location</th> <th>Credit</th> <th>WIC</th> <th>WICcash</th> <th>SFMNP</th> <th>SNAP</th> <th>Organic</th> <th>Bakedgoods</th> <th>Cheese</th> <th>Crafts</th> <th>Flowers</th> <th>Eggs</th> <th>Seafood</th> <th>Herbs</th> <th>Vegetables</th> <th>Honey</th> <th>Jams</th> <th>Maple</th> <th>Meat</th> <th>Nursery</th> <th>Nuts</th> <th>Plants</th> <th>Poultry</th> <th>Prepared</th> <th>Soap</th> <th>Trees</th> <th>Wine</th> <th>Coffee</th> <th>Beans</th> <th>Fruits</th> <th>Grains</th> <th>Juices</th> <th>Mushrooms</th> <th>PetFood</th> <th>Tofu</th> <th>WildHarvested</th> <th>updateTime</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1012063</td> <td> Caledonia Farmers Market Association - Danville</td> <td>https://sites.google.com/site/caledoniafarmersmarket/</td> <td>https://www.facebook.com/Danville.VT.Farmers.Market/        </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>nan                                                     </td> <td>Danville  </td> <td>Caledonia           </td> <td>Vermont             </td> <td>05828</td> <td>06/08/2016 to 10/12/2016</td> <td>Wed: 9:00 AM-1:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-72.1403</td> <td>44.411 </td> <td>nan                                                       </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>N   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>Y     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>Y     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>Y    </td> <td>N   </td> <td>Y     </td> <td>Y    </td> <td>Y     </td> <td>N     </td> <td>Y     </td> <td>N        </td> <td>Y      </td> <td>N   </td> <td>N            </td> <td>6/28/2016 12:10:09 PM</td>
        </tr>
        <tr>
            <td>1011871</td> <td> Stearns Homestead Farmers' Market              </td> <td>http://Stearnshomestead.com                          </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>6975 Ridge Road                                         </td> <td>Parma     </td> <td>Cuyahoga            </td> <td>Ohio                </td> <td>44130</td> <td>06/25/2016 to 10/01/2016</td> <td>Sat: 9:00 AM-1:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-81.7286</td> <td>41.3751</td> <td>nan                                                       </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y   </td> <td>-      </td> <td>Y         </td> <td>N     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>Y     </td> <td>N      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>Y      </td> <td>N   </td> <td>N            </td> <td>4/9/2016 8:05:17 PM  </td>
        </tr>
        <tr>
            <td>1011878</td> <td>100 Mile Market                                 </td> <td>http://www.pfcmarkets.com                            </td> <td>https://www.facebook.com/100MileMarket/?fref=ts             </td> <td>nan                                </td> <td>nan    </td> <td>https://www.instagram.com/100milemarket/                    </td> <td>507 Harrison St                                         </td> <td>Kalamazoo </td> <td>Kalamazoo           </td> <td>Michigan            </td> <td>49007</td> <td>05/04/2016 to 10/12/2016</td> <td>Wed: 3:00 PM-7:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-85.5749</td> <td>42.296 </td> <td>nan                                                       </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>Y         </td> <td>Y     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>Y     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/16/2016 12:37:56 PM</td>
        </tr>
        <tr>
            <td>1009364</td> <td>106 S. Main Street Farmers Market               </td> <td>http://thetownofsixmile.wordpress.com/               </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>106 S. Main Street                                      </td> <td>Six Mile  </td> <td>nan                 </td> <td>South Carolina      </td> <td>29682</td> <td>nan                     </td> <td>nan                                         </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-82.8187</td> <td>34.8042</td> <td>nan                                                       </td> <td>Y     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>N   </td> <td>-      </td> <td>N         </td> <td>N     </td> <td>N     </td> <td>N      </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>N         </td> <td>N    </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>N      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>N     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>2013                 </td>
        </tr>
        <tr>
            <td>1010691</td> <td>10th Steet Community Farmers Market             </td> <td>nan                                                  </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>http://agrimissouri.com/mo-grown/grodetail.php?type=mo-g ...</td> <td>10th Street and Poplar                                  </td> <td>Lamar     </td> <td>Barton              </td> <td>Missouri            </td> <td>64759</td> <td>04/02/2014 to 11/30/2014</td> <td>Wed: 3:00 PM-6:00 PM;Sat: 8:00 AM-1:00 PM;  </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-94.2746</td> <td>37.4956</td> <td>nan                                                       </td> <td>Y     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>N   </td> <td>-      </td> <td>Y         </td> <td>N     </td> <td>Y     </td> <td>N      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>Y     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>10/28/2014 9:49:46 AM</td>
        </tr>
        <tr>
            <td>1002454</td> <td>112st Madison Avenue                            </td> <td>nan                                                  </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>112th Madison Avenue                                    </td> <td>New York  </td> <td>New York            </td> <td>New York            </td> <td>10029</td> <td>July to November        </td> <td>Tue:8:00 am - 5:00 pm;Sat:8:00 am - 8:00 pm;</td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-73.9493</td> <td>40.7939</td> <td>Private business parking lot                              </td> <td>N     </td> <td>N   </td> <td>Y      </td> <td>Y    </td> <td>N   </td> <td>-      </td> <td>Y         </td> <td>N     </td> <td>Y     </td> <td>Y      </td> <td>N   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>N      </td> <td>Y   </td> <td>N     </td> <td>N      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>N     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>3/1/2012 10:38:22 AM </td>
        </tr>
        <tr>
            <td>1011100</td> <td>12 South Farmers Market                         </td> <td>http://www.12southfarmersmarket.com                  </td> <td>12_South_Farmers_Market                                     </td> <td>@12southfrmsmkt                    </td> <td>nan    </td> <td>@12southfrmsmkt                                             </td> <td>3000 Granny White Pike                                  </td> <td>Nashville </td> <td>Davidson            </td> <td>Tennessee           </td> <td>37204</td> <td>05/05/2015 to 10/27/2015</td> <td>Tue: 3:30 PM-6:30 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-86.7907</td> <td>36.1184</td> <td>nan                                                       </td> <td>Y     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>Y   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>Y     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>Y     </td> <td>Y        </td> <td>Y      </td> <td>N   </td> <td>N            </td> <td>5/1/2015 10:40:56 AM </td>
        </tr>
        <tr>
            <td>1009845</td> <td>125th Street Fresh Connect Farmers' Market      </td> <td>http://www.125thStreetFarmersMarket.com              </td> <td>https://www.facebook.com/125thStreetFarmersMarket           </td> <td>https://twitter.com/FarmMarket125th</td> <td>nan    </td> <td>Instagram--> 125thStreetFarmersMarket                       </td> <td>163 West 125th Street and Adam Clayton Powell, Jr. Blvd.</td> <td>New York  </td> <td>New York            </td> <td>New York            </td> <td>10027</td> <td>06/10/2014 to 11/25/2014</td> <td>Tue: 10:00 AM-7:00 PM;                      </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-73.9482</td> <td>40.809 </td> <td>Federal/State government building grounds                 </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>Y     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>Y   </td> <td>N     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>Y     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>Y     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/7/2014 4:32:01 PM  </td>
        </tr>
        <tr>
            <td>1005586</td> <td>12th & Brandywine Urban Farm Market             </td> <td>nan                                                  </td> <td>https://www.facebook.com/pages/12th-Brandywine-Urban-Far ...</td> <td>nan                                </td> <td>nan    </td> <td>https://www.facebook.com/delawareurbanfarmcoalition         </td> <td>12th & Brandywine Streets                               </td> <td>Wilmington</td> <td>New Castle          </td> <td>Delaware            </td> <td>19801</td> <td>05/16/2014 to 10/17/2014</td> <td>Fri: 8:00 AM-11:00 AM;                      </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-75.5345</td> <td>39.7421</td> <td>On a farm from: a barn, a greenhouse, a tent, a stand, etc</td> <td>N     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>Y   </td> <td>N      </td> <td>N         </td> <td>N     </td> <td>N     </td> <td>N      </td> <td>N   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>N    </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>N      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/3/2014 3:43:31 PM  </td>
        </tr>
        <tr>
            <td>1008071</td> <td>14&U Farmers' Market                            </td> <td>nan                                                  </td> <td>https://www.facebook.com/14UFarmersMarket                   </td> <td>https://twitter.com/14UFarmersMkt  </td> <td>nan    </td> <td>nan                                                         </td> <td>1400 U Street NW                                        </td> <td>Washington</td> <td>District of Columbia</td> <td>District of Columbia</td> <td>20009</td> <td>05/03/2014 to 11/22/2014</td> <td>Sat: 9:00 AM-1:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-77.0321</td> <td>38.917 </td> <td>Other                                                     </td> <td>Y     </td> <td>Y   </td> <td>Y      </td> <td>Y    </td> <td>Y   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>N      </td> <td>Y   </td> <td>Y     </td> <td>Y      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>Y    </td> <td>Y     </td> <td>Y     </td> <td>Y     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/5/2014 1:49:04 PM  </td>
        </tr>
    </tbody>
</table>
<p>... (8536 rows omitted)</p>



You'll notice that it has a large number of columns in it!

### `num_columns`

**Question 6.2.**<br/> The table property `num_columns` (example call: `tbl.num_columns`) produces the number of columns in a table.  Use it to find the number of columns in our farmers' markets dataset.


```python
num_farmers_markets_columns = farmers_markets.num_columns
print("The table has", num_farmers_markets_columns, "columns in it!")
```

    The table has 59 columns in it!


Most of the columns are about particular products -- whether the market sells tofu, pet food, etc.  If we're not interested in that stuff, it just makes the table difficult to read.  This comes up more than you might think.

### `select`

In such situations, we can use the table method `select` to pare down the columns of a table.  It takes any number of arguments.  Each should be the name or index of a column in the table.  It returns a new table with only those columns in it.

For example, the value of `imdb.select("Year", "Decade")` is a table with only the years and decades of each movie in `imdb`.

**Question 6.3.**<br/> Use `select` to create a table with only the MarketName, city, State, latitude ('y'), and longitude ('x') of each market.  Call that new table `farmers_markets_locations`.


```python
farmers_markets_locations = farmers_markets.select('MarketName', 'city', 'State', 'y', 'x')
farmers_markets_locations
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>MarketName</th> <th>city</th> <th>State</th> <th>y</th> <th>x</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> Caledonia Farmers Market Association - Danville</td> <td>Danville  </td> <td>Vermont             </td> <td>44.411 </td> <td>-72.1403</td>
        </tr>
        <tr>
            <td> Stearns Homestead Farmers' Market              </td> <td>Parma     </td> <td>Ohio                </td> <td>41.3751</td> <td>-81.7286</td>
        </tr>
        <tr>
            <td>100 Mile Market                                 </td> <td>Kalamazoo </td> <td>Michigan            </td> <td>42.296 </td> <td>-85.5749</td>
        </tr>
        <tr>
            <td>106 S. Main Street Farmers Market               </td> <td>Six Mile  </td> <td>South Carolina      </td> <td>34.8042</td> <td>-82.8187</td>
        </tr>
        <tr>
            <td>10th Steet Community Farmers Market             </td> <td>Lamar     </td> <td>Missouri            </td> <td>37.4956</td> <td>-94.2746</td>
        </tr>
        <tr>
            <td>112st Madison Avenue                            </td> <td>New York  </td> <td>New York            </td> <td>40.7939</td> <td>-73.9493</td>
        </tr>
        <tr>
            <td>12 South Farmers Market                         </td> <td>Nashville </td> <td>Tennessee           </td> <td>36.1184</td> <td>-86.7907</td>
        </tr>
        <tr>
            <td>125th Street Fresh Connect Farmers' Market      </td> <td>New York  </td> <td>New York            </td> <td>40.809 </td> <td>-73.9482</td>
        </tr>
        <tr>
            <td>12th & Brandywine Urban Farm Market             </td> <td>Wilmington</td> <td>Delaware            </td> <td>39.7421</td> <td>-75.5345</td>
        </tr>
        <tr>
            <td>14&U Farmers' Market                            </td> <td>Washington</td> <td>District of Columbia</td> <td>38.917 </td> <td>-77.0321</td>
        </tr>
    </tbody>
</table>
<p>... (8536 rows omitted)</p>



### `select` is not `column`!

The method `select` is **definitely not** the same as the method `column`.

`farmers_markets.column('y')` is an *array* of the latitudes of all the markets.  `farmers_markets.select('y')` is a *table* that happens to contain only 1 column, the latitudes of all the markets.

Recognizing this distinction is important because data types determine what we can do with our code.


```python
print(".column will give you the following datatype:", type(farmers_markets.column("y")))

print(".select will give you the following datatype:", type(farmers_markets.select("y")))
```

    .column will give you the following datatype: <class 'numpy.ndarray'>
    .select will give you the following datatype: <class 'datascience.tables.Table'>


**Question 6.4.** <br/>Below, we tried using the function `np.average` to find the average latitude ('y') and average longitude ('x') of the farmers' markets in the table, but we screwed something up.  Run the cell to see the (somewhat inscrutable) error message that results from calling `np.average` on a table.  Then, fix our code.


```python
average_latitude = np.average(farmers_markets.column("y"))
average_longitude = np.average(farmers_markets.column("x"))
print("The average of US farmers' markets' coordinates is located at (", average_latitude, ",", average_longitude, ")")
```

    The average of US farmers' markets' coordinates is located at ( 39.1864645235 , -90.9925808129 )


### `drop`

`drop` serves the same purpose as `select`, but it takes away the columns you list instead of the ones you don't list, leaving all the rest of the columns. This is usually easier when you want to keep a lot of columns. 

**Question 6.5.** <br/>Suppose you just didn't want the "FMID" or "updateTime" columns in `farmers_markets`.  Create a table that's a copy of `farmers_markets` but doesn't include those columns.  Call that table `farmers_markets_without_fmid`.


```python
farmers_markets_without_fmid = farmers_markets.drop("FMID")
farmers_markets_without_fmid
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>MarketName</th> <th>Website</th> <th>Facebook</th> <th>Twitter</th> <th>Youtube</th> <th>OtherMedia</th> <th>street</th> <th>city</th> <th>County</th> <th>State</th> <th>zip</th> <th>Season1Date</th> <th>Season1Time</th> <th>Season2Date</th> <th>Season2Time</th> <th>Season3Date</th> <th>Season3Time</th> <th>Season4Date</th> <th>Season4Time</th> <th>x</th> <th>y</th> <th>Location</th> <th>Credit</th> <th>WIC</th> <th>WICcash</th> <th>SFMNP</th> <th>SNAP</th> <th>Organic</th> <th>Bakedgoods</th> <th>Cheese</th> <th>Crafts</th> <th>Flowers</th> <th>Eggs</th> <th>Seafood</th> <th>Herbs</th> <th>Vegetables</th> <th>Honey</th> <th>Jams</th> <th>Maple</th> <th>Meat</th> <th>Nursery</th> <th>Nuts</th> <th>Plants</th> <th>Poultry</th> <th>Prepared</th> <th>Soap</th> <th>Trees</th> <th>Wine</th> <th>Coffee</th> <th>Beans</th> <th>Fruits</th> <th>Grains</th> <th>Juices</th> <th>Mushrooms</th> <th>PetFood</th> <th>Tofu</th> <th>WildHarvested</th> <th>updateTime</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> Caledonia Farmers Market Association - Danville</td> <td>https://sites.google.com/site/caledoniafarmersmarket/</td> <td>https://www.facebook.com/Danville.VT.Farmers.Market/        </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>nan                                                     </td> <td>Danville  </td> <td>Caledonia           </td> <td>Vermont             </td> <td>05828</td> <td>06/08/2016 to 10/12/2016</td> <td>Wed: 9:00 AM-1:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-72.1403</td> <td>44.411 </td> <td>nan                                                       </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>N   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>Y     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>Y     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>Y    </td> <td>N   </td> <td>Y     </td> <td>Y    </td> <td>Y     </td> <td>N     </td> <td>Y     </td> <td>N        </td> <td>Y      </td> <td>N   </td> <td>N            </td> <td>6/28/2016 12:10:09 PM</td>
        </tr>
        <tr>
            <td> Stearns Homestead Farmers' Market              </td> <td>http://Stearnshomestead.com                          </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>6975 Ridge Road                                         </td> <td>Parma     </td> <td>Cuyahoga            </td> <td>Ohio                </td> <td>44130</td> <td>06/25/2016 to 10/01/2016</td> <td>Sat: 9:00 AM-1:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-81.7286</td> <td>41.3751</td> <td>nan                                                       </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y   </td> <td>-      </td> <td>Y         </td> <td>N     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>Y     </td> <td>N      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>Y      </td> <td>N   </td> <td>N            </td> <td>4/9/2016 8:05:17 PM  </td>
        </tr>
        <tr>
            <td>100 Mile Market                                 </td> <td>http://www.pfcmarkets.com                            </td> <td>https://www.facebook.com/100MileMarket/?fref=ts             </td> <td>nan                                </td> <td>nan    </td> <td>https://www.instagram.com/100milemarket/                    </td> <td>507 Harrison St                                         </td> <td>Kalamazoo </td> <td>Kalamazoo           </td> <td>Michigan            </td> <td>49007</td> <td>05/04/2016 to 10/12/2016</td> <td>Wed: 3:00 PM-7:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-85.5749</td> <td>42.296 </td> <td>nan                                                       </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>Y         </td> <td>Y     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>Y     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/16/2016 12:37:56 PM</td>
        </tr>
        <tr>
            <td>106 S. Main Street Farmers Market               </td> <td>http://thetownofsixmile.wordpress.com/               </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>106 S. Main Street                                      </td> <td>Six Mile  </td> <td>nan                 </td> <td>South Carolina      </td> <td>29682</td> <td>nan                     </td> <td>nan                                         </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-82.8187</td> <td>34.8042</td> <td>nan                                                       </td> <td>Y     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>N   </td> <td>-      </td> <td>N         </td> <td>N     </td> <td>N     </td> <td>N      </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>N         </td> <td>N    </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>N      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>N     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>2013                 </td>
        </tr>
        <tr>
            <td>10th Steet Community Farmers Market             </td> <td>nan                                                  </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>http://agrimissouri.com/mo-grown/grodetail.php?type=mo-g ...</td> <td>10th Street and Poplar                                  </td> <td>Lamar     </td> <td>Barton              </td> <td>Missouri            </td> <td>64759</td> <td>04/02/2014 to 11/30/2014</td> <td>Wed: 3:00 PM-6:00 PM;Sat: 8:00 AM-1:00 PM;  </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-94.2746</td> <td>37.4956</td> <td>nan                                                       </td> <td>Y     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>N   </td> <td>-      </td> <td>Y         </td> <td>N     </td> <td>Y     </td> <td>N      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>Y     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>10/28/2014 9:49:46 AM</td>
        </tr>
        <tr>
            <td>112st Madison Avenue                            </td> <td>nan                                                  </td> <td>nan                                                         </td> <td>nan                                </td> <td>nan    </td> <td>nan                                                         </td> <td>112th Madison Avenue                                    </td> <td>New York  </td> <td>New York            </td> <td>New York            </td> <td>10029</td> <td>July to November        </td> <td>Tue:8:00 am - 5:00 pm;Sat:8:00 am - 8:00 pm;</td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-73.9493</td> <td>40.7939</td> <td>Private business parking lot                              </td> <td>N     </td> <td>N   </td> <td>Y      </td> <td>Y    </td> <td>N   </td> <td>-      </td> <td>Y         </td> <td>N     </td> <td>Y     </td> <td>Y      </td> <td>N   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>N      </td> <td>Y   </td> <td>N     </td> <td>N      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>N     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>3/1/2012 10:38:22 AM </td>
        </tr>
        <tr>
            <td>12 South Farmers Market                         </td> <td>http://www.12southfarmersmarket.com                  </td> <td>12_South_Farmers_Market                                     </td> <td>@12southfrmsmkt                    </td> <td>nan    </td> <td>@12southfrmsmkt                                             </td> <td>3000 Granny White Pike                                  </td> <td>Nashville </td> <td>Davidson            </td> <td>Tennessee           </td> <td>37204</td> <td>05/05/2015 to 10/27/2015</td> <td>Tue: 3:30 PM-6:30 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-86.7907</td> <td>36.1184</td> <td>nan                                                       </td> <td>Y     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>Y   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>N   </td> <td>Y     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>Y     </td> <td>Y        </td> <td>Y      </td> <td>N   </td> <td>N            </td> <td>5/1/2015 10:40:56 AM </td>
        </tr>
        <tr>
            <td>125th Street Fresh Connect Farmers' Market      </td> <td>http://www.125thStreetFarmersMarket.com              </td> <td>https://www.facebook.com/125thStreetFarmersMarket           </td> <td>https://twitter.com/FarmMarket125th</td> <td>nan    </td> <td>Instagram--> 125thStreetFarmersMarket                       </td> <td>163 West 125th Street and Adam Clayton Powell, Jr. Blvd.</td> <td>New York  </td> <td>New York            </td> <td>New York            </td> <td>10027</td> <td>06/10/2014 to 11/25/2014</td> <td>Tue: 10:00 AM-7:00 PM;                      </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-73.9482</td> <td>40.809 </td> <td>Federal/State government building grounds                 </td> <td>Y     </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>Y     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>Y    </td> <td>Y   </td> <td>N      </td> <td>Y   </td> <td>N     </td> <td>Y      </td> <td>Y       </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>Y     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>Y     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/7/2014 4:32:01 PM  </td>
        </tr>
        <tr>
            <td>12th & Brandywine Urban Farm Market             </td> <td>nan                                                  </td> <td>https://www.facebook.com/pages/12th-Brandywine-Urban-Far ...</td> <td>nan                                </td> <td>nan    </td> <td>https://www.facebook.com/delawareurbanfarmcoalition         </td> <td>12th & Brandywine Streets                               </td> <td>Wilmington</td> <td>New Castle          </td> <td>Delaware            </td> <td>19801</td> <td>05/16/2014 to 10/17/2014</td> <td>Fri: 8:00 AM-11:00 AM;                      </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-75.5345</td> <td>39.7421</td> <td>On a farm from: a barn, a greenhouse, a tent, a stand, etc</td> <td>N     </td> <td>N   </td> <td>N      </td> <td>N    </td> <td>Y   </td> <td>N      </td> <td>N         </td> <td>N     </td> <td>N     </td> <td>N      </td> <td>N   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>N    </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N      </td> <td>N   </td> <td>N     </td> <td>N      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>N    </td> <td>Y     </td> <td>N     </td> <td>N     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/3/2014 3:43:31 PM  </td>
        </tr>
        <tr>
            <td>14&U Farmers' Market                            </td> <td>nan                                                  </td> <td>https://www.facebook.com/14UFarmersMarket                   </td> <td>https://twitter.com/14UFarmersMkt  </td> <td>nan    </td> <td>nan                                                         </td> <td>1400 U Street NW                                        </td> <td>Washington</td> <td>District of Columbia</td> <td>District of Columbia</td> <td>20009</td> <td>05/03/2014 to 11/22/2014</td> <td>Sat: 9:00 AM-1:00 PM;                       </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>nan        </td> <td>-77.0321</td> <td>38.917 </td> <td>Other                                                     </td> <td>Y     </td> <td>Y   </td> <td>Y      </td> <td>Y    </td> <td>Y   </td> <td>Y      </td> <td>Y         </td> <td>Y     </td> <td>N     </td> <td>Y      </td> <td>Y   </td> <td>N      </td> <td>Y    </td> <td>Y         </td> <td>Y    </td> <td>Y   </td> <td>N    </td> <td>Y   </td> <td>N      </td> <td>Y   </td> <td>Y     </td> <td>Y      </td> <td>N       </td> <td>N   </td> <td>N    </td> <td>N   </td> <td>N     </td> <td>Y    </td> <td>Y     </td> <td>Y     </td> <td>Y     </td> <td>N        </td> <td>N      </td> <td>N   </td> <td>N            </td> <td>4/5/2014 1:49:04 PM  </td>
        </tr>
    </tbody>
</table>
<p>... (8536 rows omitted)</p>



#### `take`
Let's find the 5 northernmost farmers' markets in the US.  You already know how to sort by latitude ('y'), but we haven't seen how to get the first 5 rows of a table.  That's what `take` is for.

The table method `take` takes as its argument an array of numbers.  Each number should be the index of a row in the table.  It returns a new table with only those rows.

Most often you'll want to use `take` in conjunction with `np.arange` to take the first few rows of a table. For example: `tbl.take(np.arange(3))` gives us the first 3 rows, because np.arange creates an array of the indices (0, 1, 2).

**Question 6.6.** <br/>Make a table of the 5 northernmost farmers' markets in `farmers_markets_locations`.  Call it `northern_markets`.  (It should include the same columns as `farmers_markets_locations`.


```python
northern_markets = farmers_markets_locations.sort("y", descending=True).take(np.arange(5))
northern_markets
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>MarketName</th> <th>city</th> <th>State</th> <th>y</th> <th>x</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Tanana Valley Farmers Market </td> <td>Fairbanks     </td> <td>Alaska</td> <td>64.8628</td> <td>-147.781</td>
        </tr>
        <tr>
            <td>Ester Community Market       </td> <td>Ester         </td> <td>Alaska</td> <td>64.8459</td> <td>-148.01 </td>
        </tr>
        <tr>
            <td>Fairbanks Downtown Market    </td> <td>Fairbanks     </td> <td>Alaska</td> <td>64.8444</td> <td>-147.72 </td>
        </tr>
        <tr>
            <td>Nenana Open Air Market       </td> <td>Nenana        </td> <td>Alaska</td> <td>64.5566</td> <td>-149.096</td>
        </tr>
        <tr>
            <td>Highway's End Farmers' Market</td> <td>Delta Junction</td> <td>Alaska</td> <td>64.0385</td> <td>-145.733</td>
        </tr>
    </tbody>
</table>



## 7. Functions and CEO Incomes

We'll look at the 2015 compensation of CEOs at the 100 largest companies in California.  The data were compiled for a Los Angeles Times analysis [here](http://spreadsheets.latimes.com/california-ceo-compensation/), and ultimately came from [filings](https://www.sec.gov/answers/proxyhtf.htm) mandated by the SEC from all publicly-traded companies.  Two companies have two CEOs, so there are 102 CEOs in the dataset.

We've copied the data in raw form from the LA Times page into a file called `raw_compensation.csv`.  (The page notes that all dollar amounts are in millions of dollars.)


```python
raw_compensation = Table.read_table('raw_compensation.csv')
raw_compensation
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Rank</th> <th>Name</th> <th>Company (Headquarters)</th> <th>Total Pay</th> <th>% Change</th> <th>Cash Pay</th> <th>Equity Pay</th> <th>Other Pay</th> <th>Ratio of CEO pay to average industry worker pay</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1   </td> <td>Mark V. Hurd*     </td> <td>Oracle (Redwood City)         </td> <td>$53.25   </td> <td>(No previous year)</td> <td>$0.95   </td> <td>$52.27    </td> <td>$0.02    </td> <td>362                                            </td>
        </tr>
        <tr>
            <td>2   </td> <td>Safra A. Catz*    </td> <td>Oracle (Redwood City)         </td> <td>$53.24   </td> <td>(No previous year)</td> <td>$0.95   </td> <td>$52.27    </td> <td>$0.02    </td> <td>362                                            </td>
        </tr>
        <tr>
            <td>3   </td> <td>Robert A. Iger    </td> <td>Walt Disney (Burbank)         </td> <td>$44.91   </td> <td>-3%               </td> <td>$24.89  </td> <td>$17.28    </td> <td>$2.74    </td> <td>477                                            </td>
        </tr>
        <tr>
            <td>4   </td> <td>Marissa A. Mayer  </td> <td>Yahoo! (Sunnyvale)            </td> <td>$35.98   </td> <td>-15%              </td> <td>$1.00   </td> <td>$34.43    </td> <td>$0.55    </td> <td>342                                            </td>
        </tr>
        <tr>
            <td>5   </td> <td>Marc Benioff      </td> <td>salesforce.com (San Francisco)</td> <td>$33.36   </td> <td>-16%              </td> <td>$4.65   </td> <td>$27.26    </td> <td>$1.45    </td> <td>338                                            </td>
        </tr>
        <tr>
            <td>6   </td> <td>John H. Hammergren</td> <td>McKesson (San Francisco)      </td> <td>$24.84   </td> <td>-4%               </td> <td>$12.10  </td> <td>$12.37    </td> <td>$0.37    </td> <td>222                                            </td>
        </tr>
        <tr>
            <td>7   </td> <td>John S. Watson    </td> <td>Chevron (San Ramon)           </td> <td>$22.04   </td> <td>-15%              </td> <td>$4.31   </td> <td>$14.68    </td> <td>$3.05    </td> <td>183                                            </td>
        </tr>
        <tr>
            <td>8   </td> <td>Jeffrey Weiner    </td> <td>LinkedIn (Mountain View)      </td> <td>$19.86   </td> <td>27%               </td> <td>$2.47   </td> <td>$17.26    </td> <td>$0.13    </td> <td>182                                            </td>
        </tr>
        <tr>
            <td>9   </td> <td>John T. Chambers**</td> <td>Cisco Systems (San Jose)      </td> <td>$19.62   </td> <td>19%               </td> <td>$5.10   </td> <td>$14.51    </td> <td>$0.01    </td> <td>170                                            </td>
        </tr>
        <tr>
            <td>10  </td> <td>John G. Stumpf    </td> <td>Wells Fargo  (San Francisco)  </td> <td>$19.32   </td> <td>-10%              </td> <td>$6.80   </td> <td>$12.50    </td> <td>$0.02    </td> <td>256                                            </td>
        </tr>
    </tbody>
</table>
<p>... (92 rows omitted)</p>



**Question 7.1.** <br/> We want to compute the average of the CEOs' pay. Try running the cell below.


```python
#np.average(raw_compensation.column("Total Pay"))
```

You should see an error. Let's examine why this error occured by looking at the values in the "Total Pay" column. Use the `type` function and set `total_pay_type` to the type of the first value in the "Total Pay" column.


```python
total_pay_type = type(raw_compensation.column("Total Pay").item(0))
total_pay_type
```




    str



**Question 7.2.** <br/>You should have found that the values in "Total Pay" column are strings (text). It doesn't make sense to take the average of the text values, so we need to convert them to numbers if we want to do this. Extract the first value in the "Total Pay" column.  It's Mark Hurd's pay in 2015, in *millions* of dollars.  Call it `mark_hurd_pay_string`.


```python
mark_hurd_pay_string = raw_compensation.column("Total Pay").item(0)
mark_hurd_pay_string
```




    '$53.25 '



**Question 7.3.** <br/>Convert `mark_hurd_pay_string` to a number of *dollars*.  The string method `strip` will be useful for removing the dollar sign; it removes a specified character from the start or end of a string.  For example, the value of `"100%".strip("%")` is the string `"100"`.  You'll also need the function `float`, which converts a string that looks like a number to an actual number.  Last, remember that the answer should be in dollars, not millions of dollars.


```python
mark_hurd_pay = float(mark_hurd_pay_string.replace("$", ""))
mark_hurd_pay
```




    53.25



To compute the average pay, we need to do this for every CEO.  But that looks like it would involve copying this code 102 times.

This is where functions come in.  First, we'll define a new function, giving a name to the expression that converts "total pay" strings to numeric values.  Later in this lab we'll see the payoff: we can call that function on every pay string in the dataset at once.

**Question 7.4.** <br/>Copy the expression you used to compute `mark_hurd_pay` as the `return` expression of the function below, but replace the specific `mark_hurd_pay_string` with the generic `pay_string` name specified in the first line of the `def` statement.

*Hint*: When dealing with functions, you should generally not be referencing any variable outside of the function. Usually, you want to be working with the arguments that are passed into it, such as `pay_string` for this function. 


```python
def convert_pay_string_to_number(pay_string):
    """Converts a pay string like '$100' (in millions) to a number of dollars."""
    return float(pay_string.replace("$", ""))
```

Running that cell doesn't convert any particular pay string. Instead, it creates a function called `convert_pay_string_to_number` that can convert any string with the right format to a number representing millions of dollars.

We can call our function just like we call the built-in functions we've seen. It takes one argument, a string, and it returns a number.


```python
convert_pay_string_to_number('$42')
```




    42.0




```python
convert_pay_string_to_number(mark_hurd_pay_string)
```




    53.25




```python
# We can also compute Safra Catz's pay in the same way:
convert_pay_string_to_number(raw_compensation.where("Name", are.containing("Safra")).column("Total Pay").item(0))
```




    53.24



So, what have we gained by defining the `convert_pay_string_to_number` function? 
Well, without it, we'd have to copy that `10**6 * float(pay_string.strip("$"))` stuff each time we wanted to convert a pay string.  Now we just call a function whose name says exactly what it's doing.

Soon, we'll see how to apply this function to every pay string in a single expression. First, let's take a brief detour and introduce `interact`.

### Using `interact`

We've included a nifty function called `interact` that allows you to
call a function with different arguments.

To use it, call `interact` with the function you want to interact with as the
first argument, then specify a default value for each argument of the original
function like so:


```python
_ = interact(convert_pay_string_to_number, pay_string='$42')
```


    interactive(children=(Text(value='$42', description='pay_string'), Output()), _dom_classes=('widget-interact',…


You can now change the value in the textbox to automatically call
`convert_pay_string_to_number` with the argument you enter in the `pay_string`
textbox. For example, entering in `'$49'` in the textbox will display the result of
running `convert_pay_string_to_number('$49')`. Neat!

Note that we'll never ask you to write the `interact` function calls yourself as
part of a question. However, we'll include it here and there where it's helpful
and you'll probably find it useful to use yourself.

Now, let's continue on and write more functions.

## 8. Defining functions

Let's write a very simple function that converts a proportion to a percentage by multiplying it by 100.  For example, the value of `to_percentage(.5)` should be the number 50.  (No percent sign.)

A function definition has a few parts.

##### `def`
It always starts with `def` (short for **def**ine):

    def

##### Name
Next comes the name of the function.  Let's call our function `to_percentage`.
    
    def to_percentage

##### Signature
Next comes something called the *signature* of the function.  This tells Python how many arguments your function should have, and what names you'll use to refer to those arguments in the function's code.  `to_percentage` should take one argument, and we'll call that argument `proportion` since it should be a proportion.

    def to_percentage(proportion)

We put a colon after the signature to tell Python it's over.

    def to_percentage(proportion):

##### Documentation
Functions can do complicated things, so you should write an explanation of what your function does.  For small functions, this is less important, but it's a good habit to learn from the start.  Conventionally, Python functions are documented by writing a triple-quoted string:

    def to_percentage(proportion):
        """Converts a proportion to a percentage."""
    
    
##### Body
Now we start writing code that runs when the function is called.  This is called the *body* of the function.  We can write anything we could write anywhere else.  First let's give a name to the number we multiply a proportion by to get a percentage.

    def to_percentage(proportion):
        """Converts a proportion to a percentage."""
        factor = 100

##### `return`
The special instruction `return` in a function's body tells Python to make the value of the function call equal to whatever comes right after `return`.  We want the value of `to_percentage(.5)` to be the proportion .5 times the factor 100, so we write:

    def to_percentage(proportion):
        """Converts a proportion to a percentage."""
        factor = 100
        return proportion * factor
Note that `return` inside a function gives the function a value, while `print`, which we have used before, is a function which has no `return` value and just prints a certain value out to the console. The two are very different. 

**Question 8.1.** <br/>Define `to_percentage` in the cell below.  Call your function to convert the proportion .2 to a percentage.  Name that percentage `twenty_percent`.


```python
def to_percentage(proportion):
    """ ... """
    factor = 100
    return proportion * factor

twenty_percent = to_percentage(0.2)
twenty_percent
```




    20.0



Like the built-in functions, you can use named values as arguments to your function.

**Question 8.2.** <br/>Use `to_percentage` again to convert the proportion named `a_proportion` (defined below) to a percentage called `a_percentage`.

*Note:* You don't need to define `to_percentage` again!  Just like other named things, functions stick around after you define them.


```python
a_proportion = 2**(.5) / 2
a_percentage = to_percentage(a_proportion)
a_percentage
```




    70.71067811865476



Here's something important about functions: the names assigned within a function body are only accessible within the function body. Once the function has returned, those names are gone.  So even though you defined `factor = 100` inside `to_percentage` above and then called `to_percentage`, you cannot refer to `factor` anywhere except inside the body of `to_percentage`:


```python
# You should see an error when you run this.  (If you don't, you might
# have defined factor somewhere above.)
#factor
```

As we've seen with the built-in functions, functions can also take strings (or arrays, or tables) as arguments, and they can return those things, too.

**Question 8.3.** <br/>Define a function called `disemvowel`.  It should take a single string as its argument.  (You can call that argument whatever you want.)  It should return a copy of that string, but with all the characters that are vowels removed.  (In English, the vowels are the characters "a", "e", "i", "o", and "u".)

*Hint:* To remove all the "a"s from a string, you can use `that_string.replace("a", "")`.  The `.replace` method for strings returns another string, so you can call `replace` multiple times, one after the other. 


```python
def disemvowel(a_string):
    """Removes all vowels from a string."""
    return a_string.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")

# An example call to your function.  (It's often helpful to run
# an example call from time to time while you're writing a function,
# to see how it currently works.)
disemvowel("Can you read this without vowels?")
```




    'Cn y rd ths wtht vwls?'




```python
# Alternatively, you can use interact to call your function
_ = interact(disemvowel, a_string='Hello world')
```


    interactive(children=(Text(value='Hello world', description='a_string'), Output()), _dom_classes=('widget-inte…


##### Calls on calls on calls
Just as you write a series of lines to build up a complex computation, it's useful to define a series of small functions that build on each other.  Since you can write any code inside a function's body, you can call other functions you've written.

If a function is a like a recipe, defining a function in terms of other functions is like having a recipe for cake telling you to follow another recipe to make the frosting, and another to make the sprinkles.  This makes the cake recipe shorter and clearer, and it avoids having a bunch of duplicated frosting recipes.  It's a foundation of productive programming.

For example, suppose you want to count the number of characters *that aren't vowels* in a piece of text.  One way to do that is this to remove all the vowels and count the size of the remaining string.

**Question 8.4.** <br/>Write a function called `num_non_vowels`.  It should take a string as its argument and return a number.  The number should be the number of characters in the argument string that aren't vowels.

*Hint:* The function `len` takes a string as its argument and returns the number of characters in it.


```python
def num_non_vowels(a_string):
    """The number of characters in a string, minus the vowels."""
    return len(disemvowel(a_string))

# Try calling your function yourself to make sure the output is what
# you expect. You can also use the interact function if you'd like.
num_non_vowels("Can you read this without vowels?")
```




    22



Functions can also encapsulate code that *does things* rather than just computing values.  For example, if you call `print` inside a function, and then call that function, something will get printed.

The `movies_by_year` dataset in the textbook has information about movie sales in recent years.  Suppose you'd like to display the year with the 5th-highest total gross movie sales, printed in a human-readable way.  You might do this:


```python
movies_by_year = Table.read_table("movies_by_year.csv")
rank = 5
fifth_from_top_movie_year = movies_by_year.sort("Total Gross", descending=True).column("Year").item(rank-1)
print("Year number", rank, "for total gross movie sales was:", fifth_from_top_movie_year)
```

    Year number 5 for total gross movie sales was: 2010


After writing this, you realize you also wanted to print out the 2nd and 3rd-highest years.  Instead of copying your code, you decide to put it in a function.  Since the rank varies, you make that an argument to your function.

**Question 8.5.** <br/>Write a function called `print_kth_top_movie_year`.  It should take a single argument, the rank of the year (like 2, 3, or 5 in the above examples).  It should print out a message like the one above.  It shouldn't have a `return` statement.


```python
def print_kth_top_movie_year(k):
    # Our solution used 2 lines.
    ... 
    ...

# Example calls to your function:
print_kth_top_movie_year(2)
print_kth_top_movie_year(3)
```


```python
# interact also allows you to pass in an array for a function argument. It will
# then present a dropdown menu of options.
_ = interact(print_kth_top_movie_year, k=np.arange(1, 10))
```


    interactive(children=(Dropdown(description='k', options=(1, 2, 3, 4, 5, 6, 7, 8, 9), value=1), Output()), _dom…


##### Print is not the same as Return
The `print_kth_top_movie_year(k)` function prints the total gross movie sales for the year that was provided! However, since we did not return any value in this function, we can not use it after we call it. Let's look at an example of a function that prints a value but does not return it.


```python
def print_number_five():
    print(5)
```


```python
print_number_five()
```

    5


However, if we try to use the output of `print_number_five()`, we see that we get an error when we try to add the number 5 to it!


```python
print_number_five_output = print_number_five()
print_number_five_output + 5
```

    5



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[200], line 2
          1 print_number_five_output = print_number_five()
    ----> 2 print_number_five_output + 5


    TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'


It may seem that `print_number_five()` is returning a value, 5. In reality, it just displays the number 5 to you without giving you the actual value! If your function prints out a value without returning it and you try to use it, you will run into errors so be careful!

## 9. `apply`ing functions

Defining a function is a lot like giving a name to a value with `=`.  In fact, a function is a value just like the number 1 or the text "the"!

For example, we can make a new name for the built-in function `max` if we want:


```python
our_name_for_max = max
our_name_for_max(2, 6)
```




    6



The old name for `max` is still around:


```python
max(2, 6)
```




    6



Try just writing `max` or `our_name_for_max` (or the name of any other function) in a cell, and run that cell.  Python will print out a (very brief) description of the function.


```python
max
```




    <function max>



Why is this useful?  Since functions are just values, it's possible to pass them as arguments to other functions.  Here's a simple but not-so-practical example: we can make an array of functions.


```python
make_array(max, np.average, are.equal_to)
```




    array([<built-in function max>, <function average at 0x11714c7c0>,
           <function are.equal_to at 0x13456cea0>], dtype=object)



**Question 9.1.** <br/>Make an array containing any 3 other functions you've seen.  Call it `some_functions`.


```python
some_functions = ...
some_functions
```

Working with functions as values can lead to some funny-looking code.  For example, see if you can figure out why this works:


```python
make_array(max, np.average, are.equal_to).item(0)(4, -2, 7)
```




    7



Here's a simpler example that's actually useful: the table method `apply`.

`apply` calls a function many times, once on *each* element in a column of a table.  It produces an array of the results.  Here we use `apply` to convert every CEO's pay to a number, using the function you defined:


```python
raw_compensation.apply(convert_pay_string_to_number, "Total Pay")
```




    array([  5.32500000e+01,   5.32400000e+01,   4.49100000e+01,
             3.59800000e+01,   3.33600000e+01,   2.48400000e+01,
             2.20400000e+01,   1.98600000e+01,   1.96200000e+01,
             1.93200000e+01,   1.87600000e+01,   1.86100000e+01,
             1.83600000e+01,   1.80900000e+01,   1.71000000e+01,
             1.66300000e+01,   1.63300000e+01,   1.61400000e+01,
             1.61000000e+01,   1.60200000e+01,   1.51000000e+01,
             1.49800000e+01,   1.46300000e+01,   1.45100000e+01,
             1.44400000e+01,   1.43600000e+01,   1.43100000e+01,
             1.40900000e+01,   1.40000000e+01,   1.36700000e+01,
             1.23400000e+01,   1.22000000e+01,   1.21800000e+01,
             1.21300000e+01,   1.20500000e+01,   1.18400000e+01,
             1.17100000e+01,   1.16300000e+01,   1.11600000e+01,
             1.11100000e+01,   1.11100000e+01,   1.07300000e+01,
             1.05000000e+01,   1.04300000e+01,   1.03700000e+01,
             1.02800000e+01,   1.02700000e+01,   1.01800000e+01,
             1.01600000e+01,   9.97000000e+00,   9.96000000e+00,
             9.86000000e+00,   9.74000000e+00,   9.42000000e+00,
             9.39000000e+00,   9.22000000e+00,   9.06000000e+00,
             9.03000000e+00,   8.86000000e+00,   8.76000000e+00,
             8.57000000e+00,   8.38000000e+00,   8.36000000e+00,
             8.35000000e+00,   8.23000000e+00,   7.86000000e+00,
             7.70000000e+00,   7.58000000e+00,   7.51000000e+00,
             7.23000000e+00,   7.21000000e+00,   7.12000000e+00,
             6.88000000e+00,   6.77000000e+00,   6.64000000e+00,
             6.56000000e+00,   6.14000000e+00,   5.92000000e+00,
             5.90000000e+00,   5.89000000e+00,   5.73000000e+00,
             5.42000000e+00,   5.04000000e+00,   4.92000000e+00,
             4.92000000e+00,   4.47000000e+00,   4.25000000e+00,
             4.08000000e+00,   3.93000000e+00,   3.72000000e+00,
             2.88000000e+00,   2.83000000e+00,   2.82000000e+00,
             2.45000000e+00,   1.79000000e+00,   1.68000000e+00,
             1.53000000e+00,   9.40000000e-01,   8.10000000e-01,
             7.00000000e-02,   4.00000000e-02,   0.00000000e+00])



Here's an illustration of what that did:

<img src="apply.png" alt="For each value in the column 'Total Pay', the function `convert_pay_string_to_number` was applied."/>

Note that we didn't write something like `convert_pay_string_to_number()` or `convert_pay_string_to_number("Total Pay")`.  The job of `apply` is to call the function we give it, so instead of calling `convert_pay_string_to_number` ourselves, we just write its name as an argument to `apply`.

**Question 9.2.** <br/>Using `apply`, make a table that's a copy of `raw_compensation` with one more column called "Total Pay (\$)".  It should be the result of applying `convert_pay_string_to_number` to the "Total Pay" column, as we did above, and creating a new table which is the old one, but with the "Total Pay" column redone.  Call the new table `compensation`.


```python
compensation = raw_compensation.with_column(
    "Total Pay ($)",
    raw_compensation.apply(convert_pay_string_to_number, "Total Pay"))
compensation
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Rank</th> <th>Name</th> <th>Company (Headquarters)</th> <th>Total Pay</th> <th>% Change</th> <th>Cash Pay</th> <th>Equity Pay</th> <th>Other Pay</th> <th>Ratio of CEO pay to average industry worker pay</th> <th>Total Pay ($)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1   </td> <td>Mark V. Hurd*     </td> <td>Oracle (Redwood City)         </td> <td>$53.25   </td> <td>(No previous year)</td> <td>$0.95   </td> <td>$52.27    </td> <td>$0.02    </td> <td>362                                            </td> <td>53.25        </td>
        </tr>
        <tr>
            <td>2   </td> <td>Safra A. Catz*    </td> <td>Oracle (Redwood City)         </td> <td>$53.24   </td> <td>(No previous year)</td> <td>$0.95   </td> <td>$52.27    </td> <td>$0.02    </td> <td>362                                            </td> <td>53.24        </td>
        </tr>
        <tr>
            <td>3   </td> <td>Robert A. Iger    </td> <td>Walt Disney (Burbank)         </td> <td>$44.91   </td> <td>-3%               </td> <td>$24.89  </td> <td>$17.28    </td> <td>$2.74    </td> <td>477                                            </td> <td>44.91        </td>
        </tr>
        <tr>
            <td>4   </td> <td>Marissa A. Mayer  </td> <td>Yahoo! (Sunnyvale)            </td> <td>$35.98   </td> <td>-15%              </td> <td>$1.00   </td> <td>$34.43    </td> <td>$0.55    </td> <td>342                                            </td> <td>35.98        </td>
        </tr>
        <tr>
            <td>5   </td> <td>Marc Benioff      </td> <td>salesforce.com (San Francisco)</td> <td>$33.36   </td> <td>-16%              </td> <td>$4.65   </td> <td>$27.26    </td> <td>$1.45    </td> <td>338                                            </td> <td>33.36        </td>
        </tr>
        <tr>
            <td>6   </td> <td>John H. Hammergren</td> <td>McKesson (San Francisco)      </td> <td>$24.84   </td> <td>-4%               </td> <td>$12.10  </td> <td>$12.37    </td> <td>$0.37    </td> <td>222                                            </td> <td>24.84        </td>
        </tr>
        <tr>
            <td>7   </td> <td>John S. Watson    </td> <td>Chevron (San Ramon)           </td> <td>$22.04   </td> <td>-15%              </td> <td>$4.31   </td> <td>$14.68    </td> <td>$3.05    </td> <td>183                                            </td> <td>22.04        </td>
        </tr>
        <tr>
            <td>8   </td> <td>Jeffrey Weiner    </td> <td>LinkedIn (Mountain View)      </td> <td>$19.86   </td> <td>27%               </td> <td>$2.47   </td> <td>$17.26    </td> <td>$0.13    </td> <td>182                                            </td> <td>19.86        </td>
        </tr>
        <tr>
            <td>9   </td> <td>John T. Chambers**</td> <td>Cisco Systems (San Jose)      </td> <td>$19.62   </td> <td>19%               </td> <td>$5.10   </td> <td>$14.51    </td> <td>$0.01    </td> <td>170                                            </td> <td>19.62        </td>
        </tr>
        <tr>
            <td>10  </td> <td>John G. Stumpf    </td> <td>Wells Fargo  (San Francisco)  </td> <td>$19.32   </td> <td>-10%              </td> <td>$6.80   </td> <td>$12.50    </td> <td>$0.02    </td> <td>256                                            </td> <td>19.32        </td>
        </tr>
    </tbody>
</table>
<p>... (92 rows omitted)</p>



Now that we have the pay in numbers, we can compute things about them.

**Question 9.3.**<br/>Compute the average total pay of the CEOs in the dataset.


```python
average_total_pay = np.average(compensation.column("Total Pay ($)"))
average_total_pay
```




    11.445294117647055



**Question 9.4.** <br/>Companies pay executives in a variety of ways: directly in cash; by granting stock or other "equity" in the company; or with ancillary benefits (like private jets).  Compute the proportion of each CEO's pay that was cash.  (Your answer should be an array of numbers, one for each CEO in the dataset.)

*Note:* You might get a scary red error block but still receive an output. This is because the Total Pay for some CEOs, like Lawrence Page, is listed as 0, and as a result, you might be dividing by 0. This usually causes an error, but because we have an array, Python will try to return the calculations for the rest of the values instead of terminating the program completely. Treat the block as a warning. 


```python
cash_proportion = compensation.apply(convert_pay_string_to_number, "Cash Pay") / compensation.column("Total Pay ($)")
cash_proportion
```

    /var/folders/wf/xv73h74d6t185xgzct38jv400000gn/T/ipykernel_63313/4045390536.py:1: RuntimeWarning: invalid value encountered in divide
      cash_proportion = compensation.apply(convert_pay_string_to_number, "Cash Pay") / compensation.column("Total Pay ($)")





    array([ 0.01784038,  0.01784373,  0.55421955,  0.02779322,  0.13938849,
            0.48711755,  0.19555354,  0.12437059,  0.25993884,  0.35196687,
            0.3075693 ,  0.22138635,  0.13126362,  0.1708126 ,  0.23099415,
            0.06734817,  0.13043478,  0.28004957,  0.33229814,  0.15355805,
            0.29337748,  0.21829105,  0.31100478,  0.25086147,  0.2299169 ,
            0.16991643,  0.31795947,  0.26188786,  0.28357143,  0.15654718,
            0.38168558,  0.28934426,  0.20361248,  0.47650453,  0.45643154,
            0.36402027,  0.2177626 ,  0.24763543,  0.42562724,  0.2610261 ,
            0.18361836,  0.1444548 ,  0.33333333,  0.10834132,  0.20925747,
            0.97276265,  0.22979552,  0.22789784,  0.37893701,  0.25175527,
            0.73895582,  0.37018256,  0.2412731 ,  0.2133758 ,  0.20553781,
            0.23318872,  0.33664459,  0.3875969 ,  0.56094808,  0.11757991,
            0.35239207,  0.24463007,  0.25      ,  0.23712575,  0.43377886,
            0.31424936,  0.46363636,  0.32585752,  0.24766977,  0.98755187,
            0.27184466,  0.96207865,  0.31831395,  0.81979321,  0.23795181,
            0.17530488,  0.21172638,  0.37162162,  0.27288136,  0.26994907,
            0.55148342,  0.3597786 ,  0.        ,  0.47154472,  0.47154472,
            0.29753915,  0.16235294,  0.48529412,  0.46819338,  0.32526882,
            0.98958333,  0.61130742,  0.67021277,  0.75510204,  0.50837989,
            0.98809524,  0.98039216,  0.9893617 ,  0.87654321,  0.        ,
            1.        ,         nan])



Check out the "% Change" column in `compensation`.  It shows the percentage increase in the CEO's pay from the previous year.  For CEOs with no previous year on record, it instead says "(No previous year)".  The values in this column are *strings*, not numbers, so like the "Total Pay" column, it's not usable without a bit of extra work.

Given your current pay and the percentage increase from the previous year, you can compute your previous year's pay.  For example, if your pay is \\$100 this year, and that's an increase of 50% from the previous year, then your previous year's pay was $\frac{\$100}{1 + \frac{50}{100}}$, or around \$66.66.

**Question 9.5.** <br/>Create a new table called `with_previous_compensation`.  It should be a copy of `compensation`, but with the "(No previous year)" CEOs filtered out, and with an extra column called "2014 Total Pay ($)".  That column should have each CEO's pay in 2014.

*Hint:* This question takes several steps, but each one is still something you've seen before.  Take it one step at a time, using as many lines as you need.  You can print out your results after each step to make sure you're on the right track. 

*Hint 2:* It'll help to define a function.  You can do that just above your other code.


```python
# Definition to turn percent to number
def percent_string_to_num(percent_string):
    return float(percent_string.strip("%"))

# Compensation table where there is a previous year
having_previous_year = ...

# Get the percent changes as numbers instead of strings
percent_changes = ...

# Calculate the previous years pay
previous_pay = ...

# Put the previous pay column into the compensation table
with_previous_compensation = ...

with_previous_compensation
```

**Question 9.6.** <br/>What was the average pay of these CEOs in 2014?


```python
average_pay_2014 = ...
average_pay_2014
```

## 10. Histograms
Earlier, we computed the average pay among the CEOs in our 102-CEO dataset.  The average doesn't tell us everything about the amounts CEOs are paid, though.  Maybe just a few CEOs make the bulk of the money, even among these 102.

We can use a *histogram* to display more information about a set of numbers.  The table method `hist` takes a single argument, the name of a column of numbers.  It produces a histogram of the numbers in that column.

**Question 10.1.** <br/>Make a histogram of the pay of the CEOs in `compensation`.


```python
...
```

**Question 10.2.** <br/>Looking at the histogram, how many CEOs made more than \$30 million?  (Answer the question by filling in your answer manually.  You'll have to do a bit of arithmetic; feel free to use Python as a calculator.)


```python
num_ceos_more_than_30_million = ...
```

**Question 10.3.**<br/> Answer the same question with code. 

*Hint:* Use the table method `where` and the property `num_rows`.


```python
num_ceos_more_than_30_million_2 = ...
num_ceos_more_than_30_million_2
```

## 11. Summary

For your reference, here's a table of all the functions and methods we saw in this lab.

|Name|Example|Purpose|
|-|-|-|
|`Table`|`Table()`|Create an empty table, usually to extend with data|
|`Table.read_table`|`Table.read_table("my_data.csv")`|Create a table from a data file|
|`with_columns`|`tbl = Table().with_columns("N", np.arange(5), "2*N", np.arange(0, 10, 2))`|Create a copy of a table with more columns|
|`column`|`tbl.column("N")`|Create an array containing the elements of a column|
|`sort`|`tbl.sort("N")`|Create a copy of a table sorted by the values in a column|
|`where`|`tbl.where("N", are.above(2))`|Create a copy of a table with only the rows that match some *predicate*|
|`num_rows`|`tbl.num_rows`|Compute the number of rows in a table|
|`num_columns`|`tbl.num_columns`|Compute the number of columns in a table|
|`select`|`tbl.select("N")`|Create a copy of a table with only some of the columns|
|`drop`|`tbl.drop("2*N")`|Create a copy of a table without some of the columns|
|`take`|`tbl.take(np.arange(0, 6, 2))`|Create a copy of the table with only the rows whose indices are in the given array|

## 12. Submission

To submit your assignment, please download your notebook as a .ipynb file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as... > Notebook (.ipynb) or HTML (.html). Then, upload your files under "Lab 3" on Canvas.
