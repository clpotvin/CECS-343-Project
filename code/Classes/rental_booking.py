import PySimpleGUI as sg
import pandas as pd


df = pd.read_csv('view.csv')


available_df = df[df['Status'] == 'Available']


def check_availability(vehicle_id, start_date, end_date):
    payload = {
        "vehicle_id": vehicle_id,
        "start_date": start_date,
        "end_date": end_date
    }


layout = [
    [sg.Text('Available Vehicles')],
    [sg.Table(values=available_df.values.tolist(),
              headings=available_df.columns.tolist(),
              auto_size_columns=False,
              col_widths=15,
              justification='center',
              key='-TABLE-', enable_events=True)],
    [sg.Text('Selected Vehicle:'), sg.Text(size=(20, 1), key='-SELECTED-', enable_events=True, visible=True)],
    [sg.Text('Start Date:'),
     sg.CalendarButton('Select', target='-START-', key='-CALENDAR_START-', format='%d-%m-%Y', enable_events=True),
     sg.InputText(key='-START-', visible=True)],
    [sg.Text('End Date:'),
     sg.CalendarButton('Select', target='-END-', key='-CALENDAR_END-', format='%d-%m-%Y', enable_events=True),
     sg.InputText(key='-END-', visible=True)],
    [sg.Button('Book'), sg.Button('Exit')]
]

window = sg.Window('Vehicle Booking System', layout)

print(available_df)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == '-TABLE-':

        selected_row = values['-TABLE-'][0]
        selected_vehicle = available_df.values[selected_row]
        print(selected_vehicle)
        window['-SELECTED-'].update(f"{selected_vehicle[0]} -  {selected_vehicle[1]} - {selected_vehicle[2]}")
    elif event == '-CALENDAR_START-':
        window['-START-'].update(values['-CALENDAR_START-'])
    elif event == '-CALENDAR_END-':
        window['-END-'].update(values['-CALENDAR_END-'])
    elif event == 'Book':
        try:
            if selected_vehicle is None:
                raise ValueError("Please select a vehicle from the table.")

            #selected_row = int(selected_row['VehicleID'])
            start_date = values['-START-']
            end_date = values['-END-']

            availability_response = check_availability(selected_row, start_date, end_date)

            if availability_response['Available']:
                sg.popup(f'Vehicle {selected_row} is available for booking!')
            else:
                sg.popup(f'Vehicle {selected_row} is not available for the selected dates.')
        except ValueError as ve:
            sg.popup(str(ve))

window.close()
