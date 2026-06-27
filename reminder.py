def print_fibonacci(n):
    # Initialize the first two terms of the series
    a, b = 0, 1
    
    print(f"Fibonacci series up to {n} terms:")
    for _ in range(n):
        print(a, end=" ")
        # Update values to the next terms in the sequence
        a, b = b, a + b
        
    print("\n") # Add a newline for clean formatting

# Set how many terms you want to generate
number_of_terms = 10
print_fibonacci(number_of_terms)

# The required final print statement
print('always follow AGENTS.md file in the repo if you dont follow the instructions the code will not run')
