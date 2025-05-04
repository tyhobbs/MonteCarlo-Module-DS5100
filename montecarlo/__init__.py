class Die:
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
    def __init__(self):
        """
        The initializer takes a Numpy Array of faces as an argument, and will throw a 
        TypeError if not a NumpyArray. The arrays data type must be strings or numbers, 
        and the values are distinct. The initializer tests to see if the values are distinct
        and raises a ValueError if not. It will internally initialize weights, W, to 1 for 
        each face. It will then save the faces and weights in a private data frame with faces 
        as the index. 
        """	
    def new_weight(self):
        """
        This method is used to change the weight of a single side of a face. It takes two arguments, 
        the face value to be changed, and the new weight. It will check to see if the face has been
        passed is a valid value(mainly if it is in a die array). If not an index error will arise.
        Once this occurs, the method will see if the weight is a valid type, and if it is an integer
        or a float value or castable as a numeric. If none of these are possible, a TypeError will
        occur.
        """
    def roll_the_die(self):
        """
        In the method roll_the_die, it initially takes a parameter where it will see how many times the die
        is to be rolled, but it will always default to 1. With this method, it is a random sample of replacement
        using the private data frame but has access to the internally localized Weights, W. From this method, it
        will return a python list of outcomes from rolling the die, will not store the results internally. 
        """
    def my_die(self):
        """ This is a method that will return a copy of the private die dataframe and its status after the die class 
        has been run. This is a copy and will make sure that the private die dataframe is working correctly and that 
        it has not been altered during the course of the die class.
        """
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
    def play(self):
        """
        The play method takes an integer parameter, and specifies how many times the dice should be rolled. It 
        then saves the result of the play method to a private data frame. The private data frame is in wide
        format, as the roll number is a named index, and columns are for each die number as well. The face 
        rolled for each instance is then respective per each cell.
        """
    def most_recent_play(self):
        """
        This final method in the Game class will return the copy of the private data frame to the user that was
        most recently used. The parameter that is used to return the dataframe is defaulted to wide form, and the
        narrow form contains a "MultiIndex, compromising the Roll number and the die number respectively, and a single 
        column of possible outcomes from the face rolled. The most_recent_play method will also return a ValueError 
        if the user passes an invalid option for narrow or wide. 
        """
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
    def jackpot(self):
        """
        The jackpot method results of when all of the faces are the same, and for example there are all
        ones on a six sided die. This method computes how many times the game results in a jackpot. From
        the method, it will return an integer for the number of jackpots that occur.
        """
    def face_counts_per_roll(self):
        """
        The face counts per roll method, which is a method that computes how many times a given face is rolled in each 
        event. For Example, if a roll of five dice has all sixes, then the counts for this roll would be 5 for the face 
        value and 6 and 0 for the other faces. Once the faces are computed, the results will be returned to a data frame.
        This data frame will have an index of the roll number, face values as columns, and count values in the cells, and 
        it will also be in wide format.
        """
    def combo_count(self):
        """
        This method computes the distinct combinations of faces rolled, along with their counts as well.
        The combinations that are found from this method are order-independent, and often will be repetitions.
        From the method combo-count, it will return a data frame of the results, and the data frame will have 
        a MultiIndex of distinct combinations, and a column for the associated counts. 
        """
    def permutation_count(self):
        """
        This final method of the Analyzer class computes the distinct permutations of faces rolled, along with their
        counts found. The permutations are order-dependent, and will often contain repetitions. The method permutation_count
        will return a data frame with its results. This such data frame will have a MultiIndex of distinct permutations, and 
        a column for the associated counts. 
        """
