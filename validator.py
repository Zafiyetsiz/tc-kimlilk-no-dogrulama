#################################################
#PROJECT 2 : VALIDATOR

#Language :Turkish 
  
#Turkey ID(identification) number validator

#The simplest and the easiest way for validator

#Contact me  on ;

#Telegram  : Zafiyetsiz0
#Instagram : Zafiyetsiz

#################################################

print("tc  nin  1. rakamını yazın")
a= input(" 1.rakam: ")
a= int(a)


print("tc  nin  2. rakamını yazın")
b = input("2.rakam: ")
b= int(b)


print("tc  nin  3. rakamını yazın")
c = input("3.rakam: ")
c= int(c)


print("tc  nin  4. rakamını yazın")
d = input("4.rakam: ")
d= int(d)


print("tc  nin  5. rakamını yazın")
e = input("5.rakam: ")
e= int(e)


print("tc  nin  6. rakamını yazın")
f = input("6.rakam: ")
f= int(f)


print("tc  nin  7. rakamını yazın")
g = input("7.rakam: ")
g= int(g)


print("tc  nin  8. rakamını yazın")
h = input("8.rakam: ")
h= int(h)


print("tc  nin  9. rakamını yazın")
i = input("9.rakam: ")
i= int(i)

print("tc  nin  10. rakamını yazın")
j = input("10.rakam: ")
j = int(j)

print("tc  nin  11. rakamını yazın")
k = input("11.rakam: ")
k= int(k)


tekler=(a + c + e + g + i)   
tekler = int(tekler)
Çiftler=(b + d + f + h)
Çiftler = int(Çiftler)


x =(tekler * 7)
x = int(x)
y =(Çiftler * 9)
y = int(y)

w=(a + b +c + d + e + f + g + h + i + j)
o=(w % 10) #11.rakam

if o == k:
     print("bu tc kimkil no DOĞRU.")
         
    
else:
    print("bu tc kimlik no YANLIŞ")
