import math

candidate_square_length = None
number_of_cards, card_width, card_height = 0, 0, 0


def find_side_length(N, W, H):
    global number_of_cards, card_width, card_height
    if (type(N) or type(W) or type(H)) not in [int, float]:
        raise TypeError('The input must be positive numbers')
    if N <= 0 or W <= 0 or H <= 0:
        raise ValueError('The number/width/height must be a positive value')

    number_of_cards = N
    card_width = W
    card_height = H

    max_length = max(number_of_cards * card_width, number_of_cards * card_height)
    square_length = binary_search(1, max_length)

    return square_length


def binary_search(left, rigth):
    global candidate_square_length, number_of_cards, card_width, card_height
    if rigth >= left:
        square_length = left + (rigth - left) // 2

        if number_of_cards * card_width > number_of_cards * card_height:
            matches, current, expected, number_of_gaps = fill_up_table(square_length, card_height, card_width, number_of_cards, rigth)
        else:
            matches, current, expected, number_of_gaps = fill_up_table(square_length, card_width, card_height, number_of_cards, rigth)

        if current < expected:
            return binary_search(square_length + 1, rigth)
        elif matches and number_of_gaps <= 1:
            candidate_square_length = square_length
        return binary_search(left, square_length - 1)

    return candidate_square_length


def fill_up_table(square_length, side1, side2, number_of_cards, rigth):
    number_of_gaps = 0
    matches = False
    number_of_columns = math.floor(square_length / side1)
    if number_of_columns == 0:
        return binary_search(square_length + 1, rigth)
    if square_length % side1 != 0:
        number_of_gaps += 1

    expected_number_of_rows = math.ceil(number_of_cards / number_of_columns)

    number_of_rows = math.floor(square_length / side2)
    if square_length % side2 != 0 > number_of_cards:
        number_of_gaps += 1

    if number_of_rows == expected_number_of_rows:
        matches = True

    if number_of_rows - expected_number_of_rows == 1 \
            and number_of_cards * side1 * side2 <= expected_number_of_rows * side1 * number_of_columns * side2:
        matches = True

    current = number_of_rows
    expected = expected_number_of_rows
    return matches, current, expected, number_of_gaps