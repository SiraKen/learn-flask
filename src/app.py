from flask import Flask, escape, request, jsonify, render_template
from mysql.connector import connect
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

try:
  db = connect(
    host = 'localhost',
    user = 'flask',
    passwd = 'flask',
    database = 'flask'
  )
except Exception as e:
  print(e)
  # exit()

@app.route('/')
def hello_world():
  values = {'text': 'Hello, World!'}
  return render_template('pages/index.html', values=values)

@app.route('/db')
def db_test():
  db = connect(
    host = 'mysql',
    user = 'flask',
    passwd = 'flask',
    database = 'flask'
  )
  cursor = db.cursor(dictionary=True)

  # cursor.execute('DROP TABLE IF EXISTS users')

  # create table
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS `users` (
      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
      `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
      `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
      `email_verified_at` timestamp NULL DEFAULT NULL,
      `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
      `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `created_at` timestamp NULL DEFAULT NULL,
      `updated_at` timestamp NULL DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `users_email_unique` (`email`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
  """)

  # fetch data
  cursor.execute('SELECT * FROM users')
  users = cursor.fetchall()
  
  return jsonify(users)

@app.route('/users/<username>', methods=['GET'])
def return_user(username) -> str:
  return username

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
