# MonteCarlo Simulator
## By Tyler Hobbs
## Date of Collection: 2025 May 04
This simulator is separated into three sections:
* The Die Class: A Die or multiple Dice are initialized into the simulator
* The Game Class: A game is played with the initialized in the simulator
* The Analyzer Class: The game is analyzed to check frequencies of dice within the simulator

## Description

### The Die Class: 
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

### The Game Class: 
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

### The Analyzer Class:
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

## Getting Started

### Dependencies

* Prerequisites include running program on current OS version of Windows 10, or Mac OS 10.9, and the use of Python
  by Conda or with a notebook type software like Jupyter lab. 

### Installing

* Can be installed through the MonteCarlo Module.
* Modifications may be required based on the testing for each simulation as such.
* * There will be different numbers of Dies, and different numbers of faces and Weights for each simulation, so these
  modifications will be required.

### Executing program

* Open the Software of Choice:
* Start the Creating a Die:
* This will be by using the Die class, in which it takes a parameter of Faces and Weights.
* It also makes sure that the initialized Die is a numpy array, and is a string or number as well.
* If the initialized Die is not a numpy array, or strings or numbers a TypeError will occur.
* Once the Die is initialized as a numpy array, it is then saved in a private data frame.

* To change the Die's Weights:
* Use the method "new_weight" in the Die class and change the weights by its dictionary.
* Once the weights are changed, the weights are then initialized in a numpy array once again.
* If they are not in a numpy array, a ValueError will occur.

* Rolling the Die:
* Use the method "roll_the_die" and take the dictionary from either the first initialized Die or the
  one after the weight was changed.
* Make sure to transform the die to a numpy array so a ValueError does not occur.
* The die is then rolled randomly and placed in a private data frame.

* Gathering the data from the most recent roll:
* Use the method "my_die" and print out the previous private data frame that was just ran in the
  "roll_the_die" method.

Simulating when there are more than one similar Die:
* As this uses more than one Die, it will use the Game class, and not the Die class.
* The first step to take is to initialize two or more similar Die following the previous steps
  for initializing a single Die.
* The Dies will be created as dictionaries and transformed to numpy arrays, and eventually
  concatenated to a combined data frame together during this initialization step.

Playing a Game with two or more Dice:
* Use the data frame from the initialized dice, and each dices faces will be randomized based on
  a set number of rolls.
* The rolls for the "play" method always set to 1, and can be changed.
* Once the dices faces are randomized, they are then put in a new private data frame based on the
  number of rolls.
* This new private data frame is set to be in wide format.

Obtaining the data from the most recent play:
* Use the method "most_recent_play" and obtain the private data frame created from the "play"
  method.
* The private data frame is defaulted to wide format, and will return a ValueError if not.
* If it is in narrow, it will require itself to have a multiIndex.

Analyzing the Data from playing a game with two or more dice:
* To Examine the data that was previously ran in using the Game class, it is essential to use the
  Analyzer class for the next task.
* As stated in the Game class, the Analyzer class also will take a Game object, in that it will
  take two or more initialized dice in a combined data frame.
* Once these dice are initialized in a data frame, it also checks to make sure that the shape of the
  data frame is correct.
* This data frame is defaulted to be in wide format, and returns a ValueError if not.
* If the data frame is in narrow, a multiIndex will be required.

Checking all the Games played for when there exists faces being the same:
* To return the result of when there are a certain number of faces being the same during a set number
  of games played, the "jackpot" method will be used.
* This method uses the data frame initialized at the beginning of the Analyzer class, randomizes rolls
  based on a set number of games played and will create a new data frame on the new randomized faces.
* Then, a new column, "is_equal" is added to the data frame to where is able to check throughout the
  data frame at which points all the faces are equal.
* The "is_equal" column is then summarized and a integer is output from the "jackpot" method.

Obtaining the number of Faces per roll:
* It is important to know what the number provided for each face is for each roll, so the method
  used to track this will be the "face_counts_per_roll."
* This method also uses the same initialized data frame from the Analyzer class, and from that output,
  each column for each Die is randomized and concatenated into a new data frame based on the number of
  rolls that were performed.
* A new column is then added for the Face counts of each Die that was initialized, and in these columns,
  they take the sum of the Randomized data into each of the new columns to show where each Die is at after
  each specific roll.

Obtaining the Count from Combinations:
* While it is important to show the Faces per roll, it is also important to show the count of their faces per roll as a total.
* This will be performed with the method "combo_count" and also uses the previously used initialized data frame
  from the Analyzer class.
* From the initialized data frame, each column from for each Die is randomized and concatenated into a new data
  frame based on the number rolls that were performed once again.
* With the newly created data frame, a new column of counts is made to count all of the data within the model to track
  any changes within the faces.

Computing the permutations of faces rolled:
* As stated before, this method will also use the data frame that was initialized from the Analyzer class, and to compute
  the distinct permutations of faces rolled, it will use the method "permutation_count."
* To create permutations of each Die, each column of the data frame is permutated, and re-concatenated into a new data frame
  based on the number of rolls that were perfomed in this method.

# Examples of Calling the Classes
```
Fair_coin=Die()
Fair_coin.roll_the_die()
Fair_coin.my_die()
```
```
Dice=Game()
Dice.play()
Dice.most_recent_play()
```
```
Dice_Analysis=Analyzer()
Dice_Analysis.jackpot()
Dice_Analysis.face_counts_per_roll()
Dice_Analysis.combo_count()
Dice_Analysis.permutation_count()
```

## Authors

Tyler Hobbs
Email: vsg3se@virginia.edu

## Version History
* 0.1
    * Initial Release

