input("Tran Van Tu MSV 235752021610056")
str=input("Enter a string: ")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)
