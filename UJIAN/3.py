def Terbesar(a,b,c):
   if a >= b and a >= c:
       return a
   elif b >= a and b >= c:
       return b
   else: 
       return c
   #return max(a,b,c)

print(Terbesar(3,8,4))
