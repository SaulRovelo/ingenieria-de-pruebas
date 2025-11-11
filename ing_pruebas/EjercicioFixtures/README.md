# Ejercicio Fixtures

## Contexto

Este ejercicio implementa pruebas unitarias para la clase `DBManager`,
que administra una base de datos SQLite (`ejericicio_fixtures.db`) con
tablas `alumnos` y `cursos`.

El propósito principal no es solo validar la funcionalidad del código,
sino **comprender el uso de los *fixtures* de unittest** (los métodos
especiales que preparan y limpian el entorno de prueba).

------------------------------------------------------------------------

## Conceptos clave: Fixtures en `unittest`

Un *fixture* es el **conjunto de pasos necesarios para preparar y
restaurar el estado del entorno antes y después de una prueba**.\
Python `unittest` ofrece cuatro niveles de fixtures, y en este ejercicio
los usamos todos:

------------------------------------------------------------------------

### 1. `setUpClass(cls)`

🔹 **Se ejecuta una sola vez al inicio de la clase de pruebas.**

Sirve para inicializar recursos **compartidos por todos los tests**,
evitando repetir tareas costosas.

En este caso:

``` python
@classmethod
def setUpClass(cls):
    cls.conexion = sqlite3.connect("data/ejericicio_fixtures.db")
    cls.dbm = DBManager(cls.conexion)
```

**Qué hace:** - Abre la conexión a la base de datos. - Crea una
instancia de `DBManager` que usarán todos los tests.

**Por qué:**\
Así evitamos crear y cerrar conexiones múltiples. Cada test usará la
misma instancia ya configurada.

------------------------------------------------------------------------

### 2. `tearDownClass(cls)`

🔹 **Se ejecuta una sola vez al final de la clase de pruebas.**

Se usa para **liberar recursos globales** inicializados en `setUpClass`.

``` python
@classmethod
def tearDownClass(cls):
    cls.conexion.close()
```

**Qué hace:**\
Cierra la conexión a la base de datos una vez que todas las pruebas
terminaron.

**Por qué:**\
Dejar conexiones abiertas puede provocar bloqueos o corrupción de la
BD.\
Esto asegura limpieza y buen manejo de recursos.

------------------------------------------------------------------------

### 3. `setUp(self)`

🔹 **Se ejecuta antes de cada prueba individual.**

Sirve para dejar la base de datos en un estado conocido y predecible.

``` python
def setUp(self):
    alumnos = [("Laura", 25), ("Luis", 27)]
    self.alumnos_ids = []
    for nombre, edad in alumnos:
        self.dbm.cursor.execute('INSERT INTO alumnos (nombre, edad) VALUES (?, ?)', (nombre, edad))
        self.alumnos_ids.append(self.dbm.cursor.lastrowid)
    self.conexion.commit()
```

**Qué hace:** - Inserta alumnos de prueba **sin usar los métodos del
`DBManager`**. - Guarda sus `id`s para poder referenciarlos luego.

**Por qué:**\
Esto aísla cada test, garantizando que todos empiecen con los mismos
datos.

------------------------------------------------------------------------

### 4. `tearDown(self)`

🔹 **Se ejecuta después de cada prueba individual.**

Sirve para **devolver la base de datos a su estado original**.

``` python
def tearDown(self):
    for nombre in ["Laura", "Luis"]:
        self.dbm.cursor.execute('DELETE FROM alumnos WHERE nombre = ?', (nombre,))
    self.conexion.commit()
```

**Qué hace:** - Elimina los registros de prueba creados en `setUp`.

**Por qué:**\
Evita que los datos de un test afecten el resultado del siguiente.

------------------------------------------------------------------------

## Pruebas implementadas

### `test_get_alumnos()`

Verifica que el método `get_alumnos()` devuelva los registros que
insertamos en `setUp`.

-   Usa `subTest()` para comparar nombre y edad de cada alumno.
-   Si un campo difiere, se reporta el error sin detener las demás
    verificaciones.

------------------------------------------------------------------------

### `test_inserta_alumno_edad_invalida()`

Comprueba que `add_alumno()` lance una excepción `ValueError` con un
mensaje específico si se intenta insertar una edad inválida:

``` python
with self.assertRaisesRegex(ValueError, r"^Edad debe ser un entero"):
    self.dbm.add_alumno("Juan", -15)
```

Esto asegura que las validaciones de entrada estén correctamente
implementadas.

------------------------------------------------------------------------

## Suite de pruebas

Además de los tests individuales, se definió una **suite personalizada
(`test_suite.py`)**:

``` python
import unittest
from test.test_alumnos import TestAlumnos

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAlumnos))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
```

**Ventajas de usar una suite:** - Permite agrupar clases de prueba
(`TestAlumnos`, `TestCursos`, etc.). - Ejecutar solo un subconjunto de
pruebas. - Integrar fácilmente en pipelines o entregas controladas.

------------------------------------------------------------------------

## Flujo completo de ejecución

1.  `setUpClass()` --- se ejecuta una vez → abre conexión y crea
    `DBManager`.
2.  `setUp()` --- antes de cada test → inserta alumnos de prueba.
3.  **Prueba individual (test\_...)**
4.  `tearDown()` --- después de cada test → borra los datos de prueba.
5.  `tearDownClass()` --- al final → cierra conexión.

Este flujo garantiza **independencia, limpieza y repetibilidad** de
todas las pruebas.

------------------------------------------------------------------------

## Ejecución

-   Descubrimiento automático:

``` bash
python -m unittest discover -s test -v
```

-   Ejecución de suite personalizada:

``` bash
python test_suite.py
```

------------------------------------------------------------------------

## Conclusión

El uso de *fixtures* (`setUpClass`, `tearDownClass`, `setUp`,
`tearDown`) permite que las pruebas sean **modulares, reproducibles y
aisladas**.\
Gracias a ellos, el entorno de prueba se prepara y limpia
automáticamente, asegurando resultados consistentes y confiables.

La **suite** centraliza y organiza la ejecución, representando el último
paso para un flujo de pruebas profesional.
