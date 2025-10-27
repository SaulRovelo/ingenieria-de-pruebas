# 🧪 Práctica 2 — Pruebas de Excepciones y Saltos en `unittest`

Esta práctica extiende la practica 1 de pruebas unitarias, incorporando el manejo de **excepciones**, el uso de **decoradores de salto** y un control más robusto de los flujos de prueba mediante `unittest` en Python.

---

## 🚀 Descripción general

El proyecto valida la clase `CuentaBancaria`, que ahora incluye comprobaciones de tipo y valor en sus operaciones.  
Se aplican pruebas automatizadas para asegurar que el sistema reaccione correctamente ante **entradas inválidas** y condiciones específicas del entorno.

En esta práctica se refuerzan los siguientes temas:
- Lanzamiento de **excepciones (`TypeError`, `ValueError`)** ante montos no válidos.
- **Uso de decoradores** `@skip`, `@skipIf`, y `@skipUnless` para omitir pruebas según el contexto.
- Aplicación de **subTest()** para evaluar varios casos dentro de una misma función.
- Validación del comportamiento esperado y de errores controlados.

---

## 📂 Estructura del proyecto

```
📦 Practica2_Unittest
 ┣ 📜 cuenta.py
 ┣ 📜 test_cuenta.py
 ┗ 📄 README.md
```

---

## 🧩 Suite de pruebas (`test_cuenta.py`)

La clase `TestCuentaBancaria` contiene una serie de métodos que validan tanto los flujos normales como los casos de error.

| Método | Propósito | Tipo de assert / decorador |
|---------|------------|----------------------------|
| `test_instancia` | Comprueba que el objeto creado sea una instancia válida de `CuentaBancaria`. | `assertIsInstance`, `assertNotIsInstance` |
| `test_transferencias` | Verifica transferencias válidas e inválidas entre cuentas. | `assertTrue`, `assertFalse`, `assertEqual` |
| `test_saldo_final` | Comprueba el saldo final correcto e incorrecto. | `assertTrue`, `assertFalse` |
| `test_excepcion_tipo_invalido_en_todas` | Lanza `TypeError` si el monto no es numérico. | `assertRaises` + `subTest()` + `@skipUnless` |
| `test_excepcion_valor_invalido_en_todas` | Lanza `ValueError` si el monto es <= 0. | `assertRaises` + `subTest()` |
| `test_depositar_retirar_excepciones` | Evalúa depósitos y retiros válidos, así como errores por valor. | `assertEqual`, `assertRaises`, `subTest()` |
| `test_depositar_retirar` | Versión previa del test (omitida). | `@skip` |
| `test_transferencias` | Salta en Windows (ejemplo de `@skipIf`). | `@skipIf` |

---

## ⚙️ Ejecución

Ejecuta todas las pruebas con el comando:

```bash
python -m unittest test_cuenta.py -v
```

📄 Ejemplo de salida esperada:

```
test_excepcion_valor_invalido_en_todas ... ok
test_excepcion_tipo_invalido_en_todas ... ok
test_transferencias ... ok
test_saldo_final ... ok
test_instancia ... ok
test_depositar_retirar ... skipped 'Versión previa: esperaba Monto inválido'
---------------------------------------------------------------------
Ran 7 tests in 0.004s
OK (skipped=1)
```

---

## 💡 Conceptos reforzados

- **Manejo de excepciones:** validación de datos antes de ejecutar operaciones.  
- **Asserts avanzados:** `assertRaises`, `assertRaisesRegex`, `assertTrue`, `assertFalse`.  
- **Decoradores:** controlan qué pruebas se ejecutan según la plataforma o condición.  
- **Subtests:** agrupan múltiples valores de entrada dentro de un mismo método.  
- **Buenas prácticas:** independencia de pruebas, legibilidad y mantenimiento del código.

---

## ✅ Conclusión

Esta práctica consolida el conocimiento de **testing avanzado con `unittest`**, abordando la detección y control de errores en código productivo.  
Se demuestra cómo una buena estrategia de pruebas puede asegurar la **confiabilidad y estabilidad** del sistema incluso ante entradas inválidas o entornos variables.

---

## 👤 Autor

**Saúl Rovelo López**  
🔗 [github.com/SaulRovelo](https://github.com/SaulRovelo)
