# This class will be where the graphic user interface is implemented
# - Graphic user interface will have a login screen
# - There will be a customer view and a employee view depending on the account type
# - Customer view only allows browsing and booking of a rental vehicle
# - Employee view will allow fleet management, payment management, booking management, and possibly customer management
import PySimpleGUI as sg


class UserInterface:
    def LoginPage(self) -> int:
        """Login Page for the User Interface. Have user enter username and call on UserController to validate."""

        # Contents of the login page
        layout = [[sg.Text('Login to Club Penguin Car Rentals')],
                  [sg.Text('Username:'), sg.InputText()],
                  [sg.Text('Password:'), sg.InputText()],
                  [sg.Button('Ok'), sg.Button('Cancel')]]

        # Create the Window
        window = sg.Window('Club Penguin Car Rentals: Login', layout)

        # Loop to process events and inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break
            print(f"You entered {values}")

        window.close()

        valid = False
        # valid = UserController.isValid(values)
        valid = True

        # perm_level = UserController.getPermLevel(values[0])

        # if valid:
        #     return perm_level
        # else:
        #     return -1

        if valid:
            return 0
