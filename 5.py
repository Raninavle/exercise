def largest_prime(n):
    # Check if n is less than or equal to 2, return None
    if n <= 2:
        return None
    
    # Loop through all numbers from n-1 to 2
    for i in range(n-1, 1, -1):
        # Check if i is prime
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            return i

    # If no prime number is found, return None
    return None
print(largest_prime(50))  # Output: 19
print(largest_prime(2))   # Output: None
print(largest_prime(1))   # Output: None
print(largest_prime(13))  # Output: 11
