import random

arr_x = []
arr_y = []

for i in range(0, 20):
    arr_x.append(random.randrange(0, 100))

for i in range(0, 15):
    arr_y.append(random.randrange(0, 100))

len_x = len(arr_x)
len_y = len(arr_y)

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index

def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

quickSort(arr_x, 0, len_x-1)
quickSort(arr_y, 0, len_y-1)

print(arr_x)
print(arr_y)

def merge_sorted_arrays(arr_1, arr_2):
    merged_array = []
    i1 = 0
    i2 = 0
    while i1 < len(arr_1) and i2 < len(arr_2):
        if arr_1[i1] < arr_2[i2]:
            merged_array.append(arr_1[i1])
            i1 += 1
        else:
            merged_array.append(arr_2[i2])
            i2 += 1
    for i in range(i1, len(arr_1)):
        merged_array.append(arr_1[i])
    for i in range(i2, len(arr_2)):
        merged_array.append(arr_2[i])

    return merged_array

print(merge_sorted_arrays(arr_x, arr_y))