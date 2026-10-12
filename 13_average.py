print("stop = q")
while input != "q":
    valeur = input("insere une note sur 20 :")
    if (valeur == "q"):
        print("ok je calcule la moyenne")
        break
    else:
        valeur = int(valeur)
        if(valeur > 20 or valeur <0):
            print("valeur trop haute ou basse")
        elif(valeur == str()):
            print("valeur invalide")
      
moyenne = valeur
print(moyenne)
   
    