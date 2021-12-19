def colorize(text,color):

    colors = ["red", "yellow", "blue", "green"]

    if type(text) is not str:
        raise TypeError("text must be str")

    if color not in colors:
        raise ValueError("invalid color")


    print(f"printed{text} in {colors}")


colorize("three","blue")