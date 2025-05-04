import pandas as pd
import numpy as np
import itertools 
class Analyzer:
    """
    The analyzer class is specifically the class that is
    able to take the results of a single die game, analyze it,
    compute the results, and print out various descriptive statististical
    properties based on the single die game. 
    
    The Analyzer class is made up of an initializer, and four methods. 
    The initializer for the Analyzer class first takes a game object as its input
    parameter, and if the object is not a game object, a valueError will arise. Then,
    the first method is called the Jackpot method, in which all sides have equal value. 
    This is seen as when all sides could be a 1, and the method computes how many times
    a jackpot is returned, and as such an integer is returned. The next method is 
    computing how many times a given face is rolled for each roll event. This event will
    be returned in a dataframe of the results, and the data frame has the index of roll 
    number, face values of columns, and count values in cells. The third method computes the 
    distinct combinations of faces rolls and their counts as well. These combinations are returned
    in a data frame. The final method in the Analyzer class is the permutation count method, where
    it computes the distinct permutations of faces rolled, and their distinct counts alongside. 
    A data frame will be returned from these permutations. 
    """
    def __init__(self):
        """
        The initializer for the Analyzer class takes a Game object as its input parameter, and 
        will throw a ValueError if it is not a Game object.
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':3,'Face_4':1}
        Die_3={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array3=np.array(list(Die_3.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df1=pd.DataFrame(array1)
        df2=pd.DataFrame(array2)
        df3=pd.DataFrame(array3)
        combined=pd.concat([df1,df2,df3],axis=1)
        combined.columns=['Die_1','Die_2','Die_3']
        print(combined)
        if combined.shape[1] < combined.shape[0]:
            print("DataFrame is in Wide shape")
        else:
            raise ValueError("DataFrame is in Narrow Shape")
    def jackpot(self):
        """
        The jackpot method results of when all of the faces are the same, and for example there are all
        ones on a six sided die. This method computes how many times the game results in a jackpot. From
        the method, it will return an integer for the number of jackpots that occur.
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_3={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array3=np.array(list(Die_3.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df1=pd.DataFrame(array1)
        df2=pd.DataFrame(array2)
        df3=pd.DataFrame(array3)
        combined=pd.concat([df1,df2,df3],axis=1)
        combined.columns=['Die_1','Die_2','Die_3']
        n_rolls=1        
        RANDOM_one = np.random.choice(len(df1),n_rolls)
        RANDOM_two = np.random.choice(len(df2),n_rolls)
        RANDOM_three = np.random.choice(len(df3),n_rolls)
        df_Die_1=pd.DataFrame(RANDOM_one)
        df_Die_2=pd.DataFrame(RANDOM_two)
        df_Die_3=pd.DataFrame(RANDOM_three)
        df=pd.concat([df_Die_1,df_Die_2,df_Die_3],axis=1)
        df.columns=['Die_1','Die_2','Die_3']
        df['n_rolls']=n_rolls
        df['n_rolls']=np.arange(1,len(df)+1)
        df.set_index('n_rolls', inplace=True)
        df['is_equal']=df.apply(lambda x: 1 if x.Die_1 == x.Die_2 ==x.Die_3 else 0,axis=1)
        print(df)
        JACKPOT=df['is_equal'].sum()
        print(JACKPOT)
    def face_counts_per_roll(self):
        """
        The face counts per roll method, which is a method that computes how many times a given face is rolled in each 
        event. For Example, if a roll of five dice has all sixes, then the counts for this roll would be 5 for the face 
        value and 6 and 0 for the other faces. Once the faces are computed, the results will be returned to a data frame.
        This data frame will have an index of the roll number, face values as columns, and count values in the cells, and 
        it will also be in wide format.
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_3={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array3=np.array(list(Die_3.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df1=pd.DataFrame(array1)
        df2=pd.DataFrame(array2)
        df3=pd.DataFrame(array3)
        combined=pd.concat([df1,df2,df3],axis=1)
        combined.columns=['Die_1','Die_2','Die_3']
        n_rolls=1
        Counts_Face_1=1
        Counts_Face_2=1
        Counts_Face_3=1
        RANDOM_one = np.random.choice(len(df1),n_rolls)
        RANDOM_two = np.random.choice(len(df2),n_rolls)
        RANDOM_three = np.random.choice(len(df3),n_rolls)
        df_Die_1=pd.DataFrame(RANDOM_one)
        df_Die_2=pd.DataFrame(RANDOM_two)
        df_Die_3=pd.DataFrame(RANDOM_three)
        df=pd.concat([df_Die_1,df_Die_2,df_Die_3],axis=1)
        df.columns=['Die_1','Die_2','Die_3']
        df['Counts_Face_1']=Counts_Face_1
        df['Counts_Face_2']=Counts_Face_2
        df['Counts_Face_3']=Counts_Face_3
        df['n_rolls']=n_rolls
        df['n_rolls']=np.arange(1,len(df)+1)
        df['Counts_Face_1']=df1.sum(axis=1)
        df['Counts_Face_2']=df2.sum(axis=1)
        df['Counts_Face_3']=df3.sum(axis=1)
        print(df)
    def combo_count(self):
        """
        This method computes the distinct combinations of faces rolled, along with their counts as well.
        The combinations that are found from this method are order-independent, and often will be repetitions.
        From the method combo-count, it will return a data frame of the results, and the data frame will have 
        a MultiIndex of distinct combinations, and a column for the associated counts. 
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_3={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array3=np.array(list(Die_3.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df1=pd.DataFrame(array1)
        df2=pd.DataFrame(array2)
        df3=pd.DataFrame(array3)
        combined=pd.concat([df1,df2,df3],axis=1)
        combined.columns=['Die_1','Die_2','Die_3']
        n_rolls=1
        Counts=1
        RANDOM_one = np.random.choice(len(df1),n_rolls)
        RANDOM_two = np.random.choice(len(df2),n_rolls)
        RANDOM_three = np.random.choice(len(df3),n_rolls)
        df_Die_1=pd.DataFrame(RANDOM_one)
        df_Die_2=pd.DataFrame(RANDOM_two)
        df_Die_3=pd.DataFrame(RANDOM_three)
        df=pd.concat([df_Die_1,df_Die_2,df_Die_3],axis=1)
        df.columns=['Die_1','Die_2','Die_3']
        df['Counts']=df.sum(axis=1)
        print(df)
    def permutation_count(self):
        """
        This final method of the Analyzer class computes the distinct permutations of faces rolled, along with their
        counts found. The permutations are order-dependent, and will often contain repetitions. The method permutation_count
        will return a data frame with its results. This such data frame will have a MultiIndex of distinct permutations, and 
        a column for the associated counts. 
        """
        Die_1={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_2={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        Die_3={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1}
        array1=np.array(list(Die_1.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array2=np.array(list(Die_2.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        array3=np.array(list(Die_3.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df1=pd.DataFrame(array1)
        df2=pd.DataFrame(array2)
        df3=pd.DataFrame(array3)
        combined=pd.concat([df1,df2,df3],axis=1)
        combined.columns=['Die_1','Die_2','Die_3']
        n_rolls=1
        PERM_one=itertools.permutations(df1)
        PERM_two=itertools.permutations(df2)
        PERM_three=itertools.permutations(df3)
        df_PERM_1=pd.DataFrame(PERM_one)
        df_PERM_2=pd.DataFrame(PERM_two)
        df_PERM_3=pd.DataFrame(PERM_three)
        df_combined=pd.concat([df_PERM_1,df_PERM_2,df_PERM_3],axis=1)
        df_combined.columns=['Die_1','Die_2','Die_3']
        df_combined['n_rolls']=n_rolls
        df_combined['n_rolls']=np.arange(1,len(df_combined)+1)
        print(df_combined)