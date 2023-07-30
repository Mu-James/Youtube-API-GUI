import tkinter as tk
from tkinter import messagebox

_DELETE_WINDOW_PROTCOL = "WM_DELETE_WINDOW",

_LABLE_TEXT_WELCOME = "Welcome, please choose an option below:"
_LABLE_TEXT_API_SELECTION = "Please select an API category below:"

_BUTTON_TEXT_API_RELATED = "API Related"
_BUTTON_TEXT_NON_API_RELATED = "Non-API Related"
_BUTTON_TEXT_CLOSE = "Close"
_BUTTON_TEXT_VIDEOS = "Videos"
_BUTTON_TEXT_CHANNELS = "Channels"
_BUTTON_TEXT_PLAYLISTS = "Playlists"

_MESSAGEBOX_TITLE_CONFIRM_CLOSE = "Close Youtube API GUI?"
_MESSAGEBOX_MESSAGE_CONFIRM_CLOSE = "Are you sure you want to close Youtube API GUI?"

_WINDOW_TITLE_API_SELECTION = "Youtube API GUI: API Selection"
_WINDOW_TITLE_NON_API_SELECTION = "Youtube API GUI: Non-API Selection"

_WINDOW_TITLE_ROOT = "Youtube API GUI"
_START_RESOLUTION = "512x512"
_DEFAULT_FONT = "Arial"

def _dummy():
    pass

class YoutubeApiGUI:
    def __init__(self):
        self._root_window = tk.Tk()
        self._root_window.title(_WINDOW_TITLE_ROOT)
        self._root_window.geometry(_START_RESOLUTION)

        #Labels
        welcome = self._create_label(self._root_window, _LABLE_TEXT_WELCOME, 0, 0)

        #Buttons
        api_related = self._create_button(self._root_window, _BUTTON_TEXT_API_RELATED, 1, 0, self._open_api_selection)
        non_api_realted = self._create_button(self._root_window, _BUTTON_TEXT_NON_API_RELATED, 2, 0, self._open_non_api_selection)
        close = self._create_button(self._root_window, _BUTTON_TEXT_CLOSE, 3, 0, self._confirm_close_GUI)
        
    def run(self):
        self._root_window.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._root_window.mainloop()

    def _confirm_close_GUI(self):
        #response = tk.messagebox.askyesno(_MESSAGEBOX_TITLE_CONFIRM_CLOSE, _MESSAGEBOX_MESSAGE_CONFIRM_CLOSE)
        response = self._create_messagebox("askyesno", _MESSAGEBOX_TITLE_CONFIRM_CLOSE, _MESSAGEBOX_MESSAGE_CONFIRM_CLOSE)
        if response == True:
            self._root_window.destroy()
        elif response == False:
            pass

    def _open_api_selection(self):
        self._window_api_selection = self._create_top_level_window(self._root_window, _WINDOW_TITLE_API_SELECTION)
        self._window_api_selection.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI)
        self._root_window.withdraw()

        #Labels
        selection = self._create_label(self._window_api_selection, _LABLE_TEXT_API_SELECTION, 0, 0)

        #Buttons
        select_channels = self._create_button(self._window_api_selection, _BUTTON_TEXT_CHANNELS, 1, 0, _dummy)
        select_playlists = self._create_button(self._window_api_selection, _BUTTON_TEXT_PLAYLISTS, 2, 0, _dummy)
        select_videos = self._create_button(self._window_api_selection, _BUTTON_TEXT_VIDEOS, 3, 0, _dummy)

    def _open_non_api_selection(self):
        self._window_non_api_selection = self._create_top_level_window(self._root_window, _WINDOW_TITLE_NON_API_SELECTION)
        self._window_non_api_selection.protocol(_DELETE_WINDOW_PROTCOL, self._confirm_close_GUI )
        self._root_window.withdraw()
        
    def _create_button(self, master, text, row, column, command):
        button = tk.Button(
            master = master,
            text = text, font = _DEFAULT_FONT,
            command = command
        )
        button.grid(
            row = row,
            column = column,
        )
        return button
    
    def _create_label(self, master, text, row, column):
        label = tk.Label(
            master = master,
            text = text,
        )
        label.grid(
            row = row,
            column = column
        )
        return label
    
    def _create_messagebox(self, style, title, message):
        data = {"tk":tk}
        exec(f'messagebox = tk.messagebox.{style}(title = "{title}", message = "{message}")', data)
        return data['messagebox']
    
    def _create_top_level_window(self, root, title):
        top_window = tk.Toplevel(root)
        top_window.title(title)
        return top_window

if __name__ == "__main__":
    ytapigui = YoutubeApiGUI()
    ytapigui.run()