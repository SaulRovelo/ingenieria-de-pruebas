# 🧪 Manejo de Fixtures en Pruebas Unitarias — Práctica 5

Esta práctica implementa pruebas unitarias utilizando **fixtures** (`setUpClass`, `tearDownClass`, `setUp`, `tearDown`) para administrar un entorno controlado al interactuar con una base de datos SQLite.  
El objetivo es garantizar pruebas **reproducibles, aisladas y correctamente organizadas** para los métodos de acceso a datos definidos en la clase `DBManager`.

---

## 🎯 Objetivo

Aplicar técnicas de *Ingeniería de Pruebas* para:

- Utilizar fixtures de `unittest` para preparar y limpiar datos antes y después de cada prueba.
- Diseñar pruebas unitarias sobre operaciones **CRUD** para clientes, libros y compras.
- Validar manejo de errores mediante `assertRaises` y `assertRaisesRegex`.
- Ejecutar todos los tests en una batería de pruebas (`TestSuite`).
- Trabajar con bases de datos reales en un entorno totalmente controlado.

---

## 🧱 Clase bajo prueba

La clase `DBManager` administra tres entidades de la base de datos `tienda_libros.db`:

- **Clientes** → `add_cliente`, `get_clientes`, `delete_cliente`
- **Libros** → `add_libro`, `get_libros`, `delete_libro`
- **Compras** → `registrar_compra`, `get_compras`, `delete_compra`

Cada método realiza operaciones SQL reales mediante un cursor (`execute`, `fetchone`, `fetchall`, `commit`), por lo que la práctica requiere configurar correctamente el entorno con fixtures para evitar interferencias entre pruebas.

---

## 📚 Archivos principales

| Archivo                | Descripción                                                |
|------------------------|------------------------------------------------------------|
| `src/db_manager.py`    | Implementa la capa de acceso a datos y validaciones.      |
| `tests/test_clientes.py` | Pruebas unitarias para métodos de clientes.             |
| `tests/test_libros.py` | Pruebas unitarias para métodos de libros.                 |
| `tests/test_compras.py` | Pruebas unitarias para el registro y consulta de compras.|
| `suite_practica5.py`   | Contiene la batería de pruebas que ejecuta todas las clases.|

### Estructura sugerida del proyecto

```text
📦 Practica5
 ┣ 📂 src
 ┃ ┗ 📜 db_manager.py
 ┣ 📂 tests
 ┃ ┣ 📜 test_clientes.py
 ┃ ┣ 📜 test_libros.py
 ┃ ┗ 📜 test_compras.py
 ┣ 📂 data
 ┃ ┗ 📜 tienda_libros.db
 ┗ 📜 test_suite.py

```

---

## 🧩 Lo que se prueba

### 👤 Clientes (`tests/test_clientes.py`)

- **`test_get_clientes`**  
  Verifica que los clientes insertados en `setUp` aparezcan correctamente en la consulta.

- **`test_add_cliente_email_invalido`**  
  Confirma que agregar un cliente con correo no válido lance `ValueError`.

**Fixtures:**

- `setUp` inserta un cliente previo.  
- `tearDown` elimina el cliente creado.

---

### 📘 Libros (`tests/test_libros.py`)

- **`test_get_libros`**  
  Verifica que los libros creados en `setUp` se recuperen correctamente.

- **`test_add_libro_precio_invalido`**  
  Revisa que precios negativos, cero o tipos incorrectos produzcan `ValueError`.

**Fixtures:**

- `setUp` agrega un libro.  
- `tearDown` lo elimina.

---

### 🛒 Compras (`tests/test_compras.py`)

- **`test_registrar_compra_valida`**  
  Inserta un cliente y un libro en `setUp`, registra una compra y valida que:
  - se haya insertado solo **una compra**,
  - los campos (cliente, libro, fecha) coincidan.

- **`test_registrar_compra_cliente_inexistente`**  
  Prueba que registrar una compra con un cliente no existente lance `ValueError`.

- **`test_registrar_compra_libro_inexistente`**  
  Similar al anterior, pero para un libro inexistente.

**Fixtures:**

- `setUp` inserta cliente y libro.  
- `tearDown` limpia compras, clientes y libros.

---

## 🧰 Uso de fixtures

Cada clase de prueba implementa cuatro fixtures obligatorios:

- **`setUpClass`**
  - Abre una conexión a la base de datos.
  - Crea la instancia de `DBManager`.
  - Se ejecuta **una sola vez por clase**.

- **`setUp`**
  - Inserta datos iniciales necesarios para cada prueba.
  - Se ejecuta **antes de cada método de prueba**.

- **`tearDown`**
  - Elimina los datos creados en `setUp` para dejar la base limpia.
  - Se ejecuta **después de cada prueba**.

- **`tearDownClass`**
  - Cierra la conexión a la base de datos.
  - Se ejecuta **una sola vez al final de la clase**.

---

## ⚙️ Ejecución de las pruebas

🔹 **Ejecutar toda la suite**

```bash
python suite_practica5.py
```

🔹 **Ejecutar un archivo específico**

```bash
python -m unittest tests/test_clientes.py -v
```

🔹 **Descubrimiento automático**

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📘 Conceptos clave de la práctica

| Concepto             | Rol en esta práctica                                         |
|----------------------|--------------------------------------------------------------|
| **Fixtures**         | Preparan y limpian el entorno de pruebas (BD real).          |
| **Validación de datos** | Uso de excepciones (`ValueError`) en entradas inválidas. |
| **Aislamiento de pruebas** | Cada test debe ejecutarse sin depender del estado previo. |
| **CRUD sobre BD**    | Se prueban inserciones, eliminaciones y consultas reales.    |
| **TestSuite**        | Agrupa todas las clases de test en una sola ejecución.       |

---

## ✍️ Autor

**Saúl Rovelo López**  
🔗 <https://github.com/SaulRovelo>
