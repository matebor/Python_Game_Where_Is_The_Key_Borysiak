#
# Python Game - Where is the key?
# Author - Mateusz Borysiak
#


# Status - nieskończone (w trakcie pracy).


import random
import numpy as np


#Plansza
col = 5
row = 5
board = np.zeros((row,col))


#Klucz losowe umieszczenie
row_key = random.randint(0, row-1)
if row_key==2:
    row_key = random.randint(0, row-1)

col_key = random.randint(0, col-1)
if col_key==2:
    col_key = random.randint(0, col-1)

board[row_key, col_key] = 1
#print("Lokalizacja klucza: " + "[" + str(row_key+1) + "," + str(col_key+1) + "]")           #dla Dev


#Ruch gracza
row_user = 2
col_user = 3
board[row_user, col_user] = 4
print("Twoja lokalizacja startowa: " + "[" + str(row_user+1) + "," + str(col_user+1) + "]")
print()

print("Poczatek gry: ")
print(board)
print(" ")

def UserMotion(x):
    if x == "w":
         return row_user - 1, col_user
    elif x == "s":
         return row_user + 1, col_user
    elif x == "a":
         return row_user, col_user - 1
    elif x == "d":
         return row_user, col_user + 1
    else:
        print("Wybrano nieprawidłowy kierunek")

i = 0
while board[row_key, col_key] != board[row_user, col_user]:

     print("Wskaż kierunek ruchu: w-Góra, s-Dół, a-Lewo, d-Prawo")
     Motion = str(input())

     vector_user = UserMotion(Motion)
     
     if (vector_user[0] != -1 and vector_user[0] != 5) and (vector_user[1] != -1 and vector_user[1] != 5):

          row_user = vector_user[0]
          col_user = vector_user[1]
          board[row_user,col_user] = 4

          print("wektor klucza: " + str(row_key) + "," + str(col_key))
          print("wektor gracza: " + str(row_user) + "," + str(col_user))

          if ((row_user - row_key) == 1) or ((col_user - col_key) == 1):
               print("Gorąco!")
               
          elif (row_user - row_key) > 1 and (row_user - row_key) <= 2:
               print("Cieplo!")
          else:
               print("Zimno!")

     else:
          print("Sciana! Zmień ruch!")
          

     print("Twoja lokalizacja: " + "[" + str(row_user+1) + "," + str(col_user+1) + "]")
     print()
     i += 1
     print(board)
     print(" ")
else:
     print("Brawo wygrales! Koniec gry.")
     print("Wykonales: " + str(i) + " ruchów.")
     
#print(" ")
#print("Czy chcesz zagrać ponownie?")

print(board)
print(" ")

