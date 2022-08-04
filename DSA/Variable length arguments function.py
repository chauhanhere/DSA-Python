#Function will return the string and length of largest string

def findlargest(*x):#we can pass any number of arguments with the help of(*),Number of variable=1
    l=0
    t=''
    for i in range(0,len(x)):
        if len(x[i])>l:
            l=len(x[i])
            t=x[i]
    return l,t
print(findlargest('Bhopal','Patna','Delhi','sijdnjbdfb'))#Number of arguments pasing=4

#OR

def sum(*a):#Number of variable=1
    s=0
    for i in range(0,len(a)):
        s=s+a[i]
    return s
print('sum=',sum(10,3,40,20))#Number of arguments pasing=4

