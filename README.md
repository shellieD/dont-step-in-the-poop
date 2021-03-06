# DON'T STEP IN THE POOP

## Introduction

This project has been developed as part of the [Code Institute's](https://codeinstitute.net/) Diploma in Full-Stack Software Development.  The aim is to create a command line app that will demonstrate the skills I have learnt in the Python programming language. 

This command line app is a fun little game of chance.  The aim of the game is not disimiliar to Battleships - where you guess co-ordinates in a grid to sink your opponents ships - however, in this game you need to guess co-ordinates to make a clear path across the 'garden' without stepping in a dog poo. 

[Link to deployed site here](https://dont-step-in-the-poop.herokuapp.com/)

![Am I Responsive Screenshot](assets/docs/screenshots/amiresponsive.png)

## How To Play

The rules of the game are simple.  Make a horizontal path through the 'garden' (gameboard) without discovering a poo.  

The gameboard is made up of 8 rows and 8 columns and each space on the board is represented with a green tile.  There are 13 poos randomly distributed across the garden and only one row where no poos have landed.  

Select a row, and then a column to start guessing.   If you discover a poo, the green tile will be replaced with a poo emoji.  If you choose a coordinate which has no poo on it, the green tile will be replaced with a boot. 

Can you find the clear path through the garden by stepping on 5 poos or less?  Step on 5 poos and I'm afraid it's game over, and you need to go home and clean those boots... or just play again!


## UX 

### Site Goals

The site's aims are to:
* Provide the user with a fun and simple game of chance. 
* Provide clear instructions on how to play the game.
* Provide an appropriate response to all user inputs and handle invalid data accordingly.
* Provide an enjoyable experience to the user.


### User Stories

As a user I want:
* To play a fun and simple game of chance. 
* The purpose and the rules of the game to be apparent.
* To know that my input is valid.
* To know how many 'lives' I have left.


### Scope

To satisfy all of the site goals and user stories, the below features are planned taking into consideration the time-scale:

* Use ASCII art and Emojis on the welcome screen to provide a positive user experience.
* Provide a fun backstory and clear instructions on how to play the game.
    - The option to view the rules and story for new users.
    - The option to bypass viewing the rules and story for returning users.
* Appropriate use of data validation to handle invalid input gracefully and prevent the program from terminating.
    - Provide the user with an error message if their entry is invalid and guidance on what input is accepted.
* Display a count of how many poos have been discovered - once this reaches 5, the game is over.
* Create a grid style game-board and switch out the tiles depending on if a poo or a clear space has been guessed.  This will allow the user to know which coordinates they have already guessed.
    - Validate user guesses and alert the user if they choosen a tile they have already tried or if their input is not valid.
* Use ASCII art for win/lose screens.
    - Return to a new game-board if the user chooses to continue to play.
    - Provide goodbye message if player chooses not to continue playing. 

Features that would be nice to have for this project, but are out of scope given the small time-scale are:

* Enabling different levels of difficulty:
    - Larger/smaller game-board
    - More or less poos to dodge
    - More or less lives
* Leader Board:
    - Keeps a track of the users who used the fewest guesses to win the game.
* Allow a winning path to be either horizontal, vertical or diagonally (in this first stage of development only a horizontal clear path will win the game).


### Game Flow

To aid my understanding of how the logic of the game will work, and to prevent 'scope-creep' I created the below flow chart using [Lucid Charts](https://lucid.co/)

<details>
<summary>Game Flow Chart</summary>
<br>

![Game Flow Chart](assets/docs/flowcharts/game-flowchart.png)
</details>


### Features & Design

* Design 

As there are some limitations as to how you can style a command-line based app, I opted to use FIGlet fonts to create the Welcome Screen, Rules/Story/Game-Board heading and the goodbye screen.  I used the standard FIGlet font for the welcome screen and goodbye screen and 'bubble' for the rules, story and game-board headings.  

I also decided to use poo emojis as a design feature around each heading and for the game board I used a green tile emoji to represent the grass on the garden and a poo or shoe emoji to denote whether a poo or a a clear space had been discovered.  

I incorporated ASCII art for the win or lose screens and the source of the art is listed in the content section of this README documentation. 

I think these design features help to provide a bit of shape, color and fun to the game and provide a more pleasing user experience. 


* Main Page and Welcome Screen

In order to give the user insight into the nature of the game, I designed the welcome page to show the name of the game (which in itself is self-explanatory) styled using [FIGlet fonts](http://www.figlet.org/examples.html)  and set the background of the browser to an image created using [flaticon](https://www.flaticon.com/), to fit with the theme - lots of poos on a green background.  On the main screen the user is asked to enter their name so a personalised greeting can be created.

![Opening Screen](assets/docs/screenshots/opening-screen.png)

<br>

* Story and Rules

![View Story and Rules?](assets/docs/screenshots/seerules.png)

For first-time users of the game, I thought it would be appropriate to have the option to view the rules and story of the game.  The story gives the game some context and adds an element 'fun'.

For returning users who may not wish to view the rules, they can simple answer 'n' to this question.

By answering 'y' at this point, the player will be taken to the Story screen.  There is then an option to press enter to continue, which gives the player as much time as they need to read the story before the rules are displayed.

When the player presses 'Enter' the terminal is cleared and the rules are displayed in a consistent styling to the story screen to avoid too much screen movement.

![Story](assets/docs/screenshots/story.png)
![Rules](assets/docs/screenshots/rules.png)

Once the rules are displayed or the user selects that they do not wish to view the rules, they will be asked if they are ready to play. 

All input is validated to check that the answer is either 'y' or 'n' and if not the below error will be shown:-

![Rules](assets/docs/screenshots/ynerror.png)

It was important to include data validation for all inputs as it is incredibly frustrating and does not provide a good user experience if the game ends because of incorrect data entry.  This would result in the user having to restart the program from the beginning, potentially discouraging the user from playing. 

If the user selects that they are ready to play, they will be taken to the game-board, where the game will begin.

* Game-board 

 The game-board screen displays a heading 'Game-board' using figlet font 'bubble' which has a top and bottom border of emoji poos to give it shape and colour.  There is a brief overview of the rules and then the game-board.  The game-board consists of 8 rows and 8 colums, with each space represented as a green tile.  This is to create the effect of a garden to fit with the story of the game and to provide colour to an otherwise bland terminal.  The user is then tasked to guess a row, followed by a column to make their first guess or 'step' across the garden.  

![Game-board Screen](assets/docs/screenshots/game-board.png)

As the user progresses through the game and continues to make guesses, the green tiles update to show either a poo emoji if a poo is found or a shoe emoji if there is no poo on the path.   It also shows the amount of poos already stepped in to let the user know how many more incorrect guesses they can make.  The game is over when 5 poos are stepped in. 

![Blank Board](assets/docs/screenshots/blank-board.png) ![Updated Board](assets/docs/screenshots/updated-board.png)

A message is displayed to the player after each guess, letting them know if they have stepped in a poo or a clear path.   

![Message to player - no poo](assets/docs/screenshots/no-poo.png) ![Message to player - poo](assets/docs/screenshots/mess.png)

* You Win / You Lose

The game ends if the player 'steps' on 5 poos, or manages to find the winning path through the game board.  Once either of these criteria is met, the correct screen will appear letting the user know if they have won or lost the game.  I have used ASCII art on both winning and loosing pages to provide a bit more interest and if the player chooses to play on, they will be returned to a fresh gameboard or if they choose to stop playing, a thank you and good bye message will be displayed before terminating the game. 


### Future Development

Whilst I am happy with the functionality and simplicity of the app in it's current state, there are a number of features I would like to implement in the future.  

I would like introduce varying levels of difficulty, which could be done in a number of ways:

1. Reducing or increasing the number of rows and columns on the game board;
2. Reducing or increasing the number of poos to avoid;
3. Reducing or increasing the number of poos allowed to be stepped in before the game is declared as lost.

As the board is created as a class, I think the above would be fairly simple options to add by creating a new user input to select the difficulty level - easy, medium or hard - and passing the appropriate arguments for the number of rows/columns, number of poos and number of lives.

In it's current state, the user is only able to win the game by finding a clear path horizontally through the board.  I would also like to develop the game further so that the user can create a straight path either horizontally, vertically or diagonally through the board.  Unfortunately this was out of scope for this project due to the limited time-frame I was working within, but I think that adding this functionality would provide a better user experience.


## Testing
<br>

### Manual Testing 

Testing took place continuously throughout the development of the app.  Functions were tested using print statements as and when they were created and the functionality was tested regularly in the IDE to ensure the outcome of those functions was as expected.  I used the linter recommended by CI (flake8) to identify any problems within the code and rectified these as soon as they were brought to my attention.  In the instance that functions did not work as expected, I use the integrated debugger tool within Gitpod to see step by step exactly what was happening  to enable me to make appropriate changes.

I did uncover and resolve a bug after refactoring my code to validate the user input when choosing a row or a column and this is explained in further detail in the Issues section below.

All inputs have been tested for the following to ensure data validation is working as expected:-

* Where a 'y' or 'n' is accepted as input I have tested with other string combinations, such as other letters or numbers, symbols and no input.  No issues were uncovered here and the input validation was working as expected. 

* Where an integer between 0 and 8 (not including 8) is expected, I have tested using a strings, numbers greater than 7, letters, symbols and no input.  No issues were uncovered here and the input validation was working as expected. 

All inputs have been continuously tested in an attempt to break the game, however the loops will continue indefinitely until valid data has been entered. 

The app was deployed early on Heroku so I could see the final output as this differs from what is seen when running the program in the IDE.  This meant I was able to make changes to the styling as I went along to ensure the best possible user experience was achieved.  

Once the game was 'finished' I submitted it for peer code review in the Code Institue Slack Community.  A few small issues were brought to my attention, which were noted and tweaked and again, are discussed in further details in the 'Issues' section. 

### Issues found during development

During the development process I had created a function which asked for user input to guess a row and column to try on the gameboard and used the following code for both, although worded accordingly for row or column:-

```row = int(input("Choose a row \n"))```

Initially I used the int() function to convert the input from strings to integers and then created a function to validate that the numbers picked were between 0 and 7.   Later during the development process I realised I needed to also validate that the user input was able to be converted to a number from a string and that a letter or symbol had not been entered incorrectly instead.  I therefore changed the way the input was validated and refactored the code for obtaining user input for rows and columns.  I removed the int() function when the input was expected and instead created a separate function to handle the input. 

From the set_up_game function the below variable was defined and called the validate_choice and validate_input functions to ensure the appropriate input was accepted:

```
coord = (validate_choice("row \n"), validate_choice("column \n"))
```

     
```
def validate_choice(user_choice):
    """
    Displays 'row' or 'column' string and gets user
    input for row or column chosen.
    Calls validate_input funtion to validate user
    input
    """
    while True:
        choice = input(f"Choose a {user_choice} ")

        if validate_input(choice):
            break
    return choice
```

``` 
def validate_input(value):
    """ Validates user input for row/column

    Within the first try statement, converts the row/column value entered
    into an integer.   Returns an error if value entered is not a number.

    Within the second try statement, returns an error if the number
    is not within the range 0-8
    """
    try:
        value = int(value)
    except ValueError:
        print(f"Invalid data: {value} is not a number")
        return False

    try:
        if value not in range(8):
            raise ValueError(f"Please choose a number between 0 and 7."
                             f"\nYou entered: {value}")
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.")
        return False
    return True
```

This code correctly validated the user input by:

1. Checking that the input could be converted from a string to an integer and if not, throw an error explaining that the data 'is not a number'
2. Checking that if a number was entered, that it was within the range of 8 and if not, throw an error explaining that the number is not between 0 and 7.

However, when I came to further develop the function, I noticed that the if statements that used the coord variable no longer worked.  This was because the input was no longer being converted to an integer on input, so the data type of the coord variable had been changed from a tuple of two integers, to a tuple of two strings.  For example, if the user had chosen row 1 and column 3, the coord would now be ('1', '3') instead of previously being stored as (1, 3).

This meant the below code no longer worked.

```
flat_poos = 0  
player_guess = [] 
correct_guess = [] 

    while flat_poos < 5:

    coord = (validate_choice("row \n"), validate_choice("column \n"))

    while coord in player_guess:
        print("Oh plop... you've already guessed that!! Try again")
        coord = (validate_choice("row \n"), validate_choice("column \n"))

    player_guess.append(coord)

    if coord in poos:
        print("What a mess!!!")
        flat_poos = flat_poos + 1
        print(f"You stood in poo at coordinate: {coord}")
    elif coord in clear_path_coord:
        correct_guess.append(coord)
        print("Phew, no poo there!!")
        print(f"Clear path at coordinate: {coord}")

    else:
        print("Phew, no poo there!!")
        print(f"Clear path at coordinate: {coord}")

    print(f"You have stepped in {flat_poos} poos.")
```

At first, I couldn't understand exactly why this small change had stopped the game from functioning, until I used the debugger tool and noted that the data type of the coord had changed. 

Once I realised this, I searched the internet to find out how to convert the elements in a tuple from strings to integers and created a new variable called coord_tuple using the information I had found on Stack Overflow:

```
coord_tuple = tuple(int(el) for el in coord)
```

![List Comprehension for converting elements in a tuple from strings to integers](assets/docs/screenshots/stackoverflow.png)

I then used this variable in my if/elif/else statement which resulted in the function working as it should do once more. 


### Issues brought to my attention via Peer-Code-Review

* Whilst the app works perfectly fine in most browsers, there is an issue with Firefox, which means that only half of the emoji's used are shown in the terminal (screenshot below).  At this stage I am unsure why this is happening, but believe it could be to do with the limitation of the Code Institute template which has been utlised to allow for a web-based terminal to be used.  Whilst I would have loved to have been able to rectify this, at the time the issue was discovered, it was unfortunatley out of scope to fix and as the game still functions well (albeit not as aesthetically pleasing) I felt that this is something that could remain for the time being.  With a more sound understanding of the issue, I hope to be able to fix this in the future.   

![Firefox Issue](assets/docs/screenshots/firefox.png)

* It was brought to my attention that if the player chose not to play the game after starting the program, the 'Thank you for playing' message would be shown despite the user not having played a game.  This was because I had put the code for the message in the goodbye function.  On realising this, I moved the code from the goodbye function and added a separate 'thanks' function which would be called only if the player had played a game and then decided not to play again.  A quick resolve.

* I also realised that many people who played the game were not entirely sure of how to create a winning path.  I had feedback that a horizontal, or vertical path had been identified, but this had not won the game.  Unfortunately as explained in the scope section of this README file, it was out of scope at this stage of development to be able to win the game any other way than a horizonatal row.  I therefore decided to re-iterate the rules on the game-board screen and re-word the rules slightly in the hope that they would be made clearer.  I also decided to increase the number of poos from 7 to 13 in the hope that this would decrease the liklihood of a non-winning clear path being discovered vertically or diagonally and hopefully preventing any confusion.

### PEP8 Online Validation

<details>
<summary>PEP8 Online Results for run.py file </summary>
<br>

![PEP8 Results - run.py](assets/docs/testing/pep8-1.png)
</details>

<br>

<details>
<summary>PEP8 Online Results for gameboard.py file</summary>
<br>

![PEP8 Results - gamboard.py](assets/docs/testing/pep8-2.png)

</details>

<br>

### Development

The project was written and tested using [Gitpod](https://gitpod.io/).

The project uses [Github](https://github.com/) for utilising git version control.

The project was deployed via [Heroku](https://id.heroku.com/).

This project has been written using [Python3](https://www.python.org/downloads/)


### Libraries Used

* Pyfiglet
    - This was used to create the ASCII style text for the welcome page, headings and win/lose screens.

* Random:
    - randint was used to generate a random number between 0 and 8 to choose a random row that would be the winning path for that game.  It was also used to create random coordinates where the poos would be placed. 

* OS:
    - system used together with the clear/cls command to clear the terminal window of all previous data.  This helps to provide a smooth transition when the board updates and gives the effect that only one tile is changing rather than the whole board being generated again. 

* Time:
    - sleep was used to create a pause between the user being informed if their choice revealed a poo or a clear path and the game-board being updated. 

### Deployment

This app has been deployed via [Heroku](https://www.heroku.com/) and the live link can be found here: [DON'T STEP IN THE POOP](https://dont-step-in-the-poop.herokuapp.com/)


The following steps were followed to deploy to Heroku:

1. Visit [Heroku](https://www.heroku.com/) and log-in or create a new account.
2. Click the 'New' button.
3. Select the option to 'Create new app'.
4. Give the app a unique name.  Heroku will advise you if the name is available or not.  The unique name for this app is dont-step-in-the-poop.  Names should consist of only lower-case letters, numbers and dashes.
5. Select the appropriate region.
6. Click 'Create App'.  This will create your app in Heroku and take you to the app dashboard. 
7. Navigate to the settings tab and scroll down to 'Config vars'.  For KEY enter PORT and VALUE enter 8000.  Click the 'Add' button
8. Scroll down to 'Buildpacks' and click the 'Add Buildpack' button.  Firstly select 'python' and save changes.  Repeat, this time selecting 'node.js' and saving changes.  Make sure your buildpacks show in the correct order once selected, with Python being first in the list and node.js second.  If they are not in the correct order, you can drag and drop as required.
9. Use the menu at the top of the page to navigate to the 'Deploy' tab.
10. Select Github as the deployment method and then confirm you want to connect to Github by pressing the 'Connect to Github' button. 
11. Search for the Github Repository using the search field and click 'Search'. 
12. Click 'Connect' next to the correct Github repository. 
13. Once your repsitory is connected to Heroku, you can enable automatic deploys using the 'Enable Automatic Deploys' button or manually deploy  by selecting the branch to deploy following by the 'Deploy Branch' button. 
14.  If you choose to automatic deploys, Heroku will build a new version of the app whenever a change is pushed to Github.  Manually deploys allows you to update the app whenever you click the 'Deploy Branch'.   For this project I enabled automatic deploys to ensure the app was updated each time changes were pushed to Github.
15. When the build process is complete you will be able to view the live app by clicking the link 'Your app was successfullly deployed".

## Credits & References

### Code

Other than the below exceptions, all of the code has been custom written by myself for the application:-

1. When researching how to clear the screen when running a python program, I came across the following code from the [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/) website.  This code also included the sleep function from the time library which I have also used in this project.

```
# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

# print out some text
print('hello geeks\n'*10)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()

```

2. From the same website I also found guidance on how to use the pyfighlet library to style text within the console:


```
# import pyfiglet module
import pyfiglet

result = pyfiglet.figlet_format("Geeks For Geeks")
print(result)
``` 

3. My validate_input function was adapted from the code used in the [Code Institue's](https://codeinstitute.net/) Love Sandwiches code-along project.  I have detailed both functions below and you can see the similarities and differences betweeen the two. 

Code Institutes Validation Function:
```
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

```

My Validation Function:

``` 
def validate_input(value):
    """ Validates user input for row/column

    Within the first try statement, converts the row/column value entered
    into an integer.   Returns an error if value entered is not a number.

    Within the second try statement, returns an error if the number
    is not within the range 0-8
    """
    try:
        value = int(value)
    except ValueError:
        print(f"Invalid data: {value} is not a number")
        return False

    try:
        if value not in range(8):
            raise ValueError(f"Please choose a number between 0 and 7."
                             f"You entered: {value}")
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.")
        return False
    return True
```
4. As mentioned in the issues section, I adapted code I had seen on Stack Overflow to convert the elements in a tuple from strings to integers - Thanks Gusev Slava

![List Comprehension for converting elements in a tuple from strings to integers](assets/docs/screenshots/stackoverflow.png)


### ASCII Art & Imagery 

Background image created using [flaticon](https://www.flaticon.com/).

Poop ASCII Art from user [pr0p3rno0b10](https://replit.com/@pr0p3rno0b10/poop-emoji-ascii-art) on Replit.

Smiley face ASCII are from [loveascii.com](http://loveascii.com/smilies.html)

Poo image for favicon from [Pixabay](https://pixabay.com/)


### Acknowledgments

* Firstly the ultimate thanks goes to [Dave Horrocks](https://github.com/DaveyJH) for being an absolute legend.  His support and encouragement is incredibly appreciated and he has been there (no matter the ungodly hour!) to listen to me think out loud on many, many occassions.  His constant reminders to tackle the code line by line and to just 'try it', have given me more confidence in my abilities than if I hadn't had his support and I am very grateful for his thorough explanation of Python classes!
* Thanks also to [David Bowers](https://github.com/dnlbowers) for his words of encouragment when starting out with this project, his help with creating a 2D array and for helping me get my Favicon working.
* Thanks to [Chris Williams](https://github.com/Chr15w1986) for his encouragement and support.  It's been nice knowing that we have the same deadlines we are working towards and the same time-restrictions due to the responsibilities of working, raising children and studying.  Thanks for checking in and letting me vent, without judgement :)
* Thanks to my mentor Brian O'Hare for talking me out of requesting an extension for this project, his guidance and insight.
* Thanks to the awesome Slack community for pointing me in the right direction when I've put out a plea for help.
* Thanks to my daughters for understanding that 'Mummy is working right now and can't play until later'.
* Thanks to my husband for keeping the house in good nick and providing hot meals whilst I devote every minute I can to upskilling.
