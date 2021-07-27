# Find out if a given number is an "Armstrong Number".
x = list (input("Lütfen bir tam sayı giriniz. : "))
x1 = ""
sayac = 0
sayac2 = 0
new1 = 0
a = 0
b = 0
while b < len(x) :
  if  x[b].isdigit() : 
      b += 1
      for i in x :
         sayac +=1
         sayac2 +=1    
      while 0 < sayac and a < sayac2 :
        sayac-=1
        new1 += (int(x[sayac]))**(sayac2)
        x1 += (x[a])
        a+=1
      if new1 == int(x1) :
         print ("Tebrikler girdiğiniz sayı arsmtrong bir sayıdır")
      else :
        print ("Girilen sayı armstrong sayı değildir.")
  else :
   print("Girdiğiniz sayıyı Kontrol ediniz")
   break
  break
print(new1)
print(x1)
