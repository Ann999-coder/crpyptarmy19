

fp = open("KR.txt", "r")
#print(fp.read())
lst = []
for row in fp:
    print(row)
    lst.append(int(row))

print("list...",lst)

"""Kr = []


Kr.append(int(input()))
print("KR..............",Kr)"""