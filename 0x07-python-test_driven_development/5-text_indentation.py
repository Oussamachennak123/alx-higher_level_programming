#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    o = 0
    while o < len(text) and text[o] == ' ':
        o += 1

    while o < len(text):
        print(text[o], end="")
        if text[o] == "\n" or text[o] in ".?:":
            if text[o] in ".?:":
                print("\n")
            o += 1
            while o < len(text) and text[o] == ' ':
                o += 1
            continue
        o += 1
