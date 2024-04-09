import PySimpleGUI as sg
import pandas as pd

def load_fleet(filename):
    fleet_data = pd.read_csv(filename)
    return fleet_data

filename = "view.csv"
fleet_data = load_fleet(filename)

# Convert DataFrame to list of lists for Table widget
data = fleet_data.values.tolist()

layout = [
    [sg.Table(values=data, headings=fleet_data.columns.tolist(), auto_size_columns=False,
              col_widths=25, justification='center')],
    [sg.Button('Close')]
]

window = sg.Window('Fleet Management Viewer', layout)

while True:
    action, _ = window.read()
    if action == sg.WINDOW_CLOSED or action == 'Close':
        break

window.close()
