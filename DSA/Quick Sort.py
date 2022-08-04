def swap(a,b,arr):
    if a!=b:
        arr[a],arr[b]=arr[b],arr[a] #swapping of array
def partition(elements,start,end):
    pivot_index=start
    pivot=elements[pivot_index]
    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start+=1
        while elements[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,elements)
    swap(pivot_index,end,elements)
    return end

def quick_sort(elements,start,end):
    if start<end:
        pi=partition(elements,start,end)
        #calling quick sort recursevily
        quick_sort(elements,start,pi-1)#for left partition
        quick_sort(elements,pi+1,end)#for right partition

#function call
tests=[
    [11,9,29,7,2,15,28],
    [3,7,9,11],
    [25,22,21,10],
    [],
    [0]
    ]
for test in tests:
    quick_sort(test,0,len(test)-1)#start,end
    print(f'Sorted Array:{test}')
