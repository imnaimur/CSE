arr = [3,4,5,6,0,1,2,8,9,10,11]
st = 5
size = 10
n = len(arr)
last = (st + size) % n
print(arr[last],last)
