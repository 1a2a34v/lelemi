import sqlite3

conn = sqlite3.connect('kanji/collection.anki2')
cur = conn.cursor()
cur.execute("SELECT * FROM notes")

rows = cur.fetchall()
i=0
for row in rows:
    back = row[6].split("\x1f")
    print(back[0])
    print(back[4])
    break
    #print(row[7])
