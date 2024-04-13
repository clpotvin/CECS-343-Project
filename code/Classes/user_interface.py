import datetime

import PySimpleGUI as sg
import hashlib
from .user_controller import UserController

layout1 = [[sg.Text('Login to Club Penguin Car Rentals', font='Helvetica 20 bold underline')],
           [sg.VPush()],
           [sg.Text('Username:', font='Helvetica 16 bold', key='-LI_UNAME-'), sg.Push(),
            sg.InputText(font='Helvetica 14', size=[30, 1])],
           [sg.Text('Password:', font='Helvetica 16 bold', key='-LI_PASS-'), sg.Push(),
            sg.InputText(font='Helvetica 14', size=[30, 1])],
           [sg.VPush()],
           [sg.Button('Login', font='Helvetica 14'), sg.Button('Create New Account', font='Helvetica 14'),
            sg.Push(), sg.Button('Exit', font='Helvetica 14', key='-EX1-')]]

layout2 = [[sg.Text('Create an Account', font='Helvetica 20 bold underline')],
           [sg.VPush()],
           [sg.Text('First Name:', font='Helvetica 16 bold', key='-NU_FNAME-'), sg.Push(),
            sg.InputText(font='Helvetica 14', size=[30, 1])],
           [sg.Text('Last Name:', font='Helvetica 16 bold', key='-NU_LNAME-'), sg.Push(),
            sg.InputText(font='Helvetica 14', size=[30, 1])],
           [sg.Text('Username:', font='Helvetica 16 bold', key='-NU_UNAME-'), sg.Push(),
            sg.InputText(font='Helvetica 14', size=[30, 1])],
           [sg.Text('Password:', font='Helvetica 16 bold', key='-NU_PASS-'), sg.Push(),
            sg.InputText(font='Helvetica 14', size=[30, 1])], [sg.VPush()],
           [sg.Button('Create Account', font='Helvetica 14'), sg.Push(),
            sg.Button('Back to Login', font='Helvetica 14'),
            sg.Button('Exit', font='Helvetica 14', key='-EX2-')]]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-')]]
window = sg.Window('Club Penguin Car Rentals', layout)

uc = UserController()


class UserInterface:

    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in (None, '-EX1-', '-EX2-'):
                break
            if event == 'Login':
                if values[0] and values [1] != '':
                    values[1] = int(hashlib.sha256(values[1].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                    if uc.is_valid(values[0], values[1]):
                        print("Login success")
            if event == 'Create New Account':
                window[f'-COL{1}-'].update(visible=False)
                window[f'-COL{2}-'].update(visible=True)
            if event == 'Back to Login':
                window[f'-COL{1}-'].update(visible=True)
                window[f'-COL{2}-'].update(visible=False)
            if event == 'Create Account':
                if values[5] != '':
                    values[5] = int(hashlib.sha256(values[5].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                if values[2] and values[3] and values[4] and values[5] != '':
                    arr = [values[2], values[3], values[4], values[5]]
                    uc.new_user(arr)
