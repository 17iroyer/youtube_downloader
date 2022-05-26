# Ian Royer
# 6-1-2021
# A simple GUI for the ytdownloader to use

import ytdownload
import PySimpleGUI as sg

# The layout for the window being created
win_layout = [
        [sg.Text("Welcome to Simple YT Downloader")],
        [
            sg.Text("Link"),
            sg.In(size=(34, 1), enable_events=True, key="-LINK-"),
            sg.Button("Check Link", key="-NEWLINK-")
        ],
        [sg.HorizontalSeparator()],
        [
            sg.Text(size=(40, 6), key="-VIDINFO-")
        ],
        [sg.HorizontalSeparator()],
        [
            sg.Text("Download Location"),
            sg.In(size=(25, 1), enable_events=True, key="-LOC-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Button("Download", button_color=(0, 0xD2342F), key="-DL-"),
            sg.Text(size=(30, 1), key="-DONE-")
        ]
    ]


downloader = ytdownload.Ytdownloader()
window = sg.Window("Simple YT Downloader", win_layout)

#Event Loop
while True:
    event, values = window.read()
    if event == "-NEWLINK-":
        if(downloader.setLink(window["-LINK-"].get()) == True and downloader.check_avail() == True):
            window["-VIDINFO-"].update(downloader.getinfo())
        else:
            window["-VIDINFO-"].update("Invalid Link")
    
    if event == "-DL-":
        downloader.setLoc(window["-LOC-"].get())
        if(downloader.do_download() == True):
            window["-DONE-"].update("Complete!")
        else:
            window["-DONE-"].update("Error in downloading file")
    
    if event == sg.WIN_CLOSED:
        break

#Close when done
window.close()