from .payment_controller import PaymentController
import PySimpleGUI as sg
import pandas as pd

pc = PaymentController()
expense_data = pc.expense_data
rental_data = pc.rental_data


layout1 = [
    [sg.Text('Payments', font='Helvetica 20 bold underline', justification='center')],
    [sg.Table(values=pc.expense_list, headings=expense_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_click_events=True),
     sg.Table(values=pc.rental_list, headings=rental_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_click_events=True)],
    [sg.Button('Add Rental Payment', font='Helvetica 14',),
     sg.Button('Add Expense Payment', font='Helvetica 14')],
    [sg.Button('Close', font='Helvetica 14')]
]

layout2 = [
    [sg.Text('Add Rental Payment', font='Helvetica 20 bold underline')],
    [sg.Text('UUID:', font='Helvetica 16 bold', key='-RP_ID-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1])],
    [sg.Text('Amount:', font='Helvetica 16 bold', key='-RP_AMOUNT-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1])],
    [sg.Text('DATE:', font='Helvetica 16 bold', key='-RP_DATE-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1])],
    [sg.Text('RESERVATION:', font='Helvetica 16 bold', key='-RP_RES-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1]), sg.Push()],
    [sg.Button('Enter Payment', font='Helvetica 14',key='-RP_ENTER-'),sg.Push(),
     sg.Button('Back', font='Helvetica 14', key='-RP_BACK-')]
]

layout3 = [
    [sg.Text('Add Expense Payment', font='Helvetica 20 bold underline')],
    [sg.Text('Amount:', font='Helvetica 16 bold', key='-EP_AMOUNT-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1])],
    [sg.Text('DATE:', font='Helvetica 16 bold', key='-EP_DATE-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1])],
    [sg.Text('REASON:', font='Helvetica 16 bold', key='-EP_RES-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1]), sg.Push()],
    [sg.Button('Enter Payment', font='Helvetica 14',key='-EP_ENTER-'),sg.Push(),
     sg.Button('Back', font='Helvetica 14', key='-EP_BACK-')]
]

layout = [[sg.Column(layout1, key='-COL1-'),
           sg.Column(layout2, visible=False, key='-COL2-'),
           sg.Column(layout3, visible=False, key='-COL3-')]]
window = sg.Window('Club Penguin Car Rentals', layout)

class PaymentInterface:
    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WINDOW_CLOSED or event == 'Close':
                break

            if event == 'Add Rental Payment':
                window[f'-COL{1}-'].update(visible=False)
                window[f'-COL{2}-'].update(visible=True)

            if event == 'Add Expense Payment':
                window[f'-COL{1}-'].update(visible=False)
                window[f'-COL{3}-'].update(visible=True)

            if event == '-RP_BACK-':
                window[f'-COL{1}-'].update(visible=True)
                window[f'-COL{2}-'].update(visible=False)

            if event == '-EP_BACK-':
                window[f'-COL{1}-'].update(visible=True)
                window[f'-COL{3}-'].update(visible=False)

            if event == '-RP_ENTER-':
                if values[2] and values[3] and values[4] and values[5] !='':
                    data = [values[2], values[3], values[4], values[5]]
                    pc.new_rental(data)
                else:
                    print("please fill in all required fields.")

            if event == '-EP_ENTER-':
                if values[6] and values[7] and values[8] !='':
                    data = [values[6], values[7], values[8]]
                    pc.new_expense(data)
                else:
                    print("please fill in all required fields.")


