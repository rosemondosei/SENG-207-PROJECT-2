# SENG 207 - PROGRAMMING FOR ENGINEERS
# NAME : ROSEMOND OSEI
# ID : 10976906
# PROJECT 2 - PART 1
# BMEN DEPARTMENT


import PySimpleGUI as sg
import pyttsx3


sg.theme('DarkGreen4')


mainEngine = pyttsx3.init()
voiceChoice = mainEngine.getProperty('voices')


win_layout = [    [sg.Text('Select the type of voice:'),sg.Radio('Male', 'RADIO1', default=True, key='male'),sg.Radio('Female', 'RADIO1', key='female')],
     [sg.Text('Enter text to speak:')],
     [sg.InputText(key='type'),sg.Button('Speak')],
      [sg.Text("Volume:",text_color= '#030008',background_color='Teal')],
    [sg.Slider(range=(0, 1), resolution=0.1, default_value=0.5, orientation="h", key="-VOLUME-")],
    [sg.Text("Rate:",text_color= '#030008',background_color='Teal')],
    [sg.Slider(range=(100, 300), resolution=10, default_value=200, orientation="h", key="-SPEED-")]
]

window = sg.Window('Rosey Text-To-Speech', win_layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        if values['male']:
            mainEngine.setProperty('voice', voiceChoice[0].id)
        elif values['female']:
           mainEngine.setProperty('voice', voiceChoice[1].id)

        
        text = values['type']
        userVolume = values["-VOLUME-"]
        userRate = values["-SPEED-"]
        mainEngine.setProperty('volume', userVolume)
        mainEngine.setProperty("rate", userRate)
        mainEngine.say(text)
        mainEngine.runAndWait() 
    
        mainEngine.say(text)
        mainEngine.runAndWait()

window.close()