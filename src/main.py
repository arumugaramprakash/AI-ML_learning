def is_prime(num):
    """Check if a number is a prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(n):
    """Count and list the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    """Main function to get user input and display the results."""
    try:
        n = int(input("Enter the number of prime numbers to list: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            primes = count_primes(n)
            print(f"The first {n} prime numbers are: {', '.join(map(str, primes))}")
            print(f"Total number of prime numbers listed: {len(primes)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
