# TO-DO: Complete the selection_sort() function below

# time O(n^2) space O(1)


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
# time O(n^2) space O(1)
def bubble_sort(arr):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False

        counter += 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr):

    minimum = arr[0]

    counter_dictionary = {}

    for element in arr:
        if hasattr(counter_dictionary, f"{element}"):
            counter_dictionary[element] += 1
        else:
            counter_dictionary[element] = 1

        if element < minimum:
            minimum = element

    print(counter_dictionary)
    print(minimum)  # the minimum value in arr

    for i in range(len(arr) - 1):
        if counter_dictionary[minimum] > 0:
            arr[i] = minimum
            counter_dictionary[minimum] -= 1
        minimum += 1

    return arr
