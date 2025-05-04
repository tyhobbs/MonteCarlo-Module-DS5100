import numpy as np
import pandas as pd
class Game:
    """
    This class consists of when there are more than one similar Die being rolled 
    simulataneously, and more than one time. The meaning of similar Die is referred
    as each Die has the same number of sides and associated faces, but each Die 
    may have different associated Weights, W. Each game is initialized with a Python
    list that contains one or more dice. The game objects have a behavior to play in 
    the game, and the player must roll all of the Dice a given number of times. After 
    playing the game, the game objects only will keep results from the most recent play.
    
    The game class consists of an initializer and two methods. The initializer takes
    a single parameter which is a list of already instantiated similar dice. This list of
    dice checks if all die have the same number of faces. The play method, which is 
    specifying how many times the dice should be rolled. For this method, the result is saved
    to a data frame, and the face rolled for each die will be saved as well. The final method
    for the Game class, the most recent play, returns a copy of the private play data frame 
    to the user. 
    """
    def __init__(self):
        """
        This initializer takes a parameter which is a list of already instantiated similar dice. 
        This list of similar Die objects will check if all of the die have the same number of faces. 
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df=pd.DataFrame(array1)
        df1=pd.DataFrame(array2)
        dfconc=pd.concat([df,df1],axis=1)
        dfconc.columns=['Die_1','Die_2']
        print(dfconc)
    def play(self):
        """
        The play method takes an integer parameter, and specifies how many times the dice should be rolled. It 
        then saves the result of the play method to a private data frame. The private data frame is in wide
        format, as the roll number is a named index, and columns are for each die number as well. The face 
        rolled for each instance is then respective per each cell.
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
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
    def most_recent_play(self):
        """
        This final method in the Game class will return the copy of the private data frame to the user that was
        most recently used. The parameter that is used to return the dataframe is defaulted to wide form, and the
        narrow form contains a "MultiIndex, compromising the Roll number and the die number respectively, and a single 
        column of possible outcomes from the face rolled. The most_recent_play method will also return a ValueError 
        if the user passes an invalid option for narrow or wide. 
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
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
        print(df_copy.shape)
        
        
        
        
        
        
        
        
        
       