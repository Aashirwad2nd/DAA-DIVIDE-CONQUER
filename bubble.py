# Bubble sort in Python

def bubbleSort(array):
 
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [12, 45, 100, 11, 19]
print("Unsorted Array:")
print(data)
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)