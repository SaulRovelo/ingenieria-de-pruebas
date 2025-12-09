# 🧪 Pruebas de Caja Blanca con Mocks — Práctica 6

Esta práctica implementa pruebas de **caja blanca** para la clase `DBManager`, utilizando objetos `Mock` para simular la conexión a base de datos y verificar el flujo interno de cada método sin depender de una BD real.

---

## 🎯 Objetivo

Aplicar técnicas de *Ingeniería de Pruebas* para:

- Diseñar **pruebas de caja blanca** sobre métodos que usan una base de datos.
- Usar **mocks** para simular la conexión y el cursor (`unittest.mock`).
- Verificar **llamadas internas** con `call_count`, `call` y `call_args_list`.
- Comprobar el **manejo de excepciones** en casos inválidos.
- Agrupar los casos en una **batería de pruebas** (`TestSuite`).

---

## 🧱 Clase bajo prueba

La clase `DBManager` (en `src/db_manager.py`) administra tres entidades:

- **Clientes** → `add_cliente`, `get_clientes`, `delete_cliente`
- **Libros** → `add_libro`, `get_libros`, `delete_libro`
- **Compras** → `registrar_compra`, `get_compras`, `delete_compra`

Cada método interactúa con un cursor de base de datos (métodos `execute`, `fetchone`, `fetchall`, `commit`), lo que la hace ideal para ser probada con mocks.

---

## 📚 Archivos principales

| Archivo | Descripción |
|--------|-------------|
| `src/db_manager.py` | Implementa la lógica de acceso a datos para clientes, libros y compras. |
| `tests/test_clientes.py` | Pruebas de caja blanca para los métodos relacionados con clientes. |
| `tests/test_libros.py` | Pruebas de caja blanca para los métodos relacionados con libros. |
| `tests/test_compras.py` | Pruebas de caja blanca para el registro y consulta de compras. |
| `suite_dbmanager.py` | Define la batería de pruebas que ejecuta todas las clases de test. |

Estructura sugerida del proyecto:

```bash
📦 Practica6
 ┣ 📂 src
 ┃ ┗ 📜 db_manager.py
 ┣ 📂 tests
 ┃ ┣ 📜 test_clientes.py
 ┃ ┣ 📜 test_libros.py
 ┃ ┗ 📜 test_compras.py
 ┗ 📜 suite_dbmanager.py
```

## 🧩 Lo que se prueba

### 👤 Clientes (`tests/test_clientes.py`)

- `test_get_clientes`  
  Verifica que se ejecute `SELECT * FROM clientes` y que se llame a `fetchall()`.

- `test_delete_cliente`  
  Comprueba que se arme correctamente el `DELETE` por id y que se haga `commit()`.

- `test_add_cliente_valido`  
  Revisa que se ejecute el `INSERT` con los parámetros correctos y se confirme la transacción.

- `test_add_cliente_invalido`  
  Valida que un correo inválido lance `ValueError` sin llamar a `execute()` ni `commit()`.

### 📘 Libros (`tests/test_libros.py`)

- `test_get_libros`  
  Verifica el `SELECT * FROM libros` y el uso de `fetchall()`.

- `test_delete_libro`  
  Comprueba el `DELETE` por id y la llamada a `commit()`.

- `test_add_libro_valido`  
  Revisa el `INSERT` de un libro con precio válido.

- `test_add_libro_invalido`  
  Valida que precios no válidos (negativos, cero, etc.) generen `ValueError` y no accedan a BD.

### 🛒 Compras (`tests/test_compras.py`)

- `test_get_comprass`  
  Verifica la consulta de compras y el uso de `fetchall()`.

- `test_delete_compras`  
  Comprueba el `DELETE` por id y la llamada a `commit()`.

- `test_registrar_compra_valida`  
  Simula que cliente y libro existen (`fetchone()` con *side effects*) y verifica que:
  - se hagan 3 `execute()` (cliente, libro, insert),
  - se llame a `commit()` una sola vez.

- `test_registrar_compra_cliente_no_existe`  
  Simula cliente inexistente y comprueba que:
  - se lance `ValueError`,
  - solo se haga un `SELECT`,
  - no haya `commit()`.

- `test_registrar_compra_libro_no_existe`  
  Simula cliente válido y libro inexistente; verifica 2 `SELECT` y ausencia de `commit()`.

---

## 🧰 Uso de mocks

En cada clase de prueba se define un único fixture `setUp`, donde:

- Se crea un mock de la conexión (`self.conn = Mock()`).
- Se crea un mock del cursor (`self.cursor = Mock()`).
- La conexión mockeada devuelve el cursor mockeado (`self.conn.cursor.return_value = self.cursor`).
- Se instancia `DBManager` con la conexión mockeada.

Esto permite:

- Contar cuántas veces se llama a `execute`, `fetchall`, `commit`, etc. (`call_count`).
- Verificar los parámetros de cada llamada usando `call` y `call_args_list`.
- Simular respuestas de la base de datos (`fetchone.side_effect`, `fetchone.return_value`).

---

## ⚙️ Ejecución de las pruebas

### 🔹 Ejecutar la batería completa

Desde la raíz del proyecto:

```bash
python suite_dbmanager.py
```

Esto ejecuta todas las pruebas definidas en `TestClientes`, `TestLibros` y `TestCompras`.

### 🔹 Ejecutar un archivo de pruebas específico

```bash
python -m unittest tests/test_clientes.py -v
```

### 🔹 Descubrimiento automático de tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📘 Conceptos clave de la práctica

| Concepto      | Rol en esta práctica |
|--------------|----------------------|
| **Caja blanca** | Las pruebas se diseñan conociendo el código interno de `DBManager` (validaciones, orden de consultas, etc.). |
| **Mock**         | Simula conexión y cursor de BD para aislar el código en pruebas. |
| **`call_count`** | Verifica cuántas veces se invoca un método mockeado. |
| **`call` / `call_args_list`** | Permiten comparar llamadas esperadas con las llamadas reales realizadas por el método. |
| **`assertRaises`** | Comprueba el lanzamiento de excepciones cuando la entrada o el estado no son válidos. |
| **`TestSuite`** | Centraliza la ejecución de todas las clases de prueba en un solo archivo. |

---

## ✍️ Autor

Saúl Rovelo López  
🔗 <https://github.com/SaulRovelo>
