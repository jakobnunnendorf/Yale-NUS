# YSC2239 Midterm Spring 2023

### This exam consists of 3 questions.

### Time: March 2nd 7:05pm - 8:25pm (No submission will be accepted after the deadline)

### Venue:  Science Centre Classroom 17 at Yale-NUS College

## Table of Contents

### [1. Tennis serving strategy (40 points)](#q1)

### [2. Testing hypotheses (40 points)](#q2)

### [3. Housing price vs fertility rate (20 points)](#q3)



For all problems that you must write explanations and sentences for, you must provide your answer in the designated space. Moreover, please be sure to not re-assign variables throughout the notebook! For example, if you use max_value in your answer to one question, do not reassign it later on. Otherwise, you may fail the test!


```python
# Run this cell, but please don't change it.

# These lines import the Numpy and Datascience modules.
import numpy as np
import random
from datascience import *

# These lines do some fancy plotting magic.
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)
```

### 1. Tennis serving strategy (40 points) <a id='q1'></a>

Data, analytics, and machine learning have become ubiquitous around sports over the past decade or so. One of the values of sports analytics is in opposition scouting, for example what an optimal strategy might look like. Today we are going to analyse the serving stragegy in tennis sport (Please refer to the [link](https://www.keithprowse.co.uk/news-and-blog/2019/01/02/tennis-terminology-explained/) on Essential terminology of tennis sport). 

In tennis, the player serving the ball has an advantage because they are able to start the **point** — giving them strategic choices like where to place the ball and what type of spin to hit with. The serve is also one of the fastest shots in tennis. Not only that, but the server gets two chances at their serve in case they miss the first. So first serves are typically hit with the intent to give the server a strong advantage. They are powerful and sometimes erratic, but the server can take some risk because there is always a second chance with the second serve. As second serves have no such safety net, they are by and large delivered with more caution. 

Most players, amateur and professional, employ two different serves: players typically use their first serve to play a ball faster and into tighter, more advantageous windows, such as out wide or down the center of the “T,” where the service boxes meet. The point is to gain an advantage by forcing a weak return, pushing the opponent into an undesirable court position, or winning the point uncontested through an **ace**. The second serve, then, is typically played more safely. Players tend to use play a slower ball into windows with a higher margin for error. The player will still attempt to gain an advantage by controlling the opponent’s court position, but the advantage tends to be smaller than on a successful first serve.

The strategy for players comes down to maximizing their chance of winning a point on serve. Let's call this `p_Won`. To get the explicit formula we need a few more quantities:

`p_1stIn` : the probability of first serve landing it in,

`p_1stWon`: the probability of winning on first serve given that it lands in. 

Similarly, `p_2ndIn` and `p_2ndWon` be the corresponding probabilities on the second serve. Note by assigning an initial random value to these names, we are just declaring these variables in Python. The values of these variables can be updated.


```python
# Don't change this cell; just run it
p_1stIn = random.random()
p_1stWon = random.random()
p_2ndIn = random.random()
p_2ndWon = random.random()
```

Question 1.1 What is a player’s winning probability `p_Won` when serving? (5 points)


```python
#Answer_to_Question 1.1 
p_Won = ...
p_Won
```

Question 1.2 Here is the average statistics on Top 50 men's player. They win 73.6 percent of service points when the first serve lands in, compared to 57.5 percent when the second serve lands in. But first serve lands in just 61.9 percent of the time, compared to 91.1 percent of second serves. So what is the winning probability for the average player (denoted by `p_ave_Won`)? Show your calculation formula (5 points)


```python
#Answer_to_Question 1.2
p_ave_Won = ...
p_ave_Won
```

Question 1.3 Even for great players, risk control isn’t always easy. Sometimes the control of the second serve can get so out of whack that they are better off sticking with their first serve. So two-first-serve strategy is an alternative option in tennis. What is a player's winning probability  when serving using two-first-serve strategy (denoted by `p_Won_alt`)? (5 points)


```python
#Answer_to_Question 1.3
p_Won_alt = ...
p_Won_alt
```

Question 1.4 We can make a rational decision regarding the two serving strategies (i.e common one and the alternative two-first-serve strategy) based upon the calculation of the corresponding winning probabilities. Please help provide one example where two-first-serve is more preferable than the common strategy. (5 points)


```python
#Answer_to_Question 1.4
...

```

There is a Github repository containing excellent data on ATP matches over the timeframe. One CSV file regarding ATP Matches in 2022 is downloaded from the Github.


```python
# Don't change this cell; just run it
atp = Table.read_table("atp_2022.csv")
atp.show(5)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>tourney_id</th> <th>tourney_name</th> <th>surface</th> <th>draw_size</th> <th>tourney_level</th> <th>tourney_date</th> <th>match_num</th> <th>winner_id</th> <th>winner_seed</th> <th>winner_entry</th> <th>winner_name</th> <th>winner_hand</th> <th>winner_ht</th> <th>winner_ioc</th> <th>winner_age</th> <th>loser_id</th> <th>loser_seed</th> <th>loser_entry</th> <th>loser_name</th> <th>loser_hand</th> <th>loser_ht</th> <th>loser_ioc</th> <th>loser_age</th> <th>score</th> <th>best_of</th> <th>round</th> <th>minutes</th> <th>w_ace</th> <th>w_df</th> <th>w_svpt</th> <th>w_1stIn</th> <th>w_1stWon</th> <th>w_2ndWon</th> <th>w_SvGms</th> <th>w_bpSaved</th> <th>w_bpFaced</th> <th>l_ace</th> <th>l_df</th> <th>l_svpt</th> <th>l_1stIn</th> <th>l_1stWon</th> <th>l_2ndWon</th> <th>l_SvGms</th> <th>l_bpSaved</th> <th>l_bpFaced</th> <th>winner_rank</th> <th>winner_rank_points</th> <th>loser_rank</th> <th>loser_rank_points</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2022-8888 </td> <td>Atp Cup     </td> <td>Hard   </td> <td>16       </td> <td>A            </td> <td>20220103    </td> <td>300      </td> <td>200000   </td> <td>nan        </td> <td>nan         </td> <td>Felix Auger Aliassime</td> <td>R          </td> <td>193      </td> <td>CAN       </td> <td>21.4      </td> <td>105138  </td> <td>nan       </td> <td>nan        </td> <td>Roberto Bautista Agut</td> <td>R         </td> <td>183     </td> <td>ESP      </td> <td>33.7     </td> <td>7-6(3) 6-3       </td> <td>3      </td> <td>F    </td> <td>129    </td> <td>15   </td> <td>6   </td> <td>78    </td> <td>51     </td> <td>38      </td> <td>14      </td> <td>11     </td> <td>10       </td> <td>11       </td> <td>0    </td> <td>2   </td> <td>70    </td> <td>50     </td> <td>32      </td> <td>7       </td> <td>10     </td> <td>3        </td> <td>5        </td> <td>11         </td> <td>3308              </td> <td>19        </td> <td>2260             </td>
        </tr>
        <tr>
            <td>2022-8888 </td> <td>Atp Cup     </td> <td>Hard   </td> <td>16       </td> <td>A            </td> <td>20220103    </td> <td>299      </td> <td>133430   </td> <td>nan        </td> <td>nan         </td> <td>Denis Shapovalov     </td> <td>L          </td> <td>185      </td> <td>CAN       </td> <td>22.7      </td> <td>105807  </td> <td>nan       </td> <td>nan        </td> <td>Pablo Carreno Busta  </td> <td>R         </td> <td>188     </td> <td>ESP      </td> <td>30.4     </td> <td>6-4 6-3          </td> <td>3      </td> <td>F    </td> <td>98     </td> <td>7    </td> <td>2   </td> <td>78    </td> <td>49     </td> <td>34      </td> <td>16      </td> <td>10     </td> <td>8        </td> <td>9        </td> <td>1    </td> <td>0   </td> <td>50    </td> <td>33     </td> <td>21      </td> <td>8       </td> <td>9      </td> <td>3        </td> <td>6        </td> <td>14         </td> <td>2475              </td> <td>20        </td> <td>2230             </td>
        </tr>
        <tr>
            <td>2022-8888 </td> <td>Atp Cup     </td> <td>Hard   </td> <td>16       </td> <td>A            </td> <td>20220103    </td> <td>298      </td> <td>105138   </td> <td>nan        </td> <td>nan         </td> <td>Roberto Bautista Agut</td> <td>R          </td> <td>183      </td> <td>ESP       </td> <td>33.7      </td> <td>128034  </td> <td>nan       </td> <td>nan        </td> <td>Hubert Hurkacz       </td> <td>R         </td> <td>196     </td> <td>POL      </td> <td>24.8     </td> <td>7-6(6) 2-6 7-6(5)</td> <td>3      </td> <td>SF   </td> <td>164    </td> <td>1    </td> <td>2   </td> <td>96    </td> <td>64     </td> <td>50      </td> <td>20      </td> <td>16     </td> <td>1        </td> <td>4        </td> <td>24   </td> <td>3   </td> <td>120   </td> <td>80     </td> <td>62      </td> <td>20      </td> <td>16     </td> <td>6        </td> <td>7        </td> <td>19         </td> <td>2260              </td> <td>9         </td> <td>3706             </td>
        </tr>
        <tr>
            <td>2022-8888 </td> <td>Atp Cup     </td> <td>Hard   </td> <td>16       </td> <td>A            </td> <td>20220103    </td> <td>297      </td> <td>105807   </td> <td>nan        </td> <td>nan         </td> <td>Pablo Carreno Busta  </td> <td>R          </td> <td>188      </td> <td>ESP       </td> <td>30.4      </td> <td>126591  </td> <td>nan       </td> <td>nan        </td> <td>Jan Zielinski        </td> <td>R         </td> <td>nan     </td> <td>POL      </td> <td>25.1     </td> <td>6-2 6-1          </td> <td>3      </td> <td>SF   </td> <td>53     </td> <td>6    </td> <td>0   </td> <td>45    </td> <td>33     </td> <td>25      </td> <td>8       </td> <td>8      </td> <td>0        </td> <td>0        </td> <td>2    </td> <td>1   </td> <td>38    </td> <td>27     </td> <td>17      </td> <td>1       </td> <td>7      </td> <td>4        </td> <td>8        </td> <td>20         </td> <td>2230              </td> <td>860       </td> <td>18               </td>
        </tr>
        <tr>
            <td>2022-8888 </td> <td>Atp Cup     </td> <td>Hard   </td> <td>16       </td> <td>A            </td> <td>20220103    </td> <td>296      </td> <td>106421   </td> <td>nan        </td> <td>nan         </td> <td>Daniil Medvedev      </td> <td>R          </td> <td>198      </td> <td>RUS       </td> <td>25.8      </td> <td>200000  </td> <td>nan       </td> <td>nan        </td> <td>Felix Auger Aliassime</td> <td>R         </td> <td>193     </td> <td>CAN      </td> <td>21.4     </td> <td>6-4 6-0          </td> <td>3      </td> <td>SF   </td> <td>68     </td> <td>6    </td> <td>4   </td> <td>41    </td> <td>25     </td> <td>22      </td> <td>10      </td> <td>8      </td> <td>0        </td> <td>0        </td> <td>6    </td> <td>2   </td> <td>48    </td> <td>35     </td> <td>22      </td> <td>4       </td> <td>8      </td> <td>3        </td> <td>7        </td> <td>2          </td> <td>8640              </td> <td>11        </td> <td>3308             </td>
        </tr>
    </tbody>
</table>
<p>... (2912 rows omitted)</p>


Quesiton 1.5 Understanding data is normally our first step for data science project. Even though it may be straightforward for some columns, others are a bit technical. So you can refer to the explanation page (with the [link](https://github.com/JeffSackmann/tennis_atp/blob/master/matches_data_dictionary.txt)). Please take a few minutes to understand the data and show how can we calculate `p_1stIn`, `p_1stWon`, `p_2ndIn` and `p_2ndWon` in any given match based on the csv provided? (10 points)

Hint: **double faults** count against the player’s proper (or legal in tennis terminology) second-serve cases.


```python
#Answer_to_Question 1.5
...

```

Question 1.6 For any male player in the csv, we would like to know his performance over the year, in particular the results about `p_1stIn`, `p_1stWon`, `p_2ndIn` and `p_2ndWon`. Please help define a function called `perfmance_2022`. It takes the name of the player as the only arguments and returns an array with those four probabilitities. (10 points)

Hint: for any match listed in the file, any participating player can be the winner or the loser of the match.


```python
#Answer_to_Question 1.6
def performance_2022(player_name):
    ...

# An example call to your function:
performance_2022('Rafael Nadal')
```

### 2. Testing hypotheses (40 points) <a id='q2'></a>

An area code in US is defined to be a three digit number from 200-999 inclusive. In reality, many of these area codes are not in use, but for this question we'll simplify things and assume they all are. 

Steve gets a lot of spam calls. Throughout these questions, you should assume that the area code of Steve is 781. Steve suspects that there's a higher chance that the spammers are using his area code (781) to trick him into thinking it's someone from his area calling him. John thinks that this is not the case, and that spammers are just choosing area codes of the spam calls at random from all possible area codes (Remember, for this question we’re assuming the possible area codes are 200-999, inclusive). Steve wants to test his claim using the 50 spam calls he received in the past month. Here's a dataset of the area codes of the 50 spam calls he received in the past month


```python
# Don't change this cell; just run it
spam = Table.read_table('spam.csv')
spam.show(5)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Area Code</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>891      </td>
        </tr>
        <tr>
            <td>924      </td>
        </tr>
        <tr>
            <td>516      </td>
        </tr>
        <tr>
            <td>512      </td>
        </tr>
        <tr>
            <td>328      </td>
        </tr>
    </tbody>
</table>
<p>... (45 rows omitted)</p>


Question 2.1 What is our **null hypothesis**? (5 points)


```python
#Answer_to_Question 2.1 
null_hypothesis = ...
null_hypothesis
```

Our **alternative hypothesis** is that there's a higher chance of getting a spam call with an area code of 781. **Suppose you decide to use the number of times you see the area code 781 in 50 spam calls as your test statistic.**

Question 2.2 Write a function called `simulate` that generates exactly one simulated value of your test statistic under the null hypothesis.  It should take no arguments and simulate 50 area codes (with replacement) under the assumption that the result of each area is sampled from the range 200-999 inclusive with equal probability. Your function should return the number of times you saw the 781 area code in those 50 random spam calls. (10 points)



```python
#Answer_to_Question 2.2
def simulate():
    ...
    
# Call your function to make sure it works
simulate()
```

Question 2.3 Generate 10,000 simulated values of the number of times you see the area code 781 in 50 random spam calls. Assign test_statistics_under_null to an array that stores the result of each of these trials. (5 points)


```python
#Answer_to_Question 2.3
test_statistics_under_null = ...
repetitions = ...

...
    
test_statistics_under_null
```

Question 2.4 Using the results from Question 2.3, generate a histogram of the empirical distribution of the number of times you saw the area code 781 in your simulation. NOTE: Use the provided bins when making the histogram. (5 points)


```python
#Answer_to_Question 2.4
bins = np.arange(0,5,1) # Use these provided bins
...
```

Question 2.5 Compute an empirical P-value for this test. (10 points)


```python
#Answer_to_Question 2.5
# First calculate the observed value of the test statistic from the `spam` table.
observed_val = ...
p_value = ...
p_value
```

Question 2.6 Suppose you use a P-value cutoff of 1%. What do you conclude from the hypothesis test? Why? (5 points)


```python
#Answer_to_Question 2.6
testing_conclusion = ...
conclusion_reason = ...
testing_conclusion
conclusion_reason
```

### 3. Housing price vs fertility rate (20 points) <a id='q3'></a>

In this question, we are going to make a brief investigation on hot topics in Singapore. Fertility rate issue has been discussed quite a lot since 1980s, but the situation has not been turning better. Singapore’s total fertility rate (TFR) hit a historic low of 1.05 in 2022. While it's a complicated issue and involves quite a few evolving factors to consider, housing seems to be one of the factors. So here we just use simple method we have learned so far to see the correlation (if any) between them.

With the csv files provided, we have yearly TFRs from 1960 until 2021, the quarterly HDB index from the first quarter of 1990 to the third quarter of 2022 and the priviate property index (landed, non-landed and all) from the first quarter of 1975 until the fourth quarter of 2022).


```python
# Don't change this cell; just run it
TFR_raw = Table.read_table('TFR2021.csv')
hdb = Table.read_table('hdb-index.csv')
ura = Table.read_table('private-index.csv')
```

Question 3.1. Data manipulation is an important part of data science project. In our case, we have yearly TFRs and also quarterly housing indices. In addition, for private housing, there are three difference indices due the difference between landed and non-landed. To make the situation simple, there are three assumptions: First, we use the average of four quarters to be the housing indices for the corresponding year. Second, we ingore landed private housing as it's a niche asset class, so we only use non-landed residential entries. Third, as we can only calculate if there are data available, so we only consider the maximum shared year range in all three files. Create a table `final_raw` consists of four columns in the special order `Year`, `TFR`,`HDB_Index` and `Private_Index`. (10 points) 


```python
#Answer_to_Question 3.1
Year = ...
TFR = ...
HDB_Index = ...
Private_Index = ...
final_raw = ...
final_raw
```

Question 2. For the relationship between `TFR` and `HDB_Index`, what is the correlation coeifficient, slope and intercept? In addition, please draw the scatter plot of the data, as well as the regression line. (5 points)


```python
#Answer_to_Question 3.2
TFR_HDB_correlation = ...
TFR_HDB_slope = ...
TFR_HDB_intercept = ...

```

Question 3. For the relationship between `TFR` and `Private_Index`, what is the correlation coeifficient, slope and intercept? In addition, please draw the scatter plot of the data, as well as the regression line. (5 points)


```python
#Answer_to_Question 3.3
TFR_URA_correlation = ...
TFR_URA_slope = ...
TFR_URA_intercept = ...


```

### Final Words  (0 point) <a id='q4'></a>

If there was any question that you thought was ambiguous and required clarification to be answerable, please identify the question and state your assumptions. Be warned: We only plan to consider this information if we agree that the question was erroneous or ambiguous and we consider your assumption reasonable. (0 point)


```python
#Comment


```

### No more questions and Submission <a id='q5'></a>

To submit your answer, please download your notebook as a .ipynb and .html file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as ... > Notebook (.ipynb) or HTML (.html). Then, upload both files under "Mid-term" in the Assignments on Canvas.
