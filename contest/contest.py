n = int(input())
string = "codeforces"
for i in range(n):
    c = input()
    if c in string:
        print("Yes")
    else:
        print("No")
# n1 = int(input())
# for j in range(n1):
#     x = 0
#     y = 0
#     f = 0
#     n2 = int(input())
#     st = input()
#     for i in st:
#         if i == "U":
#             y+=1
#         if i == "D":
#             y -= 1
#         if i == "R":
#             x += 1
#         if i == "L":
#             x -= 1
#         if x == 1 and y == 1:
#             print("YES")
#             f = 1
#             break
#     if f == 0:
#         print("NO")