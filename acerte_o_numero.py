import random

print('Seja bem vindo ao GUESS NUMBER!')

choice_number = input('Digite o número inteiro para começar o desafio: ')

if choice_number.isdigit():
    choice_number = int(choice_number)

else:
    print('ERRO: Digite um valor inteiro númerico!')
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input('Adivinhe o número: ')

    if answer_user.isdigit():
        answer_user = int(answer_user)

    else:
        print('ERRO: Digite um valor inteiro númerico!')
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print('Acertou o número, PARABENS')
        break
    
    elif answer_user > random_number:
        print('Chute alto em, o numero é menor que isso')

    else:
        print('Chute baixo em, o numero é maior que isso')

print(f'Tentativas: {n_choices}')