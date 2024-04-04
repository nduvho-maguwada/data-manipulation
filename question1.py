import pandas as pd

data = {"ID": [1, 2, 3, 4, 5],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [20, 21, 19, 22, 20],
        "Math_Score": [85, 95, 70, 98, 88],
        "Science_Score": [92, 88, 94, 96, 91],
        "English_Score": [78, 85, 0, 88, 90],
        "History_Score": [80, 90, 75, 92, 85]
}

df = pd.DataFrame(data)

print(df.head())

print("null values", df.isnull().sum())

print("\naverage for math", df["Math_Score"].mean())
print("\naverage fo science", df["Science_Score"].mean())
print("\naverage for English is ", df["English_Score"].mean())
print("\naverage for History is ", df["History_Score"].mean())

df.replace(0, df["Math_Score"].mean(), inplace=False)
df.replace(0, df["Science_Score"].mean(), inplace=False)
df.replace(0, df["English_Score"].mean(), inplace=True)
df.replace(0, df["History_Score"].mean(), inplace=False)

print(df)

threshold = 70
print("\noutliers for math are: \n", df[df["Math_Score"] <= threshold])


print("_________________________")

'''Filter the dataset only to include students who scored above 90 in Mathematics and Science and
sort them in descending order of their total scores (sum of Mathematics and Science scores). Display
the first five rows of the filtered dataset.'''


math_filtered = df[df["Math_Score"] >= 90]
print("Students who got above 90 in math: \n", math_filtered)


sortedMath = df["Math_Score"].sort_values(ascending = False)

print("........\n",sortedMath)

#Group the dataset by 'Age' and calculate the median score for each subject.
df.groupby("Age")
print(df)

sortedScience = df["Science_Score"].sort_values()
sortedEnglish = df["English_Score"].sort_values()
sortedHistory = df["History_Score"].sort_values()

print("\nmedian for math is: ", sortedMath.median())
print("\nmedian for science is: ", sortedScience.median())
print("\nmedian for english is: ", sortedEnglish.median())
print("\nmedian for history is: ", sortedHistory.median())
