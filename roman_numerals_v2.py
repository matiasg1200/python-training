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
    # create dictonary to map the values of roman numerals
    arabic_numbers = {
        1 : 'I' ,
        4 : 'IV',
        5 : 'V' ,
        9 : 'IX',
        10 : 'X' ,
        40 : 'XL',
        50 : 'L',
        100 : 'C',
        400 : 'CD',
        500 : 'D',
        900 : 'CM',
        1000 : 'M'
    }
    
    # Initialize the result as an empty string
    result = ""
    value = arabic_num
    
    # Iterate through the Roman mapping
    for n in reversed(arabic_numbers):
        # If the value is >= than the key of the current iteration I want to substract
        # the value of the key to the actual value and append the key of the corresponding 
        # value to the result string
        while value >= n : 
            value -= n
            result += arabic_numbers[n]

    return result



roman_num = "XXXVVIIIIIIIIII"
num = translate_number(roman_num)
print (num)
print (back_to_roman(num))

