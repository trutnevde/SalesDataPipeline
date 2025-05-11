import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_by_category():
    df = pd.read_csv(CLEANED_DATA_PATH)

    plt.figure(figsize=(10, 6))
    sns.barplot(x="category", y="total_sales", data=df.groupby("category").sum().reset_index())
    plt.xticks(rotation=45)
    plt.title("Total Sales by Category")
    plt.tight_layout()
    plt.savefig("reports/sales_by_category.png")
    plt.close()