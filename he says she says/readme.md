This script contains two functions:

1. **she_says_he_says**: This function takes a string representing what "she says," replaces 'y' with 'i', removes spaces, and returns the reversed string.

    - It replaces 'y' with 'i', removes spaces, and reverses the resulting string.
    - Example:
        ```python
        she_says_he_says('ma rymu')  # Returns: 'umiram'
        ```

2. **solfege**: This function partitions an input string into an optional title, ': ', and a hymn. It then extracts every third word from the hymn (starting from the first word), skipping two words in between, and returns these words as a string with ', ' as a separator.

    - It first partitions the input string to extract the hymn portion.
    - It splits the hymn into a list of words.
    - It extracts every third word from the list, skipping two words between each, and joins these words with ', ' as a separator.
    - Example:
        ```python
        solfege('Hymn of St. John: Ut queant laxis re sonare fibris mi ra gestorum fa muli tuorum sol ve polluti la bii reatum Sancte Iohannes')
        # Returns: 'Ut, re, mi, fa, sol, la'
        ```