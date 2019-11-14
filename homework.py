'''list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_list=[]
for x in list:
    if x%2==0:
        even_list.append(x)
print("The list of even numbers is")
print(even_list)'''

'''number=int(input("enter any number"))
print("the multiplication table of %s :" % number)
for x in range(1,11):
    print("%s = %s =%s" %(number, x, number*x))'''

'''list=[1,2,3,4,5,6,7,8,9]
number=int(input("enter the number you want to remove"))
list.pop(number)
print(list)'''

x=1
list=[]
for x in range(1,11,1):
    num1=input("enter the number")
    list.append(int(num1))
    list.sort()
    print(list)
    print("The list is obtained")



