#python code to illstrutate function
def digitsum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
list = [ 367, 111, 562, 945, 6726, 873]
newlist = [digitsum(i) for i in list if i & 1]
print(newlist)  # [16, 6, 18, 18]