import PySimpleGUI as sg
from help import helpwindow
from utils import searchenrollmbr, createnrollmnt


def fitnesswindow():
    sg.theme("DarkTeal2")

    heading = [
        [sg.Text("Fitness",
                 font="14", justification='c', expand_x=True)]
    ]

    filteruser = [
        [sg.InputText(key='searchval', do_not_clear=True, size=(100, 4))],
        [sg.Text('first name:'), sg.Text(key='fname')],
        [sg.Text('last name:'), sg.Text(key='lname')],
        [sg.Text('address:'), sg.Text(key='address')],
        [sg.Text('mobile:'), sg.Text(key='mobile')],
        [sg.Text('email:'), sg.Text(key='email')]
    ]

    selectprogram = [
        [sg.Radio("Cardio, Thursday, 3Pm - 5Pm", "enrollment", key='1')],
        [sg.Radio("Pilates, Friday, 9Am - 11Am", "enrollment", key='2')],
        [sg.Radio("Spin, Monday, 2Pm - 4Pm", "enrollment", key='3')]
    ]

    layout = [
        [heading],
        [sg.Stretch(), sg.Frame('Find Member',
                                filteruser, size=(600, 160)), sg.Stretch()],
        [sg.Stretch(), sg.Frame('Select program to enroll',
                                selectprogram, size=(600, 100)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Find'), sg.Button('Enroll'),
         sg.Button('Help'), sg.Button('Home')]
    ]

    window = sg.Window("Fitness Enrollment", layout, size=(600, 360))

    while True:
        event, values = window.read()
        global memberid

        if event == sg.WIN_CLOSED or event == 'Home':
            window.close()
            break
        elif event == 'Help':
            window.close()
            helpwindow()
        elif event == "Find":
            try:
                searchres = searchenrollmbr(
                    mbrid=values['searchval'], lastname=values['searchval'])
                memberid = searchres[0][0]
                window['fname'].update(searchres[0][1])
                window['lname'].update(searchres[0][2])
                window['address'].update(searchres[0][3])
                window['mobile'].update(searchres[0][4])
                window['email'].update(searchres[0][5])
            except IndexError:
                sg.popup('Record for the selected user was not found')

        elif event == "Enroll":
            selectedprogram = int()

            if values['1'] == True:
                selectedprogram = 1
            elif values['2'] == True:
                selectedprogram = 2
            elif values['3'] == True:
                selectedprogram = 3
            else:
                sg.popup('Select a program to enroll into')

            try:
                createnrollmnt(mbrid=memberid, fitness=selectedprogram)
                sg.popup('Member was successfully enrolled')
            except:
                sg.popup('An error occurred, unable to process enrollment')

        else:
            pass
