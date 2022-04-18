# UWFinTech_Group4_Project1

## Project Title
Real Estate Stock Analysis - 1 year 4 months

In this project we will use Polygon API keys to get the historical price data and perform quantitative analysis. Code and analysis of different graphs and visualization helps in determining which of the real estate stocks have the most investment potential based on key risk-management metrics: the daily returns, cummulative Returns, standard deviations, Sharpe ratios.

Application is developed through CLI which gives information about the daily returns, cumulative return percentage, Betas, Standard Deviation and Sharpe ratios.
The program also uses Voilà library to deploy the notebook as a web application. 


## Technologies

Web Application for a Stock Analyzer project leverages python 3.7 with the following packages:

  [Pandas](https://github.com/pandas-dev/pandas "Pandas") 
  
  [Polygon API](https://polygon.io/docs/stocks/)

   [Voila](https://github.com/voila-dashboards/voila)


## Libraries and Dependencies

```
import os
import sys
import datetime
import requests
import json
import numpy as np
import pandas as pd
import panel as pn
from panel.interact import interact
from panel import widgets
from dotenv import load_dotenv
import hvplot.pandas
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')

from MCForecastTools import MCSimulation
```

[MCForecastTools](https://cdn.inst-fs-pdx-prod.inscloudgate.net/e0e08ad7-c5b3-43c1-8e7c-e7efc5f1f39c/MCForecastTools.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9lMGUwOGFkNy1jNWIzLTQzYzEtOGU3Yy1lN2VmYzVmMWYzOWMvTUNGb3JlY2FzdFRvb2xzLnB5IiwidGVuYW50IjoiY2FudmFzIiwidXNlcl9pZCI6IjE1MDQyMDAwMDAwMDAxNjY3OSIsImlhdCI6MTY0NzgwNTcwMiwiZXhwIjoxNjQ3ODkyMTAyfQ.AFw4Zrh-g9L-bjcvOiNwTlG8AXpxX7mml1s1WvuToE2tPxnQ1OWTfyfYG0LnT8vXcSD469j1DdN2BRCQ5ACDUA&content_type=text%2Fx-python)


# Stock List and S&P 500
 AMT, CBRE, ESS, AVB, SPY

## Project Description
Build a program which analyzes the stocks of several big real estate companieS AGAINST s & p 500 FUND "SPY"

1.) API to pull stock information into DF - Polygon.io

2.) Data cleaning/slicing

3.) Performance Analysis

* Determine the fund with the most investment potential based on key risk-management metrics:
* Daily returns 

![Daily Returns](Images/DailyReturns.png)

![BoxChart](Images/Boxplot.png)


* Cumulative Returns
```
cumulative_returns = (1 + all_stocks_df).cumprod()
```


![Cumulative Returns](Images/Cumprod.png)


* Standard deviations
```
standard_deviation = all_stocks_df.std().sort_values()
```
* Annualized Standard Deviation
```
annualized_standard_deviation = standard_deviation * np.sqrt(252)
annualized_standard_deviation.sort_values()
```

* Sharpe ratios
![Sharpe Ratio](Images/Sharpe.png)
* Betas



* Monte Carlo Sim

![MC](Images/MC.png)

4.) Interactive Dashboard

![Betas](Images/Dashboard.png)

5.) CLI Application



## Research Questions to Answer
* Historical performance
* Top 3 portfolio picks (e.g. volatility, covariance with SNP, etc.)
* Investment opportunities



## Resources :
Code from Binoy Das (slack post)

---

## Contributors

* Maureen Kaaria

Email: maureenkaaria@gmail.com
* Khaing Thwe

Email: khaingzt88@gmail.com
* Olga Koryachek

Email: olgakoryachek@live.com

[LinkedIn](https://www.linkedin.com/in/olga-koryachek-a74b1877/?msgOverlay=true "LinkedIn")
* Arthur Lovett

Email: arthur@arthurlovett.com


---

## License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/)

