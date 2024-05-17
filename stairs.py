def climb_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]

# Example usage:
num_steps = 1000
result = climb_stairs(num_steps)
print(f"There are {result} ways to climb {num_steps} steps.")

