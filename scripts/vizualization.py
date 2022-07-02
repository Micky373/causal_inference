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

def plot_ditribution(df,columns):
    for col in columns:
        sns.displot(df, x=col, hue="diagnosis",kind='kde',multiple='stack',palette=["red", "green"])
        plt.savefig('../charts/'+col+'_distribution.jpg')
        plt.show()

def feature_vs_target(df,features, fields):
    fig, axs = plt.subplots(10,3, figsize=(20,45))
    for col in range(len(features)):  
        for f in range(len(fields)):  
            sns.histplot(df, 
                        x=features[col]+"_"+fields[f], 
                        hue="diagnosis", element="poly", 
                        stat="count", 
                        palette=["red", "green"],
                        ax=axs[col][f])


def plot_outlier(df,columns,title):
    sns.set(style="darkgrid")
    data_frame = pd.melt(df, id_vars='diagnosis', value_vars=columns)
    plt.figure(figsize=(15, 8))
    res=sns.boxplot(x='variable', y='value',hue='diagnosis', data=data_frame,palette=["red", "green"])
    plt.title(title, size=18, fontweight='bold')
    res.set_xticklabels(res.get_xmajorticklabels(), fontsize = 15)
    res.set_yticklabels(res.get_ymajorticklabels(), fontsize = 15)
    plt.show()


def plot_bar(df,title,save_as):
    plt.figure(figsize=(10, 8))
    ax = sns.barplot(x="importance", y="feature", data=df)
    ax.set_xlabel('Importance', fontsize=20)
    ax.set_ylabel('Feature', fontsize=20)
    ax.set_title(title, fontsize=30)
    plt.savefig('../charts/'+save_as)
    plt.show()