The provided Python script includes two functions:

1. **camel_to_snake_case**: This function converts names written in camelCase to snake_case.

    - It uses a regular expression to find positions between lowercase and uppercase letters, or between sequences of uppercase letters followed by a lowercase letter.
    - It then inserts underscores (_) at these positions to convert the name to snake_case.
    - Example:
        ```python
        camel_to_snake_case('camelCaseNameAllowed')  # Returns: 'camel_case_name_allowed'
        ```

2. **not_both_titles**: This function extracts names from a string, filtering out those that are preceded by "Prof." or "Doc." and followed by ", Ph.D.".

    - It utilizes a regular expression pattern to match names that either fit the pattern of being preceded by "Prof." or "Doc." and followed by ", Ph.D.", or other names without these titles.
    - Example:
        ```python
        not_both_titles('doc. Josef Tyl, Rudolf Srp, Ph.D., Pavel Vlk, doc. RNDr. Petr Berka, Ph.D., Jan Hora')
        # Returns: ['doc. Josef Tyl', 'Rudolf Srp, Ph.D.', 'Pavel Vlk', 'Jan Hora']
        ```
