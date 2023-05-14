import random as rd

score_list = []

def show_score():
    if not score_list:
        print('There\'s currently no high score, Give it a try !')
    else:
        print(f'High score is {min(score_list)} attempts !')
def start_game():
    attempts = 0
    print('Hello ! Welcome to the guessing game !')
    player_name = input('Please enter your name. ')
    play = input(f'Hello ! , {player_name}, do you want to play ? (Enter Yes/No): ')

    if play.lower() != 'yes':
        print('Cool , Thank You ! :) ')
        exit()
    else:
        r = int(input('Enter the first number: '))
        s = int(input('Enter another number (It should be different and greater than the last entered number !: '))
        rnum = rd.randint(r, s)
        show_score()
    while play.lower() == 'yes':
        try:
            guess = int(input(f'Pick a number between {r} and {s}: '))
            if guess <r or guess >s:
                raise ValueError(f'Please guess a number between{r} and {s}')
            attempts += 1
            score_list.append(attempts)

            if guess == rnum:
                print('Nice! You got it :0')
                print(f'It took you {attempts} attempts .')
                play = input(' Do you want to play  again ? (Enter Yes/No)" ')
                if play.lower() != 'yes':
                    print('Okay Bye bye :D.')
                    break
                else:
                    attempts = 0
                    r = int(input('Enter the first number: '))
                    s = int(input(
                        'Enter another number (It should be different and greater than the last entered number !): '))
                    rnum = rd.randint(r, s)
                    show_score()
                    continue

            else:
                if guess > rnum:
                    print('It\'s lower')
                elif guess < rnum:
                    print('It\'s higher')
        except ValueError as error:
            print('Invalid value :( , Please try again.')

if __name__ == '__main__':
    start_game()