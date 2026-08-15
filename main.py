# HANGMAN GAME
import os
import sys
import subprocess
import random

# VARIABLES
arquivo = 'words.txt'
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

with open(arquivo, 'r') as data:
    for word in data:
        words.append(word.strip())
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

        while True: 
            cur_attempt = input("Digite uma letra: ")
            if len(cur_attempt) != 1 or not cur_attempt.isalpha():
                print('Por favor, digite uma letra válida.')
                continue
            break

        if cur_attempt in past_attempts:
            print('Essa letra já foi tentada. Tente novamente.')
            cur_attempt = input()

        cur_attempt = cur_attempt.upper()

        past_attempts.append(cur_attempt)

        if cur_attempt not in word:
            remaining_attempts-=1
        if all(char in past_attempts for char in word):
            won = True
            break

        clear_terminal()

if tries == 0:
    run_game()

clear_terminal()
if won:
    print(f'Parabéns! Você acertou a palavra: {word}')
elif tries != 0:
    print(f'Fim de jogo! A palavra era: {word}')

