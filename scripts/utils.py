from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def encoding_data(df):
  for column in df.columns:
    if df[column].dtype == np.int64 or df[column].dtype == np.float64:
      continue
    df[column] = LabelEncoder().fit_transform(df[column])
  
  return df

def corr_matrix(df,title:str,save_as):
    plt.figure(figsize=(25, 20))
    res=sns.heatmap(df.corr(), annot=True,fmt='.2f');
    res.set_xticklabels(res.get_xmajorticklabels(), fontsize = 15)
    res.set_yticklabels(res.get_ymajorticklabels(), fontsize = 15)
    plt.title(title,size=18, fontweight='bold')
    plt.savefig(f'../charts/{save_as}')
    plt.show

def find_high_corr(df):
    high_corr= df.corr()
    high_corr_columns = high_corr.index[abs(high_corr['diagnosis'])>=0.5]
    
    return high_corr_columns