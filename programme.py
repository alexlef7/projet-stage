a = 10
b = 5
c = b*a
d = c-a
if d>5:
    print(d,"est supérieur à 5")
else:
    print(d,"est inférieur à 5")

# -*- coding:Utf-8 -*-
# programme qui convertit un nombre entier de secondes fourni au départ,
# en un nombre d'années, de mois, de jours, de minutes et de secondes.
# on admet 365 jours par an et 30 jours par mois, ce qui donne un résultat très approximatif
# 1 jour = 24 heures, 1 heure = 60 minutes, 1 minute = 60 secondes
# 1 an = 12 mois = 365 jours = 8760 heures (365*24) = 525600 minutes (8760*60) = 31536000 (525600*60) secondes

nbre_depart = int(input("entrer un nombre en seconde"))
annee,mois,jour,heure,minute,seconde = 0, 0, 0, 0, 0, 0
minute = nbre_depart//60
seconde = nbre_depart%60
if minute >=60:
    heure = minute//60
    minute = minute%60

if heure >=60:
    jour = heure//60
    #heure = heure%60

if jour >=60:
    mois = jour//60
    jour = jour%60
if mois >=60:
 #   annee = mois//60
    mois = mois%60

print(nbre_depart,"secondes représentent:")
print(annee,"année(s)",mois,"mois",jour,"jour(s)",heure,"heure(s)",minute,"minute(s)",seconde,"seconde(s)")