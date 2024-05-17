# Translate Roman number 
def translate_number (roman_num) :
    # create dictonary to map the values of roman numerals
    roman_numbers = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    result = 0
    previous = 0

    # Loop through roman number in reverse order 
    for n in reversed(roman_num) :
        value = roman_numbers[n]

        # Check value of current numenral against previous one and add 
        # or substract depending on the result. This handle cases like IX
        if value < previous :
            result -= value
        else :
            result += value
        
        previous = value

    return result


def back_to_roman(arabic_num):
    # Define the mapping of values for Roman numerals
    roman_numbers = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    # Initialize the result as an empty string
    result = ""

    # Iterate through the Roman mapping
    for value, numeral in roman_numbers:
        # Repeat the subtraction until the value is less than or equal to the input
        while arabic_num >= value:
            # Subtract the value and append the corresponding numeral to the result
            arabic_num -= value
            result += numeral

    return result



roman_num = "CXXXXX"
number = translate_number(roman_num) 
final_roman = back_to_roman(number)

print ("roman num")
print (roman_num)
print ("arabic num")
print (number)
print ("back to roman")
print (final_roman)
