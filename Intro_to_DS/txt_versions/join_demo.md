```python
import pandas as pd
import zipfile
import seaborn as sns
```

# Join Review

In this notebook we'll briefly review [joining tables as discussed in data 8](https://www.inferentialthinking.com/chapters/08/4/Joining_Tables_by_Columns.html).

Often data is spread across two tables. Joining provides us with a way to naturally combine related tables.

Let's start by reading data from the given zip file. To showcase how to do read data that is inside zip files, we're going to use the `zipfile` module. Doing so will allow us to avoid needing to unzip the data. Running the cell below, we see that the zip file contains `elections.csv` and `presidents.csv`.


```python
join_demo_filename = "join_demo_data.zip"
my_zip = zipfile.ZipFile(join_demo_filename, 'r')
list_names = [f.filename for f in my_zip.filelist]
list_names
```




    ['elections.csv', 'presidents.csv']



We could call `my_zip.extractall()` to unzip the files, but we won't. Instead, we'll read directly from the zip file itself.


```python
with my_zip.open("elections.csv") as f:
    elections = pd.read_csv(f)
    
elections.head(5)
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1824</td>
      <td>Andrew Jackson</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>loss</td>
      <td>57.210122</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1824</td>
      <td>John Quincy Adams</td>
      <td>Democratic-Republican</td>
      <td>113142</td>
      <td>win</td>
      <td>42.789878</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1828</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>642806</td>
      <td>win</td>
      <td>56.203927</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1828</td>
      <td>John Quincy Adams</td>
      <td>National Republican</td>
      <td>500897</td>
      <td>loss</td>
      <td>43.796073</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1832</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>702735</td>
      <td>win</td>
      <td>54.574789</td>
    </tr>
  </tbody>
</table>
</div>




```python
with my_zip.open("presidents.csv") as f:
    presidents = pd.read_csv(f)
    
presidents.head(5)
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
      <th>Date of birth</th>
      <th>President</th>
      <th>Birthplace</th>
      <th>State of birth</th>
      <th>In office</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>February 22, 1732</td>
      <td>George Washington</td>
      <td>Westmoreland County</td>
      <td>Virginia</td>
      <td>(1st) April 30, 1789 – March 4, 1797</td>
    </tr>
    <tr>
      <th>1</th>
      <td>October 30, 1735</td>
      <td>John Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(2nd) March 4, 1797 – March 4, 1801</td>
    </tr>
    <tr>
      <th>2</th>
      <td>April 13, 1743</td>
      <td>Thomas Jefferson</td>
      <td>Shadwell</td>
      <td>Virginia</td>
      <td>(3rd) March 4, 1801 – March 4, 1809</td>
    </tr>
    <tr>
      <th>3</th>
      <td>March 16, 1751</td>
      <td>James Madison</td>
      <td>Port Conway</td>
      <td>Virginia</td>
      <td>(4th) March 4, 1809 – March 4, 1817</td>
    </tr>
    <tr>
      <th>4</th>
      <td>April 28, 1758</td>
      <td>James Monroe</td>
      <td>Monroe Hall</td>
      <td>Virginia</td>
      <td>(5th) March 4, 1817 – March 4, 1825</td>
    </tr>
  </tbody>
</table>
</div>



To join tables `df` and `df2`, we call the function `df.merge(df2)`. Merge is just the word that the authors of pandas picked for joining tables. I don't know why.

Note: Unfortunately, Pandas also has a function called `df.join`. This is a limited version of `merge`. For ths sake of generality, we will only use `merge` in this class.

I can use the merge function to combine these two tables:


```python
elections.merge(presidents, 
            how = "inner",
            left_on = "Candidate", right_on = "President")
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
      <th>Date of birth</th>
      <th>President</th>
      <th>Birthplace</th>
      <th>State of birth</th>
      <th>In office</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1824</td>
      <td>Andrew Jackson</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>loss</td>
      <td>57.210122</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1828</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>642806</td>
      <td>win</td>
      <td>56.203927</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1832</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>702735</td>
      <td>win</td>
      <td>54.574789</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1824</td>
      <td>John Quincy Adams</td>
      <td>Democratic-Republican</td>
      <td>113142</td>
      <td>win</td>
      <td>42.789878</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1828</td>
      <td>John Quincy Adams</td>
      <td>National Republican</td>
      <td>500897</td>
      <td>loss</td>
      <td>43.796073</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1836</td>
      <td>Martin Van Buren</td>
      <td>Democratic</td>
      <td>763291</td>
      <td>win</td>
      <td>52.272472</td>
      <td>December 5, 1782</td>
      <td>Martin Van Buren</td>
      <td>Kinderhook</td>
      <td>New York</td>
      <td>(8th) March 4, 1837 – March 4, 1841</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1840</td>
      <td>Martin Van Buren</td>
      <td>Democratic</td>
      <td>1128854</td>
      <td>loss</td>
      <td>46.948787</td>
      <td>December 5, 1782</td>
      <td>Martin Van Buren</td>
      <td>Kinderhook</td>
      <td>New York</td>
      <td>(8th) March 4, 1837 – March 4, 1841</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1848</td>
      <td>Martin Van Buren</td>
      <td>Free Soil</td>
      <td>291501</td>
      <td>loss</td>
      <td>10.138474</td>
      <td>December 5, 1782</td>
      <td>Martin Van Buren</td>
      <td>Kinderhook</td>
      <td>New York</td>
      <td>(8th) March 4, 1837 – March 4, 1841</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1836</td>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>550816</td>
      <td>loss</td>
      <td>37.721543</td>
      <td>February 9, 1773</td>
      <td>William Henry Harrison</td>
      <td>Charles City County</td>
      <td>Virginia</td>
      <td>(9th) March 4, 1841 – April 4, 1841</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1840</td>
      <td>William Henry Harrison</td>
      <td>Whig</td>
      <td>1275583</td>
      <td>win</td>
      <td>53.051213</td>
      <td>February 9, 1773</td>
      <td>William Henry Harrison</td>
      <td>Charles City County</td>
      <td>Virginia</td>
      <td>(9th) March 4, 1841 – April 4, 1841</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1848</td>
      <td>Zachary Taylor</td>
      <td>Whig</td>
      <td>1360235</td>
      <td>win</td>
      <td>47.309296</td>
      <td>November 24, 1784</td>
      <td>Zachary Taylor</td>
      <td>Barboursville</td>
      <td>Virginia</td>
      <td>(12th) March 4, 1849 – July 9, 1850</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1852</td>
      <td>Franklin Pierce</td>
      <td>Democratic</td>
      <td>1605943</td>
      <td>win</td>
      <td>51.013168</td>
      <td>November 23, 1804</td>
      <td>Franklin Pierce</td>
      <td>Hillsborough</td>
      <td>New Hampshire</td>
      <td>(14th) March 4, 1853 – March 4, 1857</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1856</td>
      <td>James Buchanan</td>
      <td>Democratic</td>
      <td>1835140</td>
      <td>win</td>
      <td>45.306080</td>
      <td>April 23, 1791</td>
      <td>James Buchanan</td>
      <td>Cove Gap</td>
      <td>Pennsylvania</td>
      <td>(15th) March 4, 1857 – March 4, 1861</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1856</td>
      <td>Millard Fillmore</td>
      <td>American</td>
      <td>873053</td>
      <td>loss</td>
      <td>21.554001</td>
      <td>January 7, 1800</td>
      <td>Millard Fillmore</td>
      <td>Summerhill</td>
      <td>New York</td>
      <td>(13th) July 9, 1850 – March 4, 1853</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1860</td>
      <td>Abraham Lincoln</td>
      <td>Republican</td>
      <td>1855993</td>
      <td>win</td>
      <td>39.699408</td>
      <td>February 12, 1809</td>
      <td>Abraham Lincoln</td>
      <td>Sinking Spring</td>
      <td>Kentucky</td>
      <td>(16th) March 4, 1861 – April 15, 1865</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1864</td>
      <td>Abraham Lincoln</td>
      <td>National Union</td>
      <td>2211317</td>
      <td>win</td>
      <td>54.951512</td>
      <td>February 12, 1809</td>
      <td>Abraham Lincoln</td>
      <td>Sinking Spring</td>
      <td>Kentucky</td>
      <td>(16th) March 4, 1861 – April 15, 1865</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1884</td>
      <td>Grover Cleveland</td>
      <td>Democratic</td>
      <td>4914482</td>
      <td>win</td>
      <td>48.884933</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(22nd) March 4, 1885 – March 4, 1889</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1884</td>
      <td>Grover Cleveland</td>
      <td>Democratic</td>
      <td>4914482</td>
      <td>win</td>
      <td>48.884933</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(24th) March 4, 1893 – March 4, 1897</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1888</td>
      <td>Grover Cleveland</td>
      <td>Democratic</td>
      <td>5534488</td>
      <td>loss</td>
      <td>48.656799</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(22nd) March 4, 1885 – March 4, 1889</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1888</td>
      <td>Grover Cleveland</td>
      <td>Democratic</td>
      <td>5534488</td>
      <td>loss</td>
      <td>48.656799</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(24th) March 4, 1893 – March 4, 1897</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1892</td>
      <td>Grover Cleveland</td>
      <td>Democratic</td>
      <td>5553898</td>
      <td>win</td>
      <td>46.121393</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(22nd) March 4, 1885 – March 4, 1889</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1892</td>
      <td>Grover Cleveland</td>
      <td>Democratic</td>
      <td>5553898</td>
      <td>win</td>
      <td>46.121393</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(24th) March 4, 1893 – March 4, 1897</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1888</td>
      <td>Benjamin Harrison</td>
      <td>Republican</td>
      <td>5443633</td>
      <td>win</td>
      <td>47.858041</td>
      <td>August 20, 1833</td>
      <td>Benjamin Harrison</td>
      <td>North Bend</td>
      <td>Ohio</td>
      <td>(23rd) March 4, 1889 – March 4, 1893</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1892</td>
      <td>Benjamin Harrison</td>
      <td>Republican</td>
      <td>5176108</td>
      <td>loss</td>
      <td>42.984101</td>
      <td>August 20, 1833</td>
      <td>Benjamin Harrison</td>
      <td>North Bend</td>
      <td>Ohio</td>
      <td>(23rd) March 4, 1889 – March 4, 1893</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1896</td>
      <td>William McKinley</td>
      <td>Republican</td>
      <td>7112138</td>
      <td>win</td>
      <td>51.213817</td>
      <td>January 29, 1843</td>
      <td>William McKinley</td>
      <td>Niles</td>
      <td>Ohio</td>
      <td>(25th) March 4, 1897 – September 14, 1901</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1900</td>
      <td>William McKinley</td>
      <td>Republican</td>
      <td>7228864</td>
      <td>win</td>
      <td>52.342640</td>
      <td>January 29, 1843</td>
      <td>William McKinley</td>
      <td>Niles</td>
      <td>Ohio</td>
      <td>(25th) March 4, 1897 – September 14, 1901</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1904</td>
      <td>Theodore Roosevelt</td>
      <td>Republican</td>
      <td>7630557</td>
      <td>win</td>
      <td>56.562787</td>
      <td>October 27, 1858</td>
      <td>Theodore Roosevelt</td>
      <td>New York City</td>
      <td>New York</td>
      <td>(26th) September 14, 1901 – March 4, 1909</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1912</td>
      <td>Theodore Roosevelt</td>
      <td>Progressive</td>
      <td>4122721</td>
      <td>loss</td>
      <td>27.457433</td>
      <td>October 27, 1858</td>
      <td>Theodore Roosevelt</td>
      <td>New York City</td>
      <td>New York</td>
      <td>(26th) September 14, 1901 – March 4, 1909</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1912</td>
      <td>Woodrow Wilson</td>
      <td>Democratic</td>
      <td>6296284</td>
      <td>win</td>
      <td>41.933422</td>
      <td>December 28, 1856</td>
      <td>Woodrow Wilson</td>
      <td>Staunton</td>
      <td>Virginia</td>
      <td>(28th) March 4, 1913 – March 4, 1921</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1916</td>
      <td>Woodrow Wilson</td>
      <td>Democratic</td>
      <td>9126868</td>
      <td>win</td>
      <td>49.367987</td>
      <td>December 28, 1856</td>
      <td>Woodrow Wilson</td>
      <td>Staunton</td>
      <td>Virginia</td>
      <td>(28th) March 4, 1913 – March 4, 1921</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1924</td>
      <td>Calvin Coolidge</td>
      <td>Republican</td>
      <td>15723789</td>
      <td>win</td>
      <td>54.329113</td>
      <td>July 4, 1872</td>
      <td>Calvin Coolidge</td>
      <td>Plymouth</td>
      <td>Vermont</td>
      <td>(30th) August 2, 1923 – March 4, 1929</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1928</td>
      <td>Herbert Hoover</td>
      <td>Republican</td>
      <td>21427123</td>
      <td>win</td>
      <td>58.368524</td>
      <td>August 10, 1874</td>
      <td>Herbert Hoover</td>
      <td>West Branch</td>
      <td>Iowa</td>
      <td>(31st) March 4, 1929 – March 4, 1933</td>
    </tr>
    <tr>
      <th>32</th>
      <td>1932</td>
      <td>Herbert Hoover</td>
      <td>Republican</td>
      <td>15761254</td>
      <td>loss</td>
      <td>39.830594</td>
      <td>August 10, 1874</td>
      <td>Herbert Hoover</td>
      <td>West Branch</td>
      <td>Iowa</td>
      <td>(31st) March 4, 1929 – March 4, 1933</td>
    </tr>
    <tr>
      <th>33</th>
      <td>1960</td>
      <td>Richard Nixon</td>
      <td>Republican</td>
      <td>34108157</td>
      <td>loss</td>
      <td>49.917439</td>
      <td>January 9, 1913</td>
      <td>Richard Nixon</td>
      <td>Yorba Linda</td>
      <td>California</td>
      <td>(37th) January 20, 1969 – August 9, 1974</td>
    </tr>
    <tr>
      <th>34</th>
      <td>1968</td>
      <td>Richard Nixon</td>
      <td>Republican</td>
      <td>31783783</td>
      <td>win</td>
      <td>43.565246</td>
      <td>January 9, 1913</td>
      <td>Richard Nixon</td>
      <td>Yorba Linda</td>
      <td>California</td>
      <td>(37th) January 20, 1969 – August 9, 1974</td>
    </tr>
    <tr>
      <th>35</th>
      <td>1972</td>
      <td>Richard Nixon</td>
      <td>Republican</td>
      <td>47168710</td>
      <td>win</td>
      <td>60.907806</td>
      <td>January 9, 1913</td>
      <td>Richard Nixon</td>
      <td>Yorba Linda</td>
      <td>California</td>
      <td>(37th) January 20, 1969 – August 9, 1974</td>
    </tr>
    <tr>
      <th>36</th>
      <td>1976</td>
      <td>Gerald Ford</td>
      <td>Republican</td>
      <td>39148634</td>
      <td>loss</td>
      <td>48.199499</td>
      <td>July 14, 1913</td>
      <td>Gerald Ford</td>
      <td>Omaha</td>
      <td>Nebraska</td>
      <td>(38th) August 9, 1974 – January 20, 1977</td>
    </tr>
    <tr>
      <th>37</th>
      <td>1976</td>
      <td>Jimmy Carter</td>
      <td>Democratic</td>
      <td>40831881</td>
      <td>win</td>
      <td>50.271900</td>
      <td>October 1, 1924</td>
      <td>Jimmy Carter</td>
      <td>Plains</td>
      <td>Georgia</td>
      <td>(39th) January 20, 1977 – January 20, 1981</td>
    </tr>
    <tr>
      <th>38</th>
      <td>1980</td>
      <td>Jimmy Carter</td>
      <td>Democratic</td>
      <td>35480115</td>
      <td>loss</td>
      <td>41.132848</td>
      <td>October 1, 1924</td>
      <td>Jimmy Carter</td>
      <td>Plains</td>
      <td>Georgia</td>
      <td>(39th) January 20, 1977 – January 20, 1981</td>
    </tr>
    <tr>
      <th>39</th>
      <td>1980</td>
      <td>Ronald Reagan</td>
      <td>Republican</td>
      <td>43903230</td>
      <td>win</td>
      <td>50.897944</td>
      <td>February 6, 1911</td>
      <td>Ronald Reagan</td>
      <td>Tampico</td>
      <td>Illinois</td>
      <td>(40th) January 20, 1981 – January 20, 1989</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1984</td>
      <td>Ronald Reagan</td>
      <td>Republican</td>
      <td>54455472</td>
      <td>win</td>
      <td>59.023326</td>
      <td>February 6, 1911</td>
      <td>Ronald Reagan</td>
      <td>Tampico</td>
      <td>Illinois</td>
      <td>(40th) January 20, 1981 – January 20, 1989</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1988</td>
      <td>George H. W. Bush</td>
      <td>Republican</td>
      <td>48886597</td>
      <td>win</td>
      <td>53.518845</td>
      <td>June 12, 1924</td>
      <td>George H. W. Bush</td>
      <td>Milton</td>
      <td>Massachusetts</td>
      <td>(41st) January 20, 1989 – January 20, 1993</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1992</td>
      <td>George H. W. Bush</td>
      <td>Republican</td>
      <td>39104550</td>
      <td>loss</td>
      <td>37.544784</td>
      <td>June 12, 1924</td>
      <td>George H. W. Bush</td>
      <td>Milton</td>
      <td>Massachusetts</td>
      <td>(41st) January 20, 1989 – January 20, 1993</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1992</td>
      <td>Bill Clinton</td>
      <td>Democratic</td>
      <td>44909806</td>
      <td>win</td>
      <td>43.118485</td>
      <td>August 19, 1946</td>
      <td>Bill Clinton</td>
      <td>Hope</td>
      <td>Arkansas</td>
      <td>(42nd) January 20, 1993 – January 20, 2001</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1996</td>
      <td>Bill Clinton</td>
      <td>Democratic</td>
      <td>47400125</td>
      <td>win</td>
      <td>49.296938</td>
      <td>August 19, 1946</td>
      <td>Bill Clinton</td>
      <td>Hope</td>
      <td>Arkansas</td>
      <td>(42nd) January 20, 1993 – January 20, 2001</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2000</td>
      <td>George W. Bush</td>
      <td>Republican</td>
      <td>50456002</td>
      <td>win</td>
      <td>47.974666</td>
      <td>July 6, 1946</td>
      <td>George W. Bush</td>
      <td>New Haven</td>
      <td>Connecticut</td>
      <td>(43rd) January 20, 2001 – January 20, 2009</td>
    </tr>
    <tr>
      <th>46</th>
      <td>2004</td>
      <td>George W. Bush</td>
      <td>Republican</td>
      <td>62040610</td>
      <td>win</td>
      <td>50.771824</td>
      <td>July 6, 1946</td>
      <td>George W. Bush</td>
      <td>New Haven</td>
      <td>Connecticut</td>
      <td>(43rd) January 20, 2001 – January 20, 2009</td>
    </tr>
    <tr>
      <th>47</th>
      <td>2016</td>
      <td>Donald Trump</td>
      <td>Republican</td>
      <td>62984828</td>
      <td>win</td>
      <td>46.407862</td>
      <td>June 14, 1946</td>
      <td>Donald Trump</td>
      <td>Queens</td>
      <td>New York</td>
      <td>(45th) January 20, 2017 – Incumbent</td>
    </tr>
  </tbody>
</table>
</div>



Notice that:
1. The output dataframe only contains rows that have names in both tables.  For example, presidents before 1824 do not appear in the joined table because there was no popular vote before 1824.
1. The name `Andrew Jackson` occurred three times in the election table and shows up three times in the output. 
1. `Grover Cleveland` occurs six times! Twice for every election he was in. This is because he appears three times in the `elections` table and twice in the `presidents` table. This results in 3 x 2 = 6 combinations.
1. Several presidents are missing because their names are not an exact match. For example, John F. Kennedy is "John Kennedy" in the elections table and "John F. Kennedy" in the presidents table.

With the caveats above in mind, this merged DataFrame is handy because we can use it to plot, e.g. the age of each president when they were elected.


```python
joined = elections.merge(presidents, 
            how = "inner",
            left_on = "Candidate", right_on = "President")

winners = joined.query("Result == 'win'").copy()
winners["Birthyear"] = winners["Date of birth"].str.split(',').str[1].map(int)
winners["Age"] = winners["Year"] - winners["Birthyear"]
sns.lmplot(data=winners, x="Year", y="Age")
```




    <seaborn.axisgrid.FacetGrid at 0x7f4f28470760>




    
![png](join_demo_files/join_demo_13_1.png)
    


### How could we fix the duplicate Grover Cleveland?

We could group by name/candidate and take only the first:


```python
(
        elections.merge(presidents, 
            how = "inner",
            left_on = "Candidate", right_on = "President")
        .groupby(['Candidate', 'Year']).first().reset_index()
)
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
      <th>Candidate</th>
      <th>Year</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
      <th>Date of birth</th>
      <th>President</th>
      <th>Birthplace</th>
      <th>State of birth</th>
      <th>In office</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Abraham Lincoln</td>
      <td>1860</td>
      <td>Republican</td>
      <td>1855993</td>
      <td>win</td>
      <td>39.699408</td>
      <td>February 12, 1809</td>
      <td>Abraham Lincoln</td>
      <td>Sinking Spring</td>
      <td>Kentucky</td>
      <td>(16th) March 4, 1861 – April 15, 1865</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Abraham Lincoln</td>
      <td>1864</td>
      <td>National Union</td>
      <td>2211317</td>
      <td>win</td>
      <td>54.951512</td>
      <td>February 12, 1809</td>
      <td>Abraham Lincoln</td>
      <td>Sinking Spring</td>
      <td>Kentucky</td>
      <td>(16th) March 4, 1861 – April 15, 1865</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Andrew Jackson</td>
      <td>1824</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>loss</td>
      <td>57.210122</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andrew Jackson</td>
      <td>1828</td>
      <td>Democratic</td>
      <td>642806</td>
      <td>win</td>
      <td>56.203927</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Andrew Jackson</td>
      <td>1832</td>
      <td>Democratic</td>
      <td>702735</td>
      <td>win</td>
      <td>54.574789</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Benjamin Harrison</td>
      <td>1888</td>
      <td>Republican</td>
      <td>5443633</td>
      <td>win</td>
      <td>47.858041</td>
      <td>August 20, 1833</td>
      <td>Benjamin Harrison</td>
      <td>North Bend</td>
      <td>Ohio</td>
      <td>(23rd) March 4, 1889 – March 4, 1893</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Benjamin Harrison</td>
      <td>1892</td>
      <td>Republican</td>
      <td>5176108</td>
      <td>loss</td>
      <td>42.984101</td>
      <td>August 20, 1833</td>
      <td>Benjamin Harrison</td>
      <td>North Bend</td>
      <td>Ohio</td>
      <td>(23rd) March 4, 1889 – March 4, 1893</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bill Clinton</td>
      <td>1992</td>
      <td>Democratic</td>
      <td>44909806</td>
      <td>win</td>
      <td>43.118485</td>
      <td>August 19, 1946</td>
      <td>Bill Clinton</td>
      <td>Hope</td>
      <td>Arkansas</td>
      <td>(42nd) January 20, 1993 – January 20, 2001</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bill Clinton</td>
      <td>1996</td>
      <td>Democratic</td>
      <td>47400125</td>
      <td>win</td>
      <td>49.296938</td>
      <td>August 19, 1946</td>
      <td>Bill Clinton</td>
      <td>Hope</td>
      <td>Arkansas</td>
      <td>(42nd) January 20, 1993 – January 20, 2001</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Calvin Coolidge</td>
      <td>1924</td>
      <td>Republican</td>
      <td>15723789</td>
      <td>win</td>
      <td>54.329113</td>
      <td>July 4, 1872</td>
      <td>Calvin Coolidge</td>
      <td>Plymouth</td>
      <td>Vermont</td>
      <td>(30th) August 2, 1923 – March 4, 1929</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Donald Trump</td>
      <td>2016</td>
      <td>Republican</td>
      <td>62984828</td>
      <td>win</td>
      <td>46.407862</td>
      <td>June 14, 1946</td>
      <td>Donald Trump</td>
      <td>Queens</td>
      <td>New York</td>
      <td>(45th) January 20, 2017 – Incumbent</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Franklin Pierce</td>
      <td>1852</td>
      <td>Democratic</td>
      <td>1605943</td>
      <td>win</td>
      <td>51.013168</td>
      <td>November 23, 1804</td>
      <td>Franklin Pierce</td>
      <td>Hillsborough</td>
      <td>New Hampshire</td>
      <td>(14th) March 4, 1853 – March 4, 1857</td>
    </tr>
    <tr>
      <th>12</th>
      <td>George H. W. Bush</td>
      <td>1988</td>
      <td>Republican</td>
      <td>48886597</td>
      <td>win</td>
      <td>53.518845</td>
      <td>June 12, 1924</td>
      <td>George H. W. Bush</td>
      <td>Milton</td>
      <td>Massachusetts</td>
      <td>(41st) January 20, 1989 – January 20, 1993</td>
    </tr>
    <tr>
      <th>13</th>
      <td>George H. W. Bush</td>
      <td>1992</td>
      <td>Republican</td>
      <td>39104550</td>
      <td>loss</td>
      <td>37.544784</td>
      <td>June 12, 1924</td>
      <td>George H. W. Bush</td>
      <td>Milton</td>
      <td>Massachusetts</td>
      <td>(41st) January 20, 1989 – January 20, 1993</td>
    </tr>
    <tr>
      <th>14</th>
      <td>George W. Bush</td>
      <td>2000</td>
      <td>Republican</td>
      <td>50456002</td>
      <td>win</td>
      <td>47.974666</td>
      <td>July 6, 1946</td>
      <td>George W. Bush</td>
      <td>New Haven</td>
      <td>Connecticut</td>
      <td>(43rd) January 20, 2001 – January 20, 2009</td>
    </tr>
    <tr>
      <th>15</th>
      <td>George W. Bush</td>
      <td>2004</td>
      <td>Republican</td>
      <td>62040610</td>
      <td>win</td>
      <td>50.771824</td>
      <td>July 6, 1946</td>
      <td>George W. Bush</td>
      <td>New Haven</td>
      <td>Connecticut</td>
      <td>(43rd) January 20, 2001 – January 20, 2009</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Gerald Ford</td>
      <td>1976</td>
      <td>Republican</td>
      <td>39148634</td>
      <td>loss</td>
      <td>48.199499</td>
      <td>July 14, 1913</td>
      <td>Gerald Ford</td>
      <td>Omaha</td>
      <td>Nebraska</td>
      <td>(38th) August 9, 1974 – January 20, 1977</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Grover Cleveland</td>
      <td>1884</td>
      <td>Democratic</td>
      <td>4914482</td>
      <td>win</td>
      <td>48.884933</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(22nd) March 4, 1885 – March 4, 1889</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Grover Cleveland</td>
      <td>1888</td>
      <td>Democratic</td>
      <td>5534488</td>
      <td>loss</td>
      <td>48.656799</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(22nd) March 4, 1885 – March 4, 1889</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Grover Cleveland</td>
      <td>1892</td>
      <td>Democratic</td>
      <td>5553898</td>
      <td>win</td>
      <td>46.121393</td>
      <td>March 18, 1837</td>
      <td>Grover Cleveland</td>
      <td>Caldwell</td>
      <td>New Jersey</td>
      <td>(22nd) March 4, 1885 – March 4, 1889</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Herbert Hoover</td>
      <td>1928</td>
      <td>Republican</td>
      <td>21427123</td>
      <td>win</td>
      <td>58.368524</td>
      <td>August 10, 1874</td>
      <td>Herbert Hoover</td>
      <td>West Branch</td>
      <td>Iowa</td>
      <td>(31st) March 4, 1929 – March 4, 1933</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Herbert Hoover</td>
      <td>1932</td>
      <td>Republican</td>
      <td>15761254</td>
      <td>loss</td>
      <td>39.830594</td>
      <td>August 10, 1874</td>
      <td>Herbert Hoover</td>
      <td>West Branch</td>
      <td>Iowa</td>
      <td>(31st) March 4, 1929 – March 4, 1933</td>
    </tr>
    <tr>
      <th>22</th>
      <td>James Buchanan</td>
      <td>1856</td>
      <td>Democratic</td>
      <td>1835140</td>
      <td>win</td>
      <td>45.306080</td>
      <td>April 23, 1791</td>
      <td>James Buchanan</td>
      <td>Cove Gap</td>
      <td>Pennsylvania</td>
      <td>(15th) March 4, 1857 – March 4, 1861</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Jimmy Carter</td>
      <td>1976</td>
      <td>Democratic</td>
      <td>40831881</td>
      <td>win</td>
      <td>50.271900</td>
      <td>October 1, 1924</td>
      <td>Jimmy Carter</td>
      <td>Plains</td>
      <td>Georgia</td>
      <td>(39th) January 20, 1977 – January 20, 1981</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Jimmy Carter</td>
      <td>1980</td>
      <td>Democratic</td>
      <td>35480115</td>
      <td>loss</td>
      <td>41.132848</td>
      <td>October 1, 1924</td>
      <td>Jimmy Carter</td>
      <td>Plains</td>
      <td>Georgia</td>
      <td>(39th) January 20, 1977 – January 20, 1981</td>
    </tr>
    <tr>
      <th>25</th>
      <td>John Quincy Adams</td>
      <td>1824</td>
      <td>Democratic-Republican</td>
      <td>113142</td>
      <td>win</td>
      <td>42.789878</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>26</th>
      <td>John Quincy Adams</td>
      <td>1828</td>
      <td>National Republican</td>
      <td>500897</td>
      <td>loss</td>
      <td>43.796073</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Martin Van Buren</td>
      <td>1836</td>
      <td>Democratic</td>
      <td>763291</td>
      <td>win</td>
      <td>52.272472</td>
      <td>December 5, 1782</td>
      <td>Martin Van Buren</td>
      <td>Kinderhook</td>
      <td>New York</td>
      <td>(8th) March 4, 1837 – March 4, 1841</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Martin Van Buren</td>
      <td>1840</td>
      <td>Democratic</td>
      <td>1128854</td>
      <td>loss</td>
      <td>46.948787</td>
      <td>December 5, 1782</td>
      <td>Martin Van Buren</td>
      <td>Kinderhook</td>
      <td>New York</td>
      <td>(8th) March 4, 1837 – March 4, 1841</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Martin Van Buren</td>
      <td>1848</td>
      <td>Free Soil</td>
      <td>291501</td>
      <td>loss</td>
      <td>10.138474</td>
      <td>December 5, 1782</td>
      <td>Martin Van Buren</td>
      <td>Kinderhook</td>
      <td>New York</td>
      <td>(8th) March 4, 1837 – March 4, 1841</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Millard Fillmore</td>
      <td>1856</td>
      <td>American</td>
      <td>873053</td>
      <td>loss</td>
      <td>21.554001</td>
      <td>January 7, 1800</td>
      <td>Millard Fillmore</td>
      <td>Summerhill</td>
      <td>New York</td>
      <td>(13th) July 9, 1850 – March 4, 1853</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Richard Nixon</td>
      <td>1960</td>
      <td>Republican</td>
      <td>34108157</td>
      <td>loss</td>
      <td>49.917439</td>
      <td>January 9, 1913</td>
      <td>Richard Nixon</td>
      <td>Yorba Linda</td>
      <td>California</td>
      <td>(37th) January 20, 1969 – August 9, 1974</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Richard Nixon</td>
      <td>1968</td>
      <td>Republican</td>
      <td>31783783</td>
      <td>win</td>
      <td>43.565246</td>
      <td>January 9, 1913</td>
      <td>Richard Nixon</td>
      <td>Yorba Linda</td>
      <td>California</td>
      <td>(37th) January 20, 1969 – August 9, 1974</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Richard Nixon</td>
      <td>1972</td>
      <td>Republican</td>
      <td>47168710</td>
      <td>win</td>
      <td>60.907806</td>
      <td>January 9, 1913</td>
      <td>Richard Nixon</td>
      <td>Yorba Linda</td>
      <td>California</td>
      <td>(37th) January 20, 1969 – August 9, 1974</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Ronald Reagan</td>
      <td>1980</td>
      <td>Republican</td>
      <td>43903230</td>
      <td>win</td>
      <td>50.897944</td>
      <td>February 6, 1911</td>
      <td>Ronald Reagan</td>
      <td>Tampico</td>
      <td>Illinois</td>
      <td>(40th) January 20, 1981 – January 20, 1989</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Ronald Reagan</td>
      <td>1984</td>
      <td>Republican</td>
      <td>54455472</td>
      <td>win</td>
      <td>59.023326</td>
      <td>February 6, 1911</td>
      <td>Ronald Reagan</td>
      <td>Tampico</td>
      <td>Illinois</td>
      <td>(40th) January 20, 1981 – January 20, 1989</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Theodore Roosevelt</td>
      <td>1904</td>
      <td>Republican</td>
      <td>7630557</td>
      <td>win</td>
      <td>56.562787</td>
      <td>October 27, 1858</td>
      <td>Theodore Roosevelt</td>
      <td>New York City</td>
      <td>New York</td>
      <td>(26th) September 14, 1901 – March 4, 1909</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Theodore Roosevelt</td>
      <td>1912</td>
      <td>Progressive</td>
      <td>4122721</td>
      <td>loss</td>
      <td>27.457433</td>
      <td>October 27, 1858</td>
      <td>Theodore Roosevelt</td>
      <td>New York City</td>
      <td>New York</td>
      <td>(26th) September 14, 1901 – March 4, 1909</td>
    </tr>
    <tr>
      <th>38</th>
      <td>William Henry Harrison</td>
      <td>1836</td>
      <td>Whig</td>
      <td>550816</td>
      <td>loss</td>
      <td>37.721543</td>
      <td>February 9, 1773</td>
      <td>William Henry Harrison</td>
      <td>Charles City County</td>
      <td>Virginia</td>
      <td>(9th) March 4, 1841 – April 4, 1841</td>
    </tr>
    <tr>
      <th>39</th>
      <td>William Henry Harrison</td>
      <td>1840</td>
      <td>Whig</td>
      <td>1275583</td>
      <td>win</td>
      <td>53.051213</td>
      <td>February 9, 1773</td>
      <td>William Henry Harrison</td>
      <td>Charles City County</td>
      <td>Virginia</td>
      <td>(9th) March 4, 1841 – April 4, 1841</td>
    </tr>
    <tr>
      <th>40</th>
      <td>William McKinley</td>
      <td>1896</td>
      <td>Republican</td>
      <td>7112138</td>
      <td>win</td>
      <td>51.213817</td>
      <td>January 29, 1843</td>
      <td>William McKinley</td>
      <td>Niles</td>
      <td>Ohio</td>
      <td>(25th) March 4, 1897 – September 14, 1901</td>
    </tr>
    <tr>
      <th>41</th>
      <td>William McKinley</td>
      <td>1900</td>
      <td>Republican</td>
      <td>7228864</td>
      <td>win</td>
      <td>52.342640</td>
      <td>January 29, 1843</td>
      <td>William McKinley</td>
      <td>Niles</td>
      <td>Ohio</td>
      <td>(25th) March 4, 1897 – September 14, 1901</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Woodrow Wilson</td>
      <td>1912</td>
      <td>Democratic</td>
      <td>6296284</td>
      <td>win</td>
      <td>41.933422</td>
      <td>December 28, 1856</td>
      <td>Woodrow Wilson</td>
      <td>Staunton</td>
      <td>Virginia</td>
      <td>(28th) March 4, 1913 – March 4, 1921</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Woodrow Wilson</td>
      <td>1916</td>
      <td>Democratic</td>
      <td>9126868</td>
      <td>win</td>
      <td>49.367987</td>
      <td>December 28, 1856</td>
      <td>Woodrow Wilson</td>
      <td>Staunton</td>
      <td>Virginia</td>
      <td>(28th) March 4, 1913 – March 4, 1921</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Zachary Taylor</td>
      <td>1848</td>
      <td>Whig</td>
      <td>1360235</td>
      <td>win</td>
      <td>47.309296</td>
      <td>November 24, 1784</td>
      <td>Zachary Taylor</td>
      <td>Barboursville</td>
      <td>Virginia</td>
      <td>(12th) March 4, 1849 – July 9, 1850</td>
    </tr>
  </tbody>
</table>
</div>



### Right Join

The above join was an inner join.  What if we wanted to keep all of the presidents and leave missing data for years when there was no popular vote? In this case we'd do a "right" join, where we make sure to include EVERY row from our right dataframe, in this case `presidents`.


```python
elections.merge(presidents, 
            how = "right",
            left_on = "Candidate", right_on = "President")
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
      <th>Date of birth</th>
      <th>President</th>
      <th>Birthplace</th>
      <th>State of birth</th>
      <th>In office</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>February 22, 1732</td>
      <td>George Washington</td>
      <td>Westmoreland County</td>
      <td>Virginia</td>
      <td>(1st) April 30, 1789 – March 4, 1797</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>October 30, 1735</td>
      <td>John Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(2nd) March 4, 1797 – March 4, 1801</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>April 13, 1743</td>
      <td>Thomas Jefferson</td>
      <td>Shadwell</td>
      <td>Virginia</td>
      <td>(3rd) March 4, 1801 – March 4, 1809</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>March 16, 1751</td>
      <td>James Madison</td>
      <td>Port Conway</td>
      <td>Virginia</td>
      <td>(4th) March 4, 1809 – March 4, 1817</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>April 28, 1758</td>
      <td>James Monroe</td>
      <td>Monroe Hall</td>
      <td>Virginia</td>
      <td>(5th) March 4, 1817 – March 4, 1825</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2000.0</td>
      <td>George W. Bush</td>
      <td>Republican</td>
      <td>50456002.0</td>
      <td>win</td>
      <td>47.974666</td>
      <td>July 6, 1946</td>
      <td>George W. Bush</td>
      <td>New Haven</td>
      <td>Connecticut</td>
      <td>(43rd) January 20, 2001 – January 20, 2009</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2004.0</td>
      <td>George W. Bush</td>
      <td>Republican</td>
      <td>62040610.0</td>
      <td>win</td>
      <td>50.771824</td>
      <td>July 6, 1946</td>
      <td>George W. Bush</td>
      <td>New Haven</td>
      <td>Connecticut</td>
      <td>(43rd) January 20, 2001 – January 20, 2009</td>
    </tr>
    <tr>
      <th>65</th>
      <td>1992.0</td>
      <td>Bill Clinton</td>
      <td>Democratic</td>
      <td>44909806.0</td>
      <td>win</td>
      <td>43.118485</td>
      <td>August 19, 1946</td>
      <td>Bill Clinton</td>
      <td>Hope</td>
      <td>Arkansas</td>
      <td>(42nd) January 20, 1993 – January 20, 2001</td>
    </tr>
    <tr>
      <th>66</th>
      <td>1996.0</td>
      <td>Bill Clinton</td>
      <td>Democratic</td>
      <td>47400125.0</td>
      <td>win</td>
      <td>49.296938</td>
      <td>August 19, 1946</td>
      <td>Bill Clinton</td>
      <td>Hope</td>
      <td>Arkansas</td>
      <td>(42nd) January 20, 1993 – January 20, 2001</td>
    </tr>
    <tr>
      <th>67</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>August 4, 1961</td>
      <td>Barack H. Obama</td>
      <td>Honolulu</td>
      <td>Hawaii</td>
      <td>(44th) January 20, 2009 – January 20, 2017</td>
    </tr>
  </tbody>
</table>
<p>68 rows × 11 columns</p>
</div>



Similarly, if we also want to include candidates not in the presidents table (e.g. because they had never won), we can use a "left" join.


```python
elections.merge(presidents, 
            how = "left",
            left_on = "Candidate", right_on = "President")
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
      <th>Date of birth</th>
      <th>President</th>
      <th>Birthplace</th>
      <th>State of birth</th>
      <th>In office</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1824</td>
      <td>Andrew Jackson</td>
      <td>Democratic-Republican</td>
      <td>151271</td>
      <td>loss</td>
      <td>57.210122</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1824</td>
      <td>John Quincy Adams</td>
      <td>Democratic-Republican</td>
      <td>113142</td>
      <td>win</td>
      <td>42.789878</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1828</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>642806</td>
      <td>win</td>
      <td>56.203927</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1828</td>
      <td>John Quincy Adams</td>
      <td>National Republican</td>
      <td>500897</td>
      <td>loss</td>
      <td>43.796073</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1832</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>702735</td>
      <td>win</td>
      <td>54.574789</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>176</th>
      <td>2016</td>
      <td>Donald Trump</td>
      <td>Republican</td>
      <td>62984828</td>
      <td>win</td>
      <td>46.407862</td>
      <td>June 14, 1946</td>
      <td>Donald Trump</td>
      <td>Queens</td>
      <td>New York</td>
      <td>(45th) January 20, 2017 – Incumbent</td>
    </tr>
    <tr>
      <th>177</th>
      <td>2016</td>
      <td>Evan McMullin</td>
      <td>Independent</td>
      <td>732273</td>
      <td>loss</td>
      <td>0.539546</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>178</th>
      <td>2016</td>
      <td>Gary Johnson</td>
      <td>Libertarian</td>
      <td>4489235</td>
      <td>loss</td>
      <td>3.307714</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>179</th>
      <td>2016</td>
      <td>Hillary Clinton</td>
      <td>Democratic</td>
      <td>65853514</td>
      <td>loss</td>
      <td>48.521539</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>180</th>
      <td>2016</td>
      <td>Jill Stein</td>
      <td>Green</td>
      <td>1457226</td>
      <td>loss</td>
      <td>1.073699</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>181 rows × 11 columns</p>
</div>



If we wanted to keep both, we can instead do an "outer join".


```python
elections.merge(presidents, 
            how = "outer",
            left_on = "Candidate", right_on = "President")
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
      <th>Year</th>
      <th>Candidate</th>
      <th>Party</th>
      <th>Popular vote</th>
      <th>Result</th>
      <th>%</th>
      <th>Date of birth</th>
      <th>President</th>
      <th>Birthplace</th>
      <th>State of birth</th>
      <th>In office</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1824.0</td>
      <td>Andrew Jackson</td>
      <td>Democratic-Republican</td>
      <td>151271.0</td>
      <td>loss</td>
      <td>57.210122</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1828.0</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>642806.0</td>
      <td>win</td>
      <td>56.203927</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1832.0</td>
      <td>Andrew Jackson</td>
      <td>Democratic</td>
      <td>702735.0</td>
      <td>win</td>
      <td>54.574789</td>
      <td>March 15, 1767</td>
      <td>Andrew Jackson</td>
      <td>Waxhaws Region</td>
      <td>South/North Carolina</td>
      <td>(7th) March 4, 1829 – March 4, 1837</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1824.0</td>
      <td>John Quincy Adams</td>
      <td>Democratic-Republican</td>
      <td>113142.0</td>
      <td>win</td>
      <td>42.789878</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1828.0</td>
      <td>John Quincy Adams</td>
      <td>National Republican</td>
      <td>500897.0</td>
      <td>loss</td>
      <td>43.796073</td>
      <td>July 11, 1767</td>
      <td>John Quincy Adams</td>
      <td>Braintree</td>
      <td>Massachusetts</td>
      <td>(6th) March 4, 1825 – March 4, 1829</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>196</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>May 8, 1884</td>
      <td>Harry S. Truman</td>
      <td>Lamar</td>
      <td>Missouri</td>
      <td>(33rd) April 12, 1945 – January 20, 1953</td>
    </tr>
    <tr>
      <th>197</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>October 14, 1890</td>
      <td>Dwight D. Eisenhower</td>
      <td>Denison</td>
      <td>Texas</td>
      <td>(34th) January 20, 1953 – January 20, 1961</td>
    </tr>
    <tr>
      <th>198</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>August 27, 1908</td>
      <td>Lyndon B. Johnson</td>
      <td>Stonewall</td>
      <td>Texas</td>
      <td>(36th) November 22, 1963 – January 20, 1969</td>
    </tr>
    <tr>
      <th>199</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>May 29, 1917</td>
      <td>John F. Kennedy</td>
      <td>Brookline</td>
      <td>Massachusetts</td>
      <td>(35th) January 20, 1961 – November 22, 1963</td>
    </tr>
    <tr>
      <th>200</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>August 4, 1961</td>
      <td>Barack H. Obama</td>
      <td>Honolulu</td>
      <td>Hawaii</td>
      <td>(44th) January 20, 2009 – January 20, 2017</td>
    </tr>
  </tbody>
</table>
<p>201 rows × 11 columns</p>
</div>


