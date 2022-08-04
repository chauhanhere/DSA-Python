#Space complexity of this code of greater than the below code because we are storing our sorted elements in sorted_list[] variable while in below code we are changing the elements in line
def merge(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge(left)
    right=merge(right)
    return merge_Two_Sorted(left,right)

def merge_Two_Sorted(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=j=0

    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    if j<len_b:
        sorted_list.append(b[j])
        j+=1
    return sorted_list
arr=[[21,38,29,17,4,25,32,9],
    [],
    [4],
    [8,5,6],
    [62,7,4,80,34]]
for i in arr:
    print(merge(i))

'''
def merge(arr):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge(left)
    merge(right)
    merge_Two_Sorted(left,right,arr)

def merge_Two_Sorted(a,b,arr):
    len_a=len(a)
    len_b=len(b)
    i=j=k=0

    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k]=b[j]
        j+=1
        k+=1

arr=[[21,38,29,17,4,25,32,9],
    [],
    [4],
    [62,7,4,80,34]]
for i in arr:
    merge(i)
    print(i)

'''







        
