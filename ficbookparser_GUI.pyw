import PySimpleGUI as sg
import ficbookparser as fbp

def update(x, key):
    text_elem = window[key]
    text_elem.update("{}".format(x))

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Fanfiction URL:'), sg.InputText()],
            [sg.Button('[Parse]'), sg.Button('[Download]'), sg.InputText(size=(8,1)), sg.Text("Chapter number (leave empty to download all chapters)")],
            [sg.Text("Название: []", key='-title-')],
            [sg.Output(size=(80, 20))] ]

# Create the Window
window = sg.Window('Ficbook Parser', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window
        break
    
    if event == '[Parse]':
        try:
            fic = fbp.parse(values[0])
        except:
            print('Error while parsing. Did you enter url before trying to parse?')
        else:
            update('Title: ['+fbp.get_title(fic)+']','-title-')
            fbp.get_chapters(fic, True)
            print(('{:=<50}').format(''))

    if event == '[Download]':
        num = -1
        print('Downloading...')
        if values[1] != '':
            num = int(values[1])
        try:
            fbp.export(fic, num)
            print('Download complete!')
        except:
            print('Error while trying to export. Did you parse first?')


window.close()