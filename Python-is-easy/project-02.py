import random

def main():
    words = ['juice', 'badminton', 'marvel', 'textbook', 'choice', 'difference', 'alliance', 'sorting']
    word = random.choice(words)
    field = list('_' * len(word))
    print(' '.join(field))
    
    attempts = 10

    while (attempts > 0):
        guess = input('\nChoose a letter: ')

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    field[i] = guess
            print(' '.join(field))

            if '_' not in field:
                print('Congratulations! You won!')
                return

        else:
            attempts -= 1
            print(' '.join(field))
            print(f'\nThe word doesn\'t contain the letter {guess}')
            print(f'{attempts} attempts left.')

    print('Sorry, you lost!')
    
main()
