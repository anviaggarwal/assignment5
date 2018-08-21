#Q1
year=int(input("enter year"))
if year%4==0:
    if year%100==0:
         if year%400==0:
             print(year,'is a leap year ')
         else:
             print(year,'is not a leap year ')
    else:
         print(year,'is a leap year ')
else:
     print(year,'is not a leap year ')

#Q2
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l>0 and b>0):
    if(l==b):
        print("it is square")
    else:
        print("it is rectangle")
else:
    print('not possible')

#Q3
age_1=int(input("enter first age"))
age_2=int(input("enter second age"))
age_3=int(input("enter third age"))
if(age_1>=age_2 and age_1>=age_3):
    print("Oldest age is:",age_1)
    if(age_2>=age_3):
      print("Youngest age is:",age_3)
    else:
      print("Youngest age is:",age_2)
      
elif(age_2>=age_1 and age_2>=age_3):
    print("Oldest is:",age_2)
    if(age_1>=age_3):
      print("Youngest age is:",age_3)
    else:
      print("Youngest age is:",age_1)
      
else:
    print("Oldest age is:",age_3)
    if(age_1>=age_2):
      print("Youngest age is:",age_2)
    else:
      print("Youngest age is:",age_1)

#Q4
age=int(input("Enter age:"))
sex=input("Enter Sex( M or F):")
status=input("Enter Marital Status (Y or N):")
if(sex=='F' or sex=='f'):
    print("Place of Service: URBAN AREA ONLY ")
elif(sex=='M' or sex=='m'):
    if(age>=20 and age<=40):
        print("Place of Service: ANYWHERE ")
    elif(age>40 and age<=60):
        print("Place of Service: URBAN AREA ONLY")
    else:
        print("ERROR")
else:
   print("ERROR")


#Q5
unit=int(input("Enter units:"))
cost=int(input("Enter cost:"))
amount=unit*cost
print('Amount:',amount)
if(amount>=1000):
    disc=amount-(amount*(1/10))
    print('discount:',disc)
else:
    print("NO DISCOUNT")

    
#Loops_Q1
integers=[]
for i in range(10):
    value=int(input('Enter value: '))
    integers.append(value)
print('List:',integers)



#loops_Q2
#x=1
#while x>0:
 #   print(x)
  #  x+=1


#loops_Q3
list1=[]
list2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digits:'))
    list1.append(b)
print('List is:',list1)
for i in range(a):
    sq=list1[i]*list1[i]
    list2.append(sq)
print('List of Squared element:',list2)



#Loops_Q4
list1=[]
list2=[]
list3=[]
list4=[]
n=int(input("Enter Size:"))
for i in range(n):
    d=input('Enter values:')
    list1.append(d)
print('List:',list1)
for i in range(n):
    if str(list1[i]).isdigit():
        list2.append(list1[i])
    elif str(list1[i]).isalpha():
        list3.append(list1[i])
    else:
        list4.append(list1[i])
print('Int List:',list2)
print('String List:',list3)
print('Float List:',list4)


#Loops_Q5  
print("Prime numbers are:")

for i in range(1,101):
   if i > 1:
       for x in range(2,i):
           if (i % x) == 0:
               break
       else:
           print(i)

#Loops_Q6
print('Pattern')
for i in range(0, 5,1):
    print("* "*i)

    
#Loops_Q7 
print()
l1=[]
l2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digit:'))
    l1.append(b)
print(l1)
search=int(input("Enter value to search:"))
l1.remove(search)
print(l1)      
         
         

