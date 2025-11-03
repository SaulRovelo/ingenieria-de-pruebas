# 🧪 Pruebas Unitarias en Python — Práctica 4

Esta práctica contiene la implementación de las clases `Libro` y `Usuario`, junto con sus respectivas **pruebas unitarias automatizadas** utilizando el módulo `unittest` de Python.  

---

## 🎯 Objetivo

Aplicar pruebas unitarias en Python para validar el comportamiento de clases orientadas a objetos, utilizando:

- **Subpruebas** con `subTest()`.  
- **Baterías de pruebas** con `TestSuite`.  
- **Excepciones controladas** con `assertRaises()` y `assertRaisesRegex()`.  

---

## 📚 Archivos principales

| Archivo | Descripción |
|----------|-------------|
| `biblioteca.py` | Define las clases `Libro` y `Usuario` con sus métodos y validaciones. |
| `test_libros.py` | Contiene las pruebas unitarias para la clase `Libro`. |
| `test_usuarios.py` | Contiene las pruebas unitarias para la clase `Usuario`. |
| `suite_biblioteca.py` | Implementa la batería de pruebas (`TestSuite`) para ejecutar todos los casos. |

Estructura del proyecto:

```
📦 Practica4
 ┣ 📂 src
 ┃ ┗ 📜 biblioteca.py
 ┣ 📂 test
 ┃ ┣ 📜 test_libros.py
 ┃ ┗ 📜 test_usuarios.py
 ┗ 📜 suite_biblioteca.py
```

---

## ⚙️ Ejecución de las pruebas

### 🔹 Opción 1: Ejecutar la batería completa
Desde la raíz del proyecto:

```bash
python -m Practica4.suite_biblioteca
```

### 🔹 Opción 2: Descubrimiento automático
Ejecutar todas las pruebas encontradas dentro de la carpeta `test`:

```bash
python -m unittest discover -s test -p "test_*.py" -v
```

El parámetro `-v` (verbose) muestra los nombres y resultados detallados de cada prueba.

---

## 🧩 Lo que se probó

- **Creación de libros válidos e inválidos.**  
- **Validación de tipos:** se lanzan `TypeError` y `ValueError` cuando los datos son incorrectos.  
- **Préstamo y devolución de libros:** se usa `subTest()` para probar múltiples casos sin interrumpir el flujo.  
- **Control de errores:** el usuario no puede devolver libros no prestados ni prestar objetos que no sean `Libro`.  
- **Uso de `TestSuite`:** permite ejecutar todas las pruebas desde un único punto.  

---

## 📘 Conceptos clave

| Concepto | Descripción |
|-----------|-------------|
| **`setUp()`** | Prepara objetos o datos antes de cada prueba (por ejemplo, crear libros y un usuario). |
| **`subTest()`** | Permite agrupar casos similares dentro del mismo test sin detener la ejecución al fallar uno. |
| **`assertIn()` / `assertNotIn()`** | Comprueban si un elemento está o no dentro de una colección. |
| **`assertRaisesRegex()`** | Verifica que se lance una excepción y que el mensaje coincida con una expresión regular. |
| **`TestSuite`** | Agrupa múltiples clases de prueba para ejecutarlas juntas en una batería de pruebas. |

---

## ✅ Ejemplo de salida

```
test_creacion_libro_autor_titulo_invalido ... ok
test_creacion_libro_paginas_invalidas ... ok
test_creacion_libro_valido ... ok
test_devolver_sin_prestar ... ok
test_prestar_objeto_incorrecto ... ok
test_prestar_y_devolver_libro ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

---

## 💬 Diferencias entre modos de ejecución

- **Con TestSuite (`suite_biblioteca.py`):**  
  Se ejecutan solo las clases de prueba que yo decido incluir manualmente.  
  Ideal para controlar qué módulos se prueban o el orden de ejecución.

- **Con `unittest discover`:**  
  Python busca y ejecuta automáticamente todos los archivos `test_*.py` sin necesidad de definir una suite.  
  Ideal para ejecuciones rápidas o automatizadas.

---

## ✍️ Autor

**Saúl Rovelo López**  
🔗 [github.com/SaulRovelo](https://github.com/SaulRovelo)