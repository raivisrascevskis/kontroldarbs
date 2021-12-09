def pirmais():
  print('Ievadi četrus skaitļus')
  

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

global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("atbildi uz jautajumiem")
guess1 = input("popularaka programa kodešanai? ")
check_guess(guess1, "python")
guess2 = input("kura gada izveidoja python? ")
check_guess(guess2, "1991")
guess3 = input("vai c++ ir programma kodešanai ja vai ne? ")
check_guess(guess3, "ja")
guess4 = input("vai tev patik programmet? ")
check_guess(guess4, "ja")

print("Your Score is "+ str(score))

