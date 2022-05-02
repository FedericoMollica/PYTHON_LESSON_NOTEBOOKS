'''

#XXXXXX  LEZIONE BASE CICLI 'IF', 'ELSE', 'ELIF', 'DEF' E 'FOR' XXXXXX


#'if' or 'else' sono statement che ci consentono di definire delle condizioni. 
#al termine di ogni codice per statement bisogna mettere i ':'
'''

# -*- coding: utf-8 -*-

'''
#XXXX  CICLI DI IF, ELSE ED ELIF XXXX
'''

a = 1
b = 2
if a < b:
  print('a is less than b')
  print('a is for sure less than b')
print('Not sure if a is less than b')
#questo codice e' un esempio di condizione 'if'. Se a (variabile definita sopra) e' minore di b, allora printa()

#result: 
#a is less than b
#a is for sure less than b
#Not sure if a is less than b

c = 5
d = 4
if c < d:
  print('c is less than d')
else:
  print('c is not less than d')
  print("I don't think c is less than d")
print('outside the if block')
#questa condizione di 'else' viene interpretata come un 'altrimenti' nel caso in cui 'if' non si verificasse.
#leggo il codice come: se c minore di d printa(), altrimenti printa().

#result.
#c is not less than d
#I don't think c is less than d
#outside the if block

e = 7
f = 8 
if e < f:
  print('e is less than f')
elif e == f:
  print('e is equal to f')
else:
  print('e is greater than f')
#elif corrisponde a else if, lo si traduce con 'altrimenti se dovesse verificarsi' allora printa()
#se utilizzo il simbolo '=' una volta, assegno una variabile.
#se utilizzo il simbolo '=' due volte '==', faccio riferimento all`uguale in matematica.

#result: e is less than f

e = 19
f = 8 
if e < f:
  print('e is less than f')
elif e == f:
  print('e is equal to f')
elif e > f + 10:
  print('e is greater than f by more than 10')
else:
  print('e is greater than f')
#altro esempio con più condizioni

#result: e is greater than f by more than 10

g = 7
h = 8 
if g < h:
  print('g is less than h')
else:
  if g == h:
    print('g is equal to h')
  else:
    print('g is greater than h')
#in questo caso abbiamo spezzato 'elif' in 'else' ed 'if'

#result: g is less than h

'''
#XXXX  DEF FUNCTIONS  XXXX
'''

#una funzione rappresenta una collezione di istruzioni o di codici.
#le funzioni si definiscono con 'def', seguita sempre dai ':'

def function1():
  print('ahhhh')
  print('ahhhhhh 2')
print('this is outside the function')
#definisco 'finction1() come un insieme di codici print. 
#inserendo solo il nome della funzione posso generare tutti i codici contenuti in questa.
function1()

#result:
#this is outside the function
#ahhhh
#ahhhhhh 2

def function2(x):
  return 2*x
#fare una mappatura
#inserisco un input o un argomento 
a = function2(3)
b = function2(4)
#ritorna un valore output. modificando il numero della funzione.
print(a)
print(b)

#result:
#6
#8

def function3(x, y):
  return x + y 
#codice per definire una funzione considerando più elementi
e = function3(1, 2)
print(e)

#result: 3

def function4(x):
  print(x)
  print('still in this functions')
  return 3*x
#esempio di funzione che comprende più codici
f = function4(4)
print(e)

#result:
#4
#still in this functions
#3

def function5(some_argument):
  print(some_argument)
  print('weeee')
#definizione funzione generica, in questo caso tra parentesi possiamo definire qualsiasi variabile
function5(5)

#result:
#5
#weeee

'''
#XXXX  BMI CALCULATOR  XXXX
'''

name = 'Sarah'
height_m = 1.57
weight_kg = 56

bmi = weight_kg / (height_m**2)
print('bmi: ')
print(bmi)
if bmi < 25:
  print(name)
  print('is not overweight')
else:
  print(name)
  print('is overweight')

#result:
#bmi: 
#22.7189744005842
#Sarah 
#is not overweight

'''
#XXXXX  ADVANCED BMI CALCULATOR  XXXXX
'''

name1 = 'YK'
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
  bmi = weight_kg / (height_m**2)
  if bmi < 25:
    print(name + "'s bmi:")
    print(bmi)
    return name + ' is not overweight'
  else:
    print(name + "s'bmi:")
    print(bmi)
    return name + 'is overweight'

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

#result:
#YK's bmi:
#22.5
#YK's sister's bmi:
#21.604938271604937
#YK's brothers'bmi:
#25.6
#YK is not overweight
#YK's sister is not overweight
#YK's brotheris overweight

'''
#XXX  EXERCISE XXX
'''

#create a code to convert KM to MILES 
#x = miles
#km = 1.6* miles

def convert(x):
  km = 1.6*(x)
  return(km)
convert(10)

#result: 16.0

'''
#XXXXX  CICLI DI FOR  XXXXX
'''

a = ['banana', 'apple', 'microsoft']
print(a)

#result: ['banana', 'apple', 'microsoft']

for element in a:
  print(element)
#codice di for (per ogni elemento nella lista a, printa l'elemento).
#ho scritto element, ma posso usare qualsiasi parola

#result:
#banana
#apple
#microsoft

b = [20, 10, 5]
total = 10
for fausto in b:
  total = total + fausto
print(total)
#ciclo di for per sommare gli elementi di una lista ad un valore x.
#in questo caso ho usato la parola 'fausto' invece di 'element' per dimostrare di poter usare qualsiasi parola.

#result: 45

c = list(range(1,5))
print(c)
#codice per creare velocemente una lista 1, 2 ,3 , 4

#result: [1, 2, 3, 4]

total2 = 5
for i in range(1,5):
  total2 += i
print(total2)
#codice di for (somma tutti gli elementi in range da 1 a 4 e con il valore di total2)

#result: 15

print(list(range(1,8)))

#result: [1, 2, 3, 4, 5, 6, 7]

print(4 % 3)
#codice definito 'module operator' per 'remeinder' per ottenere il resto della divisione.
#in questo caso, resto di 4/3.

#result: 1

total3 = 1
for i in range(1, 8):
  if i % 3 == 0:
    total3 += i
print(total3)
#ciclo di for (per ogni elemento in lista da 1 a 7, se il resto di ogni elemento è = 0)
#allora somma il total3 con quel determinato elemento
#in questo caso i numeri con resto 0 sono 3 e 6, il totale è 1, quindi 1 +(3+6) = 10

#result: 10

'''
#XXX  EXERCISE XXX
'''

#can you compute all multiples of 3, 5
#that are lesss than 100?

d = list(range(1,100))
total4 = 0
for g in d:
  if g % 3 == 0:
    total4 += g
  elif g % 5 == 0:
    total4 += g
print(total4) 
#ciclo di for (per ogni elemento in lista da 1 a 7, se il resto di ogni elemento è = 0)
#allora somma il total3 con quel determinato elemento
#in questo caso i numeri con resto 0 sono 3 e 6, il totale è 1, quindi 1 +(3+6) = 10

#risultato: 2318

total5 = 0
for i in range(1, 100):
  if i % 3 == 0 or i % 5 == 0:
    total5 += i
print(total5)
#altro ciclo per ottenere lo stesso risultato

#risultato: 2318

'''
#XXXXXX  LEZIONE AVANZATA SU CICLI DI 'WHILE' E 'FOR'  XXXXXX  

#XXXXX  WHILE LOOPS  XXXXX
'''

total = 0
for i in range(1,5):
  total += i
print(total)

#risultato: 10

total2 = 0
j = 1
while j < 5:
  total2 += j 
  j += 1
print(total2)
#codice per definire una condizione loop di 'while'
#leggo (once we get to the while loop check if j is less than 5 and since its true do the following:)
#total2 si somma a j con risultato 1, il loop while continua fin quando j sarà uguale a 5
#di conseguenza avrò diversi step: tot = j(1), tot = 1+j(2), tot = 3 + j(3), tot = 6 + j(4).

#il loop termina a tot = 10 perchè la condizione si blocca a j = 5.

given_list = [5, 4, 4, 3, 1, -2, -3, -5]

total3 = 0
i = 0
while given_list[i] > 0:
  total3 += given_list[i]
  i += 1
print(total3)
#codice che funziona solo se in lista c'è lmeno un numero negativo

#risultato: 17

given_list = [5, 4, 4, 3, 1]

total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
  total3 += given_list[i]
  i += 1
print(total3)
#in questo caso il codice funziona perchè non inserisco l'indice dell'elemento lista
#utilizzo il codice lunghezza(lista)

#risultato: 17

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
  if element <= 0:
    break
  total4 += element
print(total4)
#in questo esempio includiamo sia i numeri positivi che negativi
#condizione (per ogni elemento in lista, somma gli elementi al tot4)
#altrimenti se negativo, interrompi il loop. (si blocca a -2)

#risultato: -2

#given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]

total5 = 0
i = 0
while True:
  total5 += given_list2[i]
  i += 1
  if given_list2[i] <= 0:
    break
print(total5)
#stesso codice ma usando la condizione di 'while True'

#risultato: 17

'''
#XXX  EXERCISE  XXX
'''

#calculate a for or while loop to obtain the sum of all negatives numbers.
#given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total5 = 0
i = 0

for element in given_list3:
  if element <= 0:
    total5 += element
print(total5)

#risultato: -17

'''
#XXXXX  MORE ABOUT FOR LOOPS  XXXXX
'''

a = ['apple', 'banana', 'republic']
print(a)

#result: ['apple', 'banana', 'republic']

for element in a:
  print(element)

#result: ['apple', 'banana', 'republic']

for i in range(0,3): #0, 1, 2
  print(a[i])

#result: ['apple', 'banana', 'republic']

for i in range(len(a)):
    print(a[i])

#result: ['apple', 'banana', 'republic']
