# prime number program

num = int(input("enter the number:"))
          
if num > 1:
   for i in range(2,num):
      if (num%i) == 0:
          print(num,"number is not prime")
          print(i,"times",num//i,"is",num)
          break 
   else:
      print(num,"is a prime number")
