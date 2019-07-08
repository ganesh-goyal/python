import cmath
a = int(input("enter a  number:"))
b = int(input("enter b num :"))
c = int(input(" enter c numb: "))

# discreminant 
d = (pow(b,2)-4*a*c)
print(d)
# find the solution
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (+b-cmath.sqrt(d))/(2*a)
print("root of quadritic equation of sol1 and sol2 =",(sol1,sol2))
