def linear(a,x,n):
    for z in range(n):
        if a[z] == x:
            return z
    return -1

a = [10,3,2,30,44,29,6.68,47]
n = len(a)
x = int(input('Enter number to search: '))

res = linear(a,x,n)
if res == -1:
    print('Number not found')
else:
    print('Number is on index ',res)
