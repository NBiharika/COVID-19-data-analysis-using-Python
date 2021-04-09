##  COVID19 Data Analysis

# import libraries
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

print('Modules are imported.')

# importing covid19 dataset

corona_dataset_csv = pd.read_csv('Dataset/covid19_Confirmed_dataset.csv')
corona_dataset_csv.head(10)

# check the shape of the dataframe
corona_dataset_csv.shape

# Delete the useless columns
corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)
corona_dataset_csv.head(10)

# Aggregating the rows by the country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head(10)
corona_dataset_aggregated.shape

# Visualizing data related to a country 
corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['India'].plot()
corona_dataset_aggregated.loc['Japan'].plot()
plt.legend()

# Calculating a good measure
corona_dataset_aggregated.loc['China'].plot()

# Caculating the first derivative of the curve
corona_dataset_aggregated.loc['China'].diff().plot()

# Find maxmimum infection rate 
corona_dataset_aggregated.loc['China'].diff().max()
corona_dataset_aggregated.loc['India'].diff().max()
corona_dataset_aggregated.loc['Japan'].diff().max()

# Find maximum infection rate for all of the countries
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates
corona_dataset_aggregated.head()

# create a new dataframe with only needed column
corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])
corona_data.head()

## Importing the WorldHappinessReport.csv dataset
world_happiness_report = pd.read_csv("Dataset/worldwide_happiness_report.csv")
world_happiness_report.head()
world_happiness_report.shape

# drop the useless columns
columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)
world_happiness_report.head()

# changing the indices of the dataframe
world_happiness_report.set_index(['Country or region'],inplace=True)
world_happiness_report.head()

#join two dataset we have prepared
data = world_happiness_report.join(corona_data).copy()
data.head()

# correlation matrix
data.corr() # it is representing the currelation between every two columns of our dataset

# Visualization of the results
data.head()

# Plotting GDP vs maximum Infection rate
x = data['GDP per capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

# Plotting Social support vs maximum Infection rate
x = data['Social support']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

# Plotting Healthy life expectancy vs maximum Infection rate
x = data['Healthy life expectancy']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

# Plotting Freedom to make life choices vs maximum Infection rate
x = data['Freedom to make life choices']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))






