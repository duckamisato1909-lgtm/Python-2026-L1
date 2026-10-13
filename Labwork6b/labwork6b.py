import pandas as pd
import matplotlib.pyplot as plt

scores_df = pd.read_csv('scores.csv')

plt.figure(figsize=(9, 6))
plt.scatter(scores_df.index, scores_df['python'], label='Python', color='blue', alpha=0.7)
plt.scatter(scores_df.index, scores_df['math'], label='Math', color='green', alpha=0.7)
plt.scatter(scores_df.index, scores_df['database'], label='Database', color='red', alpha=0.7)
plt.title("Student Scores Scatter Plot")
plt.xlabel("Student Index")
plt.ylabel("Scores")
plt.legend()
plt.grid(True)
plt.savefig('scattered.png')
plt.close()

fig, axes = plt.subplots(3, 1, figsize=(6, 12))

axes[0].hist(scores_df['python'].dropna(), bins=10, color='blue', edgecolor='black')
axes[0].set_title('Python Marks Histogram')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Frequency')

axes[1].hist(scores_df['math'].dropna(), bins=10, color='green', edgecolor='black')
axes[1].set_title('Math Marks Histogram')
axes[1].set_xlabel('Score')
axes[1].set_ylabel('Frequency')

axes[2].hist(scores_df['database'].dropna(), bins=10, color='red', edgecolor='black')
axes[2].set_title('Database Marks Histogram')
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('histo.png')
plt.close()

plt.figure(figsize=(8, 6))
plt.boxplot([scores_df['python'].dropna(), scores_df['math'].dropna(), scores_df['database'].dropna()])
plt.xticks([1, 2, 3], ['Python', 'Math', 'Database']) 
plt.title("Box Plot of Student Scores")
plt.ylabel("Scores")
plt.grid(True)
plt.savefig('box.png')
plt.close()

print("All Lab 6b plots (scattered.png, histo.png, box.png) generated successfully!")