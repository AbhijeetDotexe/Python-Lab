def cummulative_product ( list ):
    res = 1
    for ele in list : 
        res *= ele
    return res

length_of_arr = int(input('Enter the length of the array : '))
print('Enter the elements of the array')
list = list()
for i in range (0, length_of_arr) : 
    list.append(int(input()))

print(f'the cummulative product of the list is : {cummulative_product(list)}')
