from naive_algorithm import find_substring_positions
import csv

with open('naive_algo_in.csv', 'r') as file:
    reader = csv.reader(file)
    data = []
    for line in file:
        data.append(line)
    my_string, my_pattern = data[0], data[1]

if __name__ == '__main__':
    result = 'Substrings fround at positions: {}'.format(find_substring_positions(my_string, my_pattern))
    print(result)
    with open('naive_algo_out.csv', 'w') as file:
        writer = csv.writer(file)
        file.write(result)