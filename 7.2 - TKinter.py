# TKinter

# Change this to test different geometry managers

tkmethod = 4

# When you import tkinter, it allows access to the tk widget toolkit, which allows you to create GUI programs.

# TKinter actually makes use of a scripting language called TCL, but the Python interpreter (which executes code -
# distinct from the compiler which translates code into a simpler virtual machine language, or machine language) comes
# with a TCL interpreter embedded within it so you don't need to load anything extra.

# TKinter is part of the standard Python library; unfortunately the documentation isn't so great!

# Useful links: https://docs.python.org/3/library/tk.html
# https://en.wikipedia.org/wiki/Tk_%28software%29 <-- Good history of Tk
# http://www.tkdocs.com/  <-- Very good tutorial section
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html <-- Good description of features (better than docs)

# If running Python version 2, you have to import Tkinter with a capital T. If you're not sure which version the user
# is using, you can use the following try and except lines to make sure you import the appropriate version.

import os

try:
    import tkinter
except ImportError: # Python 2
    import Tkinter as tkinter

# _test() creates a simple dialogue window to show that the GUI is working.

if tkmethod == 1:
    tkinter._test()
    print(tkinter.TkVersion)
    print(tkinter.TclVersion)
elif tkmethod == 2:
    # Another way to test it:
    mainWindow = tkinter.Tk()
    # The title for the main window exists in the white bar at the top.
    mainWindow.title("Hello World")
    # 640x480 is the resolution. The first plus is the number of pixels right; the second is the number of pixels down.
    mainWindow.geometry('640x480+500+300')
    # The following mainloop() method passes control to TKinter and allows it to generate a window. This should be
    # the last entry.

    # Everything in TK is a hierarchy and must be based on a root window. Not every window can have a child, but all
    # windows need a parent/master window.

    # Using special geometry managers (the most useful being the grid manager), you can add widgets to the screen.
    # Will start with the most common managers, called the pack manager. Within this, will use the canvas widget.

    # The tkinter.Label method creates a "hello world" title. The pack method places it just below the mainwindow title.
    label = tkinter.Label(mainWindow, text="Hello World")
    label.pack(side='top')

    # If you set the fill parameter to tkinter.X, it expands the canvas to the middle of the window. If you set it
    # to tkinter.Y, it expands it vertically to the top of the window. Use tkinter.BOTH to expand along both axes.
    # To fully expand along the X axis, use expand=True.

    # Note that the degree of expansion depends on what the side parameter is. If you set it to 'top' as opposed to
    # 'left', the fill parameters are switched.

    leftFrame = tkinter.Frame(mainWindow)
    leftFrame.pack(side='left', anchor='n', fill=tkinter.Y)

    # Change the first parameter (either mainWindow or leftFrame in this case) to determine which window the canvas
    # should exist in. Expand=False is the default value.

    canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
    canvas.pack(side='left', fill=tkinter.BOTH, expand=False, anchor='n')

    rightFrame = tkinter.Frame(mainWindow)
    rightFrame.pack(side='right', anchor='n', expand=True)

    # Buttons. If you set the side to be 'left', then the anchor can only modify the vertical positioning; the 'e' or
    # 'w' is overrided by the pack order. Note you can also use 'nw' or other intermediate points on the compass.

    button1 = tkinter.Button(rightFrame, text="Button 1")
    button2 = tkinter.Button(rightFrame, text="Button 2")
    button3 = tkinter.Button(rightFrame, text="Button 3")

    # button1.pack(side='top', anchor='n')
    # button2.pack(side='top', anchor='s')
    # button3.pack(side='top', anchor='e')

    button1.pack(side='top')
    button2.pack(side='top')
    button3.pack(side='top')

    mainWindow.mainloop()

# When widgets (like buttons, and canvases) share the same side they're placed adjacent to each other in the order that
# they are packed from chosen side.

# From the above example, pack is one of the simplest geometry managers included in Tkinter.

# -------------------------------------------------------------------------------------------------------------------- #

elif tkmethod == 3:
    mainWindow = tkinter.Tk()

    mainWindow.title("Hello World")
    mainWindow.geometry('640x480-8-200')

    label = tkinter.Label(mainWindow, text="Hello World")
    label.grid(row=0, column=0)

    leftFrame = tkinter.Frame(mainWindow)
    leftFrame.grid(row=1, column=1)

    canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
    canvas.grid(row=1, column=1)

# Sticky has the same functionality as anchor point did with the pack geometry manager.

    rightFrame = tkinter.Frame(mainWindow)
    rightFrame.grid(row=1, column=2, sticky='n')

    button1 = tkinter.Button(rightFrame, text="Button 1")
    button2 = tkinter.Button(rightFrame, text="Button 2")
    button3 = tkinter.Button(rightFrame, text="Button 3")
    button1.grid(row=0, column=0)
    button2.grid(row=1, column=0)
    button3.grid(row=2, column=0)

# Configure the columns. Note that if you control+click on column configure, it shows that in the source code it is
# equal to grid_columnconfigure, so you can user either one. The instructor prefers the one that needs less typing.

# If you don't specify column width, they default to the minimum size needed to fit the objects inside.

    mainWindow.columnconfigure(0, weight=5)
    mainWindow.columnconfigure(1, weight=1)
    mainWindow.grid_columnconfigure(2, weight=1)

# If you set the sticky to 'ns', then the object (frame, or button) will expand to fill the vertical direction.
# Similarly, if you set it to 'ew' it will try to fill the horizontal direction.

    leftFrame.config(relief='sunken', borderwidth=1)
    rightFrame.config(relief='sunken', borderwidth=1)
    leftFrame.grid(sticky='ns')
    rightFrame.grid(sticky='new')

# Note that in order for the button to expand along the horizontal axis, you need to also change the weighting of the
# right frame's column.

    rightFrame.columnconfigure(0, weight=1)
    button2.grid(sticky='ew')

    mainWindow.mainloop()

# -------------------------------------------------------------------------------------------------------------------- #

elif tkmethod == 4:
    mainWindow = tkinter.Tk()

    mainWindow.title("Grid Demo")
    mainWindow.geometry('640x480-8-200')
    mainWindow['padx'] = 8

    label = tkinter.Label(mainWindow, text='Tkinter Grid Demo')
    label.grid(row=0, column=0, columnspan=3)

    # Increasing the weight for a particular column/row means that, as you expand the window, that column/row expands
    # faster relative to the others. Note this also means that it shrinks faster when you reduce the window size.

    # For rows you want to keep close together (i.e. title of text box and the text box) its recommended to use
    # low weights, and also for titles.

    # Note that you *need* to configure the columns/rows if you want them to expand or contract when the window is being
    # resized!

    mainWindow.columnconfigure(0, weight=100)
    mainWindow.columnconfigure(1, weight=1)
    mainWindow.columnconfigure(2, weight=1000)
    mainWindow.columnconfigure(3, weight=600)
    mainWindow.columnconfigure(4, weight=1000)
    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=10)
    mainWindow.rowconfigure(2, weight=1)
    mainWindow.rowconfigure(3, weight=3)
    mainWindow.rowconfigure(4, weight=3)

    fileList = tkinter.Listbox(mainWindow)
    fileList.grid(row=1, column=0, sticky='news', rowspan=2)
    # Remember that there are many different relief types beyond 'sunken'!
    fileList.config(border=2, relief='sunken')

    # The default directory is C:. Thus by including '/...' as an argument, you change the directory to "C:/...".
    # Note that by entering 'D:/', Python will open the D drive too!
    for zone in os.listdir('D:/'):
        fileList.insert(tkinter.END, zone)

    # The first line creates a scrollbar in the main window, oriented vertically, with command set to the yview
    # method of the listbox named "fileList". Yview is used to query and change the vertical position of the view -
    # press control + click on yview to learn more.

    # Here the method is being assigned to an aspect of the listbox, so that every time yscrollcommand occurs, the
    # method is called.

    listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
    listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
    fileList['yscrollcommand'] = listScroll.set

    # Frame for the radio buttons. Note LabelFrame is distinct from Label in that the label is embedded in the frame.
    optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
    optionFrame.grid(row=1, column=2, sticky='ne')

    # Make three radio buttons that all share the same variable
    rbValue = tkinter.IntVar()
    rbValue.set(1)
    # Radio buttons
    radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
    radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
    radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)

    radio1.grid(row=0, column=0, sticky='w')
    radio2.grid(row=1, column=0, sticky='w')
    radio3.grid(row=2, column=0, sticky='w')

    # Widget to display the result
    resultLabel = tkinter.Label(mainWindow, text='Result')
    resultLabel.grid(row=2, column=2, sticky='nw')
    result = tkinter.Entry(mainWindow)
    result.grid(row=2, column=2, sticky='sw')

    # Frame for the time spinners
    timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
    timeFrame.grid(row=3, column=0, sticky='new')
    # Time Spinners. You can use from_ and to as an alternate way of entering the time range; when specifying the
    # upper bound (to), the range includes this number, as opposed to range which excludes it.
    # from_ is a reserved word in Python.
    hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
    minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
    secondSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 60)))
    hourSpinner.grid(row=0, column=0)
    tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
    minuteSpinner.grid(row=0, column=2)
    tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
    secondSpinner.grid(row=0, column=4)

    timeFrame['padx'] = 36

    # Frame for the date spinners
    dateFrame = tkinter.Frame(mainWindow)
    dateFrame.grid(row=4, column=0, sticky='new')
    # Date Labels
    dayLabel = tkinter.Label(dateFrame, text='Day')
    monthLabel = tkinter.Label(dateFrame, text='Month')
    yearLabel = tkinter.Label(dateFrame, text='Year')
    dayLabel.grid(row=0, column=0, sticky='w')
    monthLabel.grid(row=0, column=1, sticky='w')
    yearLabel.grid(row=0, column=2, sticky='w')

    # Date Spinners

    daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
    monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                                                            "Sep", "Oct", "Nov", "Dec"))
    yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
    daySpin.grid(row=1, column=0)
    monthSpin.grid(row=1, column=1)
    yearSpin.grid(row=1, column=2)

    # Buttons

    # If you set command=mainWindow.quit(), you're assigning that null value to the command, so it doesn't do anything.
    # While the quit method does run during assignment, since the mainloop hasn't started, it has no effect.
    # If you set command=mainWindow.destroy(), then the destroy() method destroys the cancel button immediately, so that
    # the button command can't be assigned.

    # To remedy this, you either set command=mainWindow.destroy or command=mainWindow.cancel. This ensures that you
    # only call the method when the button is clicked, rather than assigning what the method returns and running it only
    # once.

    # Separately, because row height is determined by the height of the buttons, you don't need to use 'ns' as the
    # sticky entry.

    okButton = tkinter.Button(mainWindow, text='OK')
    cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.quit)
    okButton.grid(row=4, column=3, sticky='e')
    cancelButton.grid(row=4, column=4, sticky='w')

    mainWindow.mainloop()

    # Prints selected radio button value after closing the program
    print(rbValue.get())
