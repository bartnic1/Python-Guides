import shelve

with shelve.open("cave data") as data:
    loc = 1
    while True:
        availableExits = ", ".join(data["locations"][loc]["exits"].keys())

        print(data["locations"][loc]["desc"])

        if loc == 0:
            break
        else:
            allExits = data["locations"][loc]["exits"].copy()
            allExits.update(data["locations"][loc]["namedExits"])

        direction = input("Available exits are " + availableExits + ". Where do you wish to go? ").upper()
        print()

        # Parse the user input, using our vocabulary dictionary if necessary
        if len(direction) > 1:  # more than 1 letter, so check vocab
            words = direction.split()
            for word in words:
                if word in data["vocabulary"]:   # does it contain a word we know?
                    direction = data["vocabulary"][word]
                    break

        if direction in allExits:
            loc = allExits[direction]
        else:
            print("You cannot go in that direction")