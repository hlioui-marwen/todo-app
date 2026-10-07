import FreeSimpleGUI as sg

layout = [[sg.Text('Hello, this is your first GUI!')], [sg.Button('OK')]]
window = sg.Window('My First Window', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'OK':
        break

window.close()