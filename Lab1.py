import pandas as pd

# Load the CSV file
df = pd.read_csv('path/to/your/university_rankings.csv')

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Calculate the mean of each numerical column
means = df.mean(numeric_only=True)

# Print the means
print("Mean values of each column:")
print(means)
