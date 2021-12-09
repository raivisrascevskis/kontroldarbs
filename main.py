def pirmais():
  vertibas = []
  for i in range(4):
   a= int(input("Ievadiet vērtības"))
   vertibas.append(a)

  print(vertibas)

  print(vertibas[1] * (vertibas[3]))
  
def otrais():
  print('ievadi 5 skaitļus no -10 lidz 10' )
  count = 0
  for i in range(5):
   num = eval(input('Ievadi skaitli: '))
  
  print('Tavi skaitli ir.')
  print(num)

  
  

  

def tresais():
  def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Pareiza atbilde!')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Piedodiet, nepareiza atbilde.')
            attempt = attempt + 1

        if attempt == 3:
            print('Pareiza atbilde ir ' + answer+'.')
    
  score = 0
  print("Atbildiet uz jautajumiem")
  guess1 = input("Popularaka programa kodesanai? ")
  check_guess(guess1, "python")
  guess2 = input("Kura gada izveidoja Python? ")
  check_guess(guess2, "1991")
  guess3 = input("Vai c++ ir programma kodešanai ja vai ne? ")
  check_guess(guess3, "Ja")
  guess4 = input("Vai tev patik programmet? ")
  check_guess(guess4, "Ja")
  print("Tavs punktu skaits ir "+ str(score))

  
   
  
  
  
  
  
print('Kuru no uzdevumiem vēlies realizēt')
print('Izvēlies ciparu')
print('1 - pirmo uzdevumu')
print('2- otro uzdevumu')
print('3 - trešo uzdevumu')
print('__________________')
print('Tu esi izvēlējies uzdevumu nr. ')

Izvele = input()

if Izvele == '1':
  pirmais()
  
if Izvele == '2':
 otrais()

if Izvele == '3':
 tresais()
  
  1 - raivis
  2 - eriks
  3 - niks
 



