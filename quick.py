#quick sort in python

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[low], arr[right] = arr[right], arr[low]
    return right

# Driver code to test the algorithm
arr = [9, 1, 13, 8, 100, 76]
n = len(arr)

print("Given array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")

quick_sort(arr, 0, n - 1)

print("\n\nSorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
