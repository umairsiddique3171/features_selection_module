import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Feature_Selection:
    
    def __init__(self,X,y,drop = None):
        self.X = X
        self.y = y
        self.drop = drop
        # self.dataset = pd.concat([X, y], axis=1)
        
        
        
    @property
    def dataset(self):
        
        return pd.concat([self.X,self.y],axis = 1)
        
        
        
    def corr_matrix(self):
        
        return self.dataset.corr()
        
        
        
    def corr_matrix_visual(self):
        
        plt.figure(figsize = (12,10))
        cor = self.dataset.corr()
        sns.heatmap(cor, annot = True , cmap = 'coolwarm') 
        # plt.cm. then you can any of the color in cmap
         
    
    
    def const_features_selection(self,thresh):
    
        from sklearn.feature_selection import VarianceThreshold
        var_thres = VarianceThreshold(threshold = thresh)
        var_thres.fit(self.X)
        print(var_thres.get_support())
        print('')
        print(f"Total Variable Features = {len(list(filter(lambda num : num == True ,var_thres.get_support().tolist() )))}")
        print('')
        print(f"Total Constant Features = {len(list(filter(lambda num : num == False ,var_thres.get_support().tolist() )))}")
        print('')
        const_cols = [column for column in self.X.columns if column not in self.X.columns[var_thres.get_support()]]
        print(f"Constant Columns = {const_cols}")
        if (self.drop == 'y') or (self.drop == 'Y'):
            self.X.drop(const_cols,axis = 1, inplace = True)
            print("Features Dropped!")
        else:
            while True:
                a = input('Do you want to drop the constant features? (y/n) ')
                if (a == 'y') or (a == 'Y'):
                    self.X.drop(const_cols,axis = 1, inplace = True)
                    print("Features Dropped!")
                    break 
                elif (a == 'n') or (a == 'N'):
                    print("Features Not Dropped!")
                    break
                    
                    
                    
    def features_corr_filter(self,thresh):
        
        col_corr = set()
        corr_matrix = self.X.corr()
        for i in range(len(corr_matrix.columns)):
            for j in range(i):
                if abs(corr_matrix.iloc[i,j]) > thresh:
                    colname = corr_matrix.columns[i]
                    col_corr.add(colname)
        print(col_corr)
        if (self.drop == 'y') or (self.drop == 'Y'):
            self.X.drop(col_corr,axis = 1, inplace = True)
            print("Features Dropped!")
        else:
            while True:
                a = input('Do you want to drop the feature with correlation above threshold? (y/n) ')
                if (a == 'y') or (a == 'Y'):
                    self.X.drop(col_corr,axis = 1, inplace = True)
                    print("Features Dropped!")
                    break 
                elif (a == 'n') or (a == 'N'):
                    print("Features Not Dropped!")
                    break
                    
                    
                    
    def features_corr_with_output_filter(self,thresh):
        col_corr = set()
        corr_matrix = self.dataset.corr()

        for i in range(len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i,-1]) <= thresh:
                col_corr.add(corr_matrix.columns[i])
        print(col_corr)
        if (self.drop == 'y') or (self.drop == 'Y'):
            self.X.drop(col_corr,axis = 1, inplace = True)
            print("Features Dropped!")
        else:
            while True:
                a = input('Do you want to drop the feature with correlation with output below threshold? (y/n) ')
                if (a == 'y') or (a == 'Y'):
                    self.X.drop(col_corr,axis = 1, inplace = True)
                    print("Features Dropped!")
                    break 
                elif (a == 'n') or (a == 'N'):
                    print("Features Not Dropped!")
                    break
                    
                    
                    
    def features_corr_visual_filter(self,thresh):
        
        plt.figure(figsize=(10,10))
        sns.set_style("whitegrid", {"axes.facecolor": ".0"})
        df = self.X.corr()
        mask = df.where((abs(df) >= thresh)).isna()
        plot_kws={"s": 1}
        sns.heatmap(df,
                    cmap='RdYlBu',
                    annot=True,
                    mask=mask,
                    linewidths=0.2, 
                    linecolor='lightgrey').set_facecolor('white')
        
        
        
    def features_corr_with_output_visual_filter(self,thresh):
        
        plt.figure(figsize=(10,10))
        sns.set_style("whitegrid", {"axes.facecolor": ".0"})
        df = self.dataset.corr()
        
        # where method in pandas replace the values not satisfying the condition with null values
        # isna method replace the null values with true bool
        mask = df.where((abs(df.iloc[:,-1:]) <= thresh)).isna()
    
        plot_kws={"s": 1}
        sns.heatmap(df,
                    cmap='RdYlBu',
                    annot=True,
                    mask=mask,
                    linewidths=0.2, 
                    linecolor='lightgrey').set_facecolor('white')
    