def bubble_sort(unsorted_list):
    for i in range(0, len(unsorted_list)-1):
        for j in range(0, len(unsorted_list)-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp
                                
if __name__ == '__main__':
    unsorted = [5,3,4,7,2]
    bubble_sort(unsorted)
    print(list(unsorted))
    