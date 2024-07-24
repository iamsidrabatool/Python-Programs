def appl(fx, value):
  return 6 + fx(value)

double= lambda x: x*2
print(double (5))

cube= lambda x:x*x*x
print(cube(3))

avg=lambda x,y:(x+y)/2
print(avg(3,4))
 
print(appl(lambda x: x * x , 2))