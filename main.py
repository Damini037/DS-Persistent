import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('movies.csv')

print(df.info())
print(df.isnull().sum())

# checking for some statistics
df.describe()

# checking for dulicated values and drop them

ddf = df.duplicated().sum()
print("duplicated values: ", ddf)
df.drop_duplicates(inplace=True)

# Now we have to convert date in date format
df['release_date'] = pd.to_datetime(df['release_date'])

# plot no -1 histgram
plt.figure(figsize=(8,6))
sns.histplot(df['vote_average'], bins=20, kde=True)
plt.title('Distribution of Average Voting')
plt.show()

plt.figure(figsize=(8,6))
sns.histplot(df['popularity'], bins=10, kde=True)
plt.title('Distribution of Movie Popularity')
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df[['popularity', 'vote_average']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between Popularity and Voting')
plt.show()

# Top ten Movies

top_10_movies = df.nlargest(10, 'popularity')

plt.figure(figsize=(10,8))
sns.barplot(x='popularity', y='title', data=top_10_movies)
plt.title('Top 10 Movies by Popularity')
plt.show()