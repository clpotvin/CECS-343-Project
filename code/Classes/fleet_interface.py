from fleet_controller import FleetController
import PySimpleGUI as sg
import pandas as pd

fc = FleetController()
fleet_data = fc.vehicle_data

# Convert DataFrame to list of lists for Table widget
data = fc.vehicle_list

layout1 = [
    [sg.Table(values=data, headings=fleet_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_click_events=True)],
    [sg.Button('Add'), sg.Button('Edit'), sg.Button('Remove')],
    [sg.Text('Add = Adds a vehicle')],
    [sg.Text('Edit = Edit a selected vehicle')],
    [sg.Text('Remove = Removes a selected vehicle')],
    [sg.Button('Close')],
]

window = sg.Window('Fleet Management Viewer', layout1)

class FleetInterface:
    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WINDOW_CLOSED or event == 'Close':
                break
            if isinstance(event, tuple):
                if event[0] == 0:
                    row_index = (event[2][0])
                    print(fc.get_vehicle_index(row_index))

        window.close()