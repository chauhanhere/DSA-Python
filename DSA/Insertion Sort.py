
def insertion_sort(elements):
    for i in range(1,len(elements)):
        print(i)
        anchor = elements[i]
        j=i-1
        while j>=0 and anchor <elements[j]:
            elements[j+1]=elements[j]
            j=j-1
            
        elements[j+1]=anchor #we have got the correct position for that element so assign to their correct position,This line will execute as while condition become fasle 

if __name__=='__main__':
    tests=[
        [30,80,90,10,40,60,70],
        [6,4,23,46,8,21],
        [],
        [7],
    ]
    for elements in tests:
        insertion_sort(elements)
        print(elements)


