a = [1, 2, 3, 4, 5]  # simple list
# elements(items) can be of different types
b = [1, 'test', a, 'sample string', 2+8j]
print(a)
print(b)

#indexing and slicing
print(a[2])
print(a[-3])
print(b[:3])
print(b[-3:])
c = a[:]  # shallow copy is created
c[0] = 2
print(a)
print(c)


# Concatenation
print(a+b)
print(a+[6, 7])

# Modifying
a[0] = 0
print(a)
a[1:4] = [100, 101, 102]  # modifying on a range
print(a)
a.append(1000)  # appending
print(a)
a[1:3] = []  # removing a range
print(a)
print(len(a))   #length
a[:] = []  # clearing the entire list
print(a)

#Nested lists
a=[1,2,3]
b=['mon','tue','wed']
x=[a,b]
print(x[0])
print(x[1])