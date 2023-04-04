#!/usr/bin/python3

def text_indentation(text):
    """ Prints a text with 2 new lines after specific characters """

    # checks whether text is string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # removes whitespace from text
    text = text.strip()

    # print text 
    string = ""
    for letter in text:
        string += letter
        if letter == '.' or letter == '?' or letter == ':':
            string += "\n\n"
        print(string)
        string = ""
