f = open('harry.txt')
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(0)
print(f.readline())
# print(f.tell())
f.close()
