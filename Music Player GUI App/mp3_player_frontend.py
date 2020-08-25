from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from pygame import mixer
import mp3_player_backend as mp3
import os

mpback = mp3.backend()


class frontend(object):
    def __init__(self, window):
        
        self.window = window

        b1 = Button(window, text = "Open a File From Your PC", width = 20, height = 4, command = mpback.open_file)
        b1.grid(row = 0, column = 0)
        b10 = Button(window, text = "Open a File From a Playlist", width = 20, height = 4, command = self.open_from_playlist_fun)
        b10.grid(row = 1, column = 0)
        b2 = Button(window, text = "Pause", width = 20, height = 2, command = mpback.pause)
        b2.grid(row = 8, column = 2)
        b3 = Button(window, text = "Resume", width = 20, height = 2, command = mpback.resume)
        b3.grid(row = 8, column = 3)
        b4 = Button(window, text = "Stop", width = 20, height = 2, command = mpback.stop)
        b4.grid(row = 8, column = 4)
        b5 = Button(window, text = "Create a Playlist", width = 20, height = 4, command = self.create_playlist)
        b5.grid(row = 2, column = 0)
        b6 = Button(window, text = "Edit a Playlist", width = 20, height = 4, command = self.edit_playlist)
        b6.grid(row = 3, column = 0)
        b7 = Button(window, text = "Delete a Playlist", width = 20, height = 4, command = self.delete_playlist)
        b7.grid(row = 4, column = 0)
        b8 = Button(window, text = "View Playlists", width = 20, height = 4, command = self.view_playlists)
        b8.grid(row = 5, column = 0)
        b11 = Button(window, text = "User Guide", height = 4, width = 20, command = self.user_guide)
        b11.grid(row = 6, column = 0)
        b9 = Button(window, text = "Exit", width = 20, height = 4, command = window.destroy)
        b9.grid(row = 7, column = 0)

    def create_playlist(self):
        create_playlist_window(self.window)

    def delete_playlist(self):
        delete_playlist_window(self.window)

    def edit_playlist(self):
        edit_playlist_window(self.window)

    def view_playlists(self):
       view_playlists_window(self.window)

    def open_from_playlist_fun(self):
        open_from_playlist_window(self.window)

    def user_guide(self):
        user_guide_window(self.window)




class create_playlist_window(object):

    def __init__(self, window):
        
        def close():
            m1.destroy()
            m2.destroy()
            self.e1.destroy()
            self.e2.destroy()
            b1.destroy()
            b2.destroy()

        def create_playlist_1():
            if self.user_name.get() == "" or self.playlist_name.get() == "":
                messagebox.showinfo(title = "Error", message = "Please enter both the user and the playlist's name")
            else:
                mpback.create_playlist(self.user_name.get(), self.playlist_name.get())
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                messagebox.showinfo(title = "Succes", message = "The Playlist has been created succefully")

        self.window = window

        m1 = Message(window, text = "Playlist's name")
        m1.grid(row = 0, column = 4)
        m2 = Message(window, text = "User name")
        m2.grid(row = 0, column = 2)
        self.user_name = StringVar()
        self.e1 = Entry(window, textvariable = self.user_name)
        self.e1.grid(row = 0, column = 3)
        self.playlist_name = StringVar()
        self.e2 = Entry(window, textvariable = self.playlist_name)
        self.e2.grid(row = 0, column = 5)

                
        b1 = Button(window, text = "Enter", command = create_playlist_1)
        b1.grid(row = 0, column = 6)
        b2 = Button(window, text = "Close", command = close)
        b2.grid(row = 0, column = 7)
    

class delete_playlist_window(object):
    def __init__(self, window):

        def close():
            m0.destroy()
            m1.destroy()
            self.e1.destroy()
            self.e0.destroy()
            b1.destroy()
            b2.destroy()

        self.window = window
        m0 = Message(window, text = "User Name")
        m0.grid(row = 0, column = 2)
        m1 = Message(window, text = "Playlist's name")
        m1.grid(row = 0, column = 4)
        self.user_name = StringVar()
        self.e0 = Entry(window, textvariable = self.user_name)
        self.e0.grid(row = 0, column = 3)
        self.playlist_name = StringVar()
        self.e1 = Entry(window, textvariable = self.playlist_name)
        self.e1.grid(row = 0, column = 5)

        b1 = Button(window, text = "Delete", command = self.delete_playlist_func)
        b1.grid(row = 0, column = 6)
        b2 = Button(window, text = "Close", command = close)
        b2.grid(row = 0, column = 7)

    def delete_playlist_func(self):
        if self.user_name.get() == "" or self.playlist_name.get() == "":
            messagebox.showinfo(title = "Error", message = "Please enter both the user and the playlist's name")
        else:
            mpback.delete_playlist(self.user_name.get(), self.playlist_name.get())
            self.e0.delete(0, END)
            self.e1.delete(0, END)


class edit_playlist_window(object):
    def __init__(self, window):

        def close():
            m0.destroy()
            m1.destroy()
            self.e1.destroy()
            self.e2.destroy()
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            try:
                self.l1.destroy()
            except:
                pass

        self.window = window

        m0 = Message(window, text = "User Name")
        m0.grid(row = 0, column = 2)
        m1 = Message(window, text = "Playlist's name you want to add/delete from")
        m1.grid(row = 0, column = 4)
        self.user_name = StringVar()
        self.e1 = Entry(window, textvariable = self.user_name)
        self.e1.grid(row = 0, column = 3)
        self.playlist_name = StringVar()
        self.e2 = Entry(window, textvariable = self.playlist_name)
        self.e2.grid(row = 0, column = 5)

        b1 = Button(window, text = "Add", command = self.add)
        b1.grid(row = 0, column = 6)

        b2 = Button(window, text = "Delete", command = self.delete)
        b2.grid(row = 0, column = 8)
        b3 = Button(window, text = "Close", command = close)
        b3.grid(row = 0, column = 9)
        b4 = Button(window, text = "Choose song to delete", command = self.view)
        b4.grid(row = 0, column = 7)

    def add(self):
        mpback.add_songs(self.user_name.get(), self.playlist_name.get())

    def view(self):
        
        self.songs = mpback.get_songs(self.user_name.get(), self.playlist_name.get())
        try:
            self.l1 = Listbox(self.window, height = 10, width = 80)
            self.l1.grid(row = 1, column = 1, rowspan = 6, columnspan = 6)
            self.l1.bind('<<ListboxSelect>>', self.get_selected_row)
            for song in self.songs:
                self.l1.insert(END, song)
        except:
            self.l1.destroy()
    
    def get_selected_row(self, event):
        if len(self.l1.curselection()) != 0:
            index = self.l1.curselection()[0]
            self.selected_song = self.l1.get(first = index)

    def delete(self):
        try:
            song_index = self.songs.index(self.selected_song)
            new_songs_list = self.songs[0:song_index] + self.songs[song_index+1:]

            mpback.update_songs(self.user_name.get(), self.playlist_name.get(), new_songs_list)
            self.l1.destroy()
        except:
            messagebox.showinfo(title = "Error", message = "Please choose a song first")
        
        
class view_playlists_window(object):
    def __init__(self, window):

        def view():
            try:
                content = mpback.view_playlists(self.user_name.get())
                l1.delete(0, END)
                if content == []:
                    messagebox.showinfo(title = "Infos", message = "You have no Playlists")
                else:
                    for items in content:
                        l1.insert(END, items)
            except:
                 messagebox.showinfo(title = "Error", message = "You have no User by this name")

        self.window = window

        def close():
            m1.destroy()
            self.e1.destroy()
            b1.destroy()
            l1.destroy()
            b2.destroy()

        m1 = Message(window, text = "User Name")
        m1.grid(row = 0, column = 2)

        self.user_name = StringVar()
        self.e1 = Entry(window, textvariable = self.user_name)
        self.e1.grid(row = 0, column = 3)

        b1 = Button(window, text = "View Playlists", command = view)
        b1.grid(row = 0, column = 4)
        b2 = Button(window, text = "Close", command = close)
        b2.grid(row = 0, column = 5)

        l1 = Listbox(window, height = 10, width = 80)
        l1.grid(row = 1, column = 1, rowspan = 6, columnspan = 6)


class open_from_playlist_window(object):
    def __init__(self, window):

        self.window = window

        def close():
            m0.destroy()
            m1.destroy()
            self.e1.destroy()
            self.e2.destroy()
            b1.destroy()
            b3.destroy()
            b4.destroy()
            self.l1.destroy()
            

        m0 = Message(window, text = "User Name")
        m0.grid(row = 0, column = 2)
        m1 = Message(window, text = "Playlist's name")
        m1.grid(row = 0, column = 4)

        self.user_name = StringVar()
        self.e1 = Entry(window, textvariable = self.user_name)
        self.e1.grid(row = 0, column = 3)
        self.playlist_name = StringVar()
        self.e2 = Entry(window, textvariable = self.playlist_name)
        self.e2.grid(row = 0, column = 5)
        
        b1 = Button(window, text = "Select Song", command = self.choose_song)
        b1.grid(row = 0, column = 6)
        b3 = Button(window, text = "Close", command = close)
        b3.grid(row = 0, column = 8)
        b4 = Button(window, text = "Open", command = self.open_chosen_song)
        b4.grid(row = 0, column = 7)
        
        self.l1 = Listbox(window, height = 10, width = 80)
        self.l1.grid(row = 1, column = 2, rowspan = 6, columnspan = 6)
        self.l1.bind('<<ListboxSelect>>', self.get_selected_row)

    def get_selected_row(self, event):
        if len(self.l1.curselection()) != 0:
            index = self.l1.curselection()[0]
            self.selected_song = self.l1.get(first = index)

    def open_chosen_song(self):
        try:
            for root, dirs, files in os.walk(r'C:\Users\Dell\Downloads\Music'):
                for name in files:
                    if name == self.selected_song:
                        song = os.path.abspath(os.path.join(root, name))
            mixer.init()
            mixer.music.load(song)
            mixer.music.set_volume(0.3)
            mixer.music.play()
        except:
            messagebox.showinfo(title = "Error", message = "Please choose a song")

    def choose_song(self):
        songs = mpback.open_from_playlist(self.user_name.get(), self.playlist_name.get())
        try:
            for name in songs:
                self.l1.insert(END, name)
        except:
            pass

class user_guide_window(object):
    def __init__(self, window):

        def close():
            self.l1.destroy()
            b1.destroy()

        self.window = window

        self.l1 = Listbox(window,height = 30, width = 120)
        self.l1.grid(row = 0, column = 1, rowspan = 6, columnspan = 6)

        b1 = Button(window, text = "Close", command = close)
        b1.grid(row = 3, column = 7)

        with open("user_guide.txt") as user_guide_file:
            user_guide = user_guide_file.readlines()
        
        for line in user_guide:
            self.l1.insert(END, line)


window = Tk()
window.geometry("1300x700")
window.title("Music Player")
frontend(window)       
window.mainloop()