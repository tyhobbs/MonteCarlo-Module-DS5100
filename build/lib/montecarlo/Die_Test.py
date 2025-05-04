import numpy as np
import pandas as pd
import unittest
from my_die import Die
class die_test(unittest.TestCase):
    """
            This is a class that shows that each specific Die has N sides and W
            Weights, and will be able to be rolled for a specific face. Specifically,
            a normal Die has all sides having equal weights, and an unfair Die has 
            unequal Weights/side. The sides contain unique symbols being alphabetic or 
            numeric. W for Weight defaults to 1.0 for each face and can be changed after 
            the object is created. W for Weights are just positive numbers(int or floats,
            including 0), but not a normalized probability distribution. The Die will have
            one behavior, and will be to roll one or more times.

            The class will be composed of an initializer and three methods. The initializer 
            saves the faces and weights in a data frame in the index. The first method, to 
            change the weight of a single side. It will then change the face value to the new 
            weight, but if it is not a valid value a IndexError will arise. The second method, 
            which is rolling the die one or more times. This method takes a parameter of how 
            many times the die is to be rolled, and returns a list of outcomes based on the 
            parameter. The final method is the method to show the die's current state. This 
            final method returns a copy of the private die data frame.
    """
    def test_increment(self,data_type=None):
        """
        The initializer takes a Numpy Array of faces as an argument, and will throw a 
        TypeError if not a NumpyArray. The arrays data type must be strings or numbers, 
        and the values are distinct. The initializer tests to see if the values are distinct
        and raises a ValueError if not. It will internally initialize weights, W, to 1 for 
        each face. It will then save the faces and weights in a private data frame with faces 
        as the index. 
        """
        Faces={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        array1=np.array(list(Faces.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        Weights=1
        if not isinstance(array1, (list,np.ndarray)):
            raise TypeError("Input must be a NumPy array")
        if not np.issubdtype(array1.dtype, np.number):
            raise TypeError("Array elements must be numeric")
        if data_type is not None:
            try:
                np.asarray(array1, dtype=data_type)
            except TypeError:
                raise TypeError(f"Invalid data type specified: {bool}")
        
        if any(not isinstance(x, (int, float)) for x in np.ravel(array1)):
            raise TypeError("Array elements must be numeric")
        df=pd.DataFrame(array1)
        df.columns=['Die_1']
        df_copy = pd.DataFrame(array1)
        df_copy=df.copy(deep=True)
        print(df)
    def test_new_weight(self):
        """
        This method is used to change the weight of a single side of a face. It takes two arguments, 
        the face value to be changed, and the new weight. It will check to see if the face has been
        passed is a valid value(mainly if it is in a die array). If not an index error will arise.
        Once this occurs, the method will see if the weight is a valid type, and if it is an integer
        or a float value or castable as a numeric. If none of these are possible, a TypeError will
        occur.
        """
        Faces={'Face_1':1,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        New_Faces={'Face_1':5,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        new_Weight=5
        array2 = np.array(list(New_Faces.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_) 
        try:
            if any(not isinstance(x, (int, float)) for x in np.ravel(array2)):
                raise TypeError("Array elements must be numeric")
            if any(not isinstance(x, (int, int)) for x in np.ravel(array2)):
                raise TypeError("Array elements must be numeric")
            if not np.issubdtype(array2.dtype, np.number):
                raise TypeError("Array elements must be numeric")
        except:
            None
        df=pd.DataFrame(array2)
        df.columns=['Die_2']
        df_copy = pd.DataFrame(array2)
        df_copy=df.copy(deep=True)
        print(df)
    def test_roll_the_die(self):
        """
        In the method roll_the_die, it initially takes a parameter where it will see how many times the die
        is to be rolled, but it will always default to 1. With this method, it is a random sample of replacement
        using the private data frame but has access to the internally localized Weights, W. From this method, it
        will return a python list of outcomes from rolling the die, will not store the results internally. 
        """
        Faces={'Face_1':5,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        Weights=1
        n_rolls=1
        array3=np.array(list(Faces.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df=pd.DataFrame(array3)
        df.columns=['Die_3']
        rdm=np.random.choice(len(df),10)
        df=pd.DataFrame(rdm)
        df['n_rolls']=10
        df['n_rolls']=np.arange(1,len(df)+1)
        df.columns=['Faces','n_rolls']
        df_copy=df
        df_copy=df.copy(deep=True)
        print(df)
    def test_my_die(self):
        """ This is a method that will return a copy of the private die dataframe and its status after the die class 
        has been run. This is a copy and will make sure that the private die dataframe is working correctly and that 
        it has not been altered during the course of the die class.
        """
        Faces={'Face_1':5,'Face_2':1,'Face_3':1,'Face_4':1,'Face_5':1,'Face_6':1}
        Weights=1
        n_rolls=1
        array3=np.array(list(Faces.values()), np.ndarray.dtype==np.int32 or np.float64 or np.string_)
        df=pd.DataFrame(array3)
        df.columns=['Die_4']
        rdm=np.random.choice(len(df),10)
        df=pd.DataFrame(rdm)
        df['n_rolls']=10
        df['n_rolls']=np.arange(1,len(df)+1)
        df.columns=['Faces','n_rolls']
        df_copy=df
        df_copy=df.copy(deep=True)
        print(df_copy)
        if __name__ == '__main__':
            "This is the test file"
        