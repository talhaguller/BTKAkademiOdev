def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    a, b = 0, 1
    
    for _ in range(2, n):
        next_num = a + b
        sequence.append(next_num)
        a, b = b, next_num
    
    return sequence

print(fibonacci(5))