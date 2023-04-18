def func ():
    x = 1001
    while ( x % 7 != 0) : 
            x += 1
    for i in range (x, 2000, 7) :
          if(i % 5 != 0 ) : 
                print( i, end = " ")
print("The required series is as follows : ")
func()
