number = int(input("Lütfen bir pozitif tam sayı giriniz: "))
if number>=1:
 for i in range(2,number) : 
  if number % i == 0 :
   print("Girdiğiniz {} sayısı asal sayı değildir.".format(number))
   break 
elif number == 0 :
  print("0 bir asal sayı değildir.")
elif number < 0 :
  print("Girdiğiniz sayı negatif bir sayıdır. Asal sayı olması imkansızdır.")
else :
   print ("Girdiğiniz {} sayısı asal sayıdır.".format(number))
