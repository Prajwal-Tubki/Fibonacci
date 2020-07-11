list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
list3=[]
print("list1:",list1)
a=len(list1)
j=0
while(j<a):
    if(list1[j]<0):
        list1.remove(list1[j])
        a-=1
        continue
    j+=1
print("list1:",list1)

print("list2:",list2)

for i in list2 :
    if (i>0):
        list3.insert(j,i)
        j+=1
print("list2:",list3)
        

