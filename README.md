# Python-Terminal-Blackjack

##### Introduction

For my second independent project I have chosen to make a terminal game of Blackjack with Python. It was definitely the hardest task I have undertaken thus far although it didnt take more than a few hours in total of coding time. If you would like to leave any feedback I would greatly appreciate it, I am still a very fresh beginner and I am very eager to improve the very rudimentary way I currently code

##### Project Description

<img width="471" alt="Screen Shot 2021-04-17 at 10 37 01 pm" src="https://user-images.githubusercontent.com/66585639/115113562-54387e80-9fce-11eb-9aa0-8fd8b11c0fde.png">

The terminal Blackjack starts by introducing itself to the player and asking the player how much money they will be bringing to the table.

Steps of the Blackjack program:

1. Asks the player which table they would like to join. Randomised table numbers from 1-88, Choice 1 has bets starting from $5, Choice 2 has bets starting from $10 and Choice 3 has bets starting from $50
2. The dealer (name randomly chosen) introduces themself
3. The player is asked to make a bet starting from the minimum for their table
4. The program shuffles the deck and pops out two cards for the player and two cards for the dealer
5. The program prints out the card names for the player and one card name for the dealer and hiding one of the dealers cards
6. The program then performs a checker on whether an ace is in either the player or the dealers hands. If it is in the players hands it asks the player if it would like the value to be treated as a 1 or as an 11. If in the dealers hand it has the value as 11 if it will be less than 21 with both cards or 1 if not.
7. An optional extra bet will then be asked for 
8. The program will then check if the values are equal to 21
9. If they are not it will ask if an extra card is wanted
10. If an extra card is not wanted the program sees who the winner is and changes the players balance according to whether they win or lose
11. If an extra card is wanted the preceding steps will repeat until the player decides they do not want any more cards and then evaluation will take place
12. Steps 4-11 will be repeated until the player indicates that they want to leave the game after which a goodbye message will be presented

##### Project Further Improvements

I have a number of improvements I wish to make on the project going forward. 

I would like to reduce my dependence on global variables and the use of the global keywords. Currently I have 3 static global vairables set at program entry and 8 global variables that are subject to change within the program. Ideally I would like to remove these and I will try and rewrite the program to not use global variables.

I also want to reduce the lines of code that I have used. Currently the code is 364 lines long (with the ASCII messages removed). Ideally I would like to lower this by: removing the amount of repetition, creating more efficient functions, creating more efficient  while/for loops and improving the if/elif program flow.

Thanks for reading 😃
