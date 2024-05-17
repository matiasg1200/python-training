cache = {
    1: 1,
    2: 2,
    3: 3
    }

def fibonacci_of(num):
        
    if num in cache: 
        return cache[num]
    
    cache[num] = fibonacci_of(num - 1) + fibonacci_of(num - 2)
    
    return cache[num]

print (fibonacci_of(1000))

