import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("students.csv")

# Display data
print("Student Data:")
print(data)

# First five records
print("\nFirst 5 Records:")
print(data.head())

# Dataset information
print("\nDataset Information:")
print(data.info())

# Missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Students with marks greater than 80
print("\nStudents with Marks > 80:")
print(data[data["Marks"] > 80])

# Visualization
data["Marks"].plot(kind="bar")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()