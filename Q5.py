def reverseList(list) :
    n = len(list)
    mid = (n-1)//2
    for i in range (0, mid) :
        temp = list[i]
        list[i] = list[n-1-i ]
        list[ n-1-i ] = temp

list= ['r', 'a', 'b', 'b', 'i', 't']
print( 'original list ', list )
reverseList(list)

print( 'reversed list ', list )
