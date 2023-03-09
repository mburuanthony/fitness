import os
import math
import pytest
import PySimpleGUI as sg

# Test for theme


def test_theme():
    sg.theme("DarkTeal2")
    assert sg.theme() == "DarkTeal2"


# Test for input fields
def test_input_fields():
    layout = [
        [sg.Text("First Name: "), sg.InputText(key="-FIRST NAME-")],
        [sg.Text("Last Name: "), sg.InputText(key="-LAST NAME-")],
        [sg.Text("Address: "), sg.InputText(key="-ADDRESS-")],
        [sg.Text("Mobile: "), sg.InputText(key="-MOBILE-")],
        [sg.Text("Email: "), sg.InputText(key="-EMAIL-")],
    ]

    window = sg.Window("Test Input Fields", layout)

    event, values = window.read()

    assert event == sg.WINDOW_CLOSED
    assert values["-FIRST NAME-"] != ""
    assert values["-LAST NAME-"] != ""
    assert values["-ADDRESS-"] != ""
    assert values["-MOBILE-"] != ""
    assert values["-EMAIL-"] != ""

# Test for radio buttons


def test_radio_buttons():
    layout = [
        [sg.Text("Type"), sg.Radio("Basic", "Type", key="-BASIC-"), sg.Radio("Regular",
                                                                             "Type", key="-REGULAR-"), sg.Radio("Premium", "Type", key="-PREMIUM-")],
        [sg.Text("Duration"), sg.Radio("3 Months", "Duration", key="-3MONTHS-"), sg.Radio("12 Months",
                                                                                          "Duration", key="-12MONTHS-"), sg.Radio("24 Months", "Duration", key="-24MONTHS-")],
    ]

    window = sg.Window("Test Radio Buttons", layout)

    event, values = window.read()

    assert event == sg.WINDOW_CLOSED
    assert any(key in values for key in ["-BASIC-", "-REGULAR-", "-PREMIUM-"])
    assert any(key in values for key in [
               "-3MONTHS-", "-12MONTHS-", "-24MONTHS-"])

# Test for checkboxes


def test_checkboxes():
    layout = [
        [sg.Checkbox("24/7 Access", key="-EXTRA1-"),
         sg.Checkbox("Diet Consultation", key="-EXTRA2-")],
        [sg.Checkbox("Online fitness videos", key="-EXTRA3-"),
         sg.Checkbox("Personal Trainer", key="-EXTRA4-")],
    ]

    window = sg.Window("Test Checkboxes", layout)

    event, values = window.read()

    assert event == sg.WINDOW_CLOSED
    assert any(key in values for key in [
               "-EXTRA1-", "-EXTRA2-", "-EXTRA3-", "-EXTRA4-"])


def test_gui():
    # create the layout
    layout = [
        [sg.Text("First Name: "), sg.InputText(key="-FIRST NAME-")],
        [sg.Text("Last Name: "), sg.InputText(key="-LAST NAME-")],
        [sg.Text("Address: "), sg.InputText(key="-ADDRESS-")],
        [sg.Text("Mobile: "), sg.InputText(key="-MOBILE-")],
        [sg.Text("Email: "), sg.InputText(key="-EMAIL-")],
        [sg.Button("Submit")]
    ]
    # create the window
    window = sg.Window("Test GUI", layout)
    # start the event loop
    event, values = window.read()
    # check if the submit button was clicked
    assert event == "Submit"
    # check if the input fields are not empty
    assert values["-FIRST NAME-"] != ""
    assert values["-LAST NAME-"] != ""
    assert values["-ADDRESS-"] != ""
    assert values["-MOBILE-"] != ""
    assert values["-EMAIL-"] != ""


def test_members_data_saved():
    # create the layout
    layout = [
        [sg.Text("First Name: "), sg.InputText(key="-FIRST NAME-")],
        [sg.Text("Last Name: "), sg.InputText(key="-LAST NAME-")],
        [sg.Text("Address: "), sg.InputText(key="-ADDRESS-")],
        [sg.Text("Mobile: "), sg.InputText(key="-MOBILE-")],
        [sg.Text("Email: "), sg.InputText(key="-EMAIL-")],
        [sg.Button("Submit")]
    ]
    # create the window
    window = sg.Window("Test GUI", layout)
    # start the event loop
    event, values = window.read()
    # check if the submit button was clicked
    if event == "Submit":
        with open("membersdatasaved.txt", "w") as f:
            f.write(values["-FIRST NAME-"] + "\n")
            f.write(values["-LAST NAME-"] + "\n")
            f.write(values["-ADDRESS-"] + "\n")
            f.write(values["-MOBILE-"] + "\n")
            f.write(values["-EMAIL-"] + "\n")

    assert event == "Submit"
    # check if the input fields are not empty
    assert values["-FIRST NAME-"] != ""
    assert values["-LAST NAME-"] != ""
    assert values["-ADDRESS-"] != ""
    assert values["-MOBILE-"] != ""
    assert values["-EMAIL-"] != ""
    # check if the members data saved in the file
    assert os.path.exists("membersdatasaved.txt")
    with open("membersdatasaved.txt", "r") as f:
        data = f.read()
    assert values["-FIRST NAME-"] in data
    assert values["-LAST NAME-"] in data
    assert values["-ADDRESS-"] in data
    assert values["-MOBILE-"] in data
    assert values["-EMAIL-"] in data
    # delete the file after the test
    os.remove("membersdatasaved.txt")

# Test that the net calculations are correct


def calculate_net_membership_cost(membership_type, duration, extras, direct_debit, payment_frequency):
    base_cost = 0
    if membership_type == "Basic":
        base_cost = 10
    elif membership_type == "Regular":
        base_cost = 15
    elif membership_type == "Premium":
        base_cost = 20
    else:
        raise ValueError("Invalid membership type")

    duration_multiplier = 1
    if duration == "3 Months":
        duration_multiplier = 3
    elif duration == "12 Months":
        duration_multiplier = 12
    elif duration == "24 Months":
        duration_multiplier = 24
    else:
        raise ValueError("Invalid duration")

    extras_cost = 0
    for extra in extras:
        if extra == "24/7 Access":
            extras_cost += 1
        elif extra == "Diet Consultation":
            extras_cost += 20
        elif extra == "Online fitness videos":
            extras_cost += 2
        elif extra == "Personal Trainer":
            extras_cost += 20
        else:
            raise ValueError("Invalid extra option")

    net_cost = base_cost * duration_multiplier + extras_cost
    discount = 0
    if duration == "12 Months":
        discount = 2
    elif duration == "24 Months":
        discount = 5
    if direct_debit:
        discount += net_cost * 0.01
    net_cost -= discount

    if payment_frequency == "Weekly":
        return net_cost
    elif payment_frequency == "Monthly":
        return net_cost * 4
    else:
        raise ValueError("Invalid payment frequency")
