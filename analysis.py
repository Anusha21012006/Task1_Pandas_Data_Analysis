import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV File
data = pd.read_csv("students.csv")

# Display Dataset
print("===== STUDENT DATASET =====")
print(data)

# Basic Analysis
average_marks = data["Marks"].mean()
maximum_marks = data["Marks"].max()
minimum_marks = data["Marks"].min()
total_students = len(data)

print("\n===== BASIC ANALYSIS =====")
print("Total Students:", total_students)
print("Average Marks:", round(average_marks, 2))
print("Maximum Marks:", maximum_marks)
print("Minimum Marks:", minimum_marks)

# -----------------------
# Bar Chart
# -----------------------
plt.figure(figsize=(8, 5))
plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# -----------------------
# Scatter Plot
# -----------------------
plt.figure(figsize=(8, 5))
plt.scatter(data["Age"], data["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# -----------------------
# Heatmap
# -----------------------
plt.figure(figsize=(6, 4))
sns.heatmap(
    data[["Age", "Marks"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()

print("\nGraphs saved successfully!")
print("1. bar_chart.png")
print("2. scatter_plot.png")
print("3. heatmap.png")