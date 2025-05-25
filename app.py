{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "92e5c241",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== 映画一覧 =====\n",
      "1. グッド・ウィル・ハンティング（2025-05-25）★5 - 最高だった\n",
      "2. ダークナイト（2025-05-26）★5 - ジョーカーやばい\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "# DBファイル名\n",
    "DB_NAME = \"filmlog.db\"\n",
    "\n",
    "# 映画テーブル作成\n",
    "def init_db():\n",
    "    conn = sqlite3.connect(DB_NAME)\n",
    "    cur = conn.cursor()\n",
    "    cur.execute('''\n",
    "        CREATE TABLE IF NOT EXISTS movies (\n",
    "            id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
    "            title TEXT NOT NULL,\n",
    "            watched_date TEXT,\n",
    "            rating INTEGER,\n",
    "            comment TEXT\n",
    "        )\n",
    "    ''')\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "\n",
    "# 映画を追加する関数\n",
    "def add_movie(title, watched_date=None, rating=None, comment=None):\n",
    "    conn = sqlite3.connect(DB_NAME)\n",
    "    cur = conn.cursor()\n",
    "    cur.execute('''\n",
    "        INSERT INTO movies (title, watched_date, rating, comment)\n",
    "        VALUES (?, ?, ?, ?)\n",
    "    ''', (title, watched_date, rating, comment))\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "\n",
    "# 映画を一覧表示する関数\n",
    "def list_movies():\n",
    "    conn = sqlite3.connect(DB_NAME)\n",
    "    cur = conn.cursor()\n",
    "    cur.execute('SELECT id, title, watched_date, rating, comment FROM movies')\n",
    "    movies = cur.fetchall()\n",
    "    conn.close()\n",
    "    return movies\n",
    "\n",
    "# テスト実行\n",
    "if __name__ == \"__main__\":\n",
    "    init_db()\n",
    "    add_movie(\"グッド・ウィル・ハンティング\", \"2025-05-25\", 5, \"最高だった\")\n",
    "    add_movie(\"ダークナイト\", \"2025-05-26\", 5, \"ジョーカーやばい\")\n",
    "    \n",
    "    print(\"===== 映画一覧 =====\")\n",
    "    for m in list_movies():\n",
    "        print(f\"{m[0]}. {m[1]}（{m[2]}）★{m[3]} - {m[4]}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
