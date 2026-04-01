def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num_1 = 10
    num_2 = 5
    
    if isinstance(num_1, (int, float)) and isinstance(num_2, (int, float)):
        result = add_numbers(num_1, num_2)
        print(f"The result of adding {num_1} and {num_2} is: {result}")
    else:
        print("Error: Inputs must be numbers.")