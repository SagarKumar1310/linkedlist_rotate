def rotate(arr,n):
    x = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = x
arr = [1,4,6,8,7]
n =len(arr)
for i in range(0,n):
    print(arr[i] ,end=' ')
rotate(arr,n)
print('\n')
for i in range(0,n):
    print(arr[i] , end=' ')

