# Lab 2: Data Types, Arrays, and Tables
Welcome to Lab 2!  

Last time, we had our first look at Python and Jupyter notebooks.  So far, we've only used Python to manipulate numbers.  There's a lot more to life than numbers, so Python lets us represent many other types of data in programs.

In this lab, you'll first see how to represent and manipulate another fundamental type of data: text.  A piece of text is called a *string* in Python.

You'll also see how to invoke *methods*.  A method is very similar to a function.  Calling a method looks different because the method is tied to a particular piece of data.

Last, you'll learn more about working with datasets in Python.

## 1. Review: The building blocks of Python code

The two building blocks of Python code are *expressions* and *statements*.  An **expression** is a piece of code that

* is self-contained, meaning it would make sense to write it on a line by itself, and
* usually has a value.


Here are two expressions that both evaluate to 3

    3
    5 - 2
    
One important form of an expression is the **call expression**, which first names a function and then describes its arguments. The function returns some value, based on its arguments. Some important mathematical functions are

| Function | Description                                                   |
|----------|---------------------------------------------------------------|
| `abs`      | Returns the absolute value of its argument                    |
| `max`      | Returns the maximum of all its arguments                      |
| `min`      | Returns the minimum of all its arguments                      |
| `pow`      | Raises its first argument to the power of its second argument |
| `round`    | Round its argument to the nearest integer                     |

Here are two call expressions that both evaluate to 3

    abs(2 - 5)
    max(round(2.8), min(pow(2, 10), -1 * pow(2, 10)))

All these expressions but the first are **compound expressions**, meaning that they are actually combinations of several smaller expressions.  `2 + 3` combines the expressions `2` and `3` by addition.  In this case, `2` and `3` are called **subexpressions** because they're expressions that are part of a larger expression. Any expression can be used as part of a larger expression.

A **statement** is a piece of code that *makes something happen* rather than *having a value*.  For example, an **assignment statement** assigns a value to a name. 

Every assignment statement has one `=` sign. The whole statement is executed by **evaluating the expression on the right-hand side** of the equals sign and then **assigning its value to the name on the left-hand side**. Here are some assignment statements:
    
    height = 1.3
    the_number_five = abs(-5)
    absolute_height_difference = abs(height - 1.688)

A key idea in programming is that large, interesting things can be built by combining many simple, uninteresting things.  The key to understanding a complicated piece of code is breaking it down into its simple components.

For example, a lot is going on in the last statement above, but it's really just a combination of a few things.  This picture describes what's going on.

<img src="statement.jpg" alt="Explanation of the statement 'absolute_height_difference = abs(height - 1.688)'">

Any names that you assign in one cell are available in later cells and can be used in place of the value assigned to them.

**Question 1.1.** <br/> In the next cell, assign the name `new_year` to the larger number among the following two numbers:

1. the absolute value of $2^{6}-2^{12}-2^{4}-2^{0}$, and 
2. $23 \times 101 \times 31 + 6 $.

Try to use just one statement (one line of code).


```python
new_year = max(abs(2**6 - 2**12 - 2**4 - 2**0), (23 * 101 * 31 + 6))
new_year
```




    72019



## 2. Text
Programming doesn't just concern numbers. Text is one of the most common types of values used in programs. 

A snippet of text is represented by a **string value** in Python. The word "*string*" is a programming term for a sequence of characters. A string might contain a single character, a word, a sentence, or a whole book.

To distinguish text data from actual code, we demarcate strings by putting quotation marks around them. Single quotes (`'`) and double quotes (`"`) are both valid, but the types of opening and closing quotation marks must match. The contents can be any sequence of characters, including numbers and symbols. 

We've seen strings before in `print` statements.  Below, two different strings are passed as arguments to the `print` function.


```python
print("I <3", 'Data Science')
```

    I <3 Data Science


Just like names can be given to numbers, names can be given to string values.  The names and strings aren't required to be similar in any way. Any name can be assigned to any string.


```python
one = 'two'
plus = '*'
print(one, plus, one)
```

    two * two


**Question 2.1.** <br/> Yuri Gagarin was the first person to travel through outer space.  When he emerged from his capsule upon landing on Earth, he [reportedly](https://en.wikiquote.org/wiki/Yuri_Gagarin) had the following conversation with a woman and girl who saw the landing:

    The woman asked: "Can it be that you have come from outer space?"
    Gagarin replied: "As a matter of fact, I have!"

The cell below contains unfinished code.  Fill in the `...`s so that it prints out this conversation *exactly* as it appears above.


```python
woman_asking = "The woman asked:"
woman_quote = '"Can it be that you have come from outer space?"'
gagarin_reply = 'Gagarin replied:'
gagarin_quote = '"As a matter of fact, I have!"'

print(woman_asking, woman_quote)
print(gagarin_reply, gagarin_quote)
```

    The woman asked: "Can it be that you have come from outer space?"
    Gagarin replied: "As a matter of fact, I have!"


### 2.1. String Methods

Strings can be transformed using **methods**, which are functions that involve an existing string and some other arguments. One example is the `replace` method, which replaces all instances of some part of a string with some alternative. 

A method is invoked on a string by placing a `.` after the string value, then the name of the method, and finally parentheses containing the arguments. Here's a sketch, where the `<` and `>` symbols aren't part of the syntax; they just mark the boundaries of sub-expressions.

    <expression that evaluates to a string>.<method name>(<argument>, <argument>, ...)

Try to predict the output of these examples, then execute them.


```python
# Replace one letter
'Hello'.replace('H', 'C')
```




    'Cello'




```python
# Replace a sequence of letters, which appears twice
'hitchhiker'.replace('hi', 'ma')
```




    'matchmaker'



Once a name is bound to a string value, methods can be invoked on that name as well. The name is still bound to the original string, so a new name is needed to capture the result. 


```python
sharp = 'edged'
hot = sharp.replace('ed', 'ma')
print('sharp:', sharp)
print('hot:', hot)
```

    sharp: edged
    hot: magma


You can call functions on the results of other functions.  For example,

    max(abs(-5), abs(3))

has value 5.  Similarly, you can invoke methods on the results of other method (or function) calls.


```python
# Calling replace on the output of another call to replace
'train'.replace('t', 'ing').replace('in', 'de')
```




    'degrade'



Here's a picture of how Python evaluates a "chained" method call like that:

<img src="chaining_method_calls.jpg" alt="In 'train'.replace('t', 'ing').replace('in', 'de'), 'train'.replace('t', 'ing')' is ran first and evaluates to 'ingrain'. Then 'ingrain'.replace('in', 'de') is evaluated to 'degrade'"/>

Other string methods do not take any arguments at all, because the original string is all that's needed to compute the result. In these cases, parentheses are still needed, but there's nothing in between the parentheses. Here are some methods that take no arguments:

|Method name|Value|
|-|-|
|`lower`|a lowercased version of the string|
|`upper`|an uppercased version of the string|
|`capitalize`|a version with the first letter capitalized|
|`title`|a version with the first letter of every word capitalized||



```python
'national university of singapore'.title()
```




    'National University Of Singapore'



All these string methods are useful, but most programmers don't memorize their names or how to use them.  Instead, people usually just search the internet for documentation and examples. A complete [list of string methods](https://docs.python.org/3/library/stdtypes.html#string-methods) appears in the Python language documentation. [Stack Overflow](http://stackoverflow.com) has a huge database of answered questions that often demonstrate how to use these methods to achieve various ends.

### 2.2. Converting to and from Strings

Strings and numbers are different *types* of values, even when a string contains the digits of a number. For example, evaluating the following cell causes an error because an integer cannot be added to a string.


```python
8 + "8"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[62], line 1
    ----> 1 8 + "8"


    TypeError: unsupported operand type(s) for +: 'int' and 'str'


However, there are built-in functions to convert numbers to strings and strings to numbers. 

|Function name|Effect|Example|
|-|-|-|
|`int`  |Converts a string of digits and perhaps a negative sign to an integer (`int`) value|`int("42")`|
|`float`|Converts a string of digits and perhaps a negative sign and decimal point to a decimal (`float`) value|`float("4.2")`|
|`str`  |  Converts any value to a string (`str`) value|`str(42)`|

Try to predict what the following cell will evaluate to, then evaluate it.


```python
8 + int("8")
```

Suppose you're writing a program that looks for dates in a text, and you want your program to find the amount of time that elapsed between two years it has identified.  It doesn't make sense to subtract two texts, but you can first convert the text containing the years into numbers.

**Question 2.2.1.** <br/> Finish the code below to compute the number of years that elapsed between `one_year` and `another_year`.  Don't just write the numbers `1618` and `1648` (or `30`); use a conversion function to turn the given text data into numbers.


```python
# Some text data:
one_year = "1618"
another_year = "1648"

# Complete the next line.  Note that we can't just write:
#   another_year - one_year
# If you don't see why, try seeing what happens when you
# write that here.
difference = int(another_year) - int(one_year)
difference
```




    30



**Question 2.2.2.** Use `replace` and `int` together to compute the difference between the the year 753 BC ([the founding of Rome](https://en.wikipedia.org/wiki/Ancient_Rome)) and the year 410 AD ([the sack of Rome](https://en.wikipedia.org/wiki/Sack_of_Rome_(410)). Try not to use any numbers in your solution, but instead manipulate the strings that are provided.

*Hint*: It's ok to be off by one year. In historical calendars, there is no year zero, but astronomical calendars do include [year zero](https://en.wikipedia.org/wiki/Year_zero) to simplify calculations.


```python
founded = 'BC 753'
sacked = 'AD 410'
start = int(founded.replace('BC ', '-'))
end = int(sacked.replace('AD ', ''))
print('Ancient Rome lasted for about', end-start, 'years from', founded, 'to', sacked)
```

    Ancient Rome lasted for about 1163 years from BC 753 to AD 410


### 2.3. Strings as function arguments

String values, like numbers, can be arguments to functions and can be returned by functions.  The function `len` takes a single string as its argument and returns the number of characters in the string: its **len**gth.  

Note that it doesn't count *words*. `len("one small step for man")` is 22, not 5.

**Question 2.3.1.**  <br/> Use `len` to find out the number of characters in the very long string in the next cell.  (It's the first sentence of the English translation of the French [Declaration of the Rights of Man](http://avalon.law.yale.edu/18th_century/rightsof.asp).)  The length of a string is the total number of characters in it, including things like spaces and punctuation.  Assign `sentence_length` to that number.


```python
a_very_long_sentence = "The representatives of the French people, organized as a National Assembly, believing that the ignorance, neglect, or contempt of the rights of man are the sole cause of public calamities and of the corruption of governments, have determined to set forth in a solemn declaration the natural, unalienable, and sacred rights of man, in order that this declaration, being constantly before all the members of the Social body, shall remind them continually of their rights and duties; in order that the acts of the legislative power, as well as those of the executive power, may be compared at any moment with the objects and purposes of all political institutions and may thus be more respected, and, lastly, in order that the grievances of the citizens, based hereafter upon simple and incontestable principles, shall tend to the maintenance of the constitution and redound to the happiness of all."
sentence_length = len(a_very_long_sentence)
sentence_length
```




    896



## 3. Importing code

> What has been will be again,  
> what has been done will be done again;  
> there is nothing new under the sun.

Most programming involves work that is very similar to work that has been done before.  Since writing code is time consuming, it's good to rely on others' published code when you can.  Rather than copy-pasting, Python allows us to **import** other code, creating a **module** that contains all of the names created by that code.

Python includes many useful modules that are just an `import` away.  We'll look at the `math` module as a first example. The `math` module is extremely useful in computing mathematical expressions in Python. 

Suppose we want to very accurately compute the area of a circle with radius 5 meters.  For that, we need the constant $\pi$, which is roughly 3.14.  Conveniently, the `math` module has `pi` defined for us:


```python
import math
radius = 5
area_of_circle = radius**2 * math.pi
area_of_circle
```

`pi` is defined inside `math`, and the way that we access names that are inside modules is by writing the module's name, then a dot, then the name of the thing we want:

    <module name>.<name>
    
In order to use a module at all, we must first write the statement `import <module name>`.  That statement creates a module object with things like `pi` in it and then assigns the name `math` to that module.  Above we have done that for `math`.

**Question 3.1.** <br/> `math` also provides the name `e` for the base of the natural logarithm, which is roughly 2.71.  Compute $e^{\pi}-\pi$, giving it the name `near_twenty`.


```python
near_twenty = math.e**math.pi - math.pi
near_twenty
```

![XKCD](http://imgs.xkcd.com/comics/e_to_the_pi_minus_pi.png)

### 3.1. Importing functions

**Modules** can provide other named things, including **functions**.  For example, `math` provides the name `sin` for the sine function.  Having imported `math` already, we can write `math.sin(3)` to compute the sine of 3.  (Note that this sine function considers its argument to be in [radians](https://en.wikipedia.org/wiki/Radian), not degrees.  180 degrees are equivalent to $\pi$ radians.)

**Question 3.1.1.** <br/> A $\frac{\pi}{4}$-radian (45-degree) angle forms a right triangle with equal base and height, pictured below.  If the hypotenuse (the radius of the circle in the picture) is 1, then the height is $\sin(\frac{\pi}{4})$.  Compute that using `sin` and `pi` from the `math` module.  Give the result the name `sine_of_pi_over_four`.

<img src="http://mathworld.wolfram.com/images/eps-gif/TrigonometryAnglesPi4_1000.gif">

(Source: [Wolfram MathWorld](http://mathworld.wolfram.com/images/eps-gif/TrigonometryAnglesPi4_1000.gif))


```python
sine_of_pi_over_four = math.sin(math.pi/4)
sine_of_pi_over_four
```

For your reference, here are some more examples of functions from the `math` module.

Note how different methods take in different number of arguments. Often, the documentation of the module will provide information on how many arguments is required for each method.


```python
# Calculating factorials.
math.factorial(5)
```


```python
# Calculating logarithms (the logarithm of 8 in base 2).
# The result is 3 because 2 to the power of 3 is 8.
math.log(8, 2)
```


```python
# Calculating square roots.
math.sqrt(5)
```

There's many variations of how we can import methods from outside sources. For example, we can import just a specific method from an outside source, we can rename a library we import, and we can import every single method from a whole library. 


```python
# Importing just cos and pi from math.
# Now, we don't have to use "math." before these names.
from math import cos, pi
print(cos(pi))
```


```python
# We can nickname math as something else, if we don't want to type the name math
import math as m
m.log(m.pi)
```


```python
# Lastly, we can import ever thing from math and use all of its names without "math."
from math import *
log(pi)
```

##### A function that displays a picture
People have written Python functions that do very cool and complicated things, like crawling web pages for data, transforming videos, or learning functions from data.  Now that you can import things, when you want to do something with code, first check to see if someone else has done it for you.

Let's see an example of a function that's used for downloading and displaying pictures.

The module `IPython.display` provides a function called `Image`.  The `Image` function takes a single argument, a string that is the URL of the image on the web.  It returns an *image* value that this Jupyter notebook understands how to display.  To display an image, make it the value of the last expression in a cell, just like you'd display a number or a string.

**Question 3.1.2.** <br/> In the next cell, import the module `IPython.display` and use its `Image` function to display the image at this URL:

    https://www.kdnuggets.com/wp-content/uploads/Fig1-Abisiga-top-10-lists-data-science.jpg

Give the name `ds` to the output of the call to `Image`.  (It might take a few seconds to load the image.)

*Hint*: A link isn't any special type of data type in Python. You can't just write a link into Python and expect it to work; you need to type the link in as a specific data type. Which one makes the most sense?


```python
# Import the module IPython.display. Watch out for capitalization.
import IPython.display
# Replace the ... with a call to the Image function
# in the IPython.display module, which should produce
# a picture.
ds = IPython.display.Image('https://www.kdnuggets.com/wp-content/uploads/Fig1-Abisiga-top-10-lists-data-science.jpg')
ds
```


    ---------------------------------------------------------------------------

    HTTPError                                 Traceback (most recent call last)

    Cell In[27], line 6
          2 import IPython.display
          3 # Replace the ... with a call to the Image function
          4 # in the IPython.display module, which should produce
          5 # a picture.
    ----> 6 ds = IPython.display.Image('https://www.kdnuggets.com/wp-content/uploads/Fig1-Abisiga-top-10-lists-data-science.jpg')
          7 ds


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/site-packages/IPython/core/display.py:970, in Image.__init__(self, data, url, filename, format, embed, width, height, retina, unconfined, metadata, alt)
        968 self.unconfined = unconfined
        969 self.alt = alt
    --> 970 super(Image, self).__init__(data=data, url=url, filename=filename,
        971         metadata=metadata)
        973 if self.width is None and self.metadata.get('width', {}):
        974     self.width = metadata['width']


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/site-packages/IPython/core/display.py:327, in DisplayObject.__init__(self, data, url, filename, metadata)
        324 elif self.metadata is None:
        325     self.metadata = {}
    --> 327 self.reload()
        328 self._check_data()


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/site-packages/IPython/core/display.py:1005, in Image.reload(self)
       1003 """Reload the raw data from file or URL."""
       1004 if self.embed:
    -> 1005     super(Image,self).reload()
       1006     if self.retina:
       1007         self._retina_shape()


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/site-packages/IPython/core/display.py:358, in DisplayObject.reload(self)
        355 elif self.url is not None:
        356     # Deferred import
        357     from urllib.request import urlopen
    --> 358     response = urlopen(self.url)
        359     data = response.read()
        360     # extract encoding from header, if there is one:


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/urllib/request.py:216, in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        214 else:
        215     opener = _opener
    --> 216 return opener.open(url, data, timeout)


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/urllib/request.py:525, in OpenerDirector.open(self, fullurl, data, timeout)
        523 for processor in self.process_response.get(protocol, []):
        524     meth = getattr(processor, meth_name)
    --> 525     response = meth(req, response)
        527 return response


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/urllib/request.py:634, in HTTPErrorProcessor.http_response(self, request, response)
        631 # According to RFC 2616, "2xx" code indicates that the client's
        632 # request was successfully received, understood, and accepted.
        633 if not (200 <= code < 300):
    --> 634     response = self.parent.error(
        635         'http', request, response, code, msg, hdrs)
        637 return response


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/urllib/request.py:563, in OpenerDirector.error(self, proto, *args)
        561 if http_err:
        562     args = (dict, 'default', 'http_error_default') + orig_args
    --> 563     return self._call_chain(*args)


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/urllib/request.py:496, in OpenerDirector._call_chain(self, chain, kind, meth_name, *args)
        494 for handler in handlers:
        495     func = getattr(handler, meth_name)
    --> 496     result = func(*args)
        497     if result is not None:
        498         return result


    File ~/opt/anaconda3/envs/ds310/lib/python3.10/urllib/request.py:643, in HTTPDefaultErrorHandler.http_error_default(self, req, fp, code, msg, hdrs)
        642 def http_error_default(self, req, fp, code, msg, hdrs):
    --> 643     raise HTTPError(req.full_url, code, msg, hdrs, fp)


    HTTPError: HTTP Error 403: Forbidden


## 4. Arrays

Up to now, we haven't done much that you couldn't do yourself by hand, without going through the trouble of learning Python.  Computers are most useful when a small amount of code performs a lot of work by *performing the same action* to *many different things*.

For example, in the time it takes you to calculate the 18% tip on a restaurant bill, a laptop can calculate 18% tips for every restaurant bill paid by every human on Earth that day.  (That's if you're pretty fast at doing arithmetic in your head!)

**Arrays** are how we put many values in one place so that we can operate on them as a group. For example, if `billions_of_numbers` is an array of numbers, the expression

    .18 * billions_of_numbers

gives a new array of numbers that's the result of multiplying each number in `billions_of_numbers` by .18 (18%).  Arrays are not limited to numbers; we can also put all the words in a book into an array of strings.

Concretely, an array is a **collection of values of the same type**, like a column in an Excel spreadsheet. 

<img src="excel_array.jpg" alt="In Excel, columns of text are like array of strings for tables.  The same can be said about numbers (ints, floats) as well">

### 4.1. Making arrays
You can type in the data that goes in an array yourself, but that's not typically how programs work. Normally, we create arrays by loading them from an external source, like a data file.

First, though, let's learn how to start from scratch. Execute the following cell so that all the names from the `datascience` module are available to you. The documentation for this module is available at [http://data8.org/datascience](http://data8.org/datascience/).


```python
from datascience import *
```

Now, to create an array, call the function `make_array`.  Each argument you pass to `make_array` will be in the array it returns.  Run this cell to see an example:


```python
make_array(0.125, 4.75, -1.3)
```




    array([ 0.125,  4.75 , -1.3  ])



Each value in an array (in the above case, the numbers 0.125, 4.75, and -1.3) is called an *element* or *item* of that array.

Arrays themselves are also values, just like numbers and strings.  That means you can assign them names or use them as arguments to functions.

**Question 4.1.1.** <br/>Make an array containing the numbers 1, 2, and 3, in that order.  Name it `small_numbers`.


```python
small_numbers = make_array(1, 2, 3)
small_numbers
```




    array([1, 2, 3])



**Question 4.1.2.** <br/> Make an array containing the numbers 0, 1, -1, $\pi$, and $e$, in that order.  Name it `interesting_numbers`.  *Hint:* How did you get the values $\pi$ and $e$ earlier?  You can refer to them in exactly the same way here.


```python
from math import *
interesting_numbers = make_array(0, 1, -1, pi, e)
interesting_numbers
```




    array([ 0.        ,  1.        , -1.        ,  3.14159265,  2.71828183])



**Question 4.1.3.** <br/> Make an array containing the five strings `"Hello"`, `","`, `" "`, `"world"`, and `"!"`.  (The third one is a single space inside quotes.)  Name it `hello_world_components`.

*Note:* If you print `hello_world_components`, you'll notice some extra information in addition to its contents: `dtype='<U5'`.  That's just NumPy's extremely cryptic way of saying that the things in the array are strings.


```python
hello_world_components = make_array("Hello", ",", " ", "world", "!")
hello_world_components
```




    array(['Hello', ',', ' ', 'world', '!'],
          dtype='<U5')



The `join` method of a string takes an array of strings as its argument and puts all of the elements together into one string. Try it:


```python
'-'.join(make_array('a', 'b', 'c', 'd'))
```




    'a-b-c-d'



**Question 4.1.4.** <br/> Assign `separator` to a string so that the name `hello` is bound to the string `'Hello, world!'` in the cell below.


```python
separator = ""
hello = separator.join(hello_world_components)
hello
```




    'Hello, world!'



#### 4.1.1.  `np.arange`
Arrays are provided by a package called [NumPy](http://www.numpy.org/) (pronounced "NUM-pie" or, if you prefer to pronounce things incorrectly, "NUM-pee").  The package is called `numpy`, but it's standard to rename it `np` for brevity.  You can do that with:

    import numpy as np

Very often in data science, we want to work with many numbers that are evenly spaced within some range.  NumPy provides a special function for this called `arange`.  `np.arange(start, stop, space)` produces an array with all the numbers starting at `start` and counting up by `space`, stopping before `stop` is reached.

For example, the value of `np.arange(1, 6, 2)` is an array with elements 1, 3, and 5 -- it starts at 1 and counts up by 2, then stops before 6.  In other words, it's equivalent to `make_array(1, 3, 5)`.

`np.arange(4, 9, 1)` is an array with elements 4, 5, 6, 7, and 8.  (It doesn't contain 9 because `np.arange` stops *before* the stop value is reached.)

**Question 4.1.1.1.** <br/>Import `numpy` as `np` and then use `np.arange` to create an array with the multiples of 99 from 0 up to (**and including**) 9999.  (So its elements are 0, 99, 198, 297, etc.)


```python
import numpy as np
multiples_of_99 = np.arange(0, 10000, 99)
multiples_of_99
```




    array([   0,   99,  198,  297,  396,  495,  594,  693,  792,  891,  990,
           1089, 1188, 1287, 1386, 1485, 1584, 1683, 1782, 1881, 1980, 2079,
           2178, 2277, 2376, 2475, 2574, 2673, 2772, 2871, 2970, 3069, 3168,
           3267, 3366, 3465, 3564, 3663, 3762, 3861, 3960, 4059, 4158, 4257,
           4356, 4455, 4554, 4653, 4752, 4851, 4950, 5049, 5148, 5247, 5346,
           5445, 5544, 5643, 5742, 5841, 5940, 6039, 6138, 6237, 6336, 6435,
           6534, 6633, 6732, 6831, 6930, 7029, 7128, 7227, 7326, 7425, 7524,
           7623, 7722, 7821, 7920, 8019, 8118, 8217, 8316, 8415, 8514, 8613,
           8712, 8811, 8910, 9009, 9108, 9207, 9306, 9405, 9504, 9603, 9702,
           9801, 9900, 9999])



##### Temperature readings
NOAA (the US National Oceanic and Atmospheric Administration) operates weather stations that measure surface temperatures at different sites around the United States.  The hourly readings are [publicly available](http://www.ncdc.noaa.gov/qclcd/QCLCD?prior=N).

Suppose we download all the hourly data from the Oakland, California site for the month of December 2015.  To analyze the data, we want to know when each reading was taken, but we find that the data don't include the timestamps of the readings (the time at which each one was taken).

However, we know the first reading was taken at the first instant of December 2015 (midnight on December 1st) and each subsequent reading was taken exactly 1 hour after the last.

**Question 4.1.1.2.** <br/>Create an array of the *time, in seconds, since the start of the month* at which each hourly reading was taken.  Name it `collection_times`.

*Hint 1:* There were 31 days in December, which is equivalent to ($31 \times 24$) hours or ($31 \times 24 \times 60 \times 60$) seconds.  So your array should have $31 \times 24$ elements in it.

*Hint 2:* The `len` function works on arrays, too.  Check its length and make sure it has $31 \times 24$ elements.


```python
collection_times = np.arange(0, 31*24*3600, 3600)
collection_times
```




    array([      0,    3600,    7200,   10800,   14400,   18000,   21600,
             25200,   28800,   32400,   36000,   39600,   43200,   46800,
             50400,   54000,   57600,   61200,   64800,   68400,   72000,
             75600,   79200,   82800,   86400,   90000,   93600,   97200,
            100800,  104400,  108000,  111600,  115200,  118800,  122400,
            126000,  129600,  133200,  136800,  140400,  144000,  147600,
            151200,  154800,  158400,  162000,  165600,  169200,  172800,
            176400,  180000,  183600,  187200,  190800,  194400,  198000,
            201600,  205200,  208800,  212400,  216000,  219600,  223200,
            226800,  230400,  234000,  237600,  241200,  244800,  248400,
            252000,  255600,  259200,  262800,  266400,  270000,  273600,
            277200,  280800,  284400,  288000,  291600,  295200,  298800,
            302400,  306000,  309600,  313200,  316800,  320400,  324000,
            327600,  331200,  334800,  338400,  342000,  345600,  349200,
            352800,  356400,  360000,  363600,  367200,  370800,  374400,
            378000,  381600,  385200,  388800,  392400,  396000,  399600,
            403200,  406800,  410400,  414000,  417600,  421200,  424800,
            428400,  432000,  435600,  439200,  442800,  446400,  450000,
            453600,  457200,  460800,  464400,  468000,  471600,  475200,
            478800,  482400,  486000,  489600,  493200,  496800,  500400,
            504000,  507600,  511200,  514800,  518400,  522000,  525600,
            529200,  532800,  536400,  540000,  543600,  547200,  550800,
            554400,  558000,  561600,  565200,  568800,  572400,  576000,
            579600,  583200,  586800,  590400,  594000,  597600,  601200,
            604800,  608400,  612000,  615600,  619200,  622800,  626400,
            630000,  633600,  637200,  640800,  644400,  648000,  651600,
            655200,  658800,  662400,  666000,  669600,  673200,  676800,
            680400,  684000,  687600,  691200,  694800,  698400,  702000,
            705600,  709200,  712800,  716400,  720000,  723600,  727200,
            730800,  734400,  738000,  741600,  745200,  748800,  752400,
            756000,  759600,  763200,  766800,  770400,  774000,  777600,
            781200,  784800,  788400,  792000,  795600,  799200,  802800,
            806400,  810000,  813600,  817200,  820800,  824400,  828000,
            831600,  835200,  838800,  842400,  846000,  849600,  853200,
            856800,  860400,  864000,  867600,  871200,  874800,  878400,
            882000,  885600,  889200,  892800,  896400,  900000,  903600,
            907200,  910800,  914400,  918000,  921600,  925200,  928800,
            932400,  936000,  939600,  943200,  946800,  950400,  954000,
            957600,  961200,  964800,  968400,  972000,  975600,  979200,
            982800,  986400,  990000,  993600,  997200, 1000800, 1004400,
           1008000, 1011600, 1015200, 1018800, 1022400, 1026000, 1029600,
           1033200, 1036800, 1040400, 1044000, 1047600, 1051200, 1054800,
           1058400, 1062000, 1065600, 1069200, 1072800, 1076400, 1080000,
           1083600, 1087200, 1090800, 1094400, 1098000, 1101600, 1105200,
           1108800, 1112400, 1116000, 1119600, 1123200, 1126800, 1130400,
           1134000, 1137600, 1141200, 1144800, 1148400, 1152000, 1155600,
           1159200, 1162800, 1166400, 1170000, 1173600, 1177200, 1180800,
           1184400, 1188000, 1191600, 1195200, 1198800, 1202400, 1206000,
           1209600, 1213200, 1216800, 1220400, 1224000, 1227600, 1231200,
           1234800, 1238400, 1242000, 1245600, 1249200, 1252800, 1256400,
           1260000, 1263600, 1267200, 1270800, 1274400, 1278000, 1281600,
           1285200, 1288800, 1292400, 1296000, 1299600, 1303200, 1306800,
           1310400, 1314000, 1317600, 1321200, 1324800, 1328400, 1332000,
           1335600, 1339200, 1342800, 1346400, 1350000, 1353600, 1357200,
           1360800, 1364400, 1368000, 1371600, 1375200, 1378800, 1382400,
           1386000, 1389600, 1393200, 1396800, 1400400, 1404000, 1407600,
           1411200, 1414800, 1418400, 1422000, 1425600, 1429200, 1432800,
           1436400, 1440000, 1443600, 1447200, 1450800, 1454400, 1458000,
           1461600, 1465200, 1468800, 1472400, 1476000, 1479600, 1483200,
           1486800, 1490400, 1494000, 1497600, 1501200, 1504800, 1508400,
           1512000, 1515600, 1519200, 1522800, 1526400, 1530000, 1533600,
           1537200, 1540800, 1544400, 1548000, 1551600, 1555200, 1558800,
           1562400, 1566000, 1569600, 1573200, 1576800, 1580400, 1584000,
           1587600, 1591200, 1594800, 1598400, 1602000, 1605600, 1609200,
           1612800, 1616400, 1620000, 1623600, 1627200, 1630800, 1634400,
           1638000, 1641600, 1645200, 1648800, 1652400, 1656000, 1659600,
           1663200, 1666800, 1670400, 1674000, 1677600, 1681200, 1684800,
           1688400, 1692000, 1695600, 1699200, 1702800, 1706400, 1710000,
           1713600, 1717200, 1720800, 1724400, 1728000, 1731600, 1735200,
           1738800, 1742400, 1746000, 1749600, 1753200, 1756800, 1760400,
           1764000, 1767600, 1771200, 1774800, 1778400, 1782000, 1785600,
           1789200, 1792800, 1796400, 1800000, 1803600, 1807200, 1810800,
           1814400, 1818000, 1821600, 1825200, 1828800, 1832400, 1836000,
           1839600, 1843200, 1846800, 1850400, 1854000, 1857600, 1861200,
           1864800, 1868400, 1872000, 1875600, 1879200, 1882800, 1886400,
           1890000, 1893600, 1897200, 1900800, 1904400, 1908000, 1911600,
           1915200, 1918800, 1922400, 1926000, 1929600, 1933200, 1936800,
           1940400, 1944000, 1947600, 1951200, 1954800, 1958400, 1962000,
           1965600, 1969200, 1972800, 1976400, 1980000, 1983600, 1987200,
           1990800, 1994400, 1998000, 2001600, 2005200, 2008800, 2012400,
           2016000, 2019600, 2023200, 2026800, 2030400, 2034000, 2037600,
           2041200, 2044800, 2048400, 2052000, 2055600, 2059200, 2062800,
           2066400, 2070000, 2073600, 2077200, 2080800, 2084400, 2088000,
           2091600, 2095200, 2098800, 2102400, 2106000, 2109600, 2113200,
           2116800, 2120400, 2124000, 2127600, 2131200, 2134800, 2138400,
           2142000, 2145600, 2149200, 2152800, 2156400, 2160000, 2163600,
           2167200, 2170800, 2174400, 2178000, 2181600, 2185200, 2188800,
           2192400, 2196000, 2199600, 2203200, 2206800, 2210400, 2214000,
           2217600, 2221200, 2224800, 2228400, 2232000, 2235600, 2239200,
           2242800, 2246400, 2250000, 2253600, 2257200, 2260800, 2264400,
           2268000, 2271600, 2275200, 2278800, 2282400, 2286000, 2289600,
           2293200, 2296800, 2300400, 2304000, 2307600, 2311200, 2314800,
           2318400, 2322000, 2325600, 2329200, 2332800, 2336400, 2340000,
           2343600, 2347200, 2350800, 2354400, 2358000, 2361600, 2365200,
           2368800, 2372400, 2376000, 2379600, 2383200, 2386800, 2390400,
           2394000, 2397600, 2401200, 2404800, 2408400, 2412000, 2415600,
           2419200, 2422800, 2426400, 2430000, 2433600, 2437200, 2440800,
           2444400, 2448000, 2451600, 2455200, 2458800, 2462400, 2466000,
           2469600, 2473200, 2476800, 2480400, 2484000, 2487600, 2491200,
           2494800, 2498400, 2502000, 2505600, 2509200, 2512800, 2516400,
           2520000, 2523600, 2527200, 2530800, 2534400, 2538000, 2541600,
           2545200, 2548800, 2552400, 2556000, 2559600, 2563200, 2566800,
           2570400, 2574000, 2577600, 2581200, 2584800, 2588400, 2592000,
           2595600, 2599200, 2602800, 2606400, 2610000, 2613600, 2617200,
           2620800, 2624400, 2628000, 2631600, 2635200, 2638800, 2642400,
           2646000, 2649600, 2653200, 2656800, 2660400, 2664000, 2667600,
           2671200, 2674800])



### 4.2. Working with single elements of arrays ("indexing")
Let's work with a more interesting dataset.  The next cell creates an array called `population` that includes estimated world populations in every year from **1950** to roughly the present.  (The estimates come from the [US Census Bureau website](http://www.census.gov/population/international/data/worldpop/table_population.php).)

Rather than type in the data manually, we've loaded them from a file on your computer called `world_population.csv`.  You'll learn how to do that next week.


```python
# Don't worry too much about what goes on in this cell.
from datascience import *
population = Table.read_table("world_population.csv").column("Population")
population
```




    array([2557628654, 2594939877, 2636772306, 2682053389, 2730228104,
           2782098943, 2835299673, 2891349717, 2948137248, 3000716593,
           3043001508, 3083966929, 3140093217, 3209827882, 3281201306,
           3350425793, 3420677923, 3490333715, 3562313822, 3637159050,
           3712697742, 3790326948, 3866568653, 3942096442, 4016608813,
           4089083233, 4160185010, 4232084578, 4304105753, 4379013942,
           4451362735, 4534410125, 4614566561, 4695736743, 4774569391,
           4856462699, 4940571232, 5027200492, 5114557167, 5201440110,
           5288955934, 5371585922, 5456136278, 5538268316, 5618682132,
           5699202985, 5779440593, 5857972543, 5935213248, 6012074922,
           6088571383, 6165219247, 6242016348, 6318590956, 6395699509,
           6473044732, 6551263534, 6629913759, 6709049780, 6788214394,
           6866332358, 6944055583, 7022349283, 7101027895, 7178722893,
           7256490011])



Here's how we get the first element of `population`, which is the world population in the first year in the dataset, 1950.


```python
population.item(0)
```




    2557628654



The value of that expression is the number 2557628654 (around 2.5 billion), because that's the first thing in the array `population`.

Notice that we wrote `.item(0)`, not `.item(1)`, to get the first element.  This is a weird convention in computer science.  0 is called the *index* of the first item.  It's the number of elements that appear *before* that item.  So 3 is the index of the 4th item.

Here are some more examples.  In the examples, we've given names to the things we get out of `population`.  Read and run each cell.


```python
# The third element in the array is the population
# in 1952.
population_1952 = population.item(2)
population_1952
```




    2636772306




```python
# The thirteenth element in the array is the population
# in 1962 (which is 1950 + 12).
population_1962 = population.item(12)
population_1962
```




    3140093217




```python
# The 66th element is the population in 2015.
population_2015 = population.item(65)
population_2015
```




    7256490011




```python
# The array has only 66 elements, so this doesn't work.
# (There's no element with 66 other elements before it.)
population_2016 = population.item(66)
population_2016
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[69], line 3
          1 # The array has only 66 elements, so this doesn't work.
          2 # (There's no element with 66 other elements before it.)
    ----> 3 population_2016 = population.item(66)
          4 population_2016


    IndexError: index 66 is out of bounds for axis 0 with size 66



```python
# Since make_array returns an array, we can call .item(3)
# on its output to get its 4th element, just like we
# "chained" together calls to the method "replace" earlier.
make_array(-1, -3, 4, -2).item(3)
```

**Question 4.2.1.** <br/> Set `population_1973` to the world population in 1973, by getting the appropriate element from `population` using `item`.


```python
population_1973 = population.item(23)
population_1973
```




    3942096442



### 4.3. Doing something to every element of an array
Arrays are primarily useful for doing the same operation many times, so we don't often have to use `.item` and work with single elements.

##### Logarithms
Here is one simple question we might ask about world population:

> How big was the population in *orders of magnitude* in each year?

The logarithm function is one way of measuring how big a number is. The logarithm (base 10) of a number increases by 1 every time we multiply the number by 10. It's like a measure of how many decimal digits the number has, or how big it is in orders of magnitude.

We could try to answer our question like this, using the `log10` function from the `math` module and the `item` method you just saw:


```python
import math

population_1950_magnitude = math.log10(population.item(0))
population_1951_magnitude = math.log10(population.item(1))
population_1952_magnitude = math.log10(population.item(2))
population_1953_magnitude = math.log10(population.item(3))
make_array(population_1950_magnitude, population_1951_magnitude, population_1952_magnitude, population_1953_magnitude)
# and so on and so forth
```




    array([ 9.40783749,  9.4141273 ,  9.42107263,  9.42846742])



But this is tedious and doesn't really take advantage of the fact that we are using a computer.

Instead, **NumPy** provides its own version of `log10` that takes the logarithm of each element of an array.  It takes a single array of numbers as its argument.  It returns an array of the same length, where the first element of the result is the logarithm of the first element of the argument, and so on.

**Question 4.3.1.** <br/> Use it to compute the logarithms of the world population in every year.  Give the result (an array of 66 numbers) the name `population_magnitudes`.  Your code should be very short. Although the function names are the same, the module name (such as `module.function(...)`) will differentiate which one Python will use.


```python
population_magnitudes = np.log10(population)
population_magnitudes
```




    array([ 9.40783749,  9.4141273 ,  9.42107263,  9.42846742,  9.43619893,
            9.44437257,  9.45259897,  9.46110062,  9.4695477 ,  9.47722498,
            9.48330217,  9.48910971,  9.49694254,  9.50648175,  9.51603288,
            9.5251    ,  9.53411218,  9.54286695,  9.55173218,  9.56076229,
            9.56968959,  9.57867667,  9.58732573,  9.59572724,  9.60385954,
            9.61162595,  9.61911264,  9.62655434,  9.63388293,  9.64137633,
            9.64849299,  9.6565208 ,  9.66413091,  9.67170374,  9.67893421,
            9.68632006,  9.69377717,  9.70132621,  9.70880804,  9.7161236 ,
            9.72336995,  9.73010253,  9.73688521,  9.74337399,  9.74963446,
            9.75581413,  9.7618858 ,  9.76774733,  9.77343633,  9.77902438,
            9.7845154 ,  9.78994853,  9.7953249 ,  9.80062024,  9.80588805,
            9.81110861,  9.81632507,  9.82150788,  9.82666101,  9.83175555,
            9.83672482,  9.84161319,  9.84648243,  9.85132122,  9.85604719,
            9.8607266 ])



<img src="array_logarithm.jpg" alt="Elementwise application of the logarithm function">

This is called *elementwise* application of the function, since it operates separately on each element of the array it's called on.  The textbook's section on arrays has a useful list of NumPy functions that are designed to work elementwise, like `np.log10`.

##### Arithmetic
Arithmetic also works elementwise on arrays.  For example, you can divide all the population numbers by 1 billion to get numbers in billions:


```python
population_in_billions = population / 1000000000
population_in_billions
```




    array([ 2.55762865,  2.59493988,  2.63677231,  2.68205339,  2.7302281 ,
            2.78209894,  2.83529967,  2.89134972,  2.94813725,  3.00071659,
            3.04300151,  3.08396693,  3.14009322,  3.20982788,  3.28120131,
            3.35042579,  3.42067792,  3.49033371,  3.56231382,  3.63715905,
            3.71269774,  3.79032695,  3.86656865,  3.94209644,  4.01660881,
            4.08908323,  4.16018501,  4.23208458,  4.30410575,  4.37901394,
            4.45136274,  4.53441012,  4.61456656,  4.69573674,  4.77456939,
            4.8564627 ,  4.94057123,  5.02720049,  5.11455717,  5.20144011,
            5.28895593,  5.37158592,  5.45613628,  5.53826832,  5.61868213,
            5.69920299,  5.77944059,  5.85797254,  5.93521325,  6.01207492,
            6.08857138,  6.16521925,  6.24201635,  6.31859096,  6.39569951,
            6.47304473,  6.55126353,  6.62991376,  6.70904978,  6.78821439,
            6.86633236,  6.94405558,  7.02234928,  7.10102789,  7.17872289,
            7.25649001])



You can do the same with addition, subtraction, multiplication, and exponentiation (`**`). For example, you can calculate a tip on several restaurant bills at once (in this case just 3):


```python
restaurant_bills = make_array(20.12, 39.90, 31.01)
print("Restaurant bills:\t", restaurant_bills)
tips = .2 * restaurant_bills
print("Tips:\t\t\t", tips)
```

    Restaurant bills:	 [ 20.12  39.9   31.01]
    Tips:			 [ 4.024  7.98   6.202]


<img src="array_multiplication.jpg" alt="Elementwise application of multiplication in Python" >

**Question 4.3.2.** <br/> Suppose the total charge at a restaurant is the original bill plus the tip.  That means we can multiply the original bill by 1.2 to get the total charge.  Compute the total charge for each bill in `restaurant_bills`.


```python
total_charges = restaurant_bills *1.2
total_charges
```




    array([ 24.144,  47.88 ,  37.212])



**Question 4.3.3.** <br/> `more_restaurant_bills.csv` contains 100,000 bills!  Compute the total charge for each one.  How is your code different?


```python
more_restaurant_bills = Table.read_table("more_restaurant_bills.csv").column("Bill")
more_total_charges = more_restaurant_bills * 1.2
more_total_charges
```




    array([ 20.244,  20.892,  12.216, ...,  19.308,  18.336,  35.664])



The function `sum` takes a single array of numbers as its argument.  It returns the sum of all the numbers in that array (so it returns a single number, not an array).

**Question 4.3.4.** <br/>What was the sum of all the bills in `more_restaurant_bills`, *including tips*?


```python
sum_of_bills = sum(more_total_charges)
sum_of_bills
```




    1795730.0640000193



**Question 4.3.5.** <br/>The powers of 2 ($2^0 = 1$, $2^1 = 2$, $2^2 = 4$, etc) arise frequently in computer science.  (For example, you may have noticed that storage on smartphones or USBs come in powers of 2, like 16 GB, 32 GB, or 64 GB.)  Use `np.arange` and the exponentiation operator `**` to compute the first 15 powers of 2, starting from `2^0`.


```python
powers_of_2 = 2 ** np.arange(0, 15)
powers_of_2
```




    array([    1,     2,     4,     8,    16,    32,    64,   128,   256,
             512,  1024,  2048,  4096,  8192, 16384])



## 5. Submission

To submit your assignment, please download your notebook as a .ipynb file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as... > Notebook (.ipynb) or HTML (.html). Then, upload your files under "Lab 2" on Canvas.


```python

```
