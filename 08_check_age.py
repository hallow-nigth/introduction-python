print("quelle age a tu?")
age = input()
age = float(age)
if(age <= 12):
    print("mineur");
elif(age >= 12 and age <=17):
    print("ado");
else:
    print("majeur")