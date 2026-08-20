print("lec_08 of python")
 #  Q- 01 

nums = float(input("enter the number :"))

if nums > 0:
     print ("positive number")

elif nums < 0 :
     print ("negetive number ")

else :
     print ("zero")


 #  Q - 02 

if nums % 2 == 0 :
     print("provided number is even")

else : 
     print("odd")

 #  Q - 04

print("inter the any 3 numbers :-")
num1 = int(input("num1 :"))
num2 = int(input("num2 :"))
num3 = int (input ("num3 :"))

print("the bigest number is :")
if num1 > num2 and num1 > num3 :
     print ("num1 ", num1)
elif ("num2 > num1 and num2 > num3") :
     print("num2 ", num2)

else :
     print("num3 " , num3)



toppings = "garlic"

if toppings == "garlic" :
     print("i'll order it ")
print ("pizza")

 
marks = 50

if marks >= 95 :
     print("scholarship")

else :
     print("batter luck next time ")

toppings = ['extra_chees' , 'mashrooms' ,'onions' , 'garlic' ]

if "extra_chees" in toppings :
     print("add it")
elif "mashrooms" in toppings :
     print("add it ")
elif "onions" in toppings :
     print("add it ")
else :
     print("we'll can't add it ")
print("your pizza is ready!")

if "extra_chees" in toppings :
     print("add it")
     if "mashrooms" in toppings :
         print("add it ")
     elif "onions" in toppings :
         print("add it ")
else :
     print("we'll can't add it ")
print("your pizza is ready!")

toppings = "extra chees"

print("add conr in pizza") if toppings == "corn" else print("add extra chees")

if "corn" not in toppings : 
     print("add it in pizza")
else :
     print("we can add corn inside of chees and garlic")
  

