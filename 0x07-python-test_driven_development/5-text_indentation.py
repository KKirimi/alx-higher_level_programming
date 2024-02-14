s text_indentation
prints a text with 2 new lines after . ? and :
"""


def text_indentation(text):
    """
    prints a text
    args:
        text(string)
    no space at the beginning or end of each printed line
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for dlim in ".:?":
        text = (dlim + "\n\n").join(
            [line.strip(" ") for line in text.split(dlim)])

    print(f"{text}", end="")
