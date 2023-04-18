def stripSpaces( str ):
    if len(str ) == 0 : return ""
    if str[0] == " " :
        return stripSpaces ( str[1:] )
    else:
        return str[0:1] + stripSpaces(str[1:])
str = input("Enter a string : ")
print("String after striping spaces")
print(stripSpaces(str))
