import PySimpleGUI as sg


def helpwindow():
    sg.theme("DarkTeal2")

    heading = [
        [sg.Text("Help",
                 font="14", justification='c', expand_x=True)],
    ]

    registeruser = [
        [sg.Text("To register a user", justification='c', expand_x=True)],
        [sg.Text("1. Click the Register button on the main screen.")],
        [sg.Text("2. Fill out these fields:")],
        [sg.Text("first name, last name, address, mobile, email, their membership options, extra options and payment options")],
        [sg.Text("3. Click on the Calculate button to view the membership summary.")],
        [sg.Text('4. Click on the Clear button to reset all inputs.')],
        [sg.Text('5. Click on Submit to save the user.')]
    ]

    searchusers = [
        [sg.Text("To search for a user", justification='c', expand_x=True)],
        [sg.Text("1. Click on the Search button on the main screen.")],
        [sg.Text("2. Enter a user's email address.")],
        [sg.Text("3. Click on the search button to perform the search action")],
        [sg.Text("4. If a user with the provided parameter exists, results will be displayed in the search results frame.")],
        [sg.Text("5. If a user does not exists, a popup will be displayed.")]
    ]

    fitness = [
        [sg.Text("To enroll a user to a fitness program",
                 justification='c', expand_x=True)],
        [sg.Text("1. Click on the Fitness button on the main screen.")],
        [sg.Text("2. Enter a member's member Id or last name on the Find Member frame.")],
        [sg.Text(
            "3. Click on Find button to get the users details and to populate other user fields.")],
        [sg.Text("4. Select the program for which they wish to enroll into.")],
        [sg.Text("5. Click on the Enroll button to save the user's enrollment details.")]
    ]

    layout = [[heading],
              [sg.Stretch(), sg.Frame('Register Members', registeruser,
                                      size=(800, 190)), sg.Stretch()],
              [sg.Stretch(), sg.Frame('Search Members', searchusers,
                                      size=(800, 180)), sg.Stretch()],
              [sg.Stretch(), sg.Frame('Fitness Enrollment',
                                      fitness, size=(800, 180)), sg.Stretch()],
              [sg.Stretch(), sg.Button('Home')]
              ]

    window = sg.Window("Help", layout, size=(800, 640))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Home':
            window.close()
            break
