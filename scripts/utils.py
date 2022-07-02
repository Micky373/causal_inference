from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# A function that recieve a dataframe and returns a dataframe after encoding

def encoding_data(df):
  for column in df.columns:
    if df[column].dtype == np.int64 or df[column].dtype == np.float64:
      continue
    df[column] = LabelEncoder().fit_transform(df[column])
  
  return df

# A function that plots correlation matrix and saves the fig in the chart folder

def corr_matrix(df,title:str,save_as):
    plt.figure(figsize=(25, 20))
    res=sns.heatmap(df.corr(), annot=True,fmt='.2f');
    res.set_xticklabels(res.get_xmajorticklabels(), fontsize = 15)
    res.set_yticklabels(res.get_ymajorticklabels(), fontsize = 15)
    plt.title(title,size=18, fontweight='bold')
    plt.savefig(f'../charts/{save_as}')
    plt.show

# A function for finding highly correlated features it recieves a dataframe and returns list of columns
def find_high_corr(df):
    high_corr= df.corr()
    high_corr_columns = high_corr.index[abs(high_corr['diagnosis'])>=0.5]
    
    return high_corr_columns

# A function for fixing outliers using median
# Receives a dataframe and returns a dataframe after fixing the outliers

def fix_outlier(df):
    column_name=list(df.columns[2:])
    for i in column_name:
        upper_quartile=df[i].quantile(0.75)
        lower_quartile=df[i].quantile(0.25)
        df[i]=np.where(df[i]>upper_quartile,df[i].median(),np.where(df[i]<lower_quartile,df[i].median(),df[i]))
    return df

# A function that is used to scale the dataframe
# Recieves a dataframe and returns a data frame after scaling

def scaler(df):
    df_new = (df-df.min())/(df.max()-df.min())
    return df_new

# A function that computes a jaccard simmilarity index
# Receive two values and check there simillarity and return index of similarity

def jaccard_similarity(g, h):
    a = g.edges
    b = h.edges
    i = set(a).intersection(b)
    result = round(len(i) / (len(a) + len(b) - len(i)),3) 
    print(f'The jaccard simillarity between {g} and {h} is {result}')