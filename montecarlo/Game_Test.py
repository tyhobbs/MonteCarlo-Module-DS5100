import numpy as np
import pandas as pd
import unittest
from my_game import Game
class test_game(unittest.TestCase):
    def test_integrate(self):
        Die_1={'Face_1':5,'Face_2':1,'Face_3':3,'Face_4':1,'Face_5':1,'Face_6':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':5}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df=pd.DataFrame(array1)
        df1=pd.DataFrame(array2)
        dfconc=pd.concat([df,df1],axis=1)
        dfconc.columns=['Die_1','Die_2']
        print(dfconc)
    def test_play(self):
        Die_1={'Face_1':5,'Face_2':1,'Face_3':3,'Face_4':1,'Face_5':1,'Face_6':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':5}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df=pd.DataFrame(array1)
        df1=pd.DataFrame(array2)
        dfconc=pd.concat([df,df1],axis=1)
        dfconc.columns=['Die_1','Die_2']
        n_rolls=10
        RANDOM_Die_1 = np.random.choice(len(df),n_rolls)
        RANDOM_Die_2=np.random.choice(len(df1),n_rolls)
        df_Die_1=pd.DataFrame(RANDOM_Die_1)
        df_Die_2=pd.DataFrame(RANDOM_Die_2)
        df_combined=pd.concat([df_Die_1,df_Die_2],axis=1)
        df_combined.columns=['Die_1','Die_2']
        df_combined['n_rolls']=n_rolls
        df_combined['n_rolls']=np.arange(1,len(df_combined)+1)
        df_combined.set_index('n_rolls', inplace=True)
        df_copy = df_combined
        df_copy=df.copy(deep=True)
        print(df_combined)
    def test_most_recent_play(self):
        Die_1={'Face_1':5,'Face_2':1,'Face_3':3,'Face_4':1,'Face_5':1,'Face_6':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':5}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df=pd.DataFrame(array1)
        df1=pd.DataFrame(array2)
        dfconc=pd.concat([df,df1],axis=1)
        dfconc.columns=['Die_1','Die_2']
        n_rolls=10
        RANDOM_Die_1 = np.random.choice(len(df),n_rolls)
        RANDOM_Die_2=np.random.choice(len(df1),n_rolls)
        df_Die_1=pd.DataFrame(RANDOM_Die_1)
        df_Die_2=pd.DataFrame(RANDOM_Die_2)
        df_combined=pd.concat([df_Die_1,df_Die_2],axis=1)
        df_combined.columns=['Die_1','Die_2']
        df_combined['n_rolls']=n_rolls
        df_combined['n_rolls']=np.arange(1,len(df_combined)+1)
        df_combined.set_index('n_rolls', inplace=True)
        df_copy = df_combined
        df_copy=df.copy(deep=True)
        print(df_copy)
        if df_copy.shape[1]  < df.shape[0]:
            print("DataFrame is in Narrow shape")
        else:
            raise ValueError("DataFrame is in Wide Shape")
    if __name__ == '__main__':
        unittest.main()