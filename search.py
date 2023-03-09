import PySimpleGUI as sg
from help import helpwindow
from utils import searchmbr, deletembr


def searchwindow():
    sg.theme("DarkTeal2")

    heading = [
        [sg.Text("City Gym Search Members",
                 font="14", justification='c', expand_x=True)],
    ]

    searchinput = [
        [sg.Text('Last Name:'), sg.InputText(
            key='searchlname', do_not_clear=True, size=(80, 4))],
        [sg.Text('Member ID:'), sg.InputText(
            key='searchid', do_not_clear=True, size=(80, 4))]
    ]

    searchresults = [
        [sg.Text('first name:'), sg.Text(key='fname')],
        [sg.Text('last name:'), sg.Text(key='lname')],
        [sg.Text('address:'), sg.Text(key='address')],
        [sg.Text('mobile:'), sg.Text(key='mobile')],
        [sg.Text('email:'), sg.Text(key='email')],
        [sg.Text('fitness class:'), sg.Text(key='fitness')],
    ]

    layout = [[heading],
              [sg.Stretch(),
               sg.Frame(
                  'Search members by their last name or member Id', searchinput, size=(600, 110)), sg.Stretch()],
              [sg.Stretch(), sg.Frame('Search results', searchresults,
                                      size=(600, 200)), sg.Stretch()],
              [sg.Stretch(), sg.Button('Search'),
               sg.Button('Delete'), sg.Button('Help'), sg.Button('Home')]]

    window = sg.Window("City Gym Search", layout)

    while True:
        event, values = window.read()
        global memberid

        if event == sg.WIN_CLOSED or event == 'Home':
            window.close()
            break
        elif event == 'Help':
            window.close()
            helpwindow()
        elif event == 'Search':
            try:
                searchres = searchmbr(
                    mbrid=values['searchid'], lastname=values['searchlname'])
                memberid = searchres[0][0]
                window['fname'].update(searchres[0][1])
                window['lname'].update(searchres[0][2])
                window['address'].update(searchres[0][3])
                window['mobile'].update(searchres[0][4])
                window['email'].update(searchres[0][5])

                if len(searchres[0]) == 7:
                    window['fitness'].update(searchres[0][6])
                else:
                    window['fitness'].update(
                        'Members is not enrolled to a fitness program')
            except Exception as e:
                sg.popup('Record for the selected user was not found')
        elif event == 'Delete':
            try:
                deletembr(mbrid=memberid)
                sg.popup('User was successfully deleted')
            except:
                sg.popup(
                    'En error occured while trying to delete member, try again')
        else:
            pass
