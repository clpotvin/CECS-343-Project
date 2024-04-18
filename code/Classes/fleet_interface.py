from fleet_controller import FleetController
import PySimpleGUI as sg
import pandas as pd

fc = FleetController()
fleet_data = fc.vehicle_data

# Convert DataFrame to list of lists for Table widget
data = fc.vehicle_list

main_layout = [
    [sg.Table(values=data, headings=fleet_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_click_events=True)],
    [sg.Button('Add'), sg.Button('Edit'), sg.Button('Remove')],
    [sg.Text('Add = Adds a vehicle')],
    [sg.Text('Edit = Edit a selected vehicle')],
    [sg.Text('Remove = Removes a selected vehicle')],
    [sg.Button('Close')],
]

layout2 = [

]

add_car_layout = [[sg.Text('Add a New Vehicle', font='Helvetica 20 bold underline')],
       [sg.VPush()],
       [sg.Text('Make:', font='Helvetica 16 bold', key='-AV_MAKE-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Model:', font='Helvetica 16 bold', key='-AV_MODEL-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Year:', font='Helvetica 16 bold', key='-AV_YEAR-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Trim:', font='Helvetica 16 bold', key='-AV_TRIM-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('License Plate:', font='Helvetica 16 bold', key='-AV_LP-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Price:', font='Helvetica 16 bold', key='-AV_PRICE-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Status:', font='Helvetica 16 bold', key='-AV_STATUS-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.VPush()],
       [sg.Button('Go Back', font='Helvetica 14', key='-AV_BACK-'),
        sg.Push(), sg.Button('Confirm', font='Helvetica 14', key='AV_CONFIRM')]]

edit_car_layout = [[sg.Text('Edit a New Vehicle', font='Helvetica 20 bold underline')],
       [sg.VPush()],
       [sg.Text('Make:', font='Helvetica 16 bold', key='-AV_MAKE-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Model:', font='Helvetica 16 bold', key='-AV_MODEL-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Year:', font='Helvetica 16 bold', key='-AV_YEAR-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Trim:', font='Helvetica 16 bold', key='-AV_TRIM-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('License Plate:', font='Helvetica 16 bold', key='-AV_LP-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Price:', font='Helvetica 16 bold', key='-AV_PRICE-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.Text('Status:', font='Helvetica 16 bold', key='-AV_STATUS-'), sg.Push(),
        sg.InputText(font='Helvetica 14', size=[30, 1])],
       [sg.VPush()],
       [sg.Button('Go Back', font='Helvetica 14', key='-AV_BACK-'),
        sg.Push(), sg.Button('Confirm', font='Helvetica 14', key='AV_CONFIRM')]]

layout_cols = [[sg.Column(main_layout, key='-COL1-'),
                sg.Column(add_car_layout, visible=False, key='-COL2-'),
                ]]

window = sg.Window('Fleet Management Viewer', layout_cols)

class FleetInterface:
    def run(self):
        current_vehicle = None
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WINDOW_CLOSED or event == 'Close':
                break
            if event == 'Add':
                window[f'-COL{1}-'].update(visible=False)
                window[f'-COL{2}-'].update(visible=True)

            if event == '-AV_BACK-':
                window[f'-COL{1}-'].update(visible=True)
                window[f'-COL{2}-'].update(visible=False)

            if event == '-AV_CONFIRM-':
                if values[1] and values[2] and values[3] and values[4] and values[5] and values[6] and values[7] != '':
                    arr = [values[1], values[2], values[3], values[4], values[5], values[6], values[7]]
                    fc.add_vehicle(arr)

            if isinstance(event, tuple):
                if event[0] == 0:
                    row_index = (event[2][0])
                    if row_index:
                        current_vehicle = fc.get_vehicle_index(row_index)
                    print(current_vehicle)


        window.close()