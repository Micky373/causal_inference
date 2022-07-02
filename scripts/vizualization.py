import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from causalnex.structure.notears import from_pandas
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from IPython.display import Image

# A function for count plotting
# Recieves dataframe and columns then plots the graph

def count_plot(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(10, 8))
    sns.countplot(data=df, x=column)
    plt.xlabel(f'{column}', fontsize=17)
    plt.ylabel("Count", fontsize=17)
    plt.title(f'\nDistribution of {column}\n', size=20, fontweight='bold')
    plt.savefig('../charts/count_plot.jpg')
    plt.show()

# A function for plotting distribution graph
# Recieves data frame and columns then plots the distribution graph

def plot_ditribution(df,columns):
    for col in columns:
        sns.displot(df, x=col, hue="diagnosis",kind='kde',multiple='stack',palette=["red", "green"])
        plt.savefig('../charts/'+col+'_distribution.jpg')
        plt.show()

# A function for bivariate analysis between the feature and target
# Recieves data frame, fieds, features then creates a plot

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


# A function for plotting outliers in a dataframe
# Recieves dataframe, columns title and plots the outlier graph of the given column

def plot_outlier(df,columns,title):
    sns.set(style="darkgrid")
    data_frame = pd.melt(df, id_vars='diagnosis', value_vars=columns)
    plt.figure(figsize=(15, 8))
    res=sns.boxplot(x='variable', y='value',hue='diagnosis', data=data_frame,palette=["red", "green"])
    plt.title(title, size=18, fontweight='bold')
    res.set_xticklabels(res.get_xmajorticklabels(), fontsize = 15)
    res.set_yticklabels(res.get_ymajorticklabels(), fontsize = 15)
    plt.show()


# A functino that creates a bar plot
# Recieves a dataframe, title and save_as then it will plot the bar chart 

def plot_bar(df,title,save_as):
    plt.figure(figsize=(10, 8))
    ax = sns.barplot(x="importance", y="feature", data=df)
    ax.set_xlabel('Importance', fontsize=20)
    ax.set_ylabel('Feature', fontsize=20)
    ax.set_title(title, fontsize=30)
    plt.savefig('../charts/'+save_as)
    plt.show()


def plot_causal(sm,title):
    viz = plot_structure(
    sm,
    graph_attributes={"scale": "2"},
    all_node_attributes=NODE_STYLE.WEAK,
    all_edge_attributes=EDGE_STYLE.WEAK)
    image = Image(Image(viz.draw(format='png')))
    image.save(f'../charts/{title}.jpg')
    return Image(viz.draw(format='png'))