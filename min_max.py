#find min and max from array (ITERVATIVE METHOD)

def find_max_min(arr):
    if not arr:
        return None, None

    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num


array = [10, 5, 20, 3, 15]
max_num, min_num = find_max_min(array)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
