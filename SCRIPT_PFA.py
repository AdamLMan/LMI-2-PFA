import random
import csv
#CSV est inclus dans la librarie standard python

#ID,Prix,Quantite,Remise
#101,15.0,3,10
#102,25.0,2,5
#103,10.0,5,0

nlin= 0

randID = 0
randPrix = 0
randQuantite =0
randRemise = 0

data = [
    ['ID','Prix','Quantite','Remise'],
]

nlin= random.randint(5,20)

for i in range(0,nlin-1) :

    #génération des données d'une colonne
    randID= random.randint(1,100)
    randPrix=random.uniform(1,100)
    randQuantite=random.randint(1,100)
    randRemise=random.uniform(0,90)


    #Ajout des données d'une colonne
    data.append([randID,randPrix,randQuantite,randRemise])


#Création fichier resultats
with open('ventes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


LINES = [[101,15.0,3,10] , [102,25.0,2,5] ,   [103,10.0,5,0]]
print(data[i][1])
#QUESTION 2
#CALCUL ET AJOUT CA BRUT
CA_BRUT = ['CA_BRUT']
for i in range (1,nlin-1) :
    CA_BRUT.append((data[i][1])*(data[i][2]))

#QUESTION 3
#Calcul et ajout CA NET
CA_NET=['CA_NET']
for i in range(1  , nlin-1) :
    CA_NET.append(CA_BRUT[i]*data[i][3])

#QUESTION 4

#Calcul et ajout TVA
TVA=['TVA']
for i in range(1,nlin-1) :
    TVA.append(CA_NET[i]*0.2)

#QUESTION 5

CA_TOTAL =0
for i in range(1 , nlin-1) :
    CA_TOTAL+=CA_NET[i]-TVA[i]

#QUESTION 6

ID_MAX  = data[1][0] # id du produit ayant généré le plus grand CA NET
LIN_MAX = 1 #numéro de la colonne du produit ayant généré le plus grand  CA NET
for i in range (1,nlin-1) : #recherche de l'id
    if (CA_NET[i]>CA_NET[LIN_MAX]) :
        LIN_MAX=i
        ID_MAX=data[i][0]

#QUESTION 7
#new_data contient les donnees de resultats_final

new_data =data 
#Ajout des colonnes
new_data[0].append('CA_NET')
new_data[0].append('TVA')

for i in range(1,nlin-1) :
    new_data[i].append(CA_NET[i])
    new_data[i].append(TVA[i])

#Création deu fhichier resultats_final.sc
with open('resultats_final.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_data)



