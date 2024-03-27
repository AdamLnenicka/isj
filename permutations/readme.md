In this script, there are three functions:

1. **all_permutations_substrings**: This function generates all permutations of all substrings of the input string.

    - It utilizes the `permutations` function from the `itertools` module to generate permutations of substrings of various lengths.
    - It returns a set of all generated permutations.
    
2. **match_permutations_substrings**: This function generates all permutations of all substrings of the input string and returns a set of input words that match one of the permutations.

    - It first generates all permutations of substrings using the `all_permutations_substrings` function.
    - It then calculates the intersection between the set of generated permutations and the set of input words.
    - The result is a set containing words that match one of the permutations.

3. **uniq_srt**: This function takes an input sequence, unifies it, and sorts it.

    - It converts the input sequence to a set to remove duplicates.
    - It then sorts the set and returns the result as a list.

4. **uniq_orig_order**: This function takes an input sequence and returns items ordered by the order of their first appearance.

    - It utilizes a dictionary to keep track of the first appearance of each item while preserving their original order.
    - It returns the keys of the dictionary, which represent unique items in the original order.
