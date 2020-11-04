from find_lenght_algorithm import find_side_length
import csv

with open('bugtrk_in.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        N, W, H = row

if __name__ == '__main__':
    side_length = find_side_length(int(N), int(W), int(H))
    print(side_length)

    with open('bugtrk_out.csv', 'w') as file:
        writer = csv.writer(file)
        file.write(str(side_length))