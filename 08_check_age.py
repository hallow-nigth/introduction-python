print("quelle age a tu?")
age = input()
age = float(age)
if(age <= 12):
    print("tu es mineur");
elif(age >= 12 and age <=17):
    print("tu es ado");
else:
    print("tu es majeur")