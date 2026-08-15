# HANGMAN GAME
import os
import sys
import subprocess
import random

# VARIABLES
arquivo = 'palavras.txt'
MAX_ATTEMPTS = 10

# CODE

def clear_terminal():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run([command])

if not os.path.exists(arquivo) or os.path.getsize(arquivo) == 0:
    print(f"Erro: O arquivo '{arquivo}' não existe ou está vazio.")
    sys.exit(1)

words = []
word = ''

won = False
tries = 0

with open("palavras.txt", 'r') as data:
    for word in data:
        words.append(word)
        if not all(char.isalpha() for char in word):
            continue

def run_game():
    global tries, won, word
    tries+=1


    word = random.choice(words).upper()

    remaining_attempts = MAX_ATTEMPTS
    past_attempts = []
    cur_attempts = 0

    while remaining_attempts > 0 and not won:
        print("Bem vindo ao jogo da forca! \n")


        for char in word:
            if char in past_attempts:
                print(f"{char} ", end="")
            else:
                print("_", end=" ")
        print('\n')

        print("Tentativas restantes: ", end="")
        print(remaining_attempts)

        print("Letras tentadas:", end=" ")

        cur_show = 1
        for attempt in past_attempts:
            if cur_show == cur_attempts:
                print(f"{attempt}", end="")
            else:
                print(f"{attempt}, ", end="")

        print('\n')

        print("Digite uma letra: ", end="")
        cur_attempt = input()

        if not cur_attempt.isalpha():
            print('Por favor, digite uma letra válida.')
            cur_attempt = input()

        if cur_attempt in past_attempts:
            print('Essa letra já foi tentada. Tente novamente.')
            cur_attempt = input()

        cur_attempt = cur_attempt.upper()

        past_attempts.append(cur_attempt)

        remaining_attempts-=1
        if all(char in past_attempts for char in word):
            won = True
            break

        clear_terminal()

if tries == 0:
    run_game()

answer = '0'
while not answer.isalpha() or not (answer.upper() == 'S' or answer.upper() == 'N'):
    print(f"A palavra era {word}")
    if won:
        print('Parabéns você ganhou!')
    elif tries != 0:
        print('Você perdeu.')

    print('Quer tentar de novo? (S/N)')
    answer = input()

    if answer.upper() == "S":
        clear_terminal()
        run_game()
