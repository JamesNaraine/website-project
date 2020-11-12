# global pascal
# global next_pascal

pascal_up_to = 5

pascal = [1]
next_pascal = []


for x in range(1,pascal_up_to +1):
    pascal.append(0)
    pascal.reverse()
    pascal.append(0)
    for i in range(1,len(pascal)):
        next_pascal.append(pascal[i-1] + pascal[i])
        next_pascal.remove(next_pascal[-1])
        next_pascal = pascal
    pascal.remove(pascal[-1])
    for i in pascal:
        next_pascal.append(pascal[i-1] + pascal[i])
        pascal = next_pascal
print(pascal)




