# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    done = True
    length = len(arr)
    while done == True:
        done = False
        for i in range(0, length - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                done = True
        length -= 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    counter_dictionary = {}

    for element in arr:
        if counter_dictionary[element]:
            counter_dictionary[element] += 1
        else:
            counter_dictionary[element] = 1

    print(counter_dictionary)

    return arr
