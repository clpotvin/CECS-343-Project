import datetime

import PySimpleGUI as sg
import hashlib
from .user_controller import UserController
from .fleet_controller import FleetController

uc = UserController()
fc = FleetController()

big_bold = 'Helvetica 16 bold'
med_bold = 'Helvetica 14 bold'
small_bold = 'Helvetica 12 bold'
big_font = 'Helvetica 16'
med_font = 'Helvetica 14'
small_font = 'Helvetica 12'



login =  [[sg.Text('Login', font='Helvetica 20 bold underline')],
         [sg.VPush()],
         [sg.Text('Username:', font=big_bold, key='-LI_UNAME-'), sg.Push(),
          sg.InputText(font=small_font, size=[30, 1])],
         [sg.Text('Password:', font=big_bold, key='-LI_PASS-'), sg.Push(),
          sg.InputText(font=small_font, size=[30, 1])],
         [sg.VPush()],[sg.VPush()],
         [sg.Button('Login', font=med_font),
          sg.Push(), sg.Button('Exit', font=med_font, key='-EX1-')]]

new_user = [[sg.Text('Create an Account', font='Helvetica 20 bold underline')],
            [sg.VPush()],
            [sg.Text('First Name:', font=big_bold, key='-NU_FNAME-'), sg.Push(),
             sg.InputText(font=small_font, size=[30, 1])],
            [sg.Text('Last Name:', font=big_bold, key='-NU_LNAME-'), sg.Push(),
             sg.InputText(font=small_font, size=[30, 1])],
            [sg.Text('Username:', font=big_bold, key='-NU_UNAME-'), sg.Push(),
             sg.InputText(font=small_font, size=[30, 1])],
            [sg.Text('Password:', font=big_bold, key='-NU_PASS-'), sg.Push(),
             sg.InputText(font=small_font, size=[30, 1])], [sg.VPush()],
            [sg.Button('Create Account', font=med_font), sg.Push(),
             sg.Button('Exit', font=med_font, key='-EX2-')]]

new_user_success = [[sg.Text('Account Creation Success!', font='Helvetica 30 bold')],
                    [sg.Push(), sg.Text('✅', font='Helvetica 150'), sg.Push()],
                    [sg.Push(), sg.Button('Go to Login', font='Helvetica 14', key='-BT_LOGIN-'), sg.Push()]]

view_whole_fleet = [[sg.Text('All Vehicles')],
                      [sg.Table(values=fc.vehicle_data[['Make', 'Model','Trim', 'Year', 'Status']].values.tolist(),
                                headings=['Make', 'Model', 'Trim', 'Year', 'Status'],
                                auto_size_columns=False,
                                def_col_width=15,
                                justification='center',
                                key='-TABLE1-', enable_events=True)],
                      [sg.Text('Selected Vehicle:'), sg.Text(size=(20, 1), key='-SELECTED1-', enable_events=True, visible=True)],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_MAKE-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_MODEL-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_TRIM-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_YEAR-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_STATUS-')],
                    [sg.Button('Update', key='-UPDATE1-'), sg.Button('Remove', key='-REMOVE1-'), sg.Push(),
                     sg.Button('Add New Vehicle', key='-ADD1-')]]

view_accounts = [[sg.Table(headings=uc.get_user_data().columns.tolist(), values=uc.get_user_data().values.tolist(),
                           key='-VAcc-', font='Helvetica 14', enable_click_events=True)],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-FNAME-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-LNAME-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-UNAME-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-PASS-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-UUID-'),
                  sg.InputOptionMenu(['MANAGER', 'EMPLOYEE', 'CUSTOMER'], default_value=' ', size=[8, 1],
                                     key='-PERM-')],
                 [sg.Button('Update Account', font='Helvetica 12'), sg.Button('Delete Account', font='Helvetica 14')]]

edit_vehicle = []

new_vehicle = [[sg.Text('Add a New Vehicle', font='Helvetica 20 bold underline')],
       [sg.VPush()],
       [sg.Text('Make:', font='Helvetica 14 bold'), sg.Push(),
        sg.InputText(font='Helvetica 14', key='-AV_MAKE-')],
       [sg.Text('Model:', font='Helvetica 14 bold'), sg.Push(),
        sg.InputText(font='Helvetica 14', key='-AV_MODEL-')],
       [sg.Text('Trim:', font='Helvetica 14 bold'), sg.Push(),
        sg.InputText(font='Helvetica 14', key='-AV_TRIM-')],
       [sg.Text('Year:', font='Helvetica 14 bold'), sg.Push(),
        sg.InputText(font='Helvetica 14', key='-AV_YEAR-')],
       [sg.Text('License Plate:', font='Helvetica 14 bold'), sg.Push(),
        sg.InputText(font='Helvetica 14', key='-AV_LP-')],
       [sg.Text('Status:', font='Helvetica 14 bold'), sg.Push(),
        sg.InputText(font='Helvetica 14', key='-AV_STATUS-')],
       [sg.VPush()],
       [sg.Button('Go Back', font='Helvetica 14', key='-AV_BACK-'),
        sg.Push(), sg.Button('Confirm', font='Helvetica 14', key='-AV_CONFIRM-')],
       [sg.Text('Error: Please enter ALL fields before confirming.', font='Helvetica 14', visible=False, key='-AV_ERROR-')]]

new_vehicle_success = [[sg.Text('Vehicle Creation Success!', font='Helvetica 30 bold')],
                    [sg.Push(), sg.Text('✅', font='Helvetica 150'), sg.Push()],
                    [sg.Push(), sg.Button('Go to Fleet Viewer', font='Helvetica 14', key='-BT_MGR-'), sg.Push()]]

available_vehicles = [[sg.Text('Available Vehicles')],
                      [sg.Table(values=fc.available_vehicles[['Make', 'Model','Trim', 'Year', 'Status']].values.tolist(),
                                headings=['Make', 'Model', 'Trim', 'Year', 'Status'],
                                auto_size_columns=False,
                                def_col_width=15,
                                justification='center',
                                key='-TABLE-', enable_events=True,font='',visible=True)],
                      [sg.Text('Selected Vehicle:'), sg.Text(size=(20, 1), key='-SELECTED-', enable_events=True, visible=True)],
                      [sg.Text('Start Date:'), sg.CalendarButton('Select', target='-START-', key='-CALENDAR_START-', format='%m-%d-%Y', enable_events=True),
                       sg.InputText(key='-START-', visible=True)],
                      [sg.Text('End Date:'), sg.CalendarButton('Select', target='-END-', key='-CALENDAR_END-', format='%m-%d-%Y', enable_events=True),
                       sg.InputText(key='-END-', visible=True)],
                      [sg.Button('Book')]]

rent_vehicle = []

payment_page = []

financial_view = []

view = [[sg.TabGroup([[sg.Tab("View Fleet", view_whole_fleet, key='-VF-'),
                       sg.Tab("View Available Vehicles", available_vehicles, key='-VAV-'),
                       sg.Tab("View Accounts", view_accounts, key='-VA-'),
                       sg.Tab("View Financials", financial_view, key='-VFi-')]], font='Helvetica 14',
                     key='-View')], [sg.Button('Exit', key='-EX3-')]]

login_screen = [[sg.Image(source='CECS-343-Project/code/UI-Assets/Login_BG.png', key='IMAGE')], [sg.TabGroup([[sg.Tab(layout=login, title='Login')], [sg.Tab(layout=new_user, title='Create New Account')]], font='Helvetica 14', key='-LGNS-')]]

layout = [[sg.Column(login_screen, visible=True, key='-LOGIN-'),
           sg.Column(new_user_success, visible=False, key='-NUSRS-'),
           sg.Column(view, key='-VIEW-', visible=False)]]

window = sg.Window('Club Penguin Car Rentals', layout,finalize=True)

           #sg.Column(new_vehicle, key='-NVV-', visible=False), sg.Column(new_vehicle_success, visible=False, key='-NVSRS-')]]

test = window['-LGNS-'].widget
w1, h1 = window['IMAGE'].get_size()
w2, h2 = window['-LGNS-'].get_size()
master = test.master
master.place(x=(w1-w2)//6, y=(h1-h2)//3, bordermode=sg.tk.INSIDE)


class UserInterface:

    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in (None, '-EX1-', '-EX2-', '-EX3-'):
                break

            # LOGIN SCREEN EVENTS
            if event == 'Login':
                if values[0] and values[1] != '':
                    values[1] = int(hashlib.sha256(values[1].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                    if uc.is_valid(values[0], values[1]):
                        user = uc.find_by_username(values[0])
                        if user is not False:
                            window[0].update(value='')
                            window[1].update(value='')
                            p_level = user.get_perm_level()
                            window['-LOGIN-'].update(visible=False)
                            window['-NUSRS-'].update(visible=False)
                            if p_level == 'Manager':
                                window['-VIEW-'].update(visible=True)
                                window['-VF-'].update(visible=True)
                                window['-VAV-'].update(visible=True)
                                window['-VA-'].update(visible=True)
                                window['-VFi-'].update(visible=True)
                            elif p_level == 'Employee':
                                window['-VIEW-'].update(visible=True)
                                window['-VF-'].update(visible=True)
                                window['-VAV-'].update(visible=True)
                                window['-VA-'].update(visible=False)
                                window['-VFi-'].update(visible=True)
                            else:
                                window['-VIEW-'].update(visible=True)
                                window['-VF-'].update(visible=False)
                                window['-VAV-'].update(visible=True)
                                window['-VA-'].update(visible=False)
                                window['-VFi-'].update(visible=False)
                        else:
                            print("Error: User not able to be found.")

            # NEW USER SCREEN EVENTS
            if event == 'Create Account':
                if values[5] != '':
                    values[5] = int(hashlib.sha256(values[5].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                if values[2] and values[3] and values[4] and values[5] != '':
                    arr = [values[2], values[3], values[4], values[5]]
                    if uc.new_user(arr):
                        window[f'-LOGIN-'].update(visible=False)
                        window[f'-NUSRS-'].update(visible=True)
            if event == '-BT_LOGIN-':
                window[2].update(value='')
                window[3].update(value='')
                window[4].update(value='')
                window[5].update(value='')
                window['-LOGIN-'].update(visible=True)
                window['-NUSRS-'].update(visible=False)

            # MANAGER VIEW - VIEW ACCOUNTS TAB EVENTS
            if '-VAcc-' in event:
                window['-FNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][0])
                window['-LNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][1])
                window['-UNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])
                window['-PASS-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][3])
                window['-UUID-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][4])
            if event == 'Update Account':
                if values['-PERM-'] == 'CUSTOMER' and int(values['-UUID-']) > 1000000000:
                    if int(values['-UUID-']) > 2000000000:
                        values['-UUID-'] = str(int(values['-UUID-']) - 2000000000)
                    else:
                        values['-UUID-'] = str(int(values['-UUID-']) - 1000000000)
                elif values['-PERM-'] == 'EMPLOYEE' and int(values['-UUID-']) < 1000000000:
                    values['-UUID-'] = str(int(values['-UUID-']) + 1000000000)
                elif values['-PERM-'] == 'MANAGER' and int(values['-UUID-']) < 2000000000:
                    if int(values['-UUID-']) > 1000000000:
                        values['-UUID-'] = str(int(values['-UUID-']) + 1000000000)
                    else:
                        values['-UUID-'] = str(int(values['-UUID-']) + 2000000000)

                if int(hashlib.sha256(values['-PASS-'].encode('utf-8')).hexdigest(), 16) % (10 ** 12) == uc.user_data['Hashed Password'][uc.user_data['Username'].tolist().index(values['-UNAME-'])]:
                    uc.update_user(values['-FNAME-'], values['-LNAME-'], values['-UNAME-'], values['-PASS-'], values['-UUID-'], uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])
                else:
                    uc.update_user(values['-FNAME-'], values['-LNAME-'], values['-UNAME-'], int(hashlib.sha256(values['-PASS-'].encode('utf-8')).hexdigest(), 16) % (10 ** 12), values['-UUID-'], uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])

                window['-FNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][0])
                window['-LNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][1])
                window['-UNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])
                window['-PASS-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][3])
                window['-UUID-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][4])

            # ALL VEHICLES EVENT
            if event == '-TABLE1-':
                selected_row = values['-TABLE1-'][0]
                selected_vehicle = fc.vehicle_data.values[selected_row]
                window['-SELECTED1-'].update(f"{selected_vehicle[0]} -  {selected_vehicle[1]} - {selected_vehicle[2]}")
                window['-VF_MAKE-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][0])
                window['-VF_MODEL-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][1])
                window['-VF_TRIM-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][2])
                window['-VF_YEAR-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][3])
                window['-VF_STATUS-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][5])
            if event == '-ADD1-':
                window[f'-MGR-'].update(visible=False)
                window[f'-NVV-'].update(visible=True)
            if event == '-AV_CONFIRM-':
                if values['-AV_MAKE-'] and values['-AV_MODEL-'] and values['-AV_TRIM-'] and\
                   values['-AV_YEAR-'] and values['-AV_LP-'] and values['-AV_STATUS-'] != '':
                    data = [values['-AV_MAKE-'], values['-AV_MODEL-'], values['-AV_TRIM-'],
                            values['-AV_YEAR-'], values['-AV_LP-'], values['-AV_STATUS-']]
                    fc.new_vehicle(data)
                    window[f'-NVV-'].update(visible=False)
                    window[f'-NVSRS-'].update(visible=True)
                else:
                    print("Please enter all required fields first.")
                    window[f'-AV_ERROR-'].update(visible=False)
                    window[f'-AV_ERROR-'].update(visible=True)
            if event == '-BT_MGR-':
                window[f'-NVSRS-'].update(visible=False)
                window[f'-MGR-'].update(visible=True)
            if event == '-AV_BACK-':
                window[f'-NVV-'].update(visible=False)
                window[f'-MGR-'].update(visible=True)


            # AVAILABLE VEHICLES EVENTS
            if event == '-TABLE-':
                selected_row = values['-TABLE-'][0]
                selected_vehicle = fc.available_vehicles.values[selected_row]
                window['-SELECTED-'].update(f"{selected_vehicle[0]} -  {selected_vehicle[1]} - {selected_vehicle[2]}")
            elif event == '-CALENDAR_START-':
                window['-START-'].update(values['-CALENDAR_START-'])
            elif event == '-CALENDAR_END-':
                window['-END-'].update(values['-CALENDAR_END-'])
            elif event == 'Book':
                try:
                    selected_row = values['-TABLE-'][0]
                    selected_vehicle = fc.available_vehicles.values[selected_row]
                    license_plate = selected_vehicle[4]
                    start_date = values['-START-']
                    end_date = values['-END-']

                    availability_response = fc.check_availability(license_plate, start_date, end_date)

                    if availability_response == 'Available':
                        sg.popup(f'Vehicle {selected_vehicle} is available for booking!')
                    else:
                        sg.popup(f'Vehicle {selected_vehicle} is not available for the selected dates.')
                except ValueError as ve:
                    sg.popup(str(ve))

            # RENTAL BOOKING EVENTS

            # PAYMENT PROCESSING EVENTS

            #
