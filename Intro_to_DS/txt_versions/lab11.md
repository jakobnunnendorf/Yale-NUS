# Lab 11: Clustering

In this lab you will explore K-Means.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import cluster
```

## Vanilla Example

Let us begin with a toy dataset with three groups that are completely separated with the variables given. There are the same number of points per group and the same variance within each group.


```python
np.random.seed(1337)

c1 = np.random.normal(size = (25, 2))
c2 = np.array([2, 8]) + np.random.normal(size = (25, 2))
c3 = np.array([8, 4]) + np.random.normal(size = (25, 2))

x1 = np.vstack((c1, c2, c3))

sns.scatterplot(x = x1[:, 0], y = x1[:, 1]);
```


    
![png](lab11_files/lab11_3_0.png)
    


Running the K-Means algorithm, we can see that it is able to accurately pick out the three initial clusters. 


```python
kmeans = cluster.KMeans(n_clusters = 3, random_state = 42).fit(x1)
sns.scatterplot(x = x1[:, 0], y = x1[:, 1], hue = kmeans.labels_)
sns.scatterplot(x = kmeans.cluster_centers_[:, 0], y = kmeans.cluster_centers_[:, 1], color = 'blue', marker = 'x', s = 300, linewidth = 5);
```


    
![png](lab11_files/lab11_5_0.png)
    


## Question 1

In the previous example, the K-Means algorithm was able to accurately find the three initial clusters. However, changing the starting centers for K-Means can change the final clusters that K-Means gives us. Change the initial centers to the points `[0, 1]`, `[1, 1]`, and `[2, 2]`; and fit a [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) object called `kmeans_q1` on the toy dataset from the previous example. Keep the `random_state` parameter as 42 and the `n_clusters` parameter as 3.

**Hint:** You will need to change the `init` and `n_init = 1` parameters in `cluster.KMeans`. You may find this link helpful: https://stackoverflow.com/questions/38355153/initial-centroids-for-scikit-learn-kmeans-clustering

<!--
BEGIN QUESTION
name: q1
-->


```python
kmeans_q1 = cluster.KMeans(n_clusters=3, init=np.array([[0, 1], [1, 1], [2, 2]]), n_init=1, random_state=42).fit(x1)
```

Running the K-Means algorithm with these centers gives us a different result from before, and this particular run of K-Means was unable to accurately find the three initial clusters.


```python
sns.scatterplot(x = x1[:, 0], y = x1[:, 1], hue = kmeans_q1.labels_)
sns.scatterplot(x = kmeans_q1.cluster_centers_[:, 0], y = kmeans_q1.cluster_centers_[:, 1], color = 'blue', marker = 'x', s = 300, linewidth = 5);
```


    
![png](lab11_files/lab11_9_0.png)
    


## Question 2

Sometimes, K-Means will have a difficult time finding the "correct" clusters even with ideal starting centers. For example, consider the data below. There are two groups of different sizes in two different senses. The smaller group has both smaller variability and is less numerous, and the larger of the two groups is more diffuse and populated.


```python
np.random.seed(1337)

c1 = 0.5 * np.random.normal(size = (25, 2))
c2 = np.array([10, 10]) + 3 * np.random.normal(size = (475, 2))

x2 = np.vstack((c1, c2))

sns.scatterplot(x = x2[:, 0], y = x2[:, 1]);
```


    
![png](lab11_files/lab11_11_0.png)
    


### Question 2

Fit a `cluster.KMeans` object called `kmeans_q2a` on the dataset above with two clusters and a `random_state` parameter of 42.

<!--
BEGIN QUESTION
name: q2a
-->


```python
kmeans_q2a = kmeans_q2a = cluster.KMeans(n_clusters=2, random_state=42).fit(x2)
```

(For notational simplicity we will call the initial cluster on the bottom left $A$ and the initial cluster on the top right $B$. We will call the bottom left cluster found by K-Means as cluster $a$ and the top right cluster found by K-Means as cluster $b$.) 

As seen below, K-Means is unable to find the two intial clusters because cluster $A$ includes points from cluster $B$. Recall that K-Means attempts to minimize inertia, so it makes sense that points in the bottom left of cluster $B$ would prefer to be in cluster $A$ rather than cluster $B$. If these points were in cluster $B$ instead, then the resulting cluster assignments would have a larger distortion.


```python
sns.scatterplot(x = x2[:, 0], y = x2[:, 1], hue = kmeans_q2a.labels_)
sns.scatterplot(x = kmeans_q2a.cluster_centers_[:, 0], y = kmeans_q2a.cluster_centers_[:, 1], color = 'red', marker = 'x', s = 300, linewidth = 5);
```


    
![png](lab11_files/lab11_15_0.png)
    


## Question 3

In the previous questions, we looked at clustering on two dimensional datasets. However, we can easily use clustering on data which have more than two dimensions. For this, let us turn to a World Bank dataset, containing various features for the world's countries.

This data comes from https://databank.worldbank.org/source/world-development-indicators#.



```python
world_bank_data = pd.read_csv("world_bank_data.csv", index_col = 'country')
world_bank_data.head(5)
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
      <th>Age dependency ratio (% of working-age population)</th>
      <th>Age dependency ratio, old (% of working-age population)</th>
      <th>Age dependency ratio, young (% of working-age population)</th>
      <th>Bird species, threatened</th>
      <th>Business extent of disclosure index (0=less disclosure to 10=more disclosure)</th>
      <th>Contributing family workers, female (% of female employment) (modeled ILO estimate)</th>
      <th>Contributing family workers, male (% of male employment) (modeled ILO estimate)</th>
      <th>Contributing family workers, total (% of total employment) (modeled ILO estimate)</th>
      <th>Cost of business start-up procedures (% of GNI per capita)</th>
      <th>Cost of business start-up procedures, female (% of GNI per capita)</th>
      <th>...</th>
      <th>Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)</th>
      <th>Urban population</th>
      <th>Urban population (% of total population)</th>
      <th>Urban population growth (annual %)</th>
      <th>Vulnerable employment, female (% of female employment) (modeled ILO estimate)</th>
      <th>Vulnerable employment, male (% of male employment) (modeled ILO estimate)</th>
      <th>Vulnerable employment, total (% of total employment) (modeled ILO estimate)</th>
      <th>Wage and salaried workers, female (% of female employment) (modeled ILO estimate)</th>
      <th>Wage and salaried workers, male (% of male employment) (modeled ILO estimate)</th>
      <th>Wage and salaried workers, total (% of total employment) (modeled ILO estimate)</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Algeria</th>
      <td>57.508032</td>
      <td>10.021442</td>
      <td>47.486590</td>
      <td>15.0</td>
      <td>4.0</td>
      <td>2.720000</td>
      <td>1.836</td>
      <td>1.978000</td>
      <td>0.0</td>
      <td>11.8</td>
      <td>...</td>
      <td>29.952999</td>
      <td>30670086.0</td>
      <td>72.629</td>
      <td>2.804996</td>
      <td>24.337001</td>
      <td>27.227001</td>
      <td>26.762000</td>
      <td>73.734001</td>
      <td>68.160004</td>
      <td>69.056000</td>
    </tr>
    <tr>
      <th>Afghanistan</th>
      <td>84.077656</td>
      <td>4.758273</td>
      <td>79.319383</td>
      <td>16.0</td>
      <td>8.0</td>
      <td>71.780998</td>
      <td>9.606</td>
      <td>31.577999</td>
      <td>0.0</td>
      <td>6.4</td>
      <td>...</td>
      <td>2.639000</td>
      <td>9477100.0</td>
      <td>25.495</td>
      <td>3.350383</td>
      <td>95.573997</td>
      <td>85.993001</td>
      <td>89.378998</td>
      <td>4.282000</td>
      <td>13.292000</td>
      <td>10.108000</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>45.810037</td>
      <td>20.041214</td>
      <td>25.768823</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>37.987000</td>
      <td>20.795</td>
      <td>28.076000</td>
      <td>0.0</td>
      <td>11.3</td>
      <td>...</td>
      <td>30.979000</td>
      <td>1728969.0</td>
      <td>60.319</td>
      <td>1.317162</td>
      <td>54.663000</td>
      <td>54.994001</td>
      <td>54.854000</td>
      <td>44.320999</td>
      <td>41.542999</td>
      <td>42.720001</td>
    </tr>
    <tr>
      <th>American Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>48339.0</td>
      <td>87.153</td>
      <td>-0.299516</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>67813.0</td>
      <td>88.062</td>
      <td>-0.092859</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 209 columns</p>
</div>



There are some missing values. For the sake of convenience and of keeping the lab short, we will fill them all with zeros. 


```python
world_bank_data = world_bank_data.fillna(0)
```



Below, fit a `cluster.KMeans` object called `kmeans_q3` with four clusters and a `random_state` parameter of 42.

Make sure you should use a centered and scaled version of the world bank data. By centered and scaled we mean that the mean in each column should be zero and the variance should be 1.

<!--
BEGIN QUESTION
name: q4
-->


```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(world_bank_data)
```




    StandardScaler()




```python
kmeans_q3 = cluster.KMeans(n_clusters=4, random_state=42).fit(scaler.transform(world_bank_data))
```

Looking at these new clusters, we see that they seem to correspond to:

0: Very small countries.

1: Developed countries.

2: Less developed countries.

3: Huge countries.


```python
labeled_world_bank_data_q3 = pd.Series(kmeans_q3.labels_, name = "cluster", index  = world_bank_data.index).to_frame()
```


```python
list(labeled_world_bank_data_q3.query('cluster == 0').index)
```




    ['American Samoa',
     'Andorra',
     'Aruba',
     'Bermuda',
     'British Virgin Islands',
     'Cayman Islands',
     'Curacao',
     'Dominica',
     'Faroe Islands',
     'Gibraltar',
     'Greenland',
     'Isle of Man',
     'Kosovo',
     'Liechtenstein',
     'Marshall Islands',
     'Monaco',
     'Nauru',
     'Northern Mariana Islands',
     'Palau',
     'San Marino',
     'Sint Maarten (Dutch part)',
     'St. Kitts and Nevis',
     'St. Martin (French part)',
     'Turks and Caicos Islands',
     'Tuvalu']




```python
list(labeled_world_bank_data_q3.query('cluster == 1').index)
```




    ['Albania',
     'Antigua and Barbuda',
     'Argentina',
     'Armenia',
     'Australia',
     'Austria',
     'Azerbaijan',
     'Bahamas, The',
     'Bahrain',
     'Barbados',
     'Belarus',
     'Belgium',
     'Bosnia and Herzegovina',
     'Brazil',
     'Brunei Darussalam',
     'Bulgaria',
     'Canada',
     'Channel Islands',
     'Chile',
     'Colombia',
     'Costa Rica',
     'Croatia',
     'Cuba',
     'Cyprus',
     'Czech Republic',
     'Denmark',
     'Dominican Republic',
     'El Salvador',
     'Estonia',
     'Finland',
     'France',
     'French Polynesia',
     'Georgia',
     'Germany',
     'Greece',
     'Grenada',
     'Guam',
     'Hong Kong SAR, China',
     'Hungary',
     'Iceland',
     'Iran, Islamic Rep.',
     'Ireland',
     'Israel',
     'Italy',
     'Jamaica',
     'Japan',
     'Jordan',
     'Kazakhstan',
     'Korea, Rep.',
     'Kuwait',
     'Latvia',
     'Lebanon',
     'Libya',
     'Lithuania',
     'Luxembourg',
     'Macao SAR, China',
     'Malaysia',
     'Maldives',
     'Malta',
     'Mauritius',
     'Mexico',
     'Moldova',
     'Montenegro',
     'Netherlands',
     'New Caledonia',
     'New Zealand',
     'North Macedonia',
     'Norway',
     'Oman',
     'Panama',
     'Poland',
     'Portugal',
     'Puerto Rico',
     'Qatar',
     'Romania',
     'Russian Federation',
     'Saudi Arabia',
     'Serbia',
     'Seychelles',
     'Singapore',
     'Slovak Republic',
     'Slovenia',
     'South Africa',
     'Spain',
     'Sri Lanka',
     'St. Lucia',
     'St. Vincent and the Grenadines',
     'Suriname',
     'Sweden',
     'Switzerland',
     'Thailand',
     'Trinidad and Tobago',
     'Tunisia',
     'Turkey',
     'Ukraine',
     'United Arab Emirates',
     'United Kingdom',
     'Uruguay',
     'Virgin Islands (U.S.)']




```python
list(labeled_world_bank_data_q3.query('cluster == 2').index)
```




    ['Algeria',
     'Afghanistan',
     'Angola',
     'Bangladesh',
     'Belize',
     'Benin',
     'Bhutan',
     'Bolivia',
     'Botswana',
     'Burkina Faso',
     'Burundi',
     'Cabo Verde',
     'Cambodia',
     'Cameroon',
     'Central African Republic',
     'Chad',
     'Comoros',
     'Congo, Dem. Rep.',
     'Congo, Rep.',
     "Cote d'Ivoire",
     'Djibouti',
     'Ecuador',
     'Egypt, Arab Rep.',
     'Equatorial Guinea',
     'Eritrea',
     'Eswatini',
     'Ethiopia',
     'Fiji',
     'Gabon',
     'Gambia, The',
     'Ghana',
     'Guatemala',
     'Guinea',
     'Guinea-Bissau',
     'Guyana',
     'Haiti',
     'Honduras',
     'Indonesia',
     'Iraq',
     'Kenya',
     'Kiribati',
     'Korea, Dem. People’s Rep.',
     'Kyrgyz Republic',
     'Lao PDR',
     'Lesotho',
     'Liberia',
     'Madagascar',
     'Malawi',
     'Mali',
     'Mauritania',
     'Micronesia, Fed. Sts.',
     'Mongolia',
     'Morocco',
     'Mozambique',
     'Myanmar',
     'Namibia',
     'Nepal',
     'Nicaragua',
     'Niger',
     'Nigeria',
     'Pakistan',
     'Papua New Guinea',
     'Paraguay',
     'Peru',
     'Philippines',
     'Rwanda',
     'Samoa',
     'Sao Tome and Principe',
     'Senegal',
     'Sierra Leone',
     'Solomon Islands',
     'Somalia',
     'South Sudan',
     'Sudan',
     'Syrian Arab Republic',
     'Tajikistan',
     'Tanzania',
     'Timor-Leste',
     'Togo',
     'Tonga',
     'Turkmenistan',
     'Uganda',
     'Uzbekistan',
     'Vanuatu',
     'Venezuela, RB',
     'Vietnam',
     'West Bank and Gaza',
     'Yemen, Rep.',
     'Zambia',
     'Zimbabwe']




```python
list(labeled_world_bank_data_q3.query('cluster == 3').index)
```




    ['China', 'India', 'United States']



## Submission

 

To submit your assignment, please download your notebook as a .ipynb file and submit to Canvas. You can do so by navigating to the toolbar at the top of this page, clicking File > Download as... > Notebook (.ipynb) or HTML (.html). Then, upload both files under "Lab #11".
