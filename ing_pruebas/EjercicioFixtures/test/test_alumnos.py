import unittest
import sqlite3
import os

from src.db_manager import DBManager


class TestAlumnos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 1. Crea la conexión a la BD
        # Usamos la ruta relativa a la carpeta data para que funcione en tu estructura
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "data", "ejericicio_fixtures.db")
        cls.conexion = sqlite3.connect(db_path)

        # 2. Crea una instancia de la clase DBManager
        cls.dbm = DBManager(cls.conexion)

    @classmethod
    def tearDownClass(cls):
        # Cierra la conexión a la BD
        cls.conexion.close()

    def setUp(self):
        # Insertamos dos alumnos SIN usar métodos de DBManager
        alumnos = [("Laura", 25), ("Luis", 27)]
        self.alumnos_ids = []

        for nombre, edad in alumnos:
            self.dbm.cursor.execute(
                'INSERT INTO alumnos (nombre, edad) VALUES (?, ?)',
                (nombre, edad)
            )
            # Guardamos el id generado
            id_alumno = self.dbm.cursor.lastrowid
            self.alumnos_ids.append(id_alumno)

        # Confirmamos los INSERT
        self.conexion.commit()

    def tearDown(self):
        # Borramos los alumnos de prueba por nombre (como en el ejemplo de la maestra)
        for nombre in ["Laura", "Luis"]:
            self.dbm.cursor.execute(
                'DELETE FROM alumnos WHERE nombre = ?',
                (nombre,)
            )
        # Confirmamos los DELETE
        self.conexion.commit()

    def test_inserta_alumno_edad_invalida(self):
        # Debe lanzar ValueError con mensaje que empieza con "Edad debe ser un entero"
        with self.assertRaisesRegex(ValueError, r"^Edad debe ser un entero"):
            self.dbm.add_alumno("Juan", -15)

    def test_get_alumnos(self):
        # Construimos el resultado esperado con los IDs generados en setUp
        resultado_esperado = [
            (self.alumnos_ids[0], "Laura", 25),
            (self.alumnos_ids[1], "Luis", 27),
        ]

        resultado = self.dbm.get_alumnos()

        # Comparamos solo las primeras dos filas (las que acabamos de insertar)
        for i in range(2):
            al_id_esp, al_nombre_esp, al_edad_esp = resultado_esperado[i]

            with self.subTest(al_nombre=al_nombre_esp):
                # ID puede variar si ya hay datos previos; aquí validamos nombre y edad,
                # y mantenemos la estructura que usa tu maestra.
                self.assertEqual(al_nombre_esp, resultado[i][1])
                self.assertEqual(al_edad_esp, resultado[i][2])


if __name__ == "__main__":
    unittest.main()
