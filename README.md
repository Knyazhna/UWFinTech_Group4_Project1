# UWFinTech_Group4_Project1

## Project Title
Real Estate Stock Analysis - 1 year 4 months


## Technologies

Web Application for a Stock Analyzer project leverages python 3.7 with the following packages:

  [Pandas](https://github.com/pandas-dev/pandas "Pandas") 
  
  [Polygon API](https://polygon.io/docs/stocks/)

   [Voila](https://github.com/voila-dashboards/voila)

# Stock List and S&P 500
 AMT, CBRE, ESS, AVB, SPY

## Project Description
Build a program which analyzes the stocks of several big real estate companieS AGAINST s & p 500 FUND "SPY"

The analysis:
* Determine the fund with the most investment potential based on key risk-management metrics:
* the daily returns, 
* standard deviations
* Sharpe ratios
* betas
* Monte Carlo Sim
* Other helpful interactive visualizations

The program will be accessed via a CLI Web Application AND we will use the Voilà library to deploy the notebook as a web application. 


## Outline
1.) API to pull stock information into DF - Polygon.io
2.) Data cleaning/slicing
3.) Analysis
* Determine the fund with the most investment potential based on key risk-management metrics:
* Daily returns 

![Daily Returns](Images/DailyReturns.png)

![BoxChart](Images/Boxplot.png)

* Standard deviations
* Cumulative Returns

![Cumulative Returns](Images/Cumprod.png)

* Sharpe ratios
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

