import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def count_plot(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(10, 8))
    sns.countplot(data=df, x=column)
    plt.xlabel(f'{column}', fontsize=17)
    plt.ylabel("Count", fontsize=17)
    plt.title(f'\nDistribution of {column}\n', size=20, fontweight='bold')
    plt.savefig('../charts/count_plot.jpg')
    plt.show()