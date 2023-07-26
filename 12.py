#python program to illustrate iterating over list, tuple, string, dictionary, set
print("List Iteration")
l = ["Sumit", "Kumar", "Arup", "Rai"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("Sumit", "Kumar", "Arup", "Rai")
for i in t:
    print(i)    

print("\nString Iteration")
s = "Sumit"
for i in s:
    print(i)

print("\nDictionary Iteration")
d = dict()
d['Sumit'] = 1
d['Arup'] = 2
for i in d:
    print("%s %d" %(i, d[i]))

print("\nSet Iteration")
set1 = {1, 2, 3, 4}
for i in set1:
    print(i)