#match statements are introduced in python 3.10 
a=4 
match a:
    case 1:b='one'
    case 2|3: b='two or three'  #multiple cases can be combined
    case _: b='none of the above'  #similar to default

print(b)


#Unpacking arguments
point=[90,-80]          #change the values to display point's quadrant
match point:
    case (0,0): b='origin'
    case (0,y): b='y axis'
    case (x,0): b='x axis'
    case (x,y): 
        x=x/abs(x)
        y=y/abs(y)
        match (x,y):
            case (1,1):b='1st qudrant'
            case (-1,1):b='2nd quadrant'
            case (-1,-1):b='3rd quadrant'
            case _:b='4th quadrant'

print("point is on ",b)

