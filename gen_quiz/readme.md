This script defines a function `gen_quiz` that generates a quiz based on a question pool and specific indexes. Here's a breakdown of its functionality:

- **gen_quiz**: This function takes a question pool, a variable number of indexes to select questions from the pool, and an alternative code set for labeling answers. It generates a quiz by selecting questions from the pool based on the provided indexes and formats the answers using the alternative codes.

    - It initializes an empty list `quiz` to store the quiz questions and answers.
    - It iterates over the provided indexes:
        - For each index, it attempts to retrieve the corresponding question and its answers from the question pool.
        - It formats the answers using the alternative codes provided and adds them to the `quiz` list.
        - If the index is out of range or if any other error occurs, it prints a message and continues to the next index.
    - It returns the generated quiz.

The script also includes doctests to verify the correctness of the gen_quiz function for various scenarios, such as selecting specific questions from the pool, using alternative codes for answers, and handling errors gracefully.