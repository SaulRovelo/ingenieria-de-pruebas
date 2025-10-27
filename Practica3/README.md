# 🧪 Pruebas Unitarias en Python — Practica 3

Esta practica contiene la implementación de una clase `Mascota` y su respectiva clase de pruebas automatizadas usando el módulo `unittest` de Python.

---

## 🎯 Objetivo

Practicar el uso de **unittest** para validar el comportamiento de clases en Python, aplicando:

- Decoradores (`@skipIf`, `@skipUnless`).
- Subpruebas con `subTest()`.
- Bloques `with self.assertRaises()` para verificar excepciones.

---

## 🐾 Archivos principales

| Archivo | Descripción |
|----------|-------------|
| `mascotas.py` | Define la clase `Mascota` con validaciones, métodos y excepciones. |
| `test_mascotas.py` | Contiene los casos de prueba unitarios implementados con `unittest`. |

Estructura del proyecto:

```
📦 Proyecto3
 ┣ 📜 mascotas.py
 ┣ 📜 test_mascotas.py
 ┗ 📄 README.md
```

---

## ⚙️ Ejecución de las pruebas

Desde la terminal:

```bash
python test_mascotas.py -v
```

El parámetro `-v` (verbose) muestra el nombre y resultado de cada prueba.

---

## 🧩 Lo que se probó

- **Creación de instancias válidas.**
- **Validaciones de errores:** nombres o edades incorrectas lanzan `TypeError` o `ValueError`.
- **Registro de microchip:** se asigna un código y no se permite duplicarlo.
- **Adopción:** cambia el estado interno y lanza error si se repite.
- **Decoradores:** controlan qué pruebas se ejecutan según el sistema operativo.
- **Subpruebas (`subTest`)**: agrupan casos similares sin interrumpir el resto.

---

## 📘 Conceptos clave

| Concepto | Descripción |
|-----------|--------------|
| **`subTest()`** | Ejecuta varios casos en un mismo test sin detenerse al primer fallo. |
| **`assertRaises()`** | Verifica que se lance una excepción esperada dentro de un bloque `with`. |
| **`@skipIf`** | Salta una prueba si se cumple una condición. |
| **`@skipUnless`** | Ejecuta una prueba solo si se cumple una condición. |
| **Excepción no lanzada** | Si la excepción esperada no ocurre dentro del `with`, la prueba **falla**. |

---

## ✅ Ejemplo de salida

```
test_instancias ... ok
test_tipo_invalido ... ok
test_edad_invalida ... ok
test_registro_chip ... ok
test_chip_duplicado ... ok
test_adoptar_y_repetir ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

---

## ✍️ Autor

**Saúl Rovelo López**   
🔗 [github.com/SaulRovelo](https://github.com/SaulRovelo)
