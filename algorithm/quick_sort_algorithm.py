ALGORITHM_NAME = 'Quick Sort'

comparison_counter = 0
exchange_counter = 0


def partition(list_to_sort: [], pivot_index: int, compare_function, wall_index: int):
    global comparison_counter
    global exchange_counter
    current_index = wall_index
    while current_index < pivot_index:
        comparison_counter += 2
        if compare_function(list_to_sort[current_index], list_to_sort[pivot_index]):
            comparison_counter += 1
            if wall_index != current_index:
                list_to_sort[wall_index], list_to_sort[current_index] = list_to_sort[current_index], list_to_sort[wall_index]
                exchange_counter += 1
            wall_index += 1
        current_index += 1
    else:
        list_to_sort[wall_index], list_to_sort[pivot_index] = list_to_sort[pivot_index], list_to_sort[wall_index]
        exchange_counter += 1
    return wall_index


def quick_sort(list_to_sort, pivot_index, compare_function=(lambda bank_1, bank_2: bank_1.number_of_loans > bank_2.number_of_loans), wall_index=0):
    global comparison_counter
    global exchange_counter
    comparison_counter += 1
    if wall_index >= pivot_index:
        return
    old_wall_index = partition(list_to_sort, pivot_index, compare_function, wall_index)
    quick_sort(list_to_sort, pivot_index=old_wall_index - 1, compare_function=compare_function, wall_index=wall_index)
    quick_sort(list_to_sort, pivot_index=pivot_index, compare_function=compare_function, wall_index=old_wall_index + 1)
    return list_to_sort


def quick_sort_get_info(list_to_sort):
    sorted_list = quick_sort(list_to_sort.copy(), len(list_to_sort) - 1)
    return 'Algorithm name: {} \nNumber of comparisons: {} \nNumber of exchanges: {} \nSorted list: {}'.format(ALGORITHM_NAME, comparison_counter,
                                                                                                               exchange_counter, sorted_list)
