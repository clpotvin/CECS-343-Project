import datetime

import PySimpleGUI as sg
import hashlib
from .user_controller import UserController
from .fleet_controller import FleetController

uc = UserController()
fc = FleetController()

login = [[sg.Text('Login to Club Penguin Car Rentals', font='Helvetica 20 bold underline')],
         [sg.VPush()],
         [sg.Text('Username:', font='Helvetica 16 bold', key='-LI_UNAME-'), sg.Push(),
          sg.InputText(font='Helvetica 14', size=[30, 1])],
         [sg.Text('Password:', font='Helvetica 16 bold', key='-LI_PASS-'), sg.Push(),
          sg.InputText(font='Helvetica 14', size=[30, 1])],
         [sg.VPush()],
         [sg.Button('Login', font='Helvetica 14'), sg.Button('Create New Account', font='Helvetica 14'),
          sg.Push(), sg.Button('Exit', font='Helvetica 14', key='-EX1-')]]

new_user = [[sg.Text('Create an Account', font='Helvetica 20 bold underline')],
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
                      [sg.Text('Selected Vehicle:'), sg.Text(size=(80, 1), key='-SELECTED1-', enable_events=True, visible=True)],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_MAKE-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_MODEL-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_TRIM-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_YEAR-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-VF_STATUS-')],
                    [sg.Button('Update', key='-VF_UPDATE-'), sg.Button('Remove', key='-VF_REMOVE-'), sg.Push(),
                     sg.Button('Add New Vehicle', key='-VF_ADD-')]]

view_accounts = [[sg.Table(headings=uc.get_user_data().columns.tolist(), values=uc.get_user_data().values.tolist(),
                           key='-VAcc-', font='Helvetica 14', enable_click_events=True)],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-FNAME-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-LNAME-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-UNAME-'),
                  sg.InputText(font='Helvetica 14', size=[30, 1], key='-PASS-')],
                 [sg.InputText(font='Helvetica 14', size=[30, 1], key='-UUID-'),
                  sg.InputOptionMenu(['MANAGER', 'EMPLOYEE', 'CUSTOMER'], default_value=' ', size=[8, 1],
                                     key='-PERM-')],
                 [sg.Button('Update Account', font='Helvetica 14'), sg.Button('Delete Account', font='Helvetica 14')]]

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
                                key='-TABLE-', enable_events=True)],
                      [sg.Text('Selected Vehicle:'), sg.Text(size=(20, 1), key='-SELECTED-', enable_events=True, visible=True)],
                      [sg.Text('Start Date:'), sg.CalendarButton('Select', target='-START-', key='-CALENDAR_START-', format='%m-%d-%Y', enable_events=True),
                       sg.InputText(key='-START-', visible=True)],
                      [sg.Text('End Date:'), sg.CalendarButton('Select', target='-END-', key='-CALENDAR_END-', format='%m-%d-%Y', enable_events=True),
                       sg.InputText(key='-END-', visible=True)],
                      [sg.Button('Book')]]

rent_vehicle = []

payment_page = []

financial_view = []

manager_view = [[sg.TabGroup([[sg.Tab("View Fleet", view_whole_fleet, key='-MVF-'),
                               sg.Tab("View Available Vehicles", available_vehicles, key='-MVAV-'),
                               sg.Tab("View Accounts", view_accounts, key='-MVA-'),
                               sg.Tab("View Financials", financial_view, key='-MVFi-')]], font='Helvetica 14',
                             key='-MGRV-')], [sg.Button('Exit', key='-EX3-')]]

# employee_view = [[sg.TabGroup([[sg.Tab("View Fleet", view_whole_fleet),
#                                sg.Tab("View Available Vehicles", available_vehicles),
#                                sg.Tab("View Financials", financial_view)]], font='Helvetica 16', key='-EMPV-')]]
#
# customer_view = [[sg.TabGroup([[sg.Tab("View Available Vehicles", available_vehicles),
#                                 sg.Tab("Book a Rental", view_accounts)]], font='Helvetica 16', key='-CSTV')]]

employee_view = []
customer_view = []

layout = [[sg.Column(login, key='-LGN-'), sg.Column(new_user, visible=False, key='-NUSR-'),
           sg.Column(new_user_success, visible=False, key='-NUSRS-'),
           sg.Column(manager_view, key='-MGR-', visible=False),
           sg.Column(employee_view, key='-EMP-', visible=False), sg.Column(customer_view, key='-CST-', visible=False),
           sg.Column(new_vehicle, key='-NVV-', visible=False), sg.Column(new_vehicle_success, visible=False, key='-NVSRS-')]]

window = sg.Window('Club Penguin Car Rentals', layout)


class UserInterface:

    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in (None, '-EX1-', '-EX2-'):
                break

            # LOGIN SCREEN EVENTS
            if event == 'Login':
                if values[0] and values[1] != '':
                    values[1] = int(hashlib.sha256(values[1].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                    if uc.is_valid(values[0], values[1]):
                        user = uc.find_by_username(values[0])
                        if user is not False:
                            p_level = user.get_perm_level()
                            window['-LGN-'].update(visible=False)
                            window['-NUSR-'].update(visible=False)
                            window['-NUSRS-'].update(visible=False)
                            if p_level == 'Manager':
                                window['-MGR-'].update(visible=True)
                                window['-EMP-'].update(visible=False)
                                window['-CST-'].update(visible=False)
                            elif p_level == 'Employee':
                                window['-MGR-'].update(visible=False)
                                window['-EMP-'].update(visible=True)
                                window['-CST-'].update(visible=False)
                            else:
                                window['-MGR-'].update(visible=False)
                                window['-EMP-'].update(visible=False)
                                window['-CST-'].update(visible=True)
                        else:
                            print("Error: User not able to be found.")
            if event == 'Create New Account':
                window[f'-LGN-'].update(visible=False)
                window[f'-NUSR-'].update(visible=True)

            # NEW USER SCREEN EVENTS
            if event == 'Back to Login' or event == '-BT_LOGIN-':
                window[f'-LGN-'].update(visible=True)
                window[f'-NUSR-'].update(visible=False)
                window[f'-NUSRS-'].update(visible=False)
            if event == 'Create Account':
                if values[5] != '':
                    values[5] = int(hashlib.sha256(values[5].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                if values[2] and values[3] and values[4] and values[5] != '':
                    arr = [values[2], values[3], values[4], values[5]]
                    if uc.new_user(arr):
                        window[f'-NUSR-'].update(visible=False)
                        window[f'-NUSRS-'].update(visible=True)

            # MANAGER VIEW - VIEW ACCOUNTS TAB EVENTS
            if '-VAcc-' in event:
                window['-FNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][0])
                window['-LNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][1])
                window['-UNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])
                window['-PASS-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][3])
                window['-UUID-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][4])
                # window['-PERM-'].update(value=uc.find_by_username([values['-VAcc-'][0]][2]).get_perm_level())
            if event == 'Update Account':
                if values['-PERM-'] == 'Customer' and values['-UUID-'] > 1000000000:
                    if values['-UUID-'] > 2000000000:
                        values['-UUID-'] -= 2000000000
                    else:
                        values['-UUID-'] -= 1000000000
                elif values['-PERM-'] == 'Employee' and values['-UUID-'] < 1000000000:
                    values['-UUID-'] += 1000000000
                elif values['-PERM-'] == 'Manager' and values['-UUID-'] < 2000000000:
                    if values['-UUID-'] > 1000000000:
                        values['-UUID-'] += 1000000000
                    else:
                        values['-UUID-'] += 2000000000
                uc.update_user(values['-FNAME-'], values['-LNAME-'], values['-UNAME-'],
                               int(hashlib.sha256(values['-PASS-'].encode('utf-8')).hexdigest(), 16) % (10 ** 12),
                               values['-UUID-'])

            # ALL VEHICLES EVENT
            if event == '-TABLE1-':
                if values['-TABLE1-']:
                    selected_row = values['-TABLE1-'][0]
                    selected_vehicle = fc.vehicle_data.values[selected_row]
                    window['-SELECTED1-'].update(f"{selected_vehicle[0]} -  {selected_vehicle[1]} - {selected_vehicle[2]}")
                    window['-VF_MAKE-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][0])
                    window['-VF_MODEL-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][1])
                    window['-VF_TRIM-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][2])
                    window['-VF_YEAR-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][3])
                    window['-VF_STATUS-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][5])
            if event == '-VF_ADD-':
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
                    window['-TABLE1-'].update(
                        values=fc.vehicle_data[['Make', 'Model', 'Trim', 'Year', 'Status']].values.tolist())
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
            if event == '-VF_REMOVE-':
                if values["-TABLE1-"]:
                    plate = fc.get_plate_by_index(values["-TABLE1-"][0])
                    fc.delete_vehicle(plate)
                    window['-TABLE1-'].update(
                        values=fc.vehicle_data[['Make', 'Model', 'Trim', 'Year', 'Status']].values.tolist())
                    window['-SELECTED1-'].update(f"Successfully removed vehicle.")
                else:
                    print('table not selected')
                    window['-SELECTED1-'].update(f"Please select a row before removing.")
            if event == '-VF_UPDATE-':
                if values["-TABLE1-"]:
                    plate = fc.get_plate_by_index(values["-TABLE1-"][0])
                    if values['-VF_MAKE-'] and values['-VF_MODEL-'] and values['-VF_TRIM-'] and \
                            values['-VF_YEAR-'] and plate and values['-VF_STATUS-'] != '':
                        data = [values['-VF_MAKE-'], values['-VF_MODEL-'], values['-VF_TRIM-'],
                                values['-VF_YEAR-'], plate, values['-VF_STATUS-']]
                        fc.update_vehicle(data)
                        window['-TABLE1-'].update(values=fc.vehicle_data[['Make', 'Model','Trim', 'Year', 'Status']].values.tolist())
                        window['-SELECTED1-'].update(f"Successfully updated vehicle. Please select another row to make further updates.")
                    else:
                        print('stuff should be not empty')
                else:
                    print('table not selected')
                    window['-SELECTED1-'].update(f"Please select a row before updating.")






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
