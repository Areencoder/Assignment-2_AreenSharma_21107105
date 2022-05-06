#Q1
givenstring="python is a case sensitive language"
stringlength=len(givenstring)
revstring=givenstring[-1::-1]
newstring=givenstring[10::27]
replacestring=givenstring.replace("a case sensitive","object oriented")
a_position=givenstring.index("a")
stringwithoutspace=givenstring.replace(" ","")
print(stringlength,revstring,newstring,replacestring,a_position,stringwithoutspace)

#Q2
name="areen sharma"
SID="21107105"
department="mechanical"
cgpa=8.5
print("hey, ",name," here!","\n","My SID is ",SID, "\n","i am from ",department,"and my CGPA is ",cgpa)

#Q3
a=56
b=10
print(a&b,a|b,a^b,a>>2,b>>2,a<<2,b<<4)

#Q4
inputstring=input("Enter string: ")
substring="name"
if substring in inputstring:
  print("Yes")
else:
  print("No")

#Q5
  a=int(input("enter side 1: "))
b=int(input("enter 2nd side: "))
c=int(input("enter 3rd side: "))
while (a+b<=c) or (b+c<=a) or (c+a<=b):
  print("No")
  break
while (a+b>c) and (b+c>a) and (c+a>b):
  print("Yes")
  break

#Q6
number_1 = int(input("Enter 1st number (a) "))


number_2 = int(input("Enter 2nd number (b) "))

ex_or = number_1 ^ number_2


bin_exor = bin(ex_or)
check_string = str(bin_exor)


bits_need_flip = check_string.count("1")

print("Number of bits needed to be flipped to convert ‘a’ to ‘b’ are:", bits_need_flip)
