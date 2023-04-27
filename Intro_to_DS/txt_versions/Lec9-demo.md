```python
from datascience import *
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import numpy as np
```

## Lecture 9 ##

### Percentiles


```python
s = [1,7,3,5,9]
```


```python
percentile(10,s)
```




    1




```python
percentile(39,s)
```




    3




```python
percentile(40,s)
```




    3




```python
percentile(41,s)
```




    5




```python
percentile(50,s)
```




    5




```python
np.median(s)
```




    5.0



## San-Francisco salary


```python
sf = Table.read_table('san_francisco_2015.csv')
sf
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>WTR            </td> <td>PUC Water Department                  </td> <td>21        </td> <td>Prof & Tech Engineers - Miscellaneous, Local 21   </td> <td>2400           </td> <td>Lab, Pharmacy & Med Techs    </td> <td>2481    </td> <td>Water Qualitytech I/II        </td> <td>21538              </td> <td>82146   </td> <td>0       </td> <td>0             </td> <td>82146       </td> <td>16942.2   </td> <td>12340.9      </td> <td>6337.73       </td> <td>35620.8       </td> <td>117767            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>DPW            </td> <td>General Services Agency - Public Works</td> <td>12        </td> <td>Carpet, Linoleum and Soft Tile Workers, Local 12  </td> <td>7300           </td> <td>Journeyman Trade             </td> <td>7393    </td> <td>Soft Floor Coverer            </td> <td>5459               </td> <td>32165.8 </td> <td>973.19  </td> <td>848.96        </td> <td>33987.9     </td> <td>0         </td> <td>4587.51      </td> <td>2634.42       </td> <td>7221.93       </td> <td>41209.8           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                         </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021                  </td> <td>1600           </td> <td>Payroll, Billing & Accounting</td> <td>1636    </td> <td>Health Care Billing Clerk 2   </td> <td>41541              </td> <td>71311   </td> <td>5757.98 </td> <td>0             </td> <td>77069       </td> <td>14697.6   </td> <td>12424.5      </td> <td>6370.06       </td> <td>33492.2       </td> <td>110561            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                         </td> <td>351       </td> <td>Municipal Executive Association - Miscellaneous   </td> <td>0900           </td> <td>Management                   </td> <td>2620    </td> <td>Food Service Mgr Administrator</td> <td>26718              </td> <td>28430.2 </td> <td>0       </td> <td>763.07        </td> <td>29193.3     </td> <td>0         </td> <td>4223.14      </td> <td>5208.51       </td> <td>9431.65       </td> <td>38625             </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>MTA            </td> <td>Municipal Transportation Agency       </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021                  </td> <td>8200           </td> <td>Protection & Apprehension    </td> <td>8201    </td> <td>School Crossing Guard         </td> <td>45810              </td> <td>7948.75 </td> <td>0       </td> <td>0             </td> <td>7948.75     </td> <td>0         </td> <td>2873.17      </td> <td>616.24        </td> <td>3489.41       </td> <td>11438.2           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection                       </td> <td>POL            </td> <td>Police                                </td> <td>911       </td> <td>Police Officers' Association                      </td> <td>Q000           </td> <td>Police Services              </td> <td>Q002    </td> <td>Police Officer                </td> <td>32906              </td> <td>2235    </td> <td>0       </td> <td>0             </td> <td>2235        </td> <td>490.36    </td> <td>286.72       </td> <td>176.57        </td> <td>953.65        </td> <td>3188.65           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                         </td> <td>791       </td> <td>SEIU - Staff and Per Diem Nurses, Local 1021      </td> <td>2300           </td> <td>Nursing                      </td> <td>2328    </td> <td>Nurse Practitioner            </td> <td>7506               </td> <td>187247  </td> <td>0       </td> <td>11704.1       </td> <td>198951      </td> <td>37683.7   </td> <td>12424.5      </td> <td>11221.7       </td> <td>61329.9       </td> <td>260281            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce </td> <td>MTA            </td> <td>Municipal Transportation Agency       </td> <td>253       </td> <td>Transport Workers - Transit Operators, Local 250-A</td> <td>9100           </td> <td>Street Transit               </td> <td>9163    </td> <td>Transit Operator              </td> <td>36773              </td> <td>66988.5 </td> <td>3512.88 </td> <td>2770.39       </td> <td>73271.8     </td> <td>19127.2   </td> <td>13203        </td> <td>5455.1        </td> <td>37785.3       </td> <td>111057            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance        </td> <td>CAT            </td> <td>City Attorney                         </td> <td>311       </td> <td>Municipal Attorneys' Association                  </td> <td>8100           </td> <td>Legal & Court                </td> <td>8177    </td> <td>Attorney (Civil/Criminal)     </td> <td>12963              </td> <td>135190  </td> <td>0       </td> <td>1562.5        </td> <td>136752      </td> <td>27501.8   </td> <td>12424.5      </td> <td>10103         </td> <td>50029.3       </td> <td>186781            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>3                      </td> <td>Human Welfare & Neighborhood Development</td> <td>DSS            </td> <td>Human Services                        </td> <td>535       </td> <td>SEIU - Human Services, Local 1021                 </td> <td>9700           </td> <td>Community Development        </td> <td>9703    </td> <td>Emp & Training Spec 2         </td> <td>35179              </td> <td>70474.8 </td> <td>147.28  </td> <td>1647.24       </td> <td>72269.3     </td> <td>14650.3   </td> <td>10696.9      </td> <td>5993.11       </td> <td>31340.3       </td> <td>103610            </td>
        </tr>
    </tbody>
</table>
<p>... (42979 rows omitted)</p>




```python
# Who is making the most money
sf.sort('Total Compensation', descending=True).show(5)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance       </td> <td>RET            </td> <td>Retirement System                   </td> <td>351       </td> <td>Municipal Executive Association - Miscellaneous</td> <td>1100           </td> <td>Administrative & Mgmt (Unrep)</td> <td>1119    </td> <td>Chief Investment Officer</td> <td>46881              </td> <td>507832  </td> <td>0       </td> <td>0             </td> <td>507832      </td> <td>105053    </td> <td>12424.5      </td> <td>23566.2       </td> <td>141044        </td> <td>648875            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance       </td> <td>ADM            </td> <td>General Services Agency - City Admin</td> <td>164       </td> <td>Physicians and Dentists - Miscellaneous        </td> <td>2500           </td> <td>Med Therapy & Auxiliary      </td> <td>2598    </td> <td>Asst Med Examiner       </td> <td>1016               </td> <td>279311  </td> <td>3829.36 </td> <td>114434        </td> <td>397574      </td> <td>56211.6   </td> <td>12424.5      </td> <td>14299.1       </td> <td>82935.2       </td> <td>480509            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance       </td> <td>ADM            </td> <td>General Services Agency - City Admin</td> <td>164       </td> <td>Physicians and Dentists - Miscellaneous        </td> <td>2500           </td> <td>Med Therapy & Auxiliary      </td> <td>2598    </td> <td>Asst Med Examiner       </td> <td>13746              </td> <td>279311  </td> <td>9046.92 </td> <td>56742.6       </td> <td>345101      </td> <td>56211.6   </td> <td>12424.5      </td> <td>13482.7       </td> <td>82118.8       </td> <td>427219            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>2                      </td> <td>Public Works, Transportation & Commerce</td> <td>AIR            </td> <td>Airport Commission                  </td> <td>351       </td> <td>Municipal Executive Association - Miscellaneous</td> <td>0900           </td> <td>Management                   </td> <td>0965    </td> <td>Dept Head V             </td> <td>17356              </td> <td>326764  </td> <td>0       </td> <td>0             </td> <td>326764      </td> <td>65806.3   </td> <td>12424.5      </td> <td>21691.2       </td> <td>99922.1       </td> <td>426686            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                       </td> <td>DPH            </td> <td>Public Health                       </td> <td>351       </td> <td>Municipal Executive Association - Miscellaneous</td> <td>0900           </td> <td>Management                   </td> <td>1164    </td> <td>Adm, SFGH Medical Center</td> <td>1523               </td> <td>256098  </td> <td>0       </td> <td>82292.3       </td> <td>338390      </td> <td>51977.5   </td> <td>11468.8      </td> <td>20963.3       </td> <td>84409.6       </td> <td>422800            </td>
        </tr>
    </tbody>
</table>
<p>... (42984 rows omitted)</p>



```python
# Who is making the least money
sf.sort('Total Compensation', descending=False).show(5)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection               </td> <td>FIR            </td> <td>Fire Department   </td> <td>798       </td> <td>Firefighters - Miscellaneous, Local 798        </td> <td>H000           </td> <td>Fire Services           </td> <td>H002    </td> <td>Firefighter               </td> <td>43833              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-423.76       </td> <td>-423.76       </td> <td>-423.76           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                </td> <td>DPH            </td> <td>Public Health     </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021               </td> <td>9900           </td> <td>Public Service Aide     </td> <td>9924    </td> <td>PS Aide Health Services   </td> <td>27871              </td> <td>-292.4  </td> <td>0       </td> <td>0             </td> <td>-292.4      </td> <td>0         </td> <td>-95.58       </td> <td>-22.63        </td> <td>-118.21       </td> <td>-410.61           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>1                      </td> <td>Public Protection               </td> <td>JUV            </td> <td>Juvenile Probation</td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021               </td> <td>8300           </td> <td>Correction & Detention  </td> <td>8320    </td> <td>Counselor, Juvenile Hall  </td> <td>10517              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-159.12       </td> <td>-159.12       </td> <td>-159.12           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance</td> <td>CPC            </td> <td>City Planning     </td> <td>21        </td> <td>Prof & Tech Engineers - Miscellaneous, Local 21</td> <td>1000           </td> <td>Information Systems     </td> <td>1053    </td> <td>IS Business Analyst-Senior</td> <td>18961              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-26.53        </td> <td>-26.53        </td> <td>-26.53            </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>6                      </td> <td>General Administration & Finance</td> <td>CPC            </td> <td>City Planning     </td> <td>21        </td> <td>Prof & Tech Engineers - Miscellaneous, Local 21</td> <td>5200           </td> <td>Professional Engineering</td> <td>5277    </td> <td>Planner 1                 </td> <td>19387              </td> <td>0       </td> <td>0       </td> <td>0             </td> <td>0           </td> <td>0         </td> <td>0            </td> <td>-9.51         </td> <td>-9.51         </td> <td>-9.51             </td>
        </tr>
    </tbody>
</table>
<p>... (42984 rows omitted)</p>



```python
# data cleaning
min_salary = 10 * 20 * 52
sf = sf.where('Total Compensation', are.above(min_salary))
```


```python
pop_median = percentile(50, sf.column('Total Compensation'))
pop_median
```




    107516.69




```python
our_sample = sf.sample(300, with_replacement=False)
our_sample.show(5)
```


<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Year Type</th> <th>Year</th> <th>Organization Group Code</th> <th>Organization Group</th> <th>Department Code</th> <th>Department</th> <th>Union Code</th> <th>Union</th> <th>Job Family Code</th> <th>Job Family</th> <th>Job Code</th> <th>Job</th> <th>Employee Identifier</th> <th>Salaries</th> <th>Overtime</th> <th>Other Salaries</th> <th>Total Salary</th> <th>Retirement</th> <th>Health/Dental</th> <th>Other Benefits</th> <th>Total Benefits</th> <th>Total Compensation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>3                      </td> <td>Human Welfare & Neighborhood Development</td> <td>DSS            </td> <td>Human Services                </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021            </td> <td>1400           </td> <td>Clerical, Secretarial & Steno</td> <td>1404    </td> <td>Clerk                    </td> <td>5553               </td> <td>22453.1 </td> <td>268.05  </td> <td>480           </td> <td>23201.2     </td> <td>5212.92   </td> <td>5787.91      </td> <td>1893.46       </td> <td>12894.3       </td> <td>36095.5           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                 </td> <td>791       </td> <td>SEIU - Staff and Per Diem Nurses, Local 1021</td> <td>2300           </td> <td>Nursing                      </td> <td>P103    </td> <td>Special Nurse            </td> <td>1756               </td> <td>26376.8 </td> <td>2642.04 </td> <td>6007.43       </td> <td>35026.2     </td> <td>2157.21   </td> <td>2028.66      </td> <td>3437.78       </td> <td>7623.65       </td> <td>42649.9           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>5                      </td> <td>Culture & Recreation                    </td> <td>REC            </td> <td>Recreation and Park Commission</td> <td>261       </td> <td>Laborers, Local 261                         </td> <td>3400           </td> <td>Agriculture & Horticulture   </td> <td>3417    </td> <td>Gardener                 </td> <td>44004              </td> <td>66102   </td> <td>0       </td> <td>75.6          </td> <td>66177.6     </td> <td>13638.1   </td> <td>12424.5      </td> <td>5458.82       </td> <td>31521.4       </td> <td>97699             </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>4                      </td> <td>Community Health                        </td> <td>DPH            </td> <td>Public Health                 </td> <td>790       </td> <td>SEIU - Miscellaneous, Local 1021            </td> <td>2500           </td> <td>Med Therapy & Auxiliary      </td> <td>2585    </td> <td>Health Worker 1          </td> <td>48832              </td> <td>48653.7 </td> <td>0       </td> <td>0             </td> <td>48653.7     </td> <td>11668.3   </td> <td>12119.9      </td> <td>3956.77       </td> <td>27744.9       </td> <td>76398.6           </td>
        </tr>
        <tr>
            <td>Calendar </td> <td>2015</td> <td>3                      </td> <td>Human Welfare & Neighborhood Development</td> <td>DSS            </td> <td>Human Services                </td> <td>535       </td> <td>SEIU - Human Services, Local 1021           </td> <td>2900           </td> <td>Human Services               </td> <td>2905    </td> <td>Senior Eligibility Worker</td> <td>12282              </td> <td>77071.1 </td> <td>0       </td> <td>624           </td> <td>77695.1     </td> <td>16013.4   </td> <td>12424.5      </td> <td>5991.27       </td> <td>34429.2       </td> <td>112124            </td>
        </tr>
    </tbody>
</table>
<p>... (295 rows omitted)</p>



```python
sf_bins = np.arange(0, 700000, 25000)
```

# Bootstrap


```python
def generate_sample_median(samp_size):
    our_sample = sf.sample(samp_size, with_replacement=False)
    return percentile(50, our_sample.column('Total Compensation'))

sample_median = generate_sample_median(300)
sample_median
```




    106234.64




```python
# Take a bootstrap (re)sample of size 300, WITH replacement
boot_sample = our_sample.sample(300, with_replacement=True)
boot_sample.hist('Total Compensation', bins=sf_bins)
plots.title('Bootstrap sample');

print("Population Median =       ", pop_median)
print("Our Sample Median =       ", sample_median)
print("Bootstrap Sample Median = ", 
      percentile(50,boot_sample.column('Total Compensation')))
```

    Population Median =        107516.69
    Our Sample Median =        106234.64
    Bootstrap Sample Median =  117890.06



    
![png](Lec9-demo_files/Lec9-demo_20_1.png)
    



```python
def one_bootstrap_median():
    boot_resample = our_sample.sample()
    return percentile(50, boot_resample.column('Total Compensation'))
```


```python
bootstrap_medians = make_array()
for i in np.arange(1000):
    new_median = one_bootstrap_median()
    bootstrap_medians = np.append(bootstrap_medians, new_median)
```


```python
med_bins = np.arange(90000, 125001, 2500)
Table().with_column(
    'Bootstrap Medians', bootstrap_medians
).hist('Bootstrap Medians', bins=med_bins)

plots.scatter(pop_median, -1e-6, color="red");
plots.scatter(sample_median, -1e-6, color="blue");
```


    
![png](Lec9-demo_files/Lec9-demo_23_0.png)
    


## Confidence Intervals

The confidence interval is an interval based on the middle 95% of bootstrap samples.  The interval will be shown in yellow, the sample median (our estimate) in blue, and the true population median (the parameter) in red.


```python
left = percentile(2.5, bootstrap_medians)
right = percentile(97.5, bootstrap_medians)

Table().with_column(
    'Bootstrap Medians', bootstrap_medians
).hist('Bootstrap Medians', bins=med_bins)

plots.plot([left, right], [-1e-6,-1e-6], color="gold",lw=3, zorder=1);
plots.scatter(pop_median, -1e-6, color="red", zorder=2);
plots.scatter(sample_median, -1e-6, color="blue", zorder=2);
```


    
![png](Lec9-demo_files/Lec9-demo_26_0.png)
    


## Draw a fresh sample from population, then draw bootstrap samples and calculate a new Confidence Interval


```python
our_sample = sf.sample(300, with_replacement=False)
bootstrap_medians = make_array()
for i in np.arange(1000):
    new_median = one_bootstrap_median()
    bootstrap_medians = np.append(bootstrap_medians, new_median)
```


```python
left = percentile(2.5, bootstrap_medians)
right = percentile(97.5, bootstrap_medians)

Table().with_column(
    'Bootstrap Medians', bootstrap_medians
).hist('Bootstrap Medians', bins=med_bins)

plots.plot([left, right], [-1e-6,-1e-6], color="gold",lw=3, zorder=1);
plots.scatter(pop_median, -1e-6, color="red", zorder=2);
plots.scatter(sample_median, -1e-6, color="blue", zorder=2);
```


    
![png](Lec9-demo_files/Lec9-demo_29_0.png)
    


## Average (Mean) ##


```python
values = make_array(2, 3, 3, 9)
```


```python
sum(values)/len(values)
```




    4.25




```python
np.average(values)
```




    4.25




```python
np.mean(values)
```




    4.25




```python
values_table = Table().with_columns('value', values)
values_table
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2    </td>
        </tr>
        <tr>
            <td>3    </td>
        </tr>
        <tr>
            <td>3    </td>
        </tr>
        <tr>
            <td>9    </td>
        </tr>
    </tbody>
</table>



## Standard Deviation ##


```python
sd_table = Table().with_columns('Value', values)
sd_table
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2    </td>
        </tr>
        <tr>
            <td>3    </td>
        </tr>
        <tr>
            <td>3    </td>
        </tr>
        <tr>
            <td>9    </td>
        </tr>
    </tbody>
</table>




```python
average_value = np.average(sd_table.column(0))
average_value
```




    4.25




```python
deviations = values - average_value
sd_table = sd_table.with_column('Deviation', deviations)
sd_table
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Deviation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2    </td> <td>-2.25    </td>
        </tr>
        <tr>
            <td>3    </td> <td>-1.25    </td>
        </tr>
        <tr>
            <td>3    </td> <td>-1.25    </td>
        </tr>
        <tr>
            <td>9    </td> <td>4.75     </td>
        </tr>
    </tbody>
</table>




```python
sum(deviations)
```




    0.0




```python
sd_table = sd_table.with_columns('Squared Deviation', deviations ** 2)
sd_table
```




<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Deviation</th> <th>Squared Deviation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2    </td> <td>-2.25    </td> <td>5.0625           </td>
        </tr>
        <tr>
            <td>3    </td> <td>-1.25    </td> <td>1.5625           </td>
        </tr>
        <tr>
            <td>3    </td> <td>-1.25    </td> <td>1.5625           </td>
        </tr>
        <tr>
            <td>9    </td> <td>4.75     </td> <td>22.5625          </td>
        </tr>
    </tbody>
</table>




```python
# Variance of the data

variance = np.mean(sd_table.column('Squared Deviation'))
variance
```




    7.6875




```python
# Standard Deviation (SD) is the square root of the variance

sd = variance ** 0.5
sd
```




    2.7726341266023544




```python
np.std(values)
```




    2.7726341266023544




```python
np.median(values)
```




    3.0


