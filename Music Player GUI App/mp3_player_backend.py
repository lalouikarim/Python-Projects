from pygame import mixer
from tkinter import *
import sqlite3
from tkinter import messagebox
import os

    
class backend():

    def fileDialog(self):
        self.filename = filedialog.askopenfilenames(title = "Select A File", filetype =
        (("mp3 files","*.mp3"),("all files","*.*")))
    def open_file(self):
        self.fileDialog()
        try:
            mixer.init()
            mixer.music.load(self.filename[0])
            mixer.music.set_volume(0.3)
            mixer.music.play()
        except:
            pass

    def pause(self):
        try:
            mixer.music.pause()
        except:
            pass

    def resume(self):
        try:
            mixer.music.unpause()
        except:
            pass

    def stop(self):
        try:
            mixer.music.stop()
        except:
            pass
    def create_playlist(self, user_name, playlist_name):
        self.conn = sqlite3.connect("Playlists.db")
        self.curs = self.conn.cursor()
        self.curs.execute(f"CREATE TABLE IF NOT EXISTS {user_name} (Playlist_Name text, Songs_Names text)")
        self.conn.execute(f"INSERT INTO {user_name} VALUES (?, ?)", (playlist_name, None))
        self.conn.commit()
    def get_songs_names(self):
        self.fileDialog()
        songs_names = str(self.filename)
        self.songs_list = []
        try:
            for song in self.filename:
                slash_index = song.rindex("/")
                song = song[slash_index+1:]
                self.songs_list.append(song)
        except:
            pass
    def add_songs(self, user_name, playlist_name):
        self.conn = sqlite3.connect("Playlists.db")
        self.curs = self.conn.cursor()
        
        self.get_songs_names()
        
        try:
            if user_name == "" or playlist_name == "":
                messagebox.showinfo(title = "Error", message = "Please enter both the User Name and the Playlist Name")
            else:
                self.curs.execute(f"SELECT * FROM {user_name} WHERE Playlist_Name = ?", (playlist_name,))
                result = self.curs.fetchall()
                try:
                    if len(self.filename) == 0:
                        messagebox.showinfo(title = "Error", message = "Please choose songs to add")
                    elif len(result) == 0:
                        messagebox.showinfo(title = "Error", message = "There's no such user name or playlist")
                    else:
                        songs_list = self.songs_list
                        for song in songs_list:
                            self.curs.execute(f"SELECT * FROM {user_name} WHERE Playlist_Name = ?", (playlist_name,))
                            mylist = []
                            result = self.curs.fetchall()
                            #print(self.playlists)
                            if len(result) != 0:
                                try:
                                    for existant_song in result:
                                        mylist.append(existant_song[1])
                                        separator = ', '
                                    existant = separator.join(mylist)
                                    self.curs.execute(f"UPDATE {user_name} SET Songs_Names = ? WHERE Playlist_Name = ?", (song + ", " + existant, playlist_name))
                                    self.conn.commit()
                                except:
                                    self.curs.execute(f"UPDATE {user_name} SET Songs_Names = ? WHERE Playlist_Name = ?", (song, playlist_name))
                                    self.conn.commit()
                        messagebox.showinfo(title = "Succes", message = "The song(s) have been succefully added")
                        self.conn.close()
                except:
                    messagebox.showinfo(title = "Error", message = "There's no such user name or playlist")
        except:            
            messagebox.showinfo(title = "Error", message = "There's no such user name or playlist")            
    
    #delete songs
    def update_songs(self, user_name, playlist_name, x):
        self.conn = sqlite3.connect("Playlists.db")
        self.curs = self.conn.cursor()
        self.curs.execute(f"UPDATE {user_name} SET Songs_Names = ? WHERE Playlist_Name = ?", (None, playlist_name))
        self.conn.commit()
        try:
            for song in x:
                self.curs.execute(f"SELECT * FROM {user_name} WHERE Playlist_Name = ?", (playlist_name,))
                mylist = []
                result = self.curs.fetchall()
                try:
                    for existant_song in result:
                        mylist.append(existant_song[1])
                        separator = ', '
                    existant = separator.join(mylist)
                    self.curs.execute(f"UPDATE {user_name} SET Songs_Names = ? WHERE Playlist_Name = ?", (song + ", " + existant, playlist_name))
                    self.conn.commit()
                except:
                    self.curs.execute(f"UPDATE {user_name} SET Songs_Names = ? WHERE Playlist_Name = ?", (song, playlist_name))
                    self.conn.commit()
            self.conn.close()
            messagebox.showinfo(title = "Succes", message = "The song has been succefully deleted")
        except:
            messagebox.showinfo(title = "Error", message = "An error has occured. Please try again.")

    """
    to get songs names after the user hits the delete button, the difference between this function and get_song_names is 
    the argument in this one doesn't have the full path of the song, it only contains the name of the song(which was created by get_songs_names)
    """
    def get_songs_names_1(self, x):
        names_list = []
        h = 0
        x += ","
        for i in range(len(x)):
            if x[i] == ",":
                names_list.append(x[h:i])
                h = i+2
        return names_list

    def get_songs(self, user_name, playlist_name):
        if user_name == "" or playlist_name == "":
            messagebox.showinfo(title = "Error", message = "Please enter both the User Name and the Playlist Name")
        else:
            self.conn = sqlite3.connect("Playlists.db")
            self.curs = self.conn.cursor()
            try:
                self.curs.execute(f"SELECT Songs_Names FROM {user_name} WHERE Playlist_Name = ?", (playlist_name,))
                result = self.curs.fetchall()
                names_list = self.get_songs_names_1(result[0][0])
                self.conn.close()
                return names_list
            except:
                messagebox.showinfo(title = "Error", message = "There's no such user name or playlist")

    def view_playlists(self, user_name):
        try:
            self.conn = sqlite3.connect("Playlists.db")
            self.curs = self.conn.cursor()
            self.curs.execute(f"SELECT * FROM {user_name}")
            result =  self.curs.fetchall()
            self.conn.close()
            return result
        except:
            pass



    def delete_playlist(self, user_name, playlist_name):
        
        self.conn = sqlite3.connect("Playlists.db")
        self.curs = self.conn.cursor()
        try:
            self.curs.execute(f"SELECT * FROM {user_name} WHERE Playlist_Name = ?", (playlist_name,))
            result = self.curs.fetchall()
            if len(result) != 0:
                self.curs.execute(f"DELETE FROM {user_name} WHERE Playlist_Name = ?", (playlist_name,))
                self.conn.commit()
                self.conn.close()
                messagebox.showinfo(title = "Succes", message = "The Playlist has been deleted succefully")
            else:
                messagebox.showinfo(title = "Error", message = "There's no such user name or playlist")
        except:
            messagebox.showinfo(title = "Error", message = "There's no such user name or playlist")

    def open_from_playlist(self, user_name, playlist_name):
        self.conn = sqlite3.connect("Playlists.db")
        self.curs = self.conn.cursor()
        try:
            self.curs.execute(f"SELECT Songs_Names FROM {user_name} WHERE Playlist_Name = ?", (playlist_name,))
            result = self.curs.fetchall()
            self.conn.close()
            songs_list = self.get_songs_names_1(result[0][0])
            return songs_list
        except:
            messagebox.showinfo(title = "Error", message = "There's no such user or playlist")



