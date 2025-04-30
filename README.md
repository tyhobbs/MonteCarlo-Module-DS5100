# MonteCarlo Simulator
## By Tyler Hobbs

This simulator is separated into three sections:
*The Die Class: A Die or multiple Dice are initialized into the simulator
*The Game Class: A game is played with the initialized in the simulator
*The Analyzer Class: The game is analyzed to check frequencies of dice within the simulator

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

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Tyler Hobbs
Email: vsg3se@virginia.edu

## Version History
* 0.1
    * Initial Release

## License

This project is licensed under the Tyler Hobbs License - see the LICENSE.md file for details
