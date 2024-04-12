import PySimpleGUI as sg
import pandas as pd

filename = "view.csv"

def load_and_filter_fleet(filename):
    fleet_data = pd.read_csv(filename)
    if "Status" in fleet_data.columns:
        available_cars = fleet_data[fleet_data["Status"] == "Available"]
        return available_cars
    else:
        sg.popup_error(f"Error: 'Status' column not found in the CSV file.")
        return pd.DataFrame()

custom_font = ("Arial", 12)  # Example of a custom font (Arial, size 12)

available_cars = load_and_filter_fleet(filename)  # Load and filter fleet data

# Check if there are available cars to display
if not available_cars.empty:
    layout = [
        [sg.Text("Available Cars for Rent", font=custom_font)],
        [sg.Table(values=available_cars.values.tolist(),  # Use filtered data for values
                  headings=available_cars.columns.tolist(),  # Use filtered data for headings
                  display_row_numbers=False, auto_size_columns=False,
                  col_widths=50,  # Set the width of each column to 50 pixels
                  justification='center', key='-TABLE-')],
        [sg.Button("Close")]
    ]

    window = sg.Window("Car Rental - Available Cars", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break

    window.close()
else:
    sg.popup_error("No available cars found in the fleet data.")
