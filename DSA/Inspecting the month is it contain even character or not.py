def inspect(a):
    if len(a)%2==0:
        return 'even'
    else:
        return a[0]
print(list(map(inspect,['january','february','March'])))
