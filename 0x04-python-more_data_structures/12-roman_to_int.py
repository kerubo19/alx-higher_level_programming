#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(roman_string) - 1, -1, -1):
        current = roman_string[i]
        previous = roman_string[i - 1] if i > 0 else None
        current_value = roman_dict.get(current, 0)
        previous_value = roman_dict.get(previous, 0)
        if current_value >= previous_value:
            result += current_value
        else:
            result -= current_value
    return result
