def find_substring_positions(input_str, pattern_str):
    if type(input_str) != str or type(pattern_str) != str:
        raise TypeError('The input string and the pattern must be string type')
    input_str = input_str.lower()
    pattern_str = pattern_str.lower()
    pattern_len = len(pattern_str)
    input_len = len(input_str)
    if input_len < pattern_len or pattern_len == 0 or input_len == 0:
        raise ValueError('The input string and pattern lengths must have al least 1 character;'
                         'the input string cannot be shorter than the pattern')
    index_list = []

    for i in range(input_len - pattern_len + 1):
        j = 0
        while j < pattern_len:
            if input_str[i + j] != pattern_str[j]:
                break
            j += 1

        if j == pattern_len:
            index_list.append(i)

    return index_list
