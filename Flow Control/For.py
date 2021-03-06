#for statements
str="Python"
for c in str:           #simple for statement
    print(c)

prize={'first':'gold','second':'silver','third':'bronze'}
for pos,medal in prize.items():     #accessing subelements
    print(pos+" is given "+ medal)

for i in range(5): #0-4 
    print(i)

print("---------")
for i in range(2,8):    #2-7
    print(i)

print("---------")
for i in range(2,10,3): #2-10 with step=3
    print(i)

print("---------")
arr=[10,20,30,40]
for i in range(len(arr)):     #iterate over indices of arr
    print(arr[i])

print("---------")
print(range(10))       #prints the iterable object returned 

print("---------")
for i in range(5):
    if(i==4):
        break
    if(i==2):
        continue
    print(i)

print("---------")
a=[7,23,66,32,90]  #add 10 to change the output
b=10
for i in a:
    if(i==b):
        print(b, "is present in a")
        break
else:           #when the loop exits normally(without break)
    print("element not found")