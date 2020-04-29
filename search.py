#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # if we hit the end, return nothing
    # if location arr[loc] is the item, return the location
    # to move through, call function
    end = len(array)-1
    if index > end:
        return None
    if array[index] == item:
        return index
    if array[end] == item:
        return end
    return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    '''
    variables:
    loc = location
    end = end of array
    mid = current middle point
    '''
    loc=0
    end=len(array)-1
    while loc <= end: 
        mid = loc + (end - loc)//2; 
        if array[mid] == item: 
            return mid
        elif array[mid] < item: 
            loc = mid + 1
        else: 
            end = mid - 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left is None and right is None:
        left=0
        right =len(array)-1

    if right >= left:
        mid = left + ((right - left)//2)
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            return binary_search_recursive(array, item, left, mid-1)
        elif array[mid] < item:
            return binary_search_recursive(array, item, mid+1, right)
    return None
