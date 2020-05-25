
## insert sorting 插入排序 ##
def insert_sort(array):
    length = len(array)

    for i in range(1,length):  ## 选取一个新对象
        for j in range(0,i):  ## 新对象 已排序的逐一进行比较
            
            if array[i-j]<array[i-j-1]:
                array[i-j],array[i-j-1] = array[i-j-1],array[i-j]
            else:
                break 
    return array

## time complexity O(N) ~ O(N^2)
## space complexity N

# print(insert_sort(arrange(10)))