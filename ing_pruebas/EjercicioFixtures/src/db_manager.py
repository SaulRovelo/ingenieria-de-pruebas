
class DBManager:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    # Métodos para Alumnos
    def add_alumno(self, nombre, edad):
        """Recibe el nombre y la edad de un alumno y lo inserta en la tabla alumnos"""
        # Verifica que la edad sea un valor valido
        if not isinstance(edad, int) or edad < 0:
            # si no es un valor valido, lanza una excepcion y termina
            raise ValueError("Edad debe ser un entero positivo")
        # Si la edad es valida, inserta los datos del nuevo alumno en la tabla alumnos
        self.cursor.execute(
            'INSERT INTO alumnos (nombre, edad) VALUES (?, ?)',
            (nombre, edad)
        )
        self.conn.commit()
        # Devuelve el id del nuevo alumno
        return self.cursor.lastrowid

    def get_alumnos(self):
        """Obtiene todos los alumnos de la tabla alumnos"""
        self.cursor.execute('SELECT * FROM alumnos')
        return self.cursor.fetchall()
        # [(1,"daniela",40), (2,"Juan",30)]

    def delete_alumno(self, alumno_id):
        """Recibe el id de un alumno y lo borra de la tabla alumnos"""
        self.cursor.execute('DELETE FROM alumnos WHERE id=?', (alumno_id,))
        self.conn.commit()

    # Métodos para Cursos
    def add_curso(self, nombre, creditos):
        if not isinstance(creditos, int) or creditos <= 0:
            raise ValueError("Créditos debe ser un entero positivo")
        self.cursor.execute(
            'INSERT INTO cursos (nombre, creditos) VALUES (?, ?)',
            (nombre, creditos)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_cursos(self):
        self.cursor.execute('SELECT * FROM cursos')
        return self.cursor.fetchall()

    def delete_curso(self, curso_id):
        self.cursor.execute('DELETE FROM cursos WHERE id=?', (curso_id,))
        self.conn.commit()
