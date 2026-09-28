print("donne un nombre en sec ")
sec = input()
sec = int(sec)
#on calcule le heures min et sec ,en ayant les sec seulement, on les decompose alors
h = sec//3600
min = sec%3600//60
minsec = sec % 3600//60

min = str(min)
minsec = str(minsec)
h = str(h)
print(h +"heure " + min + "min " + minsec + "sec")



