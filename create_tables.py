import sqlite3

conn = sqlite3.connect('song_db.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE song_tbl
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           title TEXT NOT NULL,
           artist TEXT NOT NULL,
           runtime TEXT NOT NULL,
           path_name TEXT NOT NULL,
           file_path TEXT NULL,
           file_name TEXT NULL,
           date_added TEXT NULL,
           play_count TEXT NULL,
           last_played TEXT NULL,
           album TEXT NULL,
           genre TEXT NULL)
          ''')

conn.commit()
conn.close()
