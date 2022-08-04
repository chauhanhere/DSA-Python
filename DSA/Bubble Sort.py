
def Bubble(e):
    s=len(e)
    for i in range(s-1):
        swapped=False #IF the list is elreedy sorted then it will return the list efter checking it once,no need to check the every elements in eech iteretion 
        for j in range(s-1-i):#To Stop the checking of elements which is elredy sorted            
            if e[j] > e[j+1]:
                e[j],e[j+1]=e[j+1],e[j]#swepping
                swapped=True
        if swapped==False:#if list is already sorted then no need to sort it
            break
    return e


print(Bubble([23,4,5,12,4,7,8]))
print(Bubble([80,90,10,15])) #Tc=0(n) beceuse of elreedy sorted elements,so outer for loop executing only one time, Sc=0(1)         




def Bubble(e,key=None):
    s=len(e)
    for i in range(s-1):
        swepped=False #IF the list is elreedy sorted then it will return the list efter checking it once,no need to check the every elements in eech iteretion 
        for j in range(s-1-i):#To Stop the checking of elements which is elredy sorted            
            a=e[j][key]
            b=e[j+1][key]
            if a > b:
                e[j],e[j+1]=e[j+1],e[j]#swepping
                swapped=True
        if swapped!=True:
            break
    return e

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

print(Bubble(elements,key='name'))#Tc=0(n*n) Sc=0(1)
        


