# Covid Risk Assigment
print("This is a Covid Risk Diagnostic Study! Please answer the following questions")
age = bool (input("Are you a cigarette addict older than 75 years old? Yes or No ?"))
chronic = bool (input("Do you have a severe chronic disease? Yes or No ?"))
immune =bool (input("Is your immune system too weak? Yes or No"))
print(age,chronic,immune)
if age == True and chronic == True and immune == True :
  print("You are in risky group!")
else :
  print("You are not in risky group")  
