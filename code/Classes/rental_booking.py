import PySimpleGUI as sg
import pandas as pd
import datetime
from fleet_managment import FleetManagement


def init(self):
    self.reservation_data = pd.read_csv("CECS-343-Project/code/Data/reservations")
    self.reservations = [Reservation(n[0], FleetManagment.search_by_plate(n[1]), n[2], date_str_to_date_obj(n[3]),
                                     date_str_to_date_obj(n[4]), n[5]) for n in self.reservation_data.values]
def check_availability(license_plate, start_date, end_date):
    view_df = pd.read_csv('view.csv')
    data_df = pd.read_csv('data.csv')

    start_date_obj = date_str_to_date_obj(start_date)
    end_date_obj = date_str_to_date_obj(end_date)

    if not view_df.empty and 'Status' in view_df.columns and 'License Plate' in view_df.columns:
        print(view_df["License Plate"])
        print(license_plate)
        if license_plate in view_df['License Plate'].tolist():
            idx = view_df['License Plate'].tolist().index(license_plate)
            vehicle_status = view_df['Status'][idx]
        else:
            return 'Not Available'

    idxs = [x for x in range(0, len(data_df['License Plate'].tolist())) if data_df['License Plate'][x] == license_plate]
    temp = []
    for i in idxs:
        temp.append([pd.to_datetime(data_df['Start Date'][i], format='%m-%d-%Y'),
                     pd.to_datetime(data_df['End Date'][i], format='%m-%d-%Y')])
    vehicle_bookings = pd.DataFrame.from_records(temp, columns=['Start Date', 'End Date'])
    print(temp)
    print(idxs)

    print(vehicle_bookings['Start Date'].values)

    overlapping_bookings = vehicle_bookings[
        (vehicle_bookings['Start Date'] <= end_date_obj) & (start_date_obj <= vehicle_bookings['End Date'])
    ]

    if not overlapping_bookings.empty or vehicle_status != 'Available':
        return 'Not Available'
    else:
        return 'Available'


def date_str_to_date_obj(date_string):
    format_str = '%m-%d-%Y'
    dt = datetime.datetime.strptime(date_string, format_str)
    return dt.date()

df = pd.read_csv('view.csv')
available_df = df[df['Status'] == 'Available']

# Modify table_data generation to include the make of the vehicle
table_data = available_df[['Make', 'Model','Trim', 'Year', 'Status']].values.tolist()


layout = [
    [sg.Text('Available Vehicles')],
    [sg.Table(values=table_data,
              headings=['Make', 'Model', 'Trim', 'Year', 'Status'],  # Adjusted headings without License Plate
              auto_size_columns=False,
              col_widths=15,
              justification='center',
              key='-TABLE-', enable_events=True)],
    # Your existing layout definition

    [sg.Text('Selected Vehicle:'), sg.Text(size=(20, 1), key='-SELECTED-', enable_events=True, visible=True)],
    [sg.Text('Start Date:'),
     sg.CalendarButton('Select', target='-START-', key='-CALENDAR_START-', format='%m-%d-%Y', enable_events=True),
     sg.InputText(key='-START-', visible=True)],
    [sg.Text('End Date:'),
     sg.CalendarButton('Select', target='-END-', key='-CALENDAR_END-', format='%m-%d-%Y', enable_events=True),
     sg.InputText(key='-END-', visible=True)],
    [sg.Button('Book'), sg.Button('Exit')]
]

window = sg.Window('Vehicle Booking System', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == '-TABLE-':
        selected_row = values['-TABLE-'][0]
        selected_vehicle = available_df.values[selected_row]
        window['-SELECTED-'].update(f"{selected_vehicle[0]} -  {selected_vehicle[1]} - {selected_vehicle[2]}")
    elif event == '-CALENDAR_START-':
        window['-START-'].update(values['-CALENDAR_START-'])
    elif event == '-CALENDAR_END-':
        window['-END-'].update(values['-CALENDAR_END-'])
    elif event == 'Book':
        try:
            selected_row = values['-TABLE-'][0]
            selected_vehicle = available_df.values[selected_row]
            license_plate = selected_vehicle[4]
            start_date = values['-START-']
            end_date = values['-END-']

            availability_response = check_availability(license_plate, start_date, end_date)

            if availability_response == 'Available':
                sg.popup(f'Vehicle {selected_vehicle} is available for booking!')
            else:
                sg.popup(f'Vehicle {selected_vehicle} is not available for the selected dates.')
        except ValueError as ve:
            sg.popup(str(ve))

window.close()