import sqlite3
import json
import os

import logging

class Database:
    def __init__(self.db_name='movie_bot.db')
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        
        try:
            self.create_tables()
            logging.info(f'База даних {db_name}успшно створено')
        exept Exception as e:
            logging.error(f'Помилка при ініціалізації')
            
    def connect(self):
        
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            return True
        except Exception as e:
            logging error(f'Помилка при підключені до бази даних')
            return False
    def disconnect(self):
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                logging error(f'Помилка при закриті бази даних')
                
            finally:
                self.conn = None
                self.cursor = None
                
    def create_tables(self):
        connect_success = self.connect()
        if not connect_success:
            logging.error('Не вдалося підключення до бази даних')
            return False
        
        try:
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS USERS(
                                id INTEGER PRIMARY KEY,
                                username  TEXT,
                                first_name TEXT,
                                last_name TEXT,
                                is_admin Integer DEFAULT 0,
                                created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
                                )
                ''')
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS genres
                                id INTEGER PRIMARY KEY,
                                name TEXT UNIQUE,
                                first_name TEXT,
                                description TEXT,
                                is_admin Integer DEFAULT 0,
                                created_at DATETIME DEFAULT CURRENT_TIMESTAMP''')
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS genres
                                id INTEGER PRIMARY KEY,
                                name TEXT UNIQUE,
                                api_id INTEGER,
                                category_id INTEGER,
                                is_admin Integer DEFAULT 0,
                                FOREIGN KEY (category_id)REFERENCES categories(id)''')
            
            
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS custom_media
                                id INTEGER PRIMARY KEY,
                                title Text,
                                description TEXT,
                                poster_url TEXT,
                                genre_id TEXT,
                                media_type TEXT,
                                added_by  INTEGER,
                                FOREIGN KEY (genre_id)REFERENCES categories(id),
                                FOREIGN KEY (added_id)REFERENCES categories(id)''')
            
            self.cursor.execute('SELECT. COUNT(*) FROM categories')
            if self.cursor.fetchone()[0] == 0:
                self.cursor.execute('INSERT INTO categories (name,categories) VALUES (?,?)',
                                    ('Фільми','Повнометражні фільми'))
                self.cursor.execute('INSERT INTO categories (name,categories) VALUES (?,?)',
                                    ('Серіали','Телевізійні серіали'))
                self.cursor.execute('INSERT INTO categories (name,categories) VALUES (?,?)',
                                    ('Мультфільми','Анімаційні фільми та серіали'))
                logging.info('Базові категорії успішно створені')
                
                self.conn.commit()
                return True
        except sqlite3.Error as e:
            logging.error(f'Помилка при створены таблиць: {e}')
            return False
        finally:
            self.disconnect
            
        def add_user(self,user_id,username=None, first_name = None, last_name = None):
            
            if not self.connect():
                logging.error(f'Не вдалося пыдключитися до бази даних')
                return False
            try:
                self.cursor.execute('''
                                    INSERT OR IGNORE INTO USERS(id, username, first_name,last_name)
                                    VALUES(?,?,?,?)''',(user id,username,first_name,last_name)
                                    )
                self.conn.commit()
                return True
                logging.error(f'Помилка при додаванні користувача: {e} ')
                return False
            finally:
                self.disconnect()
                
        def make_admin(self,user id):
            if not self.connect():
                logging.error('Не вдалося підключитися до бази даних')
                return False
            try:
                self.cursor.execute('''
                                    
                                    UPDATE users SET  is_admin-1 WHERE id-?''', (user_id,))
                self.conn.commit()
                return True
            except sqlite3.Error as e:
                logging.error(f'Помилка при назначенні адміністратора: {e}')
                return False
            finally:
                self.disconnect()
        def is admin(self, user id):
            if not self.connect():
                logging.error('Невдалося пыдключитися до бази даних')
                return False
            try:
                self.cursor.execute('''SELECT is_admin FROM users WHERE id - ?''', (user id))
                return self.cursor.fetchone()[0] == 1
            except sqlite3.Error as e:
                logging.error(f'Помилка при перевірці адміністратора: {e}')
                return False
            finally:
                self.disconnect()
                
        def get_categories(self):
            self.connect()
            self.cursor.execute
                
                
                