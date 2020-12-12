import csv

from fantz import find_min_number

with open('fantz_in.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    X, N = file.readline().rsplit()


if __name__ == '__main__':
    min_number = find_min_number(X, N)
    print(min_number)

    with open('fantz_out.csv', 'w') as file:
        writer = csv.writer(file)
        file.write(str(min_number))