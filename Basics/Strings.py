a = "Hi"  # double quotes
b = 'Hi'  # single quotes
print(a)
print(b)  # both give same output

# Escaping
a = 'has\'nt'
b = "\"Hi\""
print(a)    # has'nt
print(b)    # "Hi"

# single and double quotes in the other. No escape needed
a = "has'nt"  # single quotes in double quotes
b = '"Hi'  # double quotes in sinlge quotes
print(a)    # has'nt
print(b)    # "Hi"

# raw strings
print('tes\ts')
print(r'tes\ts')

# multiline strings. use '\' to prevent adding newline
print('''
line1
line2\
ilne3
''')

# String concatenation and muliplication
print(3*'hi'+' hello')
print('hello' 'world')
print('hi'
      ' python')
a = 'hi'
print(a+' world')

# String indexing(subscripting)
a = "Python"
print(a[0])
print(a[5])
print(a[-1])

# Slicing(to get substring)
print(a[2:4])
print(a[-5:-2])
print(a[2:])
print(a[:4])
print(a[3:1])   #gives empty string as output

#Immutable
a='Hello'
# a[2]='b'  #TypeError. Python strings are immutable.

#len()
a="abcd"
print(len(a))


