from .payment_controller import PaymentController
import PySimpleGUI as sg


pc = PaymentController()
expense_data = pc.expense_data
rental_data = pc.rental_data

# the main window showing the financial view of rentals and expenses
layout1 = [
    [sg.Text('Payments', font='Helvetica 20 bold underline', justification='center')],
    [sg.Table(values=pc.expense_list, headings=expense_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_click_events=True, key='-TABLE1-'),
     sg.Table(values=pc.rental_list, headings=rental_data.columns.tolist(), auto_size_columns=False,
              max_col_width=25, justification='center', enable_click_events=True, key='-TABLE2-')],
    [sg.Button('Add Rental Payment', font='Helvetica 14',),
     sg.Button('Add Expense Payment', font='Helvetica 14')],
    [sg.Button('Close', font='Helvetica 14')]
]

# temporary window to add a rental payment manually
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
    [sg.Button('Enter Payment', font='Helvetica 14', key='-RP_ENTER-'), sg.Push(),
     sg.Button('Back', font='Helvetica 14', key='-RP_BACK-')]
]

# window to add an expense payment
layout3 = [
    [sg.Text('Add Expense Payment', font='Helvetica 20 bold underline')],
    [sg.Text('Amount:', font='Helvetica 16 bold', key='-EP_AMOUNT-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1])],
    [sg.Text('DATE:', font='Helvetica 16 bold', key='-EP_DATE-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1])],
    [sg.Text('REASON:', font='Helvetica 16 bold', key='-EP_RES-'), sg.Push(),
     sg.InputText(font='Helvetica 14', size=[30, 1]), sg.Push()],
    [sg.Button('Enter Payment', font='Helvetica 14', key='-EP_ENTER-'), sg.Push(),
     sg.Button('Back', font='Helvetica 14', key='-EP_BACK-')]
]

# an after purchase look at the information
layout4 = [
    [sg.Text('Thank you for your purchase!', font='Helvetica 20 bold')],
    [sg.Text('UUID:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][0], font='Helvetica 20 bold', key='-P_UUID-')],
    [sg.Text('Amount:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][1], font='Helvetica 20 bold', key='-P_AMOUNT-')],
    [sg.Text('Date:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][2], font='Helvetica 20 bold', key='-P_DATE-')],
    [sg.Text('License Plate:', font='Helvetica 20 bold'), sg.Push(),
     sg.Text(pc.rental_list[-1][3], font='Helvetica 20 bold', key='-P_PLATE-')],
    [sg.Button('Continue', font='Helvetica 20 bold', key='-P_CON-')]

]

layout = [[sg.Column(layout1, key='-COL1-'),
           sg.Column(layout2, visible=False, key='-COL2-'),
           sg.Column(layout3, visible=False, key='-COL3-'),
           sg.Column(layout4, visible=False, key='-COL4-')]]
window = sg.Window('Club Penguin Car Rentals', layout)


class PaymentInterface:
    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WINDOW_CLOSED or event == 'Close':
                break

            # buttons that change the window
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

            if event == '-P_CON-':
                window[f'-COL{1}-'].update(visible=True)
                window[f'-COL{4}-'].update(visible=False)

            # enters the values and updates the table switching to layout 4
            if event == '-RP_ENTER-':
                if values[0] and values[1] and values[2] and values[3] != '':
                    data = [values[0], values[1], values[2], values[3]]
                    pc.new_rental(data)
                    window['-TABLE2-'].update(values=pc.rental_data.values.tolist())

                    window['-P_UUID-'].update(pc.rental_list[-1][0])
                    window['-P_AMOUNT-'].update(pc.rental_list[-1][1])
                    window['-P_DATE-'].update(pc.rental_list[-1][2])
                    window['-P_PLATE-'].update(pc.rental_list[-1][3])
                    window[f'-COL{4}-'].update(visible=True)
                    window[f'-COL{2}-'].update(visible=False)

                else:
                    print("please fill in all required fields.")

            # enters the values and updates the table
            if event == '-EP_ENTER-':
                if values[4] and values[5] and values[6] != '':
                    data = [values[4], values[5], values[6]]
                    pc.new_expense(data)
                    window['-TABLE1-'].update(values=pc.expense_data.values.tolist())

                else:
                    print("please fill in all required fields.")
