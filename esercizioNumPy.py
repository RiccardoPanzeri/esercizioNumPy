from numpy import *
import numpy as np
#dichiaro le matrici con array(), che conterranno valori pseudorandomici grazie al metodo randint()
m1 = random.randint(10, size = (5, 5)) #utilizzo il metodo randint() con due parametri: uno per il valore massimo che può assumere un valore di una matrice, e come secondo parametro il numero di righe e colonne
m2 = random.randint(10, size = (5, 5))
 #al contrario di C, Python, se utilizziamo il modulo numpy, permette di stampare direttamente array e matrici tramite print()
print(f"matrice1:\n\n{m1}\n\n")
print(f"matrice2:\n\n{m2}\n\n")

#è possibile effettuare una permutazione su una matrice, in due modi diversi:

#shuffle() permette di mischiare le righe della matrice in maniera casuale, modificando la matrice originale:
random.shuffle(m1) #al metodo shuffle passo come parametro la matrice stessa
print(f"matrice 1 permutata:\n\n {m1}\n\n")

#mentre permutation() restituisce una matrice con le righe mischiate tra loro casualmente, ma senza modificare la matrice originale:
mP = random.permutation(m2) #creo una nuova matrice a cui assegno il return del metodo permutation() applicato alla matrice m2
print(f"matrice permutata senza modificare m2:\n\n{mP}\n\n")

#è possibile stampare direttamente solo i valori della matrice in un determinato range (slicing della matrice):
print(f"prima riga di m2:\n\n{m2[0:1, 0:5]}\n\n") #stampo solo tutti gli elementi della prima riga di m2 (l'ultimo numero, per quanto riguarda le righe, righe non è compreso), specificando range di righe e range di colonne

#posso sommare due matrici in due modi diversi, con add() e sum():

#con add(), vado a sommare ogni elemento della prima matrice con il suo corrispondente della seconda:
m3 = np.add(m1, m2)
print(f"matrice risultante dalla somma tra m2 e m1 (permutata) con add():\n\n{m3}\n\n")

#mentre con sum() vado a sommare tutti gli elementi della matrice tra loro, e otterrò un unico numero intero come risultato 
risultato = np.sum([m1, m2])
print(f"risultato ottenuto con sum() tra m2 e m1 (permutata):\n\n{risultato}\n\n")

#è possibile anche effettuare una somma cumulativa di una singola matrice tramite cumsum(), ottenendo un array:
aC = cumsum(m1[0:6, 0:5])
print(f"array ottenuto tramite somma cumulativa di m1(permutata):\n\n{aC}\n\n")

#è anche possibile moltiplicare tutti gli elementi di una o più matrici tra loro con prod(), ottenendo un unico numero intero come risultato:
risultato = np.prod([m1[0:1, 0:5], m2[0:1, 0:5]])
print(f"Risultato applicando prod() sulla prima riga di m1 (permutata) e m2:\n\n{risultato}\n\n")
