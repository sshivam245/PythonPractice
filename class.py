#a = 3
#n= int(input("eneter the n terms"))
#for i in range(1,n+1):
 #   print(a,end=",")
  #  a+=5

#n= int(input("eneter the n terms"))
#a=3
#while a<n:
    #print(a,end=" ")
   # a+=5
    
#num1=float(input("enter numer1: "))
#num2=float(input("enter number2: "))
#print(num1 if num1 >= num2 else num2)


#a=float(input("enter numer1: "))
#b=float(input("enter number2: "))
#c=float(input("enter number3: "))
#if (a >= b) and (a >= c):
 #       print(a)
  
#elif (b >= a) and (b >= c):
 #       print(b)
#else:
 #       print(c)




#list = ("This", "will be", "printed on separate", "lines")
#for item in list:
 # print(item)


#WAP to initialize a tuple with first 20 even numbers only and print the tuple

#even = tuple()
#for i in range(1,41):
 #   if i % 2==0:
  #      even +=(i,)
   #     print(even)
   

    # reverse str

#str= input("pls enter str: ")
#print(str[::-1])



#college = ["DU" , "Amity" , "IIT" , "IIM"]
#print(college[::-1])

#sports = ["table tennis" , "tennis" , "cricket" , "football"]
#sports.clear()
#print(sports)

#college = ["DU" , "Amity" , "IIT" , "IIM"]
#print(college[::-1])


#tech_companies = ["google" , "microsoft" , "apple" , "adobe"]
#tech_companies.reverse()
#print(tech_companies)

#l=[1,2,3,45]
#for i in range(0,len(l)):
  #l[i]+=5
#print(l)


    
    

#num = int(input("enter a number:  "))
#def find_evenodd(num):
 # if(num%2==0):
  #  return("number is even")
  #else:
   #return("number is odd")

#find_evenodd(num)

   
   

#number = int(input("enter a number:  "))
#absolute_number = abs(number)
#print(absolute_number)

#def findpow(x,y):
 # pow=x**y
  #return pow
#a=int(input("enter a number: "))
#b=int(input("enter a number: "))
#for i in range(0,b):
 # power = pow(a,i)
  #print ("the",a,"raised to",i,"::",power)


#n=5
#i=0
#while i<n:
 # print(i)
  #i=i+1



# constructor 

#class person:
 # def __init__(self , s , h , i ):
  #  self.name = s
   # self.age = h
    #self.phone = i

  #def hellofunc(self):
   # print("hello my name is " + self.name)  
    #print("my age is" + (self.age))
    #print("my phone is"+ (self.phone))
    
#p1=person("shivam","19","9958479002")
#p1.hellofunc()


#class manager:
 # def __init__(self,name,salary):
  #  self.name = name
   # self.salary = salary
  #def displayM(self):
    
   # print("name: " , self.name, "salary: ", self.salary)
#emp1=manager("a", 2000)
#emp2=manager("b",1000)

#emp1.displayM()
#emp2.displayM()


#class animal:
  #def __init__(self):
   # print("\n\n\n Animal constructor")
  #def speak(self):
   # print("\tamimal speaking")

#class dog(animal):
 # def __init__(self):
  #  print("dog constructor")
  #def bark(self):
   # print("\t\tdog barking")

#class cat(animal):
  #def __init__(self):
 #   print("cat constructor")
  #def sing(self):
   # print("\t\tcat singing")

#class dogchild(dog):
 # def __init__(self):
  #  print("dog child constructour ")
  #def eat(self):
   # print("\t\t\tdog child eating")

#q=animal()
#p=dog()
#a=dogchild()
#a.eat()
#a.bark()
#a.speak()



#class ht:
 # def __init__(self,ft,inc):
  #  print("height constrictor")
   # self.feet=ft
    #self.inch=inc
  
  #def input(self,ft,inc):
   # print("input function")
    #self.feet=ft
    #self.inch=inc

  #def output(self):
   # print("output function")
    #print(self.frt,self.inch)

#print("hi")
#c=ht(6,5)
#c.output()
#c.input(5,8)
#c.output


list=[]
for i in  range(0,5):
  a=int(input("enter a num: "))
  list.append(a)

print("the sum is", sum(list))

list.insert(4,9)
print(list)
  

