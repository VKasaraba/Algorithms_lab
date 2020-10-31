from linkedlist import LinkedList


def find_side_lenght(N, W, H):
    if (type(N) or type(W) or type(H)) not in [int, float]:
        raise TypeError('The input must be positive numbers')
    if N == 0:
        return 0
    if N < 0 or W <= 0 or H <= 0:
        raise ValueError('The number/width/height must be a positive value')

    linked_list = LinkedList()
    linked_list.add_to_end(1)
    index = 1

    total_width = W
    total_hight = H
    for i in range(1, N):
        if total_width + W < total_hight + H:
            if index < linked_list.length:
                linked_list.get_node(index).value += 1
                index += 1
            else:
                linked_list.add_to_end(1)
        else:
            if index < linked_list.length and linked_list.get_node(index).value < linked_list.get_node(index-1).value:
                linked_list.get_node(index).value += 1
                if linked_list.get_node(index).value == linked_list.get_node(index-1).value:
                    index += 1
            else:
                linked_list.get_node(index=0).value += 1
                index = 1

        total_width = linked_list.length * W
        total_hight = linked_list.get_node(index=0).value * H

    if total_width > total_hight:
        return total_width
    else:
        return total_hight