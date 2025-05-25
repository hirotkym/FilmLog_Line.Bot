#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3

# DBファイル名
DB_NAME = "filmlog.db"

# 映画テーブル作成
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            watched_date TEXT,
            rating INTEGER,
            comment TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 映画を追加する関数
def add_movie(title, watched_date=None, rating=None, comment=None):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO movies (title, watched_date, rating, comment)
        VALUES (?, ?, ?, ?)
    ''', (title, watched_date, rating, comment))
    conn.commit()
    conn.close()

# 映画を一覧表示する関数
def list_movies():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT id, title, watched_date, rating, comment FROM movies')
    movies = cur.fetchall()
    conn.close()
    return movies

# テスト実行
if __name__ == "__main__":
    init_db()
    add_movie("グッド・ウィル・ハンティング", "2025-05-25", 5, "最高だった")
    add_movie("ダークナイト", "2025-05-26", 5, "ジョーカーやばい")
    
    print("===== 映画一覧 =====")
    for m in list_movies():
        print(f"{m[0]}. {m[1]}（{m[2]}）★{m[3]} - {m[4]}")

