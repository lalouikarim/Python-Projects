import sqlite3

def create_table():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, Title text, Author text, Year integer, ISBN integer)")
    conn.commit()
    conn.close()

create_table()    

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE bookstore SET Title = ?, Author = ?, Year = ?, ISBN = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    content = cur.fetchall()
    conn.close()
    return content

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id = ?", (id,))    
    conn.commit()
    conn.close()

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE Title = ? OR Author = ? OR Year = ? OR ISBN = ?", (title, author, year, isbn))
    result = cur.fetchall()
    conn.close()
    return result

#insert("The Sun", "John Smith", 1918, 913123134)
#delete(2)
#update(1, "The Moon", "John Smooth", 1917, 999999)
#print(view())