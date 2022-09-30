# visual_part.py
import PySimpleGUI as sg
import random as r

def is_not_valid(s):
    if s.isdigit():
        if int(s) == float(s):
            if 0 < int(s) < 101:
                return False
    return True

print('Choose the theme 1 - Dark, 2 - Blue, 3 - Va-11 Hall-A')
theme_num = input()
if theme_num.isdigit() and theme_num in ['1', '2', '3']:
    theme_num = int(theme_num)
else:
    print('Wrong data - theme set as default')
    theme_num = 1
theme_names = ['DarkAmber', 'BluePurple', 'DarkPurple1']
sg.theme(theme_names[theme_num - 1])


layout = [  [sg.Text('''Hi! Let's play the game! 
I have a number from 1 to 100 - try to guess it. You will have only 7 attempts''')],
            [sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Text(key='-ANSWER-')],
            [sg.Text('Enter the number to guess'), sg.Input(key='-IN NUM-')],
            [sg.Button('Send'), sg.Exit('Close')],
            ]

window = sg.Window('The number guess game', layout)
guess_num = r.randrange(1, 101)
game_result = 'START'
game_cycle = 0

while game_cycle < 7:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break

    game_cycle += 1
    if is_not_valid(values['-IN NUM-']):
        game_result = 'WRONG'
        break

    num_input = int(values['-IN NUM-'])
    if event == 'Send':
        window['-OUTPUT-'].update('Your num is: ' + str(num_input))
        if num_input == guess_num:
            game_result = 'WON'
            break
        elif num_input > guess_num:
            window['-ANSWER-'].update('my num is less')
        else:
            window['-ANSWER-'].update('my num is bigger')

    if game_cycle == 7:
        game_result = 'LOSE'

window.close()

if game_result == 'WON':
    sg.popup('You Won! Congratulation!')
elif game_result == 'LOSE':
    sg.popup('You lose, sorry! =(')
elif game_result == 'WRONG':
    sg.popup('Wrong data. Only int from 1 to 100 are allowed')
elif game_result == 'START':
    sg.popup('You have closed the game, enjoy your day!')