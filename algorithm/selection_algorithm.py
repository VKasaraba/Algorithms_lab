ALGORITHM_NAME = 'Selection Sort'

comparison_counter = 0
exchange_counter = 0


def selection_sort(list_to_sort: [], compare_function):
    global comparison_counter
    global exchange_counter
    wall_index = 0
    while wall_index < len(list_to_sort) - 1:
        comparison_counter += 1
        smallest_index = wall_index
        current_index = smallest_index + 1
        while current_index < len(list_to_sort):
            comparison_counter += 2
            if compare_function(list_to_sort[current_index], list_to_sort[smallest_index]):
                smallest_index = current_index
            current_index += 1
        exchange_counter += 1
        list_to_sort[smallest_index], list_to_sort[wall_index] = list_to_sort[wall_index], list_to_sort[smallest_index]
        wall_index += 1
    return list_to_sort


def selection_sort_get_info(list_to_sort: []):
    sorted_list = selection_sort(list_to_sort, lambda bank_1, bank_2: bank_1.number_of_clients < bank_2.number_of_clients)
    return 'Algorithm name: {} \nNumber of comparisons: {} \nNumber of exchanges: {} \nSorted list: {}'.format(ALGORITHM_NAME, comparison_counter,
                                                                                                               exchange_counter, sorted_list)
