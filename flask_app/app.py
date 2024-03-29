from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Функция для соединения с базой данных
def connect_db():
    conn = psycopg2.connect(
        dbname="students",
        user="postgres",
        password="password",
        host="db"
    )
    return conn

# Главная страница - отображение HTML
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Получение фамилии студента из запроса
        last_name = request.form['lastname']

        # Подключение к базе данных
        conn = connect_db()
        cursor = conn.cursor()

        # Выполнение запроса к базе данных
        cursor.execute("SELECT lastname, student_id FROM students WHERE lastname = %s", (last_name,))
        student_info = cursor.fetchone()

        # Закрытие соединения с базой данных
        cursor.close()
        conn.close()

        # Если студент найден, возвращаем его информацию
        if student_info:
            return render_template('result.html', student_info=student_info)
        else:
            return render_template('index.html', student_info=None)
    return render_template('index.html', student_info=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
