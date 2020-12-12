import math as m

x = None
n = None
breakings = []


def find_min_number(X, N):
    try:
        int(N)
    except ValueError:
        raise TypeError('N must be an integer')
    if any(elem not in ['0', '1'] for elem in X):
        raise TypeError('The sequence must contain only 1s and 0s')
    if len(X) not in range(1, 100) or int(N) not in range(1, 100):
        raise ValueError('The length of the sequence and the number must be in range 1..99')

    global breakings, n, x
    n = N
    x = X
    if x[0] == '0':
        return -1
    if int(n) == 1:
        if '0' in x:
            return -1;
        else:
            return len(x)
    if check_power(x):
        return 1
    breakings = [float('inf') for i in x]
    cut_sequence(x)
    return breakings[-1]


def cut_sequence(x):
    for i in range(len(x)):
        sub_sequence = x[:i + 1]
        if check_power(sub_sequence):
            breakings[i] = 1
        elif len(sub_sequence) > 1:
            for j in range(len(sub_sequence) - 1, 0, -1):
                right = sub_sequence[j:]
                if breakings[j - 1] > 0 and check_power(right):
                    breakings[i] = min(breakings[i], breakings[j - 1] + 1)
                    if breakings[i] == 2:
                        break
            if breakings[i] == float('inf'):
                breakings[i] = -1
        else:
            breakings[i] = -1


def check_power(byte_number):
    global n
    if byte_number[0] == '0':
        return False
    n = int(n)
    number = int(byte_number, 2)
    return float("{:.14f}".format(m.log(number, n))).is_integer()
