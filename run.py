from random import randrange
import pyfiglet


def start_game():
    """
    Opens the title screen, requests players name and asks if player
    would like to see view rules and story.
    """
    print("\U0001f4a9" * 26)
    title = pyfiglet.figlet_format("DONT STEP\nIN THE\nPOOP")
    print(title)
    print("\U0001f4a9" * 26)

    name = input("Please enter your name: ")
    rules_response = input("Hi " + name + ". Would you like to see "
                           "the game rules & backstory? Enter y/n \n").lower()

    while rules_response not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        rules_response = input("Hi " + name + ". Would you like to see "
                               "the game rules & backstory? "
                               "Enter y/n \n").lower()

    if rules_response == 'y':
        game_rules()
    elif rules_response == 'n':

        ready_to_play = input("Are you ready to play? y/n \n").lower()

        while ready_to_play not in ('y', 'n'):
            print("You have made an incorrect selection. Please try again\n")
            ready_to_play = input("Are you ready to play? y/n \n").lower()

        if ready_to_play == 'y':
            open_game_board()
        if ready_to_play == 'n':
            print("You said NO!  Goodbye for now.\n")
            print("\U0001f4a9" * 22)
            result = pyfiglet.figlet_format("GOODBYE")
            print(result)
            print("\U0001f4a9" * 22)
            exit()


def game_rules():
    """
    Displays game rules to user.
    Accepts user input and calls game function if user is
    ready to play.
    """
    print("\U0001f4a9" * 22)
    print(" \n")
    story = pyfiglet.figlet_format("                STORY", font="digital")
    print(story)
    print(" \n"
          "Hello Postie!  I see you have some very important \n"
          "letters to deliver! \U0001f4ec \n"
          " \n"
          "Unfortunately, some very naughty pooches \U0001f415 have also \n"
          "made a few deliveries at this house. \U0001f4a9 \n"
          " \n"
          "Can you make it across the garden without stepping \n"
          "in that stinky dog poop? \n"
          " \n")
    rules = pyfiglet.figlet_format("                RULES", font="digital")
    print(rules)
    print(" \n"
          "Make a  horizontal path across the garden using\n"
          "the numbers on your keypad to select the row\n"
          "and column you would like to try first. \n"
          "If the tile you pick does not contain poo, the tile will be\n"
          "replaced with a shoe. \U0001f97e \n"
          " \n"
          "If you step in poo it will be replaced with.... well you know... \n"
          "and you will need to try and make a new path! \n"
          " \n")
    print("\U0001f4a9" * 22)

    ready_to_play = input("Are you ready to play? y/n \n").lower()

    while ready_to_play not in ('y', 'n'):
        print("You have made an incorrect selection. Please try again\n")
        ready_to_play = input("Are you ready to play? y/n \n").lower()

    if ready_to_play == 'y':
        open_game_board()
    elif ready_to_play == 'n':
        print("You said NO!  Goodbye for now.\n")
        print("\U0001f4a9" * 22)
        result = pyfiglet.figlet_format("GOODBYE")
        print(result)
        print("\U0001f4a9" * 22)
        exit()


def open_game_board():
    """
    Opens game board ready to play or something like that
    """
    print("\U0001f4a9" * 22)
    print(" \n")
    game_board = pyfiglet.figlet_format("          GAME-BOARD", font="digital")
    print(game_board)
    print(" \n"
          "Top left corner is row 0, col 0.\n"
          "Bottom right corner is row 7, col 7.\n"
          "Make a clear path from left to right \n"
          "across the garden without stepping in dog poop! \U0001f4a9\n"
          "Good luck!")
    print("\U0001f4a9" * 22 + " \n")

    rows = (8)
    cols = (8)
    board = [["\U0001f7e9" for i in range(cols)] for j in range(rows)]

    for row in board:
        print("".join(row))


def validate_choice(user_choice):
    while True:
        choice = int(input(f"Choose a {user_choice} "))

        if validate_input(choice):
            print("it works")
            break
    return choice


def set_up_game():
    """
    Selects a random row as a clear path through the board.
    Distributes a poo randomly to each other row.
    """

    clear_path = randrange(0, 8)
    print(clear_path)

    poos = []
    for i in range(8):
        if i != clear_path:
            poos.append((i, randrange(0, 8)))
    print(poos)

    flat_poos = 0
    player_guess = []

    while flat_poos < 7:

        coord = (validate_choice("row \n"), validate_choice("column \n"))

        while coord in player_guess:
            print("DUH... you've already guessed that!! Try again")
            coord = (validate_choice("row \n"), validate_choice("column \n"))

        player_guess.append(coord)

        if coord in poos:
            print("What a mess!!!")
            flat_poos = flat_poos + 1
            print(flat_poos)
        else:
            print("Phew, no poo there!!")
        print(player_guess)


def validate_input(value):
    """
    Checks that the value entered is within
    the range 0-7
    """
    try:
        if value not in range(8):
            raise ValueError(
                f"Please choose a number between 0 and 7. You entered: {value}"
            )
    except ValueError as error:
        print(f"Invalid Data {error}. Please try again. ")
        return False

    return True


start_game()
set_up_game()
