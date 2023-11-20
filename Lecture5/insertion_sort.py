def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]

        while search_index > 0 and unsorted_list[search_index-1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1

        unsorted_list[search_index] = insert_value

if __name__ == '__main__':
    unsorted = [5, 1, 100, 2, 10]
    insertion_sort(unsorted)
    print(list(unsorted))