import PySimpleGUI as sg
from utils import creatembr


def registerwindow():
    sg.theme("DarkTeal2")

    # Heading
    heading = [
        [sg.Text("City Gym Membership Registration",
                 font="14", justification='c', expand_x=True)],
    ]

    # Customer Details
    customer_details = [
        [sg.Text("First Name: "), sg.Push(), sg.InputText(
            key="-FIRST NAME-", do_not_clear=True, size=(63, 1))],
        [sg.Text("Last Name: "), sg.Push(), sg.InputText(
            key="-LAST NAME-", do_not_clear=True, size=(63, 1))],
        [sg.Text("Address: "), sg.Push(), sg.InputText(
            key="-ADDRESS-", do_not_clear=True, size=(63, 1))],
        [sg.Text("Mobile: "), sg.Push(), sg.InputText(
            key="-MOBILE-", do_not_clear=True, size=(63, 1))],
        [sg.Text("Email: "), sg.Push(), sg.InputText(
            key="-EMAIL-", do_not_clear=True, size=(63, 1))],
    ]

    # Membership Options
    base_membership = [
        [sg.Text("Type"), sg.Radio("Basic - $10.00 Weekly", "Type", key="-BASIC-"), sg.Radio("Regular - $15.00 Weekly",
                                                                                             "Type", key="-REGULAR-"), sg.Radio("Premium - $20.00 Weekly", "Type", key="-PREMIUM-")],
        [sg.Text("Duration"), sg.Radio("3 Months", "Duration", key="-3MONTHS-"), sg.Radio("12 Months",
                                                                                          "Duration", key="-12MONTHS-"), sg.Radio("24 Months", "Duration", key="-24MONTHS-")],
        [sg.Text(
            "Sign up for 12-months contract to received a $2 per week discount on any membership type.")],
        [sg.Text(
            "Sign up for 24-months contract to received a $5 per week discount on any membership type.")],
    ]

    # Extra options
    extras = [
        [sg.Checkbox("24/7 Access ($1 per week)", key="-EXTRA1-"),
         sg.Checkbox("Diet Consultation ($20 per week)", key="-EXTRA2-")],
        [sg.Checkbox("Online fitness videos ($2 per week)", key="-EXTRA3-"),
         sg.Checkbox("Personal Trainer ($20 per week)", key="-EXTRA4-")],
    ]

    # Payment options
    payment_options = [
        [sg.Text("For direct debits, there is a 1% discount on the base membership cost.")],
        [sg.Text("Pay by Direct Debit? "), sg.Radio("Yes", "Direct Debit",
                                                    key="-YES-"), sg.Radio("No", "Direct Debit", key="-NO-")],
        [sg.Text("Payment Frequency"), sg.Radio("Weekly", "Frequency",
                                                key="-WEEKLY-"), sg.Radio("Monthly", "Frequency", key="-MONTHLY-")],
    ]

    # Membership Summary
    membership_summary = [
        [sg.Text("Base Membership cost : ")],
        [sg.Text("Extra charges: ")],
        [sg.Text("Total discount: ")],
        [sg.Text("Net membership cost: ")],
        [sg.Text("Regular payment amount: ")],
    ]

    # Layout of GUI
    layout = [
        [heading],
        [sg.Stretch(), sg.Frame("Customer Details", customer_details,
                                size=(600, 155)), sg.Stretch()],
        [sg.Stretch(), sg.Frame("Membership Options",
                                base_membership, size=(600, 140)), sg.Stretch()],
        [sg.Stretch(), sg.Frame("Extra Options", extras, size=(600, 85)), sg.Stretch()],
        [sg.Stretch(), sg.Frame("Payment Options", payment_options,
                                size=(600, 110)), sg.Stretch()],
        [sg.Stretch(), sg.Frame("Membership Summary",
                                membership_summary, size=(600, 150)), sg.Stretch()],
        [sg.Stretch(), sg.Button("Calculate"), sg.Button(
            "CLEAR"), sg.Button("Submit"), sg.Stretch(), sg.Button('Close')],
    ]

    window = sg.Window("BIT502 Assessment 2 - RASELL V 5074751",
                       layout, size=(650, 800))

    # Input functions

    def formatInputInformation(values):
        information = "Submitted!"
        firstname = "\nFirst Name: " + values["-FIRST NAME-"]
        information += firstname
        lastname = "\nLast Name: " + values["-LAST NAME-"]
        information += lastname
        address = "\nAddress: " + values["-ADDRESS-"]
        information += address
        mobile = "\nMobile: " + values["-MOBILE-"]
        information += mobile
        email = "\nEmail: " + values["-EMAIL-"]
        information += email
        membership_type = "\nMembership_options: " + values["-MEMBERSHIP-"]
        information += membership_type
        membership_duration = "\nDuration: " + values["-DURATION-"]
        information += membership_duration
        payment = "\nDirect Debit: "
        if values["-YES-"]:
            payment += "Yes"
        else:
            payment += "No"
        information += payment
        paymentfrequency = "\nPayment Frequency: "
        if values["-WEEKLY-"]:
            paymentfrequency += "Weekly"
        else:
            paymentfrequency += "Monthly"
        information += paymentfrequency
        extras = "\nExtra Options: "
        if values["-EXTRA1-"]:
            extras += "24/7 Access ($1 per week)"
        if values["-EXTRA2-"]:
            extras += "Diet Consultation ($20 per week)"
        if values["-EXTRA3-"]:
            extras += "Online fitness videos ($2 per week)"
        if values["-EXTRA4-"]:
            extras += "Personal Trainer ($20 per week)"
        information += extras

        return information

    # Validates inputs to ensure user completes all sections of registration form requirements

    def validate(values):
        is_valid = True
        values_invalid = []

        if len(values["-FIRST NAME-"]) == 0:
            values_invalid.append("First Name")
            is_valid = False
        if len(values["-LAST NAME-"]) == 0:
            values_invalid.append("Last Name")
            is_valid = False
        if len(values["-ADDRESS-"]) == 0:
            values_invalid.append("Address")
            is_valid = False
        if len(values["-MOBILE-"]) == 0:
            values_invalid.append("Mobile")
            is_valid = False
        if len(values["-EMAIL-"]) == 0:
            values_invalid.append("Email")
            is_valid = False
        if not values["-BASIC-"] and not values["-REGULAR-"] and not values["-PREMIUM-"]:
            values_invalid.append("Membership Type")
            is_valid = False
        if not values["-3MONTHS-"] and not values["-12MONTHS-"] and not values["-24MONTHS-"]:
            values_invalid.append("Membership Duration")
            is_valid = False
        if not values["-YES-"] and not values["-NO-"]:
            values_invalid.append("Payment Option")
            is_valid = False
        if not values["-WEEKLY-"] and not values["-MONTHLY-"]:
            values_invalid.append("Payment Frequency")
            is_valid = False

        result = [is_valid, values_invalid]

        return result

    # Generates error message when inputs are incomplete

    def generate_error_message(values_invalid):
        error_message = ""
        for value_invalid in values_invalid:
            error_message += ("\nInvalid" + ":" + value_invalid)
        return error_message

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            window.close()
            break
        # Calucaltes membership and discount cost
        extra_charges = (0)
        total_discount = (0)
        base_cost = (0)
        regular_payment = ("$0.00")

        if values['-BASIC-'] == True:
            type_of_membership = ("Basic")
            base = ("$10.00")
            base_cost = (10)

        elif values['-REGULAR-'] == True:
            type_of_membership = ("Regular")
            base = ("$15.00")
            base_cost = (15)

        elif values['-PREMIUM-'] == True:
            type_of_membership = ("Premium")
            base = ("$20.00")
            base_cost = (20)

        if values['-3MONTHS-'] == True:
            duration = ("Three months")

        elif values['-12MONTHS-'] == True:
            duration = ("Twelve months")
            total_discount = (total_discount + 2)

        elif values['-24MONTHS-'] == True:
            duration = ("Twenty-four months")
            total_discount = (total_discount + 5)

        if values['-YES-'] == True:
            payment_method = ("Direct debit")
            debit_discount = (base_cost/100)
            total_discount = (debit_discount + total_discount)

        if values['-EXTRA1-'] == True:
            extra_charges = (extra_charges + 1)

        if values['-EXTRA3-'] == True:
            extra_charges = (extra_charges + 2)

        if values['-EXTRA4-'] == True:
            extra_charges = (extra_charges + 20)

        if values['-EXTRA2-'] == True:
            extra_charges = (extra_charges + 20)

        if values['-WEEKLY-'] == True:
            frequency_of_payment = ("Weekly")
            try:  # Attempt to calculate the regular payment, format it as a currency and convert it to a string
                regular_payment = str('${:,.2f}'.format(
                    base_cost + extra_charges - total_discount))

            except:  # If calculation is unsuccessful, the regular payment should be displayed as $0.00
                regular_payment = ("$0.00")

        # If "Monthly" payment option is selected...
        elif values['-MONTHLY-'] == True:
            # store frequency of payment in a variable to be displayed in user's file
            frequency_of_payment = ("Monthly")

            try:  # Attempt to calculate the regular payment, format it as a currency and convert it to a string
                regular_payment = str('${:,.2f}'.format(
                    (base_cost + extra_charges - total_discount) * 4))

            except:  # If calculation is unsuccessful, the "Regular payment" should be displayed as $0.00
                regular_payment = ("$0.00")

        try:  # Attempt to calculate the net cost, format it as a currency and convert it to a string
            net_cost = str('${:,.2f}'.format(
                base_cost + extra_charges - total_discount))

        except:  # If calculation is unsuccessful, the "Net cost" should be displayed as $0.00
            net_cost = "$0.00"

        try:  # Attempt to calculate the total discount, format it as a currency and convert it to a string
            total_discount = ('${:,.2f}'.format(total_discount))

        except:  # If calculation is unsuccessful, the "Total discount" should be displayed as $0.00
            total_discount = ("$0.00")

        try:  # Attempt to calculate the extra charges, format it as a currency and convert it to a string
            extra_charges = ('${:,.2f}'.format(extra_charges))

        except:  # If calculation is unsuccessful, the "Extra charges" should be displayed as $0.00
            extra_charges = ("$0.00")

        if event == "Calculate":
            first_name = values["-FIRST NAME-"]
            last_name = values["-LAST NAME-"]
            address = values["-ADDRESS-"]
            mobile = values["-MOBILE-"]
            email = values["-EMAIL-"]

            # Added error message here for calculations if data is missing
            if not all([first_name, last_name, address, mobile, email]):
                sg.Popup(
                    "Error", "Please fill in all the fields before calculating.")
            else:
                # Perform calculations here
                membership_summary[0][0].update(
                    f"Base membership cost: {base}")
                membership_summary[1][0].update(
                    f"Extra charges: {extra_charges}")
                membership_summary[2][0].update(
                    f"Total discount: {total_discount}")
                membership_summary[3][0].update(
                    f"Net membership cost: {net_cost}")
                membership_summary[4][0].update(
                    f"Regular payment amount: {regular_payment}")

        # This will address the form CLEAR function
        elif event == "CLEAR":
            window["-FIRST NAME-"].update("")
            window["-LAST NAME-"].update("")
            window["-ADDRESS-"].update("")
            window["-MOBILE-"].update("")
            window["-EMAIL-"].update("")
            window["-BASIC-"].update(False)
            window["-REGULAR-"].update(False)
            window["-PREMIUM-"].update(False)
            window["-3MONTHS-"].update(False)
            window["-12MONTHS-"].update(False)
            window["-24MONTHS-"].update(False)
            window["-EXTRA1-"].update(False)
            window["-EXTRA2-"].update(False)
            window["-EXTRA3-"].update(False)
            window["-EXTRA4-"].update(False)
            window["-YES-"].update(False)
            window["-NO-"].update(False)
            window["-WEEKLY-"].update(False)
            window["-MONTHLY-"].update(False)

    # Making the submit button save to the txt file called membersdatasaved to C:Temp, and not deleting data
        elif event == "Submit":
            """
            with open("membersdatasaved.txt", "a") as f:
                f.write("Customer Details: \n")
                f.write("First Name: " + values["-FIRST NAME-"] + "\n")
                f.write("Last Name: " + values["-LAST NAME-"] + "\n")
                f.write("Address: " + values["-ADDRESS-"] + "\n")
                f.write("Mobile: " + values["-MOBILE-"] + "\n")
                f.write("Email: " + values["-EMAIL-"] + "\n")
                f.write("Membership Options: \n")
                # Write the total_discount to the file
                f.write(f"Total discount: {total_discount}\n")
                if values["-BASIC-"]:
                    f.write("Type: Basic - $10.00 Weekly\n")
                elif values["-REGULAR-"]:
                    f.write("Type: Regular - $15.00 Weekly\n")
                elif values["-PREMIUM-"]:
                    f.write("Type: Premium - $20.00 Weekly\n")
                if values["-3MONTHS-"]:
                    f.write("Duration: 3 Months\n")
                elif values["-12MONTHS-"]:
                    f.write("Duration: 12 Months\n")
                elif values["-24MONTHS-"]:
                    f.write("Duration: 24 Months\n")
                if values["-BASIC-"]:
                    f.write("Membership Type: Basic\n")
                elif values["-REGULAR-"]:
                    f.write("Membership Type: Regular\n")
                else:
                    f.write("Membership Type: Premium\n")
                    f.write("Payment options : \n")
                if values["-YES-"]:
                    f.write("Pay by Direct Debit : Yes\n")
                else:
                    f.write("Pay by Direct Debit : No\n")

                if values["-WEEKLY-"]:
                    f.write("Payment Frequency : Weekly\n")
                else:
                    f.write("Payment Frequency : Monthly\n")
            """
            validation_result = validate(values)
            if validation_result[0]:
                creatembr(fName=values["-FIRST NAME-"],
                          lName=values["-LAST NAME-"],
                          address=values["-ADDRESS-"],
                          mobile=values["-MOBILE-"],
                          email=values["-EMAIL-"])
                sg.popup("Member was succesfully created")

            else:
                error_message = generate_error_message(validation_result[1])
                sg.popup(error_message)

        # window.close()
