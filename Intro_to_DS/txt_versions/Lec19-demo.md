# Lecture 19



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from scipy.optimize import minimize
import sklearn.linear_model as lm

# plt.rcParams['figure.figsize'] = (4, 4)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['lines.linewidth'] = 3
sns.set()
```

## Motivating Logistic Regression

In this lecture, we will look at data from the 2017-18 NBA season.


```python
df = pd.read_csv('nba.csv')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SEASON_ID</th>
      <th>TEAM_ID</th>
      <th>TEAM_ABBREVIATION</th>
      <th>TEAM_NAME</th>
      <th>GAME_ID</th>
      <th>GAME_DATE</th>
      <th>MATCHUP</th>
      <th>WL</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>...</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>PLUS_MINUS</th>
      <th>VIDEO_AVAILABLE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22017</td>
      <td>1610612744</td>
      <td>GSW</td>
      <td>Golden State Warriors</td>
      <td>21700002</td>
      <td>2017-10-17</td>
      <td>GSW vs. HOU</td>
      <td>L</td>
      <td>240</td>
      <td>43</td>
      <td>...</td>
      <td>35</td>
      <td>41</td>
      <td>34</td>
      <td>5</td>
      <td>9</td>
      <td>17</td>
      <td>25</td>
      <td>121</td>
      <td>-1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22017</td>
      <td>1610612745</td>
      <td>HOU</td>
      <td>Houston Rockets</td>
      <td>21700002</td>
      <td>2017-10-17</td>
      <td>HOU @ GSW</td>
      <td>W</td>
      <td>240</td>
      <td>47</td>
      <td>...</td>
      <td>33</td>
      <td>43</td>
      <td>28</td>
      <td>9</td>
      <td>5</td>
      <td>13</td>
      <td>16</td>
      <td>122</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22017</td>
      <td>1610612738</td>
      <td>BOS</td>
      <td>Boston Celtics</td>
      <td>21700001</td>
      <td>2017-10-17</td>
      <td>BOS @ CLE</td>
      <td>L</td>
      <td>240</td>
      <td>36</td>
      <td>...</td>
      <td>37</td>
      <td>46</td>
      <td>24</td>
      <td>11</td>
      <td>4</td>
      <td>12</td>
      <td>24</td>
      <td>99</td>
      <td>-3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22017</td>
      <td>1610612739</td>
      <td>CLE</td>
      <td>Cleveland Cavaliers</td>
      <td>21700001</td>
      <td>2017-10-17</td>
      <td>CLE vs. BOS</td>
      <td>W</td>
      <td>240</td>
      <td>38</td>
      <td>...</td>
      <td>41</td>
      <td>50</td>
      <td>19</td>
      <td>3</td>
      <td>4</td>
      <td>17</td>
      <td>25</td>
      <td>102</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22017</td>
      <td>1610612750</td>
      <td>MIN</td>
      <td>Minnesota Timberwolves</td>
      <td>21700011</td>
      <td>2017-10-18</td>
      <td>MIN @ SAS</td>
      <td>L</td>
      <td>240</td>
      <td>37</td>
      <td>...</td>
      <td>31</td>
      <td>42</td>
      <td>23</td>
      <td>7</td>
      <td>4</td>
      <td>13</td>
      <td>16</td>
      <td>99</td>
      <td>-8</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 29 columns</p>
</div>



We are eventually going to want to perform **binary classification**, which is where we predict a 1 or 0. A reasonable thing to do given this data is to predict whether or not a team wins. Right now, the `WL` column consists of `"W"` and `"L"`.


```python
df['WL']
```




    0       L
    1       W
    2       L
    3       W
    4       L
           ..
    2455    W
    2456    W
    2457    L
    2458    W
    2459    L
    Name: WL, Length: 2460, dtype: object



Let's fix that, so that wins are encoded as `1` and losses are encoded as `0`.


```python
df["WON"] = df["WL"]
df["WON"] = df["WON"].replace("W", 1)
df["WON"] = df["WON"].replace("L", 0)
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SEASON_ID</th>
      <th>TEAM_ID</th>
      <th>TEAM_ABBREVIATION</th>
      <th>TEAM_NAME</th>
      <th>GAME_ID</th>
      <th>GAME_DATE</th>
      <th>MATCHUP</th>
      <th>WL</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>...</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>PLUS_MINUS</th>
      <th>VIDEO_AVAILABLE</th>
      <th>WON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22017</td>
      <td>1610612744</td>
      <td>GSW</td>
      <td>Golden State Warriors</td>
      <td>21700002</td>
      <td>2017-10-17</td>
      <td>GSW vs. HOU</td>
      <td>L</td>
      <td>240</td>
      <td>43</td>
      <td>...</td>
      <td>41</td>
      <td>34</td>
      <td>5</td>
      <td>9</td>
      <td>17</td>
      <td>25</td>
      <td>121</td>
      <td>-1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22017</td>
      <td>1610612745</td>
      <td>HOU</td>
      <td>Houston Rockets</td>
      <td>21700002</td>
      <td>2017-10-17</td>
      <td>HOU @ GSW</td>
      <td>W</td>
      <td>240</td>
      <td>47</td>
      <td>...</td>
      <td>43</td>
      <td>28</td>
      <td>9</td>
      <td>5</td>
      <td>13</td>
      <td>16</td>
      <td>122</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22017</td>
      <td>1610612738</td>
      <td>BOS</td>
      <td>Boston Celtics</td>
      <td>21700001</td>
      <td>2017-10-17</td>
      <td>BOS @ CLE</td>
      <td>L</td>
      <td>240</td>
      <td>36</td>
      <td>...</td>
      <td>46</td>
      <td>24</td>
      <td>11</td>
      <td>4</td>
      <td>12</td>
      <td>24</td>
      <td>99</td>
      <td>-3</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22017</td>
      <td>1610612739</td>
      <td>CLE</td>
      <td>Cleveland Cavaliers</td>
      <td>21700001</td>
      <td>2017-10-17</td>
      <td>CLE vs. BOS</td>
      <td>W</td>
      <td>240</td>
      <td>38</td>
      <td>...</td>
      <td>50</td>
      <td>19</td>
      <td>3</td>
      <td>4</td>
      <td>17</td>
      <td>25</td>
      <td>102</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22017</td>
      <td>1610612750</td>
      <td>MIN</td>
      <td>Minnesota Timberwolves</td>
      <td>21700011</td>
      <td>2017-10-18</td>
      <td>MIN @ SAS</td>
      <td>L</td>
      <td>240</td>
      <td>37</td>
      <td>...</td>
      <td>42</td>
      <td>23</td>
      <td>7</td>
      <td>4</td>
      <td>13</td>
      <td>16</td>
      <td>99</td>
      <td>-8</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>



There is a row for each team and each game in this dataset. It contains the `FG_PCT` (field goal percentage) for each team per game. Note field goal percentage is the ratio of field goals made to field goals attempted. A higher field goal percentage denotes higher efficiency. In basketball, a FG_PCT of 50% or above is considered a good percentage.


```python
df['FG_PCT']
```




    0       0.538
    1       0.485
    2       0.409
    3       0.458
    4       0.435
            ...  
    2455    0.472
    2456    0.553
    2457    0.484
    2458    0.591
    2459    0.402
    Name: FG_PCT, Length: 2460, dtype: float64



Let's try and get the field goal percentage difference between two teams in a single game. We will then try and use this value to predict whether or not a team wins, given their field goal percentage difference.

This data cleaning and EDA is not the point of this lecture, but you may want to come back to this and try and understand it.


```python
one_team = df.groupby("GAME_ID").first()
opponent = df.groupby("GAME_ID").last()
games = one_team.merge(opponent, left_index = True, right_index = True, suffixes = ["", "_OPP"])
games["FG_PCT_DIFF"] = games["FG_PCT"] - games["FG_PCT_OPP"]
games['WON'] = games['WL'].replace('L', 0).replace('W', 1)
games = games[['TEAM_NAME', 'MATCHUP', 'WON', 'FG_PCT_DIFF']]
games.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TEAM_NAME</th>
      <th>MATCHUP</th>
      <th>WON</th>
      <th>FG_PCT_DIFF</th>
    </tr>
    <tr>
      <th>GAME_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21700001</th>
      <td>Boston Celtics</td>
      <td>BOS @ CLE</td>
      <td>0</td>
      <td>-0.049</td>
    </tr>
    <tr>
      <th>21700002</th>
      <td>Golden State Warriors</td>
      <td>GSW vs. HOU</td>
      <td>0</td>
      <td>0.053</td>
    </tr>
    <tr>
      <th>21700003</th>
      <td>Charlotte Hornets</td>
      <td>CHA @ DET</td>
      <td>0</td>
      <td>-0.030</td>
    </tr>
    <tr>
      <th>21700004</th>
      <td>Indiana Pacers</td>
      <td>IND vs. BKN</td>
      <td>1</td>
      <td>0.041</td>
    </tr>
    <tr>
      <th>21700005</th>
      <td>Orlando Magic</td>
      <td>ORL vs. MIA</td>
      <td>1</td>
      <td>0.042</td>
    </tr>
  </tbody>
</table>
</div>



To have a better visualizaion, we are going to use seaborn package. Let's start by looking at a `sns.jointplot` of `FG_PCT_DIFF` and `WON`.


```python
sns.jointplot(data = games, x = "FG_PCT_DIFF", y = "WON");
```


    
![png](Lec19-demo_files/Lec19-demo_13_0.png)
    


A reasonable thing to do here might be to model the **probability of winning, given `FG_PCT_DIFF`**.

We already know how to use ordinary least squares, right? Why not use it here?

We'll also jitter the data, to get a better picture of what it looks like. But the line of best fit that's being drawn is on top of the original, non-jittered data.


```python
sns.jointplot(data = games, x = "FG_PCT_DIFF", y = "WON", 
              y_jitter = 0.1, 
              kind="reg", 
              ci = None,
              joint_kws={'line_kws':{'color':'green'}});
```


    
![png](Lec19-demo_files/Lec19-demo_15_0.png)
    


The green line drawn is a valid model. It is the line that minimizes MSE for this set of $x$ (`FG_PCT_DIFF`) and $y$ (`WON`) data.

But there are some issues:
- The outputs are bigger than 1 and less than 0. How do we interpret that?
- This is very susceptible to outliers. See:


```python
games2 = games.copy()
games2.iloc[0] = ['hello', 'hello', 1, 120]
games2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TEAM_NAME</th>
      <th>MATCHUP</th>
      <th>WON</th>
      <th>FG_PCT_DIFF</th>
    </tr>
    <tr>
      <th>GAME_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21700001</th>
      <td>hello</td>
      <td>hello</td>
      <td>1</td>
      <td>120.000</td>
    </tr>
    <tr>
      <th>21700002</th>
      <td>Golden State Warriors</td>
      <td>GSW vs. HOU</td>
      <td>0</td>
      <td>0.053</td>
    </tr>
    <tr>
      <th>21700003</th>
      <td>Charlotte Hornets</td>
      <td>CHA @ DET</td>
      <td>0</td>
      <td>-0.030</td>
    </tr>
    <tr>
      <th>21700004</th>
      <td>Indiana Pacers</td>
      <td>IND vs. BKN</td>
      <td>1</td>
      <td>0.041</td>
    </tr>
    <tr>
      <th>21700005</th>
      <td>Orlando Magic</td>
      <td>ORL vs. MIA</td>
      <td>1</td>
      <td>0.042</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.jointplot(data = games2, x = "FG_PCT_DIFF", y = "WON", 
              y_jitter = 0.1, 
              kind="reg", 
              ci = False,
              joint_kws={'line_kws':{'color':'green'}});
```


    
![png](Lec19-demo_files/Lec19-demo_18_0.png)
    


We need a better model. Let's try:

- binned the $x$ axis.
- took the average $y$ value for each bin on the $x$ axis.

Here, we will formally partition the $x$-axis into 20 bins.


```python
bins = pd.cut(games["FG_PCT_DIFF"], 20)
bins
```




    GAME_ID
    21700001    (-0.0648, -0.0382]
    21700002      (0.0416, 0.0682]
    21700003    (-0.0382, -0.0116]
    21700004       (0.015, 0.0416]
    21700005      (0.0416, 0.0682]
                       ...        
    21701226        (0.175, 0.201]
    21701227      (0.0682, 0.0948]
    21701228       (0.015, 0.0416]
    21701229    (-0.0914, -0.0648]
    21701230     (-0.118, -0.0914]
    Name: FG_PCT_DIFF, Length: 1230, dtype: category
    Categories (20, interval[float64, right]): [(-0.252, -0.224] < (-0.224, -0.198] < (-0.198, -0.171] < (-0.171, -0.145] ... (0.175, 0.201] < (0.201, 0.228] < (0.228, 0.254] < (0.254, 0.281]]




```python
games["bin"] = [(b.left + b.right) / 2 for b in bins]
games
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TEAM_NAME</th>
      <th>MATCHUP</th>
      <th>WON</th>
      <th>FG_PCT_DIFF</th>
      <th>bin</th>
    </tr>
    <tr>
      <th>GAME_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21700001</th>
      <td>Boston Celtics</td>
      <td>BOS @ CLE</td>
      <td>0</td>
      <td>-0.049</td>
      <td>-0.0515</td>
    </tr>
    <tr>
      <th>21700002</th>
      <td>Golden State Warriors</td>
      <td>GSW vs. HOU</td>
      <td>0</td>
      <td>0.053</td>
      <td>0.0549</td>
    </tr>
    <tr>
      <th>21700003</th>
      <td>Charlotte Hornets</td>
      <td>CHA @ DET</td>
      <td>0</td>
      <td>-0.030</td>
      <td>-0.0249</td>
    </tr>
    <tr>
      <th>21700004</th>
      <td>Indiana Pacers</td>
      <td>IND vs. BKN</td>
      <td>1</td>
      <td>0.041</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <th>21700005</th>
      <td>Orlando Magic</td>
      <td>ORL vs. MIA</td>
      <td>1</td>
      <td>0.042</td>
      <td>0.0549</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>21701226</th>
      <td>New Orleans Pelicans</td>
      <td>NOP vs. SAS</td>
      <td>1</td>
      <td>0.189</td>
      <td>0.1880</td>
    </tr>
    <tr>
      <th>21701227</th>
      <td>Oklahoma City Thunder</td>
      <td>OKC vs. MEM</td>
      <td>1</td>
      <td>0.069</td>
      <td>0.0815</td>
    </tr>
    <tr>
      <th>21701228</th>
      <td>LA Clippers</td>
      <td>LAC vs. LAL</td>
      <td>0</td>
      <td>0.017</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <th>21701229</th>
      <td>Utah Jazz</td>
      <td>UTA @ POR</td>
      <td>0</td>
      <td>-0.090</td>
      <td>-0.0781</td>
    </tr>
    <tr>
      <th>21701230</th>
      <td>Houston Rockets</td>
      <td>HOU @ SAC</td>
      <td>0</td>
      <td>-0.097</td>
      <td>-0.1047</td>
    </tr>
  </tbody>
</table>
<p>1230 rows × 5 columns</p>
</div>



We now know which `"bin"` each game belongs to. We can plot the average `WON` for each bin.


```python
win_rates_by_bin = games.groupby("bin")["WON"].mean()
win_rates_by_bin
```




    bin
    -0.2380    0.000000
    -0.2110    0.000000
    -0.1845    0.000000
    -0.1580    0.000000
    -0.1315    0.000000
    -0.1047    0.033898
    -0.0781    0.083333
    -0.0515    0.148438
    -0.0249    0.363636
     0.0017    0.505747
     0.0283    0.705128
     0.0549    0.792793
     0.0815    0.907407
     0.1079    0.984615
     0.1345    1.000000
     0.1615    1.000000
     0.1880    1.000000
     0.2410    1.000000
     0.2675    1.000000
    Name: WON, dtype: float64




```python
plt.plot(win_rates_by_bin, 'r')
```




    [<matplotlib.lines.Line2D at 0x15e2d3210>]




    
![png](Lec19-demo_files/Lec19-demo_24_1.png)
    



```python
sns.jointplot(data = games, x = "FG_PCT_DIFF", y = "WON", 
              y_jitter = 0.1, 
              kind="reg", 
              ci=False,
              joint_kws={'line_kws':{'color':'green'}});
plt.plot(win_rates_by_bin, 'r', linewidth = 5);
```


    
![png](Lec19-demo_files/Lec19-demo_25_0.png)
    


It seems like our red graph of averages does a much better job at matching the data than our simple linear regression line.

**What is this graph of averages plotting?** Since the $y$ axis is only 0s and 1s, and we took the mean of the $y$-values in each bin for a given $x$, the graph of average is plotting the **proportion** of times a team won, given their `FG_PCT_DIFF`. Remember, `WON = 1` each time a team won.

**Logistic regression aims to model the probability of an observation belonging to class 1, given some set of features.**

For now, consider these questions:

What are:
1. $P(Y = 1 | X = 0.0283)$? 
2. $P(Y = 0 | X = 0.0283)$? 
3. $\frac{P(Y = 1 | X = 0.0283)}{P(Y = 0 | X = 0.0283)}$? In other words, how many wins are there for each loss?


```python
win_rates_by_bin
```




    bin
    -0.2380    0.000000
    -0.2110    0.000000
    -0.1845    0.000000
    -0.1580    0.000000
    -0.1315    0.000000
    -0.1047    0.033898
    -0.0781    0.083333
    -0.0515    0.148438
    -0.0249    0.363636
     0.0017    0.505747
     0.0283    0.705128
     0.0549    0.792793
     0.0815    0.907407
     0.1079    0.984615
     0.1345    1.000000
     0.1615    1.000000
     0.1880    1.000000
     0.2410    1.000000
     0.2675    1.000000
    Name: WON, dtype: float64



The **odds** of an event are defined as the probability that it happens divided by the probability that it doesn't happen.

If some event happens with probability $p$, then $\text{odds}(p) = \frac{p}{1-p}$.


```python
odds_by_bin = win_rates_by_bin / (1 - win_rates_by_bin)
odds_by_bin
```




    bin
    -0.2380     0.000000
    -0.2110     0.000000
    -0.1845     0.000000
    -0.1580     0.000000
    -0.1315     0.000000
    -0.1047     0.035088
    -0.0781     0.090909
    -0.0515     0.174312
    -0.0249     0.571429
     0.0017     1.023256
     0.0283     2.391304
     0.0549     3.826087
     0.0815     9.800000
     0.1079    64.000000
     0.1345          inf
     0.1615          inf
     0.1880          inf
     0.2410          inf
     0.2675          inf
    Name: WON, dtype: float64



If we plot the odds of these probabilities, they look exponential:


```python
plt.plot(odds_by_bin);
```


    
![png](Lec19-demo_files/Lec19-demo_32_0.png)
    


But if we take the log of these odds:


```python
plt.plot(np.log(odds_by_bin));
```

    /opt/homebrew/lib/python3.11/site-packages/pandas/core/arraylike.py:402: RuntimeWarning: divide by zero encountered in log
      result = getattr(ufunc, method)(*inputs, **kwargs)



    
![png](Lec19-demo_files/Lec19-demo_34_1.png)
    


We noticed that the **log-odds grows linearly with $x$**. 

In the lecture slides, we formalize what this means, and how this allows us to arrive at the `sigma` function above.

## The Logistic Function

In the slides, we show that our model is

$$P(Y = 1 | x) = \sigma(x^T \theta)$$

where $$\sigma(t) = \frac{1}{1 + e^{-t}}$$

Let's explore the shape of the logistic function, $\sigma$.


```python
def sigma(t):
    return 1 / (1 + np.exp(-t))
```


```python
plt.plot(win_rates_by_bin, 'r', linewidth = 5);
x = win_rates_by_bin.index
plt.plot(x, sigma(x * 30), 'black', linewidth = 5);
plt.xlabel('FG_PCT_DIFF')
plt.ylabel('WON');
```


    
![png](Lec19-demo_files/Lec19-demo_37_0.png)
    


First, the vanilla curve $\sigma(x)$:


```python
x = np.linspace(-5,5,50)
plt.plot(x, sigma(x));
plt.xlabel('x')
plt.ylabel(r'$\frac{1}{1 + e^{-x}}$');
```


    
![png](Lec19-demo_files/Lec19-demo_39_0.png)
    


Now, we look at $\sigma(\theta_1 x)$, for several values of $\theta_1$:


```python
def flatten(li): 
    return [item for sub in li for item in sub]
fig, axes = plt.subplots(2, 3)
flatten(axes)
```




    [<Axes: >, <Axes: >, <Axes: >, <Axes: >, <Axes: >, <Axes: >]




    
![png](Lec19-demo_files/Lec19-demo_41_1.png)
    



```python
def flatten(li): 
    return [item for sub in li for item in sub]

bs = [-2, -1, -0.5, 2, 1, 0.5]
xs = np.linspace(-10, 10, 100)

fig, axes = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(10, 6))
for ax, b in zip(flatten(axes), bs):
    ys = sigma(xs * b)
    ax.plot(xs, ys)
    ax.set_title(r'$ \theta_1 = $' + str(b))

# add a big axes, hide frame
fig.add_subplot(111, frameon=False) #111 the same as 1,1,1
# hide tick and tick label of the big axes
plt.tick_params(labelcolor='none', top=False, bottom=False,
                left=False, right=False)
plt.grid(False)
plt.xlabel('$x$')
plt.ylabel(r'$ \frac{1}{1+\exp(-\theta_1 \cdot x)} $')
plt.tight_layout()
plt.savefig('sigmoids.png')
```


    
![png](Lec19-demo_files/Lec19-demo_42_0.png)
    


Let's explore the shape of $\sigma(\theta_0 + \theta_1x)$, for different values of $\theta_0, \theta_1$. There's quite a bit going on here, so let's use `plotly`.


```python
fig = go.Figure()
for theta1 in [-1,1, 5]:
    for theta0 in [-2, 0, 2]:
        fig.add_trace(go.Scatter(name=f"{theta0} + {theta1} x", x=xs, y=sigma(theta0 + theta1*xs)))
fig
```


        <script type="text/javascript">
        window.PlotlyConfig = {MathJaxConfig: 'local'};
        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
        if (typeof require !== 'undefined') {
        require.undef("plotly");
        define('plotly', function(require, exports, module) {
            /**
* plotly.js v2.18.2
* Copyright 2012-2023, Plotly, Inc.
* All rights reserved.
* Licensed under the MIT license
*/
/*! For license information please see plotly.min.js.LICENSE.txt */
        });
        require(['plotly'], function(Plotly) {
            window._Plotly = Plotly;
        });
        }
        </script>




<div>                            <div id="2e27fd91-2678-4bf3-b055-ab6348193e7c" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("2e27fd91-2678-4bf3-b055-ab6348193e7c")) {                    Plotly.newPlot(                        "2e27fd91-2678-4bf3-b055-ab6348193e7c",                        [{"name":"-2 + -1 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[0.9996646498695336,0.9995896049301781,0.999497774807042,0.9993854093819373,0.9992479227792297,0.9990797081458725,0.9988739118996964,0.9986221588339111,0.9983142177652076,0.9979375954426708,0.9974770441881992,0.9969139662331893,0.9962256950083802,0.9953846308570221,0.9943572060020109,0.9931026514880604,0.9915715378558265,0.9897040624382485,0.9874280608262846,0.9846567303029896,0.9812860718046186,0.9771920881813124,0.9722278252938079,0.9662204149478009,0.9589683814952454,0.950239612916065,0.9397705745144642,0.9272675528437321,0.9124109373658964,0.8948637309379361,0.8742855462724639,0.850353173993199,0.8227882504972028,0.791391472673955,0.7560811514076523,0.7169318141604084,0.6742065062693061,0.628375159857885,0.5801117914777869,0.5302659827682414,0.4798089657991921,0.4297605216677123,0.3811078816263186,0.3347300110709839,0.29133917497056433,0.2514471293046628,0.21535741030420025,0.1831799972206518,0.15486145461129774,0.1302228405778754,0.10899868348430335,0.09087230339198726,0.0755048784158733,0.06255741682857321,0.051705992288555776,0.04265125213094287,0.03512344505198073,0.028884185181570758,0.02372600172120029,0.019470505977400267,0.01596579366548898,0.013083515733575012,0.010715904295329846,0.008772930599259385,0.0071796939564060976,0.005874087564459341,0.004804752887159514,0.0039293133489465785,0.0032128664149852233,0.0026267075405361088,0.0021472577676324113,0.0017551673808188493,0.001434569972506858,0.0011724638388482262,0.000958200406512903,0.0007830621269202472,0.0006399148270537988,0.0005229218067633642,0.00042730899792949105,0.00034917225408029144,0.0002853193377414427,0.00023314044185035804,0.0001905021483653389,0.0001556606189086567,0.00012719055431560273,0.00010392707526083658,8.49181849054511e-05,6.938589424534378e-05,5.669443649526451e-05,4.632428107126362e-05,3.785089117568662e-05,3.0927360533750495e-05,2.5270221875728775e-05,2.06478484361333e-05,1.687097512075971e-05,1.37849522560392e-05,1.126341542630157e-05,9.203112654547672e-06,7.519677416343213e-06,6.144174602214718e-06],"type":"scatter"},{"name":"0 + -1 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[0.9999546021312976,0.9999444393510606,0.9999320016825577,0.999916779980278,0.9998981511845727,0.9998753528540559,0.9998474520137535,0.9998133070550387,0.9997715211446788,0.9997203852613508,0.9996578085662833,0.9995812333155556,0.9994875309178055,0.9993728750127243,0.9992325865700818,0.9990609449609381,0.9988509577051191,0.9985940801244912,0.9982798744047808,0.9978955955708816,0.9974256896068625,0.9968511864223202,0.9961489676440697,0.995290886427886,0.9942427138780918,0.9929628846354357,0.9914010133898106,0.9894961554867145,0.9871747899072354,0.9843485138571816,0.9809114580100765,0.9767374641691144,0.9716771179556968,0.9655548043337887,0.9581660599944802,0.9492756394379457,0.9386168925965079,0.9258932636749527,0.9107829397488015,0.8929478537858229,0.8720482950755473,0.8477641768561095,0.8198234066423302,0.7880366661307628,0.7523361988609284,0.7128140986174976,0.6697535703681886,0.623645482503293,0.5751831319371523,0.5252310760920885,0.4747689239079115,0.42481686806284763,0.37635451749670706,0.33024642963181144,0.28718590138250283,0.2476638011390717,0.21196333386923713,0.18017659335766972,0.15223582314389075,0.12795170492445268,0.10705214621417715,0.08921706025119844,0.07410673632504738,0.061383107403492225,0.05072436056205437,0.04183394000551971,0.034445195666211154,0.028322882044303225,0.02326253583088552,0.019088541989923387,0.015651486142818367,0.012825210092764697,0.010503844513285425,0.008598986610189428,0.007037115364564376,0.00575728612190819,0.004709113572114015,0.003851032355930255,0.0031488135776798513,0.0025743103931375336,0.0021044044291184316,0.0017201255952192596,0.0014059198755086346,0.001149042294880872,0.0009390550390618314,0.0007674134299182647,0.0006271249872756847,0.0005124690821944592,0.00041876668444437313,0.00034219143371662803,0.0002796147386491928,0.00022847885532128418,0.0001866929449613085,0.00015254798624649623,0.00012464714594414533,0.00010184881542721289,8.322001972209245e-05,6.7998317442358e-05,5.556064893935837e-05,4.5397868702434395e-05],"type":"scatter"},{"name":"2 + -1 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[0.9999938558253978,0.9999924803225836,0.9999907968873454,0.9999887365845738,0.9999862150477439,0.9999831290248792,0.9999793521515637,0.9999747297781243,0.9999690726394662,0.9999621491088242,0.9999536757189287,0.9999433055635047,0.9999306141057547,0.9999150818150946,0.999896072924739,0.9998728094456845,0.9998443393810914,0.9998094978516346,0.9997668595581497,0.9997146806622584,0.9996508277459197,0.9995726910020706,0.9994770781932366,0.9993600851729462,0.9992169378730799,0.9990417995934872,0.9988275361611518,0.9985654300274931,0.9982448326191812,0.9978527422323676,0.9973732924594639,0.9967871335850149,0.9960706866510534,0.9951952471128405,0.9941259124355407,0.992820306043594,0.9912270694007407,0.9892840957046701,0.986916484266425,0.984034206334511,0.9805294940225998,0.9762739982787998,0.9711158148184292,0.9648765549480193,0.9573487478690571,0.9482940077114443,0.9374425831714268,0.9244951215841267,0.9091276966080127,0.8910013165156967,0.8697771594221246,0.8451385453887023,0.8168200027793482,0.7846425896957997,0.7485528706953376,0.7086608250294356,0.6652699889290161,0.6188921183736814,0.5702394783322882,0.5201910342008079,0.46973401723175856,0.41988820852221304,0.3716248401421153,0.3257934937306941,0.2830681858395916,0.24391884859234775,0.20860852732604485,0.17721174950279725,0.14964682600680101,0.125714453727536,0.10513626906206389,0.08758906263410375,0.07273244715626795,0.06022942548553574,0.049760387083935,0.04103161850475471,0.033779585052199246,0.027772174706191984,0.022807911818687677,0.018713928195381303,0.015343269697010479,0.01257193917371529,0.010295937561751515,0.008428462144173537,0.006897348511939483,0.005642793997988926,0.004615369142977778,0.0037743049916199,0.0030860337668107427,0.0025229558118008578,0.002062404557329249,0.0016857822347925108,0.0013778411660887362,0.0011260881003036015,0.000920291854127426,0.0007520772207702588,0.0006145906180626042,0.000502225192957993,0.00041039506982176846,0.0003353501304664781],"type":"scatter"},{"name":"-2 + 1 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[6.144174602214718e-06,7.519677416343227e-06,9.203112654547672e-06,1.126341542630157e-05,1.3784952256039174e-05,1.687097512075971e-05,2.0647848436133338e-05,2.5270221875728734e-05,3.0927360533750495e-05,3.7850891175686555e-05,4.632428107126362e-05,5.669443649526451e-05,6.938589424534366e-05,8.49181849054511e-05,0.00010392707526083678,0.00012719055431560273,0.0001556606189086567,0.00019050214836533854,0.00023314044185035804,0.0002853193377414427,0.0003491722540802911,0.00042730899792949105,0.0005229218067633642,0.0006399148270537982,0.0007830621269202465,0.000958200406512903,0.0011724638388482262,0.0014345699725068566,0.0017551673808188476,0.0021472577676324113,0.0026267075405361088,0.0032128664149852202,0.003929313348946575,0.004804752887159518,0.005874087564459341,0.0071796939564060976,0.008772930599259378,0.010715904295329835,0.013083515733575012,0.01596579366548898,0.019470505977400267,0.023726001721200252,0.028884185181570758,0.03512344505198073,0.04265125213094287,0.05170599228855568,0.06255741682857321,0.0755048784158733,0.09087230339198726,0.10899868348430335,0.1302228405778754,0.15486145461129774,0.1831799972206518,0.21535741030420025,0.25144712930466245,0.29133917497056433,0.3347300110709839,0.3811078816263186,0.4297605216677119,0.4798089657991921,0.5302659827682414,0.5801117914777869,0.6283751598578847,0.6742065062693059,0.7169318141604084,0.7560811514076523,0.791391472673955,0.8227882504972027,0.850353173993199,0.8742855462724639,0.8948637309379361,0.9124109373658962,0.9272675528437321,0.9397705745144642,0.950239612916065,0.9589683814952452,0.9662204149478006,0.9722278252938079,0.9771920881813124,0.9812860718046186,0.9846567303029896,0.9874280608262846,0.9897040624382485,0.9915715378558265,0.9931026514880604,0.9943572060020109,0.9953846308570221,0.9962256950083802,0.9969139662331893,0.9974770441881992,0.9979375954426708,0.9983142177652076,0.9986221588339111,0.9988739118996964,0.9990797081458725,0.9992479227792297,0.9993854093819373,0.999497774807042,0.9995896049301781,0.9996646498695336],"type":"scatter"},{"name":"0 + 1 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[4.5397868702434395e-05,5.556064893935847e-05,6.7998317442358e-05,8.322001972209245e-05,0.00010184881542721271,0.00012464714594414533,0.00015254798624649647,0.00018669294496130814,0.00022847885532128418,0.0002796147386491923,0.00034219143371662803,0.0004187666844443735,0.0005124690821944584,0.0006271249872756847,0.000767413429918266,0.0009390550390618305,0.001149042294880872,0.0014059198755086322,0.0017201255952192596,0.0021044044291184333,0.0025743103931375314,0.0031488135776798513,0.003851032355930255,0.004709113572114011,0.0057572861219081835,0.007037115364564376,0.008598986610189428,0.010503844513285416,0.012825210092764685,0.015651486142818367,0.019088541989923387,0.0232625358308855,0.0283228820443032,0.03444519566621118,0.04183394000551971,0.05072436056205437,0.06138310740349217,0.07410673632504733,0.08921706025119844,0.10705214621417715,0.12795170492445268,0.15223582314389053,0.18017659335766972,0.21196333386923713,0.2476638011390717,0.28718590138250244,0.33024642963181144,0.37635451749670706,0.42481686806284763,0.4747689239079115,0.5252310760920885,0.5751831319371523,0.623645482503293,0.6697535703681886,0.7128140986174972,0.7523361988609284,0.7880366661307628,0.8198234066423302,0.8477641768561092,0.8720482950755473,0.8929478537858229,0.9107829397488015,0.9258932636749527,0.9386168925965077,0.9492756394379457,0.9581660599944802,0.9655548043337889,0.9716771179556968,0.9767374641691144,0.9809114580100765,0.9843485138571816,0.9871747899072354,0.9894961554867145,0.9914010133898106,0.9929628846354357,0.9942427138780918,0.995290886427886,0.9961489676440697,0.9968511864223202,0.9974256896068625,0.9978955955708816,0.9982798744047808,0.9985940801244912,0.9988509577051191,0.9990609449609381,0.9992325865700818,0.9993728750127243,0.9994875309178055,0.9995812333155556,0.9996578085662833,0.9997203852613508,0.9997715211446788,0.9998133070550387,0.9998474520137535,0.9998753528540559,0.9998981511845727,0.999916779980278,0.9999320016825577,0.9999444393510606,0.9999546021312976],"type":"scatter"},{"name":"2 + 1 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[0.0003353501304664781,0.0004103950698217691,0.000502225192957993,0.0006145906180626042,0.0007520772207702574,0.000920291854127426,0.0011260881003036034,0.0013778411660887336,0.0016857822347925108,0.002062404557329245,0.0025229558118008578,0.0030860337668107457,0.0037743049916198934,0.004615369142977778,0.005642793997988936,0.006897348511939476,0.008428462144173537,0.010295937561751496,0.01257193917371529,0.015343269697010492,0.018713928195381285,0.022807911818687677,0.027772174706191984,0.03377958505219922,0.041031618504754674,0.049760387083935,0.06022942548553574,0.07273244715626788,0.08758906263410368,0.10513626906206389,0.125714453727536,0.1496468260068009,0.1772117495027971,0.20860852732604498,0.24391884859234775,0.2830681858395916,0.3257934937306939,0.37162484014211505,0.41988820852221304,0.46973401723175856,0.5201910342008079,0.5702394783322877,0.6188921183736814,0.6652699889290161,0.7086608250294356,0.7485528706953372,0.7846425896957997,0.8168200027793482,0.8451385453887023,0.8697771594221246,0.8910013165156967,0.9091276966080127,0.9244951215841267,0.9374425831714268,0.9482940077114442,0.9573487478690571,0.9648765549480193,0.9711158148184292,0.9762739982787998,0.9805294940225998,0.984034206334511,0.986916484266425,0.9892840957046701,0.9912270694007407,0.992820306043594,0.9941259124355407,0.9951952471128405,0.9960706866510534,0.9967871335850149,0.9973732924594639,0.9978527422323676,0.9982448326191812,0.9985654300274931,0.9988275361611518,0.9990417995934872,0.9992169378730799,0.9993600851729462,0.9994770781932366,0.9995726910020706,0.9996508277459197,0.9997146806622584,0.9997668595581497,0.9998094978516346,0.9998443393810914,0.9998728094456845,0.999896072924739,0.9999150818150946,0.9999306141057547,0.9999433055635047,0.9999536757189287,0.9999621491088242,0.9999690726394662,0.9999747297781243,0.9999793521515637,0.9999831290248792,0.9999862150477439,0.9999887365845738,0.9999907968873454,0.9999924803225836,0.9999938558253978],"type":"scatter"},{"name":"-2 + 5 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[2.6102790696677047e-23,7.167508817382739e-23,1.9681107374392442e-22,5.404192688859592e-22,1.483925577090402e-21,4.074679133633486e-21,1.1188573267011402e-20,3.072246124068465e-20,8.436014156231223e-20,2.316426873700147e-19,6.36062643071407e-19,1.746550648778887e-18,4.795815635422367e-18,1.3168726383653672e-17,3.6159720838030587e-17,9.929019504174104e-17,2.726387981695487e-16,7.486329766608592e-16,2.0556550920370787e-15,5.64457883790525e-15,1.5499326896203476e-14,4.255926635697795e-14,1.168625686117884e-13,3.208903985325401e-13,8.811260020511707e-13,2.419464823629463e-12,6.6435561079091514e-12,1.8242396966284978e-11,5.009140310753247e-11,1.3754489992620516e-10,3.7768156448339735e-10,1.0370676351311662e-09,2.84766157455826e-09,7.81933226231315e-09,2.1470934974858232e-08,5.8956573559223886e-08,1.6188756299780322e-07,4.4452343074872473e-07,1.2206063228065605e-06,3.351629348453139e-06,9.203112654547688e-06,2.527022187572864e-05,6.938589424534353e-05,0.00019050214836533854,0.0005229218067633652,0.0014345699725068503,0.0039293133489465655,0.010715904295329825,0.028884185181570803,0.07550487841587356,0.18317999722065129,0.3811078816263181,0.6283751598578852,0.8227882504972033,0.9272675528437319,0.9722278252938079,0.9897040624382485,0.9962256950083802,0.9986221588339111,0.999497774807042,0.9998170401051004,0.9999333615124951,0.9999757304212727,0.999991161315239,0.9999967810903231,0.9999988277280198,0.9999995730791029,0.9999998445229699,0.9999999433780288,0.9999999793792858,0.999999992490303,0.9999999972651021,0.9999999990039989,0.9999999996372742,0.9999999998679017,0.9999999999518923,0.99999999998248,0.9999999999936195,0.9999999999976763,0.9999999999991538,0.9999999999996918,0.9999999999998879,0.9999999999999591,0.9999999999999851,0.9999999999999947,0.999999999999998,0.9999999999999993,0.9999999999999998,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],"type":"scatter"},{"name":"0 + 5 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[1.928749847963918e-22,5.296112474122114e-22,1.4542480647846349e-21,3.9931882947414406e-21,1.096480933575902e-20,3.010803270355997e-20,8.267299553694303e-20,2.270099896046414e-19,6.233418185176562e-19,1.7116208118840931e-18,4.699902552088729e-18,1.2905360723450921e-17,3.543655077026461e-17,9.73044580002851e-17,2.6718620579387954e-16,7.336608212371899e-16,2.0145433744198228e-15,5.531691062056503e-15,1.518935079511417e-14,4.1708109688117163e-14,1.1452539593170082e-13,3.1447280664095646e-13,8.63504075336992e-13,2.3710771563602915e-12,6.510689459345931e-12,1.78775613109111e-11,4.908960877565043e-11,1.3479409454713154e-10,3.7012818751725187e-10,1.0163269807834022e-09,2.790710260765653e-09,7.662950883595711e-09,2.1041530742353307e-08,5.777748185595394e-08,1.586499212622808e-07,4.356332653368673e-07,1.1961950474749672e-06,3.2845992385499644e-06,9.019058258600438e-06,2.4764846970352077e-05,6.799831744235813e-05,0.00018669294496130747,0.0005124690821944575,0.0014059198755086322,0.003851032355930262,0.010503844513285369,0.028322882044303128,0.07410673632504726,0.18017659335766997,0.37635451749670784,0.6236454825032922,0.81982340664233,0.9258932636749527,0.9716771179556968,0.9894961554867145,0.9961489676440697,0.9985940801244912,0.9994875309178055,0.9998133070550387,0.9999320016825577,0.9999752351530297,0.9999909809417414,0.9999967154007615,0.9999988038049525,0.9999995643667347,0.9999998413500787,0.9999999422225181,0.9999999789584693,0.9999999923370492,0.9999999972092897,0.999999998983673,0.9999999996298718,0.9999999998652058,0.9999999999509104,0.9999999999821225,0.9999999999934892,0.999999999997629,0.9999999999991365,0.9999999999996856,0.9999999999998854,0.9999999999999583,0.9999999999999849,0.9999999999999944,0.999999999999998,0.9999999999999993,0.9999999999999998,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],"type":"scatter"},{"name":"2 + 5 x","x":[-10.0,-9.797979797979798,-9.595959595959595,-9.393939393939394,-9.191919191919192,-8.98989898989899,-8.787878787878787,-8.585858585858587,-8.383838383838384,-8.181818181818182,-7.979797979797979,-7.777777777777778,-7.575757575757576,-7.373737373737374,-7.171717171717171,-6.96969696969697,-6.767676767676768,-6.565656565656566,-6.363636363636363,-6.161616161616162,-5.959595959595959,-5.757575757575758,-5.555555555555555,-5.353535353535354,-5.151515151515151,-4.94949494949495,-4.747474747474747,-4.545454545454546,-4.343434343434343,-4.141414141414142,-3.9393939393939394,-3.737373737373738,-3.5353535353535355,-3.333333333333333,-3.1313131313131315,-2.929292929292929,-2.7272727272727275,-2.525252525252525,-2.3232323232323235,-2.121212121212121,-1.9191919191919187,-1.717171717171718,-1.5151515151515156,-1.3131313131313131,-1.1111111111111107,-0.9090909090909101,-0.7070707070707076,-0.5050505050505052,-0.30303030303030276,-0.10101010101010033,0.10101010101010033,0.30303030303030276,0.5050505050505052,0.7070707070707076,0.9090909090909083,1.1111111111111107,1.3131313131313131,1.5151515151515156,1.7171717171717162,1.9191919191919187,2.121212121212121,2.3232323232323235,2.525252525252524,2.7272727272727266,2.929292929292929,3.1313131313131315,3.333333333333334,3.5353535353535346,3.737373737373737,3.9393939393939394,4.141414141414142,4.3434343434343425,4.545454545454545,4.747474747474747,4.94949494949495,5.1515151515151505,5.353535353535353,5.555555555555555,5.757575757575758,5.9595959595959584,6.161616161616163,6.363636363636363,6.565656565656564,6.767676767676768,6.969696969696969,7.171717171717173,7.373737373737374,7.575757575757574,7.777777777777779,7.979797979797979,8.18181818181818,8.383838383838384,8.585858585858585,8.787878787878789,8.98989898989899,9.19191919191919,9.393939393939394,9.595959595959595,9.7979797979798,10.0],"y":[1.4251640827409352e-21,3.91332721775347e-21,1.0745520532455e-20,2.950589232343772e-20,8.101959129600192e-20,2.2246994267504325e-19,6.108754018891153e-19,1.6773895482063593e-18,4.60590766583641e-18,1.2647262199108789e-17,3.4727843616890957e-17,9.535843436251509e-17,2.618426615940893e-16,7.189880988401476e-16,1.9742538634714023e-15,5.421060965709102e-15,1.4885574007316933e-14,4.0873975579487323e-14,1.122349651314246e-13,3.081835622657686e-13,8.462345752909622e-13,2.3236572098535296e-12,6.380480054285071e-12,1.7520022122973744e-11,4.8107849655822395e-11,1.3209830342330593e-10,3.6272587300407535e-10,9.960011255555538e-10,2.7348979348930937e-09,7.509697027102131e-09,2.062071430499137e-08,5.662197119008251e-08,1.5547703016098702e-07,4.269208970934861e-07,1.1722719800557926e-06,3.2189096769902397e-06,8.838684760901125e-06,2.4269578727178082e-05,6.663848750481959e-05,0.0001829598948995803,0.0005022251929579939,0.0013778411660887288,0.003774304991619886,0.010295937561751496,0.02777217470619203,0.07273244715626759,0.17721174950279672,0.37162484014211483,0.6188921183736819,0.8168200027793486,0.9244951215841265,0.9711158148184292,0.9892840957046701,0.9960706866510534,0.9985654300274931,0.9994770781932366,0.9998094978516346,0.9999306141057547,0.9999747297781243,0.9999907968873454,0.9999966483706515,0.9999987793936773,0.9999995554765693,0.9999998381124371,0.9999999410434265,0.999999978529065,0.9999999921806678,0.9999999971523383,0.9999999989629325,0.9999999996223183,0.9999999998624551,0.9999999999499085,0.9999999999817577,0.9999999999933564,0.9999999999975806,0.9999999999991189,0.9999999999996791,0.9999999999998832,0.9999999999999574,0.9999999999999845,0.9999999999999944,0.999999999999998,0.9999999999999993,0.9999999999999998,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],"type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('2e27fd91-2678-4bf3-b055-ab6348193e7c');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>
