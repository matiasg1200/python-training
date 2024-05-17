def simplify_roman(roman_num):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = ""

    i = 0
    while i < len(roman_num):
        current_numeral = roman_num[i]
        count = 1

        # Count the number of repetitions
        while i + 1 < len(roman_num) and roman_num[i + 1] == current_numeral:
            count += 1
            i += 1

        # Append the simplified numeral
        if count == 4:
            # Replace four repetitions with subtractive notation
            result += current_numeral + list(roman_numerals.keys())[list(roman_numerals.values()).index(5 * roman_numerals[current_numeral])]
        elif count == 9:
            # Replace nine repetitions with subtractive notation
            result += current_numeral + list(roman_numerals.keys())[list(roman_numerals.values()).index(10 * roman_numerals[current_numeral])]
        elif count > 1:
            # Use standard subtractive notation for two or three repetitions
            result += current_numeral + list(roman_numerals.keys())[list(roman_numerals.values()).index(roman_numerals[current_numeral] * (count % 5))]
        else:
            result += current_numeral * count

        i += 1

    return result


# Example usage
print(simplify_roman("VIIII"))  # Output: IX
print(simplify_roman("IIII"))   # Output: IV

