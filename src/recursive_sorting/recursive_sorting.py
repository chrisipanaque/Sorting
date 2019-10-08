# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # while len(arrA) > 0 and len(arrB) > 0:
    #     if arrA[0] < arrB[0]:
    #         merged_arr.append(arrA.pop(0))
    #     else:
    #         merged_arr.append(arrB.pop(0))

    # return merged_arr + arrA + arrB
    m = l = r = 0
    while l < len(arrA) and r < len(arrB):
        if arrA[l] <= arrB[r]:
            merged_arr[m] = arrA[l]
            l += 1
        else:
            merged_arr[m] = arrB[r]
            r += 1
        m += 1

    while l < len(arrA):
        merged_arr[m] = arrA[l]
        l += 1
        m += 1

    while r < len(arrB):
        merged_arr[m] = arrB[r]
        r += 1
        m += 1

    return merged_arr


# list1 = [-3, 9]
# list2 = [1, 8]

# print("MERGED", merge(list1, list2))

# arr = [4, 8, 9, 1]
# print(merge_sort(arr))

# center = len(arr) // 2
# left = arr[0:center]
# right = arr[center:]

# print(left)
# print(right)


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # if len(arr) == 1:
    #     return arr

    if len(arr) > 1:
        center = len(arr) // 2
        left = arr[:center]
        right = arr[center:]
        result_left = merge_sort(left)
        result_right = merge_sort(right)
        # print(result_left)
        # print(result_right)

        arr = merge(result_left, result_right)
    return arr


print("MERGESORT", merge_sort([3, 4, 0, 8, -3, 1, 5]))

arr = [4, 8, 9, 1]
print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
