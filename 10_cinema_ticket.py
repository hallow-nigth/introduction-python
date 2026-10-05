age = int(input("quelle age as tu? "))
imax = bool(input("est-ce en imax?"))
special = bool(input("est tu une personne speciale?"))
prix = 14.1

if(imax == True):
    prix = 18.5

if (age < 18):
    prix = prix -4
               
if(special == True):
    prix = prix//2
    
print("votre prix est "+ str(prix))
               