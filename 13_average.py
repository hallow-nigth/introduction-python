print("stop = q")
x = 0
while input != "q":
    rep = input("insere une note sur 20 :")
    if (rep == "q"):
        print("ok je calcule la moyenne")
        break
    else:
        rep = int(rep)
        x += 1
        if(rep > 20 or rep <0):
            print("valeur trop haute ou basse")
        elif(rep == str()):
            print("valeur invalide")
        total =0
        total += rep
moyenne = total / x
      

print(moyenne)
   
    