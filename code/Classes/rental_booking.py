import PySimpleGUI as sg
import pandas as pd

# Load data from CSV
df = pd.read_csv('view.csv')

# Filter out only available vehicles
available_df = df[df['Status'] == 'Available']

layout = [
    [sg.Text('Available Vehicles')],
    [sg.Table(values=available_df.values.tolist(),
              headings=available_df.columns.tolist(),
              #display_row_numbers=True,   #display the row number
              auto_size_columns=False,
              col_widths=15,
              justification='center',
              key='-TABLE-')],
    [sg.Text('Please select a vehicle to book')],
    #[sg.InputText(key='-INPUT-')],
    [sg.Button('Select'), sg.Button('Exit')]
]

window = sg.Window('Vehicle Booking System', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Select':
        try:
            selected_index = int(values['-INPUT-']) - 1
            if 0 <= selected_index < len(available_df):
                vehicle_id = available_df.iloc[selected_index]['VehicleID']
                df.loc[df['VehicleID'] == vehicle_id, 'Availability'] = 'Booked'
                sg.popup(f'Vehicle {vehicle_id} booked successfully!')
                # Update the table display
                available_df = df[df['Availability'] == 'Available']  # Update available vehicles
                window['-TABLE-'].update(values=available_df.values.tolist())
        except ValueError:
            sg.popup("Please enter a valid vehicle ID.")

window.close()
