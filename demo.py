# myList=[['Prashant', 'Ashish'],[ 'Komal', 'Ankush', 'Sandip']]
# # newList=myList.copy()
# # myList.insert(1,"Nirbhay")
# print(myList)
# print(myList[0][0])
# print(myList[0][1])
# print(myList[1][0])
# print(myList[1][1])
# print(myList[2][0])
# list1=["Prashant","Jha"]
# print(list1*2)

# list2=[50,25.50]  #list
# del list2[0]
# print(list2)
# myList=[44,78,56,98,23,14] 
# myList.sort()
# print(myList)
# math=50   
# print(id(math))
# phy=50
# print(id(phy))
# myList=[44,58,7453,2,5,69]
# newList=myList
# print(id(myList))
# print(id(newList))   
# for i in range(2,21,2): 
#     print(i)
# no=int(input("Enter the digit:"))
# if no>0:
#     print("Positive")
# if no<0:
#     print("Negative")
# if no==0:
#     print("Zero")

# p2=int(input("Enter paper 1: "))
# p1=int(input("Enter paper 2: "))
# p3=int(input("Enter paper 3: "))
# sum=(p1+p2+p3)
# result=((sum/300)*100)

# if result>=60:
#     print("Eligible")
# else:
#     print("Not Eligible")
# p1=int(input("Enter number 1: "))
# p2=int(input("Enter number 2: "))
# p3=int(input("Enter number 3: "))
# p4=int(input("Enter number 4: "))
# p5=int(input("Enter number 5: "))

# if p1>p2 and p1>p3 and p1>p4 and p1>p5:
#     print("p1 is greater")
# elif p2>p1 and p2>p3 and p2>p4 and p2>p5:
#     print("p2 is greater")
# elif p3>p1 and p3>p2 and p3>p4 and p3>p5:
#     print("p3 is greater")
# elif p4>p1 and p4>p2 and p4>p3 and p4>p5:
#     print("p4 is greater")
# elif p5>p1 and p5>p2 and p5>p3 and p5>p4:
#     print("p5 is greater")
# print(25) 
# print("Hello World")
#Question:  per > 90 ==>'A'
# per > 80 ==>'B'
# per > 70 ==>'C'
# per > 60 ==>'D'
# per < 60 ==> 'Fail'
# per=int(input("Enter the percentage: "))
# if  per>=90:
#     print("Grade A")
# elif per>=80 and per<90:    
#     print("Grade B")
# elif per>=70 and per<80:
#     print("Grade C")
# elif per>=60 and per<70:    
#     print("Grade D")
# else:
#     print("Fail")   
# myDict={
#     "name":"Prashant",
#     "age":21,
#     "gender":"Male",
#     "city":"Patna"
# }
# print(myDict)
# print(type(myDict))
# m
# name= "Prashant Jha"
# print(name[0:8])
# print(name[0])
# s="Help4Code is the best platform for practicing programming"
# print(s.find("Code"))
# print(s.find("python"))
# print(s.replace("programming","coding"))
# s="Prashant", "Ashish", "Sandip"
# m='|'.join(s)
# print(m)
# s="Python is a high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.title())
# print("Subject Marks: ")
# phy=50
# chem=60
# maths=70
# print("phy ={} chem ={} maths={}".format(phy,chem,maths))
# print("phy ={x} chem ={y} maths={z}".format(x=phy,y=chem,z=maths))
# print("phy ={0} chem ={1} maths={2}".format(phy,chem,maths))
# total=phy+chem+maths
# print("Total Marks", f"{total}")

# print('prashantjha777'.isalnum())
# print('prashantjha777'.isalpha())
# print('prashantjha777'.isdigit())
# print('prashantjha777'.islower())
# print('prashantjha777'.isupper())
# print('prashantjha777'.isspace())
# print('prashantjha777'.istitle())
# print('prashantjha777'.startswith('prashant'))
# print('My name is Prashant'.istitle())
# print(''.istitle())
# a=50
# b=90
# c=50
# d=10
# print((a+b)*c/d)
# print((a+b)/c*d)
name="Prashant"
# for i in name:
#     print(i)
data=['a','e','i','o','u']
vowels=0
con=0
for i in name:
    if i in data:
        vowels+=1
    else:
        con+=1
print("Vowels=", vowels)
print("Consonants=", con)