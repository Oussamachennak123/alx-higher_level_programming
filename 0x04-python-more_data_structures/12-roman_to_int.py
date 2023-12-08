#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    dice = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    som = 0
    prev_value = 0
    for char in roman_string:
        if char in dice:
            current_value = dice[char]
            if current_value > prev_value:
                som += current_value - 2 * prev_value
            else:
                som += current_value
            prev_value = current_value
        else:
            return 0
    return som
