import PySimpleGUI as sg
from register import registerwindow
from search import searchwindow
from fitness import fitnesswindow
from help import helpwindow

sg.theme("DarkTeal2")

heading = [
    [sg.Text("City Gym App",
             font="16", justification='c', expand_x=True, pad=(12, 12))]
]

description = [
    [sg.Text('City Gym App allows you to efficiently manage users',
             font='14', justification='c', expand_x=True, pad=(16, 16))]
]

layout = [[heading],
          [description],
          [sg.Stretch(), sg.Button('Register', pad=(16, 16)), sg.Button('Search', pad=(16, 16)),
          sg.Button('Fitness', pad=(16, 16)), sg.Button(
              'Help', pad=(16, 16)), sg.Button('Quit', pad=(16, 16)),
           sg.Stretch()]
          ]

window = sg.Window("City Gym", layout, size=(600, 250))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Register':
        registerwindow()
    elif event == 'Search':
        searchwindow()
    elif event == 'Fitness':
        fitnesswindow()
    elif event == 'Help':
        helpwindow()
    else:
        pass
