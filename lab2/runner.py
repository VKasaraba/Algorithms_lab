from algorithm import find_side_lenght
import csv

with open('bugtrk_in.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        N, W, H = row

if __name__ == '__main__':
    side_lenght = find_side_lenght(int(N), int(W), int(H))
    print(side_lenght)

    with open('bugtrk_out.csv', 'w') as file:
        writer = csv.writer(file)
        file.write(str(side_lenght))
