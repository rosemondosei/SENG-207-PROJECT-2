# SENG 207 - PROGRAMMING FOR ENGINEERS
# NAME : ROSEMOND OSEI
# ID : 10976906
# PROJECT 2 - PART 2
# BMEN DEPARTMENT



import PySimpleGUI as sg
import qrcode

sg.theme('NeutralBlue')

layout = [
    [sg.Text('Link: ')],
    [sg.Input(key='linkUser')],
    [sg.Text('Choose a color:'), sg.Combo(values=['red','orange','green', 'blue'], key='colorUser', default_value='black')],
    [sg.Slider(range=(1, 20), orientation='h', default_value=10, key='sizeUser')],
    [sg.Button('Generate'), sg.Button('Save As')],
    [sg.Image(key='image')]
]

window = sg.Window('Rosey Qr Code Generator', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Generate':
        input = values['linkUser']
        color = values['colorUser']
        size = values['sizeUser']
        if input.strip() == "":
            sg.popup_error("Input cannot be empty!")
            continue

        try:
            qr = qrcode.QRCode(version=1,box_size=size, border=3, error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(input)
            qr.make(fit=True)
            img = qr.make_image(fill_color=color, back_color='white')
            img.save('qr-code.png')
        except:
            sg.popup_error('Invalid input, Try Again!')
            continue
        
        window['image'].update('qr-code.png')
    
    if event == 'Save As':
        nameFile = sg.popup_get_file('QR Code SAVE', save_as=True, default_extension='.png')
        if nameFile:
            img.save(nameFile)
    
        

window.close()