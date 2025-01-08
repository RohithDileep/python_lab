a=[3,3,7,1,4,3,2,7,9,2]
num=int(input("Enter the number: "))
def count_occ(a,b):
    count=0
    for i in range(len(a)):
        if a[i] == num:
            count+=1
    return count
c=count_occ(a,num)
print(num,"repeats",c,"times")
