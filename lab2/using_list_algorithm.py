N = 10
W = 2
H = 3


def find_side_lenght(N, W, H):
    array = [1]
    index = 1

    total_width = W
    total_hight = H
    for i in range(1, N):
        if total_width + W < total_hight + H:
            if index < len(array):
                array[index] += 1
                index += 1
            else:
                array.append(1)
        else:
            if index < len(array) and array[index] < array[index - 1]:
                array[index] += 1
                if array[index] == array[index - 1]:
                    index += 1
            else:
                array[0] += 1
                index = 1

        total_width = len(array) * W
        total_hight = array[0] * H

    if total_width > total_hight:
        return total_width
    else:
        return total_hight


print(find_side_lenght(N, W, H))
