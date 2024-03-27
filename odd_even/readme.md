This script consists of two functions:

1. **first_odd_or_even**: This function takes a list of integers and returns 0 under three conditions: if there are an equal number of even and odd numbers in the list, if there are only odd or only even numbers in the list, or if the list is empty. Otherwise, it returns the first odd number in the list if there are more even numbers, and the first even number if there are more odd numbers.

    - It initializes a dictionary to store counts and the first occurrence of even and odd numbers.
    - It iterates through the input list, updating counts and the first occurrence accordingly.
    - It evaluates the conditions and returns the appropriate result.
    - Example:
        ```python
        first_odd_or_even([2, 4, 2, 3, 6])  # Returns: 3
        ```

2. **to_pilot_alpha**: This function converts a word into a list of pilot alpha codes, where each letter in the word corresponds to its pilot alpha representation.

    - It initializes a list of pilot alpha codes.
    - It converts the input word to lowercase.
    - It iterates through each character in the word, converting it to its corresponding pilot alpha code and appending it to the result list.
    - Example:
        ```python
        to_pilot_alpha('Smrz')  # Returns: ['Sierra', 'Mike', 'Romeo', 'Zulu']
        ```
