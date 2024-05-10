import datetime

import PySimpleGUI as sg
import hashlib
from .user_controller import UserController
from .fleet_controller import FleetController
from .payment_controller import PaymentController

uc = UserController()
fc = FleetController()
pc = PaymentController()

big_bold = 'Helvetica 16 bold'
med_bold = 'Helvetica 14 bold'
small_bold = 'Helvetica 12 bold'
big_font = 'Helvetica 16'
med_font = 'Helvetica 14'
small_font = 'Helvetica 12'

login = [[sg.Text('Login', font='Helvetica 20 bold underline')],
         [sg.VPush()],
         [sg.Text('Username:', font=big_bold, key='-LI_UNAME-'), sg.Push(),
          sg.InputText(font=med_font, size=(20, 1))],
         [sg.Text('Password:', font=big_bold, key='-LI_PASS-'), sg.Push(),
          sg.InputText(font=med_font, size=(20, 1), password_char='*')],
         [sg.VPush()], [sg.VPush()], [sg.VPush()], [sg.VPush()],
         [sg.Button('Login', font=med_font),
          sg.Push(), sg.Button('Exit', font=med_font, key='-EX1-')]]

new_user = [[sg.Text('Create an Account', font='Helvetica 20 bold underline')],
            [sg.VPush()],
            [sg.Text('First Name:', font=big_bold, key='-NU_FNAME-'), sg.Push(),
             sg.InputText(font=med_font, size=(20, 1))],
            [sg.Text('Last Name:', font=big_bold, key='-NU_LNAME-'), sg.Push(),
             sg.InputText(font=med_font, size=(20, 1))],
            [sg.Text('Username:', font=big_bold, key='-NU_UNAME-'), sg.Push(),
             sg.InputText(font=med_font, size=(20, 1))],
            [sg.Text('Password:', font=big_bold, key='-NU_PASS-'), sg.Push(),
             sg.InputText(font=med_font, size=(20, 1), password_char='*')], [sg.VPush()],
            [sg.Button('Create Account', font=med_font), sg.Push(),
             sg.Button('Exit', font=med_font, key='-EX2-')]]

new_user_success = [[sg.Text('Account Creation Success!', font='Helvetica 30 bold')],
                    [sg.Push(), sg.Text('✅', font='Helvetica 150'), sg.Push()],
                    [sg.Push(), sg.Button('Go to Login', font=med_font, key='-BT_LOGIN-'), sg.Push()]]

view_whole_fleet = [[sg.Table(values=fc.vehicle_data[['Make', 'Model', 'Trim', 'Year', 'Status']].values.tolist(),
                              headings=['Make', 'Model', 'Trim', 'Year', 'Status'], auto_size_columns=False,
                              def_col_width=12, justification='center', key='-TABLE1-', font=med_font,
                              enable_events=True)],
                    [sg.Text('Selected Vehicle:', font=med_font),
                     sg.Text(size=(80, 1), key='-SELECTED1-', enable_events=True, visible=True, font=med_font)],
                    [sg.Text('Make:', font=med_bold, key='-VF-MAKE-', size=(6, 1)),
                     sg.InputText(font=med_font, size=(20, 1), key='-VF_MAKE-'),
                     sg.Text('Model:', font=med_bold, key='-VF-MODEL-', size=(6, 1)),
                     sg.InputText(font=med_font, size=(20, 1), key='-VF_MODEL-')],
                    [sg.Text('Trim:', font=med_bold, key='-VF-TRIM-', size=(6, 1)),
                     sg.InputText(font=med_font, size=(20, 1), key='-VF_TRIM-'),
                     sg.Text('Year:', font=med_bold, key='-VF-YEAR-', size=(6, 1)),
                     sg.InputText(font=med_font, size=(20, 1), key='-VF_YEAR-')],
                    [sg.Text('Price:', font=med_bold, key='-VF-COST-', size=(6, 1)),
                     sg.InputText(font=med_font, size=(20, 1), key='-VF_COST-'),
                     sg.Text('Status:', font=med_bold, key='-VF-STATUS-', size=(6, 1)),
                     sg.InputText(font=med_font, size=(20, 1), key='-VF_STATUS-')],
                    [sg.Button('Update', key='-VF_UPDATE-', font=med_font),
                     sg.Button('Remove', key='-VF_REMOVE-', font=med_font), sg.Push(),
                     sg.Button('Add New Vehicle', key='-VF_ADD-', font=med_font)]]

view_accounts = [[sg.Table(headings=['First Name', 'Last Name', 'Username', 'UUID'],
                           values=uc.get_user_data()[['First Name', 'Last Name', 'Username', 'UUID']].values.tolist(),
                           auto_size_columns=False,
                           def_col_width=15, justification='center',
                           key='-VAcc-', font=med_font, enable_click_events=True)],
                 [sg.Text('First Name:', font=med_bold, key='-VA_FNAME-', size=(10, 1)),
                  sg.InputText(font=med_font, size=(20, 1), key='-FNAME-'),
                  sg.Text('Last Name:', font=med_bold, key='-VA_LNAME-', size=(10, 1)),
                  sg.InputText(font=med_font, size=(20, 1), key='-LNAME-')],
                 [sg.Text('Username:', font=med_bold, key='-VA_UNAME-', size=(10, 1)),
                  sg.InputText(font=med_font, size=(20, 1), key='-UNAME-'),
                  sg.Text('Password:', font=med_bold, key='-VA_PASS-', size=(10, 1)),
                  sg.InputText(font=med_font, size=(20, 1), key='-PASS-', password_char='*')],
                 [sg.Text('UUID:', font=med_bold, key='-VA_UUID-', size=(10, 1)),
                  sg.InputText(font=med_font, size=(20, 1), key='-UUID-', readonly=True,
                               disabled_readonly_background_color='white'),
                  sg.Text('Permission:', font=med_bold, key='-VA_PERM-', size=(10, 1)),
                  sg.InputOptionMenu(['MANAGER', 'EMPLOYEE', 'CUSTOMER'], default_value=' ', size=[8, 1],
                                     key='-PERM-')], [sg.VPush()],
                 [sg.Button('Update Account', font=med_font), sg.Button('Delete Account', font=med_font)]]

new_vehicle = [[sg.Text('Add a New Vehicle', font='Helvetica 20 bold underline')],
               [sg.VPush()],
               [sg.Text('Make:', font=med_bold), sg.Push(),
                sg.InputText(font=med_font, key='-AV_MAKE-')],
               [sg.Text('Model:', font=med_bold), sg.Push(),
                sg.InputText(font=med_font, key='-AV_MODEL-')],
               [sg.Text('Trim:', font=med_bold), sg.Push(),
                sg.InputText(font=med_font, key='-AV_TRIM-')],
               [sg.Text('Year:', font=med_bold), sg.Push(),
                sg.InputText(font=med_font, key='-AV_YEAR-')],
               [sg.Text('License Plate:', font=med_bold), sg.Push(),
                sg.InputText(font=med_font, key='-AV_LP-')],
               [sg.Text('Daily Price:', font=med_bold), sg.Push(),
                sg.InputText(font=med_font, key='-AV_PRICE-')],
               [sg.Text('Status:', font=med_bold), sg.Push(),
                sg.InputText(font=med_font, key='-AV_STATUS-')],
               [sg.VPush()],
               [sg.Button('Go Back', font='small_font', key='-AV_BACK-'),
                sg.Push(), sg.Button('Confirm', font='small_font', key='-AV_CONFIRM-')],
               [sg.Text('Error: Please enter ALL fields before confirming.', font='small_font', visible=False,
                        key='-AV_ERROR-')]]

new_vehicle_success = [[sg.Text('Vehicle Creation Success!', font='Helvetica 30 bold')],
                       [sg.Push(), sg.Text('✅', font='Helvetica 150'), sg.Push()],
                       [sg.Push(), sg.Button('Go to Fleet Viewer', font='small_font', key='-BT_MGR-'), sg.Push()]]

available_vehicles = [[sg.Table(values=[], auto_size_columns=False,
                                def_col_width=15, justification='center', key='-TABLE-', font=med_font,
                                headings=['Make', 'Model', 'Trim', 'Year'],
                                enable_events=True)],
                      [sg.Text('Selected Vehicle:', font=med_font),
                       sg.Text(size=(20, 1), key='-SELECTED-', enable_events=True, visible=True)],
                      [sg.Text('Start Date:', font=med_bold, size=(8, 1)),
                       sg.CalendarButton('Select', target='-START-', key='-CALENDAR_START-', format='%m-%d-%Y',
                                         enable_events=True, font=med_font),
                       sg.InputText(key='-START-', visible=True, readonly=True,
                                    disabled_readonly_background_color='white', font=med_font, size=(12, 1))],
                      [sg.Text('End Date:', font=med_bold, size=(8, 1)),
                       sg.CalendarButton('Select', target='-END-', key='-CALENDAR_END-', format='%m-%d-%Y',
                                         enable_events=True, font=med_font),
                       sg.InputText(key='-END-', visible=True, readonly=True,
                                    disabled_readonly_background_color='white',
                                    font=med_font, size=(12, 1))], [sg.VPush()],
                      [sg.Button('Search', font=med_font), sg.Button('Book', font=med_font)]]

payment_page = [
    [sg.Text('Thank you for your purchase!', font='Helvetica 20 bold')],
    [sg.Text('UUID:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][0], font='Helvetica 20 bold', key='-P_UUID-')],
    [sg.Text('Amount:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][1], font='Helvetica 20 bold', key='-P_AMOUNT-')],
    [sg.Text('Date:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][2], font='Helvetica 20 bold', key='-P_DATE-')],
    [sg.Text('License Plate:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][3], font='Helvetica 20 bold', key='-P_PLATE-')],
    [sg.Button('Continue', font='Helvetica 20 bold', key='-P_CON-')]]

add_expense = [
    [sg.Text('Add Expense Payment', font='Helvetica 20 bold underline')],
    [sg.Text('Amount:', font=med_bold, key='-EP_AMOUNT-', size=(8, 1)),
     sg.InputText(font=med_font, size=(8, 1), key='-EP-AMOUNT-')],
    [sg.Text('Date:', font=med_bold, key='-EP_DATE-', size=(8, 1)),
     sg.InputText(readonly=True, disabled_readonly_background_color='white', font=med_font, size=(12, 1),
                  key='-EP-DATE-'),
     sg.CalendarButton('Select Date', target='-EP-DATE-', key='-EP_DATE_BT-', format='%m-%d-%Y', enable_events=True,
                       font=med_font)],
    [sg.Text('Reason:', font=med_bold, key='-EP_RES-', size=(8, 1)),
     sg.Multiline(font=med_font, size=(30, 5), wrap_lines=True, key='-EP-RES-')],
    [sg.Button('Enter Payment', font=med_font, key='-EP_ENTER-'), sg.Push(),
     sg.Button('Back', font=med_font, key='-EP_BACK-')]
]

financial_view = [
    [sg.Text('Payments', font='Helvetica 20 bold underline', justification='center')],
    [sg.Table(values=pc.expense_list, headings=pc.expense_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_events=True, key='-FIN_TAB1-', font=med_font),
     sg.Table(values=pc.rental_list, headings=pc.rental_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_events=True, key='-FIN_TAB2-', font=med_font)],
    [sg.InputText(font=med_font, size=(10, 1), key='-FIN_AMT-', readonly=True,
                  disabled_readonly_background_color='white'),
     sg.InputText(font=med_font, size=(10, 1), key='-FIN_DATE-', readonly=True,
                  disabled_readonly_background_color='white')],
    [sg.Multiline(font=med_font, size=(50, 2), wrap_lines=True, key='-FIN_RES-')],
    [sg.Button('Add Expense Payment', font=med_font)]
]

view = [[sg.TabGroup([[sg.Tab("View Fleet", view_whole_fleet, key='-VF-'),
                       sg.Tab("View Available Vehicles", available_vehicles, key='-VAV-'),
                       sg.Tab("View Accounts", view_accounts, key='-VA-'),
                       sg.Tab("View Financials", financial_view, key='-VFi-')]], font=med_font,
                     key='-View')],
        [sg.Push(), sg.Button('Logout', key='-LGO-', font=med_font), sg.Button('Exit', key='-EX3-', font=med_font)]]

login_screen = [[sg.Image(source='CECS-343-Project/code/UI-Assets/Login_BG.png', key='IMAGE')], [
    sg.TabGroup([[sg.Tab(layout=login, title='Login')], [sg.Tab(layout=new_user, title='Create New Account')]],
                font=med_font, key='-LGNS-', enable_events=True)]]

layout = [[sg.Column(login_screen, visible=True, key='-LOGIN-'),
           sg.Column(new_user_success, visible=False, key='-NUSRS-'),
           sg.Column(new_vehicle, key='-NVV-', visible=False),
           sg.Column(new_vehicle_success, visible=False, key='-NVSRS-'),
           sg.Column(payment_page, key='-PAY_PAGE-', visible=False),
           sg.Column(add_expense, key='-EXPENSE-', visible=False),
           sg.Column(view, key='-VIEW-', visible=False)]]

window = sg.Window('Club Penguin Car Rentals', layout, finalize=True)

test = window['-LGNS-'].widget
w1, h1 = window['IMAGE'].get_size()
w2, h2 = window['-LGNS-'].get_size()
master = test.master
master.place(x=(w1 - w2) // 6, y=(h1 - h2) // 3, bordermode=sg.tk.INSIDE)


class UserInterface:

    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in (None, '-EX1-', '-EX2-', '-EX3-'):
                break

            if event == '-LGO-':
                window['-LOGIN-'].update(visible=True)
                window['-NUSRS-'].update(visible=False)
                window['-VIEW-'].update(visible=False)
                window['-VF-'].update(visible=False)
                window['-VAV-'].update(visible=False)
                window['-VA-'].update(visible=False)
                window['-VFi-'].update(visible=False)

            # LOGIN SCREEN EVENTS
            if event == 'Login':
                if values[0] and values[1] != '':
                    values[1] = int(hashlib.sha256(values[1].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                    if uc.is_valid(values[0], values[1]):
                        user = uc.find_by_username(values[0])
                        print(user)
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

            # NEW USER SCREEN EVENTS
            if event == 'Create Account':
                if values[5] != '':
                    values[5] = int(hashlib.sha256(values[5].encode('utf-8')).hexdigest(), 16) % (10 ** 12)
                if values[2] and values[3] and values[4] and values[5] != '':
                    arr = [values[2], values[3], values[4], values[5]]
                    if uc.new_user(arr):
                        window[f'-LOGIN-'].update(visible=False)
                        window[f'-NUSRS-'].update(visible=True)
                        window[2].update(value='')
                        window[3].update(value='')
                        window[4].update(value='')
                        window[5].update(value='')
            elif event == '-BT_LOGIN-':
                window['-LOGIN-'].update(visible=True)
                window['-NUSRS-'].update(visible=False)

            # VIEW ACCOUNTS TAB EVENTS
            if '-VAcc-' in event:
                window['-FNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][0])
                window['-LNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][1])
                window['-UNAME-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])
                window['-PASS-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][3])
                window['-UUID-'].update(value=uc.get_user_data().values.tolist()[values['-VAcc-'][0]][4])
                if uc.get_user_data().values.tolist()[values['-VAcc-'][0]][4] > 2000000000:
                    window['-PERM-'].update(value='MANAGER')
                elif 1000000000 < uc.get_user_data().values.tolist()[values['-VAcc-'][0]][4] < 2000000000:
                    window['-PERM-'].update(value='EMPLOYEE')
                else:
                    window['-PERM-'].update(value='CUSTOMER')
            elif event == 'Update Account':
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

                if values['-PASS-'] == uc.user_data['Hashed Password'].values.tolist()[values['-VAcc-'][0]]:
                    uc.update_user(values['-FNAME-'], values['-LNAME-'], values['-UNAME-'], values['-PASS-'],
                                   values['-UUID-'], uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])
                else:
                    uc.update_user(values['-FNAME-'], values['-LNAME-'], values['-UNAME-'],
                                   int(hashlib.sha256(values['-PASS-'].encode('utf-8')).hexdigest(), 16) % (10 ** 12),
                                   values['-UUID-'], uc.get_user_data().values.tolist()[values['-VAcc-'][0]][2])

                window['-FNAME-'].update(value='')
                window['-LNAME-'].update(value='')
                window['-UNAME-'].update(value='')
                window['-PASS-'].update(value='')
                window['-UUID-'].update(value='')
                window['-PERM-'].update(value='')
                values['-VAcc-'] = []
                window['-VAcc-'].update(values=uc.get_user_data().values.tolist(), select_rows=[])
            elif event == 'Delete Account':
                uc.delete_user(values['-UNAME-'])
                window['-FNAME-'].update(value=' ')
                window['-LNAME-'].update(value=' ')
                window['-UNAME-'].update(value=' ')
                window['-PASS-'].update(value='')
                window['-UUID-'].update(value=' ')
                window['-PERM-'].update(value=' ')
                values['-VAcc-'] = []
                window['-VAcc-'].update(values=uc.get_user_data().values.tolist(), select_rows=[])
            else:
                window['-FNAME-'].update(value=' ')
                window['-LNAME-'].update(value=' ')
                window['-UNAME-'].update(value=' ')
                window['-PASS-'].update(value='')
                window['-UUID-'].update(value=' ')
                window['-PERM-'].update(value=' ')
                values['-VAcc-'] = []
                window['-VAcc-'].update(select_rows=[])

            # ALL VEHICLES EVENT
            if event == '-TABLE1-':
                if values['-TABLE1-']:
                    selected_row = values['-TABLE1-'][0]
                    selected_vehicle = fc.vehicle_data.values[selected_row]
                    window['-SELECTED1-'].update(
                        f"{selected_vehicle[0]} -  {selected_vehicle[1]} - {selected_vehicle[2]}")
                    window['-VF_MAKE-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][0])
                    window['-VF_MODEL-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][1])
                    window['-VF_TRIM-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][2])
                    window['-VF_YEAR-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][3])
                    window['-VF_COST-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][5])
                    window['-VF_STATUS-'].update(value=fc.vehicle_data.values.tolist()[values['-TABLE1-'][0]][6])
            if event == '-VF_ADD-':
                window[f'-VIEW-'].update(visible=False)
                window[f'-NVV-'].update(visible=True)
            if event == '-AV_CONFIRM-':
                if values['-AV_MAKE-'] and values['-AV_MODEL-'] and values['-AV_TRIM-'] and values['-AV_YEAR-'] and \
                        values['-AV_LP-'] and values['-AV_PRICE-'] and values['-AV_STATUS-'] != '':
                    data = [values['-AV_MAKE-'], values['-AV_MODEL-'], values['-AV_TRIM-'], values['-AV_YEAR-'],
                            values['-AV_LP-'], values['-AV_PRICE-'], values['-AV_STATUS-']]
                    fc.add_vehicle(data)
                    window['-NVV-'].update(visible=False)
                    window['-NVSRS-'].update(visible=True)
                    window['-TABLE1-'].update(
                        values=fc.vehicle_data[['Make', 'Model', 'Trim', 'Year', 'Status']].values.tolist())
                else:
                    window[f'-AV_ERROR-'].update(visible=False)
                    window[f'-AV_ERROR-'].update(visible=True)
            if event == '-BT_MGR-':
                window[f'-NVSRS-'].update(visible=False)
                window[f'-VIEW-'].update(visible=True)
            if event == '-AV_BACK-':
                window[f'-NVV-'].update(visible=False)
                window[f'-VIEW-'].update(visible=True)
            if event == '-VF_REMOVE-':
                if values["-TABLE1-"]:
                    plate = fc.get_plate_by_index(values["-TABLE1-"][0])
                    if fc.delete_vehicle(plate):
                        window['-TABLE1-'].update(
                            values=fc.vehicle_data[['Make', 'Model', 'Trim', 'Year', 'Status']].values.tolist())
                        window['-SELECTED1-'].update(f"Successfully removed vehicle.")
                    else:
                        window['-SELECTED1-'].update("Error: Failed to remove vehicle.")
                    window['-VF_MAKE-'].update(value='')
                    window['-VF_MODEL-'].update(value='')
                    window['-VF_TRIM-'].update(value='')
                    window['-VF_YEAR-'].update(value='')
                    window['-VF_COST-'].update(value='')
                    window['-VF_STATUS-'].update(value='')
                else:
                    window['-SELECTED1-'].update(f"Please select a row before removing.")
            if event == '-VF_UPDATE-':
                if values["-TABLE1-"]:
                    plate = fc.get_plate_by_index(values["-TABLE1-"][0])
                    if values['-VF_MAKE-'] and values['-VF_MODEL-'] and values['-VF_TRIM-'] and \
                            values['-VF_YEAR-'] and plate and values['-VF_STATUS-'] != '':
                        data = [values['-VF_MAKE-'], values['-VF_MODEL-'], values['-VF_TRIM-'],
                                values['-VF_YEAR-'], plate, values['-VF_COST-'], values['-VF_STATUS-']]
                        fc.update_vehicle(data)
                        window['-TABLE1-'].update(
                            values=fc.vehicle_data[['Make', 'Model', 'Trim', 'Year', 'Status']].values.tolist())
                        window['-SELECTED1-'].update(
                            value="Successfully updated vehicle. Please select another row to make further updates.")
                        window['-VF_MAKE-'].update(value='')
                        window['-VF_MODEL-'].update(value='')
                        window['-VF_TRIM-'].update(value='')
                        window['-VF_YEAR-'].update(value='')
                        window['-VF_COST-'].update(value='')
                        window['-VF_STATUS-'].update(value='')
                    else:
                        sg.popup('Please fill all boxes.')
                else:
                    window['-SELECTED1-'].update(f"Please select a row before updating.")

            # AVAILABLE VEHICLES EVENTS
            if event == '-TABLE-':
                selected_row = values['-TABLE-'][0]
                selected_vehicle = available[selected_row]
                window['-SELECTED-'].update(f"{selected_vehicle[0]} -  {selected_vehicle[1]} - {selected_vehicle[2]}")
            elif event == '-CALENDAR_START-':
                window['-START-'].update(values['-CALENDAR_START-'])
            elif event == '-CALENDAR_END-':
                window['-END-'].update(values['-CALENDAR_END-'])
            elif event == 'Search':
                if values['-START-'] and values['-END-'] != '':
                    available = fc.get_availability(values['-START-'], values['-END-'])
                    window['-TABLE-'].update(values=available)
            elif event == 'Book':
                fc.book_rental(uc.current_user, available[values['-TABLE-'][0]][4], values['-START-'], values['-END-'])

            # PAYMENT PROCESSING EVENTS
            if event == 'Book':
                format_str = '%m-%d-%Y'
                sd = datetime.datetime.strptime(values['-START-'], format_str).date()
                ed = datetime.datetime.strptime(values['-END-'], format_str).date()
                pc.new_rental(fc.search_by_plate(available[values['-TABLE-'][0]][4]), uc.current_user, (ed - sd).days)
                window['-FIN_TAB2-'].update(values=pc.rental_data.values.tolist())
                window['-P_UUID-'].update(pc.rental_list[-1][0])
                window['-P_AMOUNT-'].update(pc.rental_list[-1][1])
                window['-P_DATE-'].update(pc.rental_list[-1][2])
                window['-P_PLATE-'].update(pc.rental_list[-1][3])
                window['-VIEW-'].update(visible=False)
                window['-PAY_PAGE-'].update(visible=True)

            if event == '-P_CON-':
                window['-VIEW-'].update(visible=True)
                window['-PAY_PAGE-'].update(visible=False)

            # FINANCIAL VIEW EVENTS
            if event == 'Add Expense Payment':
                window['-VIEW-'].update(visible=False)
                window['-EXPENSE-'].update(visible=True)
            if event == '-EP_ENTER-':
                if values['-EP-AMOUNT-'] and values['-EP-DATE-'] and values['-EP-RES-'] != '':
                    d = [values['-EP-AMOUNT-'], values['-EP-DATE-'], values['-EP-RES-']]
                    pc.new_expense(d)
                    window['-VIEW-'].update(visible=True)
                    window['-EXPENSE-'].update(visible=False)
                    window['-FIN_TAB1-'].update(values=pc.expense_data.values.tolist())
                    window['-EP-AMOUNT-'].update(value='')
                    window['-EP-DATE-'].update(value='')
                    window['-EP-RES-'].update(value='')
            if event == '-EP_BACK-':
                window['-VIEW-'].update(visible=True)
                window['-EXPENSE-'].update(visible=False)
                window['-EP-AMOUNT-'].update(value='')
                window['-EP-DATE-'].update(value='')
                window['-EP-RES-'].update(value='')
            if event == '-FIN_TAB1-':
                window['-FIN_AMT-'].update(value=pc.expense_data.values.tolist()[values['-FIN_TAB1-'][0]][0])
                window['-FIN_DATE-'].update(value=pc.expense_data.values.tolist()[values['-FIN_TAB1-'][0]][1])
                window['-FIN_RES-'].update(value=pc.expense_data.values.tolist()[values['-FIN_TAB1-'][0]][2])
            else:
                window['-FIN_AMT-'].update(value='')
                window['-FIN_DATE-'].update(value='')
                window['-FIN_RES-'].update(value='')
