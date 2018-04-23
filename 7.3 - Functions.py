# Functions:
# Remember that // means you take the floor of the result. / is normal division, possibly yielding a decimal value.
# Also remember that inserting a comma into the print statement (outside of each item) spaces the items by the default
# character, which is normally a single space.

# Also on the enhanced circles and challenge video, the instructor explicitly states that "class functions are called
# methods", to help distinguish between the two.

prelimtest = False

if prelimtest:

    def python_food():
        width = 80
        text = "Spam and eggs"
        left_margin = (width - len(text))//2
        print(" "*left_margin, text)

# By default, functions return "None" if you don't explicitly include any return statements.
# print(python_food())


    def center_text(text):
        left_margin = (80 - len(str(text)))//2
        print(" "*left_margin, text)

# Call the function

    center_text('spam and eggs')
    center_text('spam, spam and eggs')
    center_text('spam, spam, spam and spam')
    center_text(12)

# 'Parameter' refers to a variable defined in the function definition. Arguments refer to the values used when the
# function is called. For example, in the center_text function, "text" would be the parameter. When this function
# is called, "spam and eggs" is the argument. So you can think of parameters as variables, and arguments as the specific
# values for these variables.

# Note in the print function docstring (ctrl + click), the first parameter is actually *args. This means it can accept
# multiple arguments, such as:

    print("first", "second", 3, 4, "spam")

# The same functionality can be extended to center_text. The parameters of print have also been included in center_text2
# so that, if the user desires, the output of the centering function can be sent to a file on the computer, for example.

basictest = False

if basictest:
    def center_text(*arguments, sep=' ', end='\n', file=None, flush=False):
        text = ''
        for arg in arguments:
            text += str(arg) + sep
        text = ''.join(list(text)[:-1])
        left_margin = (80 - len(text))//2
        print(' '*left_margin, text, end=end, file=file, flush=flush)

    center_text('first', 'second', 3, 4, 'spam', sep=":")

    with open("centered", mode='w') as centered_file:
        center_text("spam and eggs", file=centered_file)
        center_text("spam, spam and eggs", file=centered_file)
        center_text(12, file=centered_file)
        center_text("spam, spam, spam and spam", file=centered_file)

        center_text("first", "second", 3, 4, "spam", sep=":", file=centered_file)

# Two functions that take exactly the same parameters are said to have the same signature.
# Modifying the above for use with a return statement:

returntest = False

if returntest:
    def center_text(*arguments, sep=' ', end='\n', file=None, flush=False):
        text = ''
        for arg in arguments:
            text += str(arg) + sep
        text = ''.join(list(text)[:-1])
        left_margin = (80 - len(text))//2
        return ' '*left_margin + text

    print(center_text("spam and eggs"))
    print(center_text("spam, spam and eggs"))
    print(center_text(12))
    print(center_text("spam, spam, spam and spam"))
    print(center_text("first", "second", 3, 4, "spam", sep=":"))

# Parabolas: To be more efficient, only need to calculate half of the domain values, since they are mirrored about
# the y axis.

from math import sin, cos, pi, sqrt

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(x):
    return (1/50)*x**2


def modparabola(page, size):
    for x in range(size):
        y = (1/size)*x**2
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, a, b):
    for angle in range(360):
        anglerad = angle*(2*pi/360)
        plot(page, a + radius*cos(anglerad), b + radius*sin(anglerad))


def instructorcircle(page, radius, g, h):
    for x in range(g, g + radius):
        y = h + (sqrt(radius**2 - ((x-g)**2)))
        plot(page, x, y)
        plot(page, x, 2*h - y)
        plot(page, 2*g - x, y)
        plot(page, 2*g - x, 2*h - y)
# pageoval works by defining the top left and bottom right corners (resp) of a rectangle. An oval is drawn to fit inside


def pageoval(page, radius, g, h, colour='red'):
    page.create_oval(g + radius, -h + radius, g - radius, -h - radius, outline=colour, width=2)


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2

# The scrollregion indicates where the two corners are at the top left and bottom right, in the form (x1,y1,x2,y2).
# Note that these coordinates are relative to an origin placed at the top left of the rectangular canvas, AND that
# the positive y axis goes down, and negative y goes up.
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
# A horizontal and vertical line are drawn to represent the x and y axes:
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
# locals() returns all of the variables that are local to the function it is called in (thus, it should be indented).
    print(locals())
# Set y to -y in the plot function so that no matter what you're plotting, you won't forget that the axes are flipped:

plotting = False

if plotting:

    def plot(canvas, x, y):
        canvas.create_line(x, -y, x + 1, -y - 1, fill='red')

    mainWindow = tkinter.Tk()
    mainWindow.title("Parabola")
    mainWindow.geometry('640x480-500-300')

# For a tkinter Canvas, the origin starts at the top left of the screen. As inserted below, the canvas will fill the
# entire screen without needing any sticky='news' statement.

    canvas = tkinter.Canvas(mainWindow, width=640, height=480)
    canvas.grid(row=0, column=0)

# repr should give the memory address where the object is stored in earlier versions of python 3 (changed now).
# print(repr(canvas), repr(mainWindow))

    draw_axes(canvas)

# Ensure parabola fits inside screen:

    i = 0
    for y in range(-100, 101):
        plot(canvas, y, parabola(y))
        i += 1
    print("Points = {}".format(i))

# The new function limits the parabola so that it only extends X pixels along the horizontal and vertical axes, where
# X is the secondary size parameter.

    modparabola(canvas, 100)
    modparabola(canvas, 200)

# Circles were drawn using your method, instructor method, and the page.create_oval method.

    pageoval(canvas, 100, 100, -100)

# On scope:
# Functions can still make use of variables defined globally in the main program. Just remember that the main
# program can not access the parameters and variables defined in the function, as they are local to that function.

    mainWindow.mainloop()

# -------------------------------------------------------------------------------------------------------------------- #

# Blackjack (keeping import of tkinter from parabola and circle section)

import random


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    # For each suit, retrieve the image for the cards:
    for suit in suits:
        # First the number cards from 1 to 10. Name refers to the directory:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        # Next the face cards:
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))

# Note: In python 3 if you mix pack and grid managers in the same container, you will get an error. However, since each
# widget serves as its own container, packing the images into the frame is okay.

# Pop is a way to retrieve and remove an item from a list (think of it as being the opposite of append). It defaults
# to removing the item from the end, but it can be specified to remove items at any point (the same is true of append).


def _deal_card(frame):
    # Pop the next card off the top of the deck (hence use 0). Jean-Paul states that it is more efficient to pop an item
    # from the end of a list rather than the beginning, so it may be better to just leave it as deck.pop().
    next_card = deck.pop(0)
    # Add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # Now return the card's face value
    return next_card


def deal_dealer():
    global dealer_wins
    global player_wins
    dealer_score = score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    while 0 < dealer_score < player_score:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_wins += 1
        dealer_wins_label.set(dealer_wins)
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
        player_wins += 1
        player_wins_label.set(player_wins)
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
        dealer_wins += 1
        dealer_wins_label.set(dealer_wins)
    else:
        result_text.set("Draw!")


# It is important to note that, if you try to set a global variable's value inside a function, Python will instead
# treat it as a local variable with the same name. You will then be shadowing the global variable name.
# Thus you can use the global tag to tell the function to use the global variable.

# However, if you are merely appending items to a list, then Python won't make that assumption and everything works.


def deal_player():
    global dealer_wins
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_wins += 1
        dealer_wins_label.set(dealer_wins)

        # Unnecessary code:

        # global player_score
        # global player_ace
        # card_value = _deal_card(player_card_frame)[0]
        # if card_value == 1 and not player_ace:
        #     player_ace = True
        #     card_value = 11
        # player_score += card_value
        # # If the player goes bust, check if there is an ace and subtract
        # if player_score > 21 and player_ace:
        #     player_score -= 10
        #     player_ace = False
        # player_score_label.set(player_score)
        # if player_score > 21:
        #     result_text.set("Dealer Wins!")

# Set up screen and frames for the dealer and player


def score_hand(hand):
    # Calculate the total score of all cards in the hand.
    # Only one ace can have the value 11, and this will reduce to one if the total score is over 21.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If the player goes bust, check if there is an ace and subtract 10:
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def shuffle():
    random.shuffle(deck)


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global deck

    dealer_hand.clear()
    player_hand.clear()

    deck = list(cards)
    random.shuffle(deck)
    result_text.set('')

    dealer_card_frame.destroy()
    player_card_frame.destroy()

    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    initial_deal()
# Something interesting about the above: If you don't destroy the frames, when you go to create new ones Python will
# automatically destroy them for you. However, if you don't explicitly destroy them, the program can sometimes
# leak memory, meaning that the memory space reserved for those objects can't be re-used until the program is restarted.


def play():
    initial_deal()
    mainWindow.mainloop()

# This if statement ensures that the game does not run on import, but will when run from blackjack.py directly:

mainWindow = tkinter.Tk()

mainWindow.title("Black Jack")
mainWindow.geometry("640x480-500-300")
mainWindow.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text, background='green', fg='white')
result.grid(row=0, column=0, columnspan=3)

# FRAMES

total_wins_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
total_wins_frame.grid(row=1, column=0, sticky='ew', rowspan=4)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background='green')
card_frame.grid(row=1, column=1, sticky='ew', columnspan=3, rowspan=2)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=4, sticky='w')

# LABELS

# Total number of wins:
dealer_wins_label = tkinter.IntVar()
tkinter.Label(total_wins_frame, text="Dealer Wins", background='green', fg='white').grid(row=0, column=0)
tkinter.Label(total_wins_frame, textvariable=dealer_wins_label, background='green', fg='white').grid(row=1,
                                                                                                     column=0)

player_wins_label = tkinter.IntVar()
tkinter.Label(total_wins_frame, text="Player Wins", background='green', fg='white').grid(row=2, column=0)
tkinter.Label(total_wins_frame, textvariable=player_wins_label, background='green', fg='white').grid(row=3,
                                                                                                     column=0)

# Total score per round:
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer Score", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player Score", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# BUTTONS

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

# This one isn't really necessary, but it was added as part of the instructions (they don't auto shuffle the deck
# when creating a new game).

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# After rewriting the functions above, the following two variables are no longer necessary. In general this tends
# to be recommended, since the code assumes that only the functions using the global variables have control. In
# the future, if this changes, the program will no longer work. Thus the code was rewritten so that only the
# functions have access to local variables.

# player_ace = False
# player_score = 0

# Note the difficulty involved in issuing a command. If you set command = _deal_card(dealer_card_frame), then you are
# setting it equal to the output of the function, and not calling the function when the button is pressed.
# If you don't include parentheses, then its difficult to specify the frame for which the card image should appear.

# Therefore, two new functions are created that take no arguments, and which assume the appropriate frame through
# an internal variable.

dealer_wins = 0
player_wins = 0
dealer_wins_label.set(dealer_wins)
player_wins_label.set(player_wins)

# Load cards
cards = []
load_images(cards)

# Create a new deck of cards and shuffle them. Note that 'cards' is already a list, so you don't need to use the
# list function (but it was there in the instructor's code).
deck = list(cards)
shuffle()

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == '__main__':
    play()

