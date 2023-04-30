import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

covid_data_csv = pd.read_csv("owid-covid-data.csv")
covid_data_xcel = pd.read_excel("owid-covid-data.xlsx")

Afghanistan = covid_data_csv.iloc[200:500, [1,2,4]]

#Understanding the dataset
covid_data_csv.shape
covid_data_csv.head()
covid_data_csv.describe()

#Listing unique continets in the dataset
continents = list(covid_data_csv.continent.unique())

#Grouping by specific columns
new_df = covid_data_csv.groupby(['date', 'continent'])[['date', 'continent','population_density','total_cases','total_deaths','total_vaccinations']].sum().reset_index()

#checking if the new df has any missing values
new_df.isna().sum()

#Graphical display of the data. Let's create a plot with the total deaths > 1million

df1 = new_df[new_df['total_deaths'] > 1000000]
#countries = df1['location'].unique()
#len(countries)

#Graphical illustration of total deaths per continent
plt.bar(new_df['continent'], new_df['total_deaths'])
plt.title("Total deaths per continent")
plt.xlabel("Continent")
plt.ylabel("Number of total deaths")
plt.show()

len(continents)


#Showing the trend of total cases, total deaths and total vaccinations per continent
plt.subplot(2,2,1)
plt.scatter(new_df['continent'], new_df['total_cases'], label = "Total Cases") 
plt.title("Total Cases")
plt.xlabel("Continent")
plt.ylabel("Total number of cases")


plt.subplot(2,2,2)
plt.scatter(new_df['continent'], new_df['total_deaths'], label = "Total Deaths")
plt.title("Total Deaths")
plt.xlabel("Continent")
plt.ylabel("Total number of deaths")

plt.subplot(2,2,3)
plt.scatter(new_df['continent'], new_df['total_vaccinations'], label = "Total Vaccinations")
plt.title("Total Vaccinations")
plt.xlabel("Continent")
plt.ylabel("Total number of Vaccinations")

plt.tight_layout() #makes the padding fit better

plt.show()

''' 
plt.scatter(new_df['continent'], new_df['total_cases'], label = "Total Cases")
plt.scatter(new_df['continent'], new_df['total_deaths'], label = "Total Deaths")
plt.scatter(new_df['continent'], new_df['total_vaccinations'], label = "Total Vaccinations") 
plt.title("Trends per continent")
plt.xlabel("Continent")
plt.ylabel("Total numbers")

plt.legend()
plt.show() 
'''