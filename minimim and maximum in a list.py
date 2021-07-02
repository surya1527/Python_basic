value = int(input("enter number of elements to be inserted into the list: "))            #enter the number of elements in the list

# Enter the space saparated integers

l = list(map(int,input().split()))    
l.sort()

print("minimum value is: " ,l[0],end = ' ')                     #index value of min integer is "0"

#end function will prinet the value in the same line
print("and maximum value is",l[value - 1])