def quickSort(array):
  # 基线条件：为空或者只包含一个元素的数组是“有序”的
    if (len(array) < 2):
        return array 
    else:
        pivot = array[0] # 基准值
        less = [i for i in array[1:] if i < pivot] #由所有小于基准值的元素
        greater = [i for i in array[1:] if i > pivot] #所有大于基准值的元素
        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([10, 5, 2, 3]))
