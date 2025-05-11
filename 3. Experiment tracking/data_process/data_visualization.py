import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
import os

# Set environment variable to silence specific warnings
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

# Ensure the existence of the directory for plots
plots_dir = "plots"
os.makedirs(plots_dir, exist_ok=True)

# Load the datasets
data_dir = "data"
X_train = pd.read_csv(f"{data_dir}/X_train.csv")
X_test = pd.read_csv(f"{data_dir}/X_test.csv")
y_train = pd.read_csv(f"{data_dir}/y_train.csv")
y_test = pd.read_csv(f"{data_dir}/y_test.csv")

# Combine the training features and target for easier plotting
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# Setting up the visualization environment
sns.set(style="whitegrid")

# Initialize MLflow
mlflow.set_experiment("Data Visualization")
with mlflow.start_run(run_name="Data PLots"):
    # Histograms for each feature in the training data
    train_data.hist(bins=15, figsize=(15, 10), layout=(3, 4))
    plt.suptitle("Histograms of Features and Target in Training Data")
    histogram_path = f"{plots_dir}/histograms.png"
    plt.savefig(histogram_path)
    mlflow.log_artifact(histogram_path)
    plt.show()

    # Box plots for each feature to identify outliers
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=X_train, orient="h", palette="Set2")
    plt.title("Box Plot of Features in Training Data")
    box_plot_path = f"{plots_dir}/box_plot.png"
    plt.savefig(box_plot_path)
    mlflow.log_artifact(box_plot_path)
    plt.show()

    # Scatter plot for features vs. target
    g = sns.PairGrid(
        train_data, y_vars=["Progression"], x_vars=X_train.columns, height=3, aspect=1.5
    )
    g.map(sns.scatterplot)
    g.add_legend()
    plt.suptitle("Scatter Plots of Features vs. Target in Training Data")
    scatter_path = f"{plots_dir}/scatter_plots.png"
    plt.savefig(scatter_path)
    mlflow.log_artifact(scatter_path)
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    correlation_matrix = train_data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap of Training Data")
    correlation_path = f"{plots_dir}/correlation_heatmap.png"
    plt.savefig(correlation_path)
    mlflow.log_artifact(correlation_path)
    plt.show()