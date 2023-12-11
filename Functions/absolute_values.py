# Define a function
def absolute_values(a: list):
    """"
    Function return the absolute float values
    from a list with numbers

    Parameters: list(with numbers)

    Returns the list with the absolute values of the numbers
    """
    result_list = []
    for number in a:
        result_list.append(abs(float(number)))
    return result_list

# Read User input
float_list = input().split()

# Call the function and print its result
print(absolute_values(float_list))