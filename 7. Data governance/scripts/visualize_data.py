# scripts/visualize_data.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output directory exists
os.makedirs("data/plots", exist_ok=True)

# Load processed train dataset
df = pd.read_csv("data/processed/train.csv")

# 1. Histogram for Alcohol
plt.figure(figsize=(8, 5))
plt.hist(df['alcohol'], bins=20, color='skyblue', edgecolor='black')
plt.title('Alcohol Distribution')
plt.xlabel('Alcohol')
plt.ylabel('Frequency')
plt.savefig("data/plots/alcohol_distribution.png")
plt.close()

# 2. Boxplot for All Numeric Features
plt.figure(figsize=(12, 6))
sns.boxplot(data=df.select_dtypes(include='number'))
plt.xticks(rotation=45)
plt.title('Boxplot of Numeric Features')
plt.tight_layout()
plt.savefig("data/plots/numeric_features_boxplot.png")
plt.close()

# 3. Correlation Heatmap
plt.figure(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("data/plots/correlation_heatmap.png")
plt.close()

# 4. Scatter Plot: Alcohol vs. Quality
plt.figure(figsize=(8, 5))
sns.scatterplot(x='alcohol', y='quality', data=df)
plt.title('Alcohol vs. Quality')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.savefig("data/plots/alcohol_vs_quality.png")
plt.close()
