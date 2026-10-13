import pandas as pd

print("==================================================")
print(" PART 1: DATA MANIPULATION WITH STUDENTS.CSV")
print("==================================================")

# 1. Load the dataset
students_df = pd.read_csv('students.csv')

# 2. Display first five rows
print("\n[1] First five rows of students.csv:")
print(students_df.head())

# 3. Find number of rows and columns
print("\n[2] Number of rows and columns (Shape):")
print(students_df.shape)

# 4. Select name and GPA
print("\n[3] Selected Name and GPA columns:")
print(students_df[['name', 'GPA']])

# 5. Find students with GPA >= 3.5
print("\n[4] Students with GPA >= 3.5:")
print(students_df[students_df['GPA'] >= 3.5])

# 6. Sort students by GPA (Descending)
print("\n[5] Students sorted by GPA (Descending):")
print(students_df.sort_values(by='GPA', ascending=False))

# 7. Find average GPA by major
print("\n[6] Average GPA by Major:")
print(students_df.groupby('major')['GPA'].mean())


print("\n==================================================")
print(" PART 2: FROM RAW DATA TO USEFUL INFO")
print("==================================================")

# 1. Load both files
students = pd.read_csv('students.csv')
scores = pd.read_csv('scores.csv')

# 2. Check missing values
print("\n[7] Checking missing values:")
print("--- Students missing values ---")
print(students.isnull().sum())
print("--- Scores missing values ---")
print(scores.isnull().sum())

# 3. Fill or remove missing data appropriately
students = students.dropna()
scores = scores.fillna(0)

# 4. Merge the two datasets on 'student_id'
merged_df = pd.merge(students, scores, on='student_id')
print("\n[8] Merged dataset shape:", merged_df.shape)

# 5. Calculate each student's average score
score_columns = [col for col in scores.columns if col != 'student_id']
merged_df['average_score'] = merged_df[score_columns].mean(axis=1)

print("\n[9] Dataset preview with calculated average score:")
print(merged_df[['student_id', 'name', 'average_score']].head())

# 6. Find the top 5 students
top_5_students = merged_df.nlargest(5, 'average_score')
print("\n[10] Top 5 students with the highest average score:")
print(top_5_students[['student_id', 'name', 'major', 'average_score']])

# 7. Compute average score by major
avg_score_by_major = merged_df.groupby('major')['average_score'].mean()
print("\n[11] Average score by major:")
print(avg_score_by_major)