from algorithm.quick_sort_algorithm import quick_sort_get_info
from algorithm.selection_algorithm import selection_sort_get_info

from model.bank import Bank
import timeit


def read_from_csv(filename):
    with open(filename, 'r') as f:
        f.readline()
        objects = [Bank(*item) for item in [line.strip().split(',') for line in f.readlines()]]
    return objects


if __name__ == '__main__':
    banks_list = read_from_csv('banks.csv')

    # Selection Sort: sort by number of clients (ascending)
    start_time = timeit.default_timer()
    print(selection_sort_get_info(banks_list.copy()))
    end_time = timeit.default_timer()
    print('Execution time: {} seconds'.format(end_time - start_time))

    print('\n\n')

    # Quick Sort: sort by number of loans (descending)
    start_time_2 = timeit.default_timer()
    print(quick_sort_get_info(banks_list))
    end_time_2 = timeit.default_timer()
    print('Execution time: {} seconds'.format(end_time_2 - start_time_2))

