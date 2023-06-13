
# def printReverse(lst):
#     n = len(lst)
#     last = (st+size-1)%n
#     # print("last",last)
#     i = 0
#     while i<size:
#         print(lst[last])
#         last -=1
#         if last < 0:
#             last = n-1
#         # if last <= n-1:
#         #     print("last -i",last -i)
#         i +=1




# def insertElement(lst):
#     global size
#     n = len(lst)
#     last = (st+size-1)%n
#     i = 0
#     while i < last+1:
#         lst[last+1] = lst[last]
#         last -=1
#     lst[idx] = elem
#     size +=1
#     print(lst)
# t = insertElement(arr)




def insertElement(lst):
    global size
    n = len(lst)
    last = (st + size) % n
    loop = last - idx
    count = 0
    count1 = 0
    j = last -1
    if idx > st:
        loop = n-idx + last
    for i in range(loop):
        lst[last] = lst[j]
        last -= 1
        j -= 1
        if j < 0:
            j = n-1-count
            count += 1
        if last < 0:
            last = n-1- count1
            count1 +=1

    lst[idx] = elem
    size += 1
    print(lst)

arr = [3,4,5,6,0,1,2,8,9,10,11]
st = 5
size = 10
idx = 2
elem = 7
t = insertElement(arr)
