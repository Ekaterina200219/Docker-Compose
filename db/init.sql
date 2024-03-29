CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    lastname VARCHAR(100),
    student_id VARCHAR(10)
);


INSERT INTO students (lastname, student_id) VALUES
('Митрюхина', '20Б1512'),
('Нигьматуллина', '20Б1807'),
('Петров', '20Б4536'),
('Ромашкина', '20Б2020'),
('Попов', '20Б3189'),
('Румянцева', '20Б7018');

