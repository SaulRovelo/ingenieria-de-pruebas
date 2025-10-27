# 🧪 Práctica 1 — Unit Testing en Python con `unittest`

Implementación y validación de una clase bancaria mediante pruebas unitarias automatizadas en Python.  
Este proyecto demuestra el uso de **`unittest`**, **subTest()** y asserts básicos para garantizar el correcto funcionamiento de los métodos de una clase.

---

## 🚀 Descripción general

Se desarrolla una clase `CuentaBancaria` que modela operaciones bancarias simples (depósito, retiro, transferencia y consulta de saldo).  
A partir de ella se construye una suite de pruebas automatizadas que valida múltiples escenarios y comportamientos esperados.

El enfoque se centra en:
- Aplicar **asserts de igualdad, booleanos e instancia**.
- Utilizar **`subTest()`** para ejecutar rangos de valores sin detener la ejecución.
- Verificar **transferencias válidas e inválidas** entre objetos.
- Garantizar que cada prueba sea **independiente, legible y reproducible**.

---

## 📂 Estructura del proyecto

```
📦 Practica1
 ┣ 📜 cuenta.py
 ┣ 📜 test_cuenta.py
 ┗ 📄 README.md
```

---

## 🧪 Suite de pruebas (`test_cuenta.py`)

La clase de pruebas automatizadas implementa cuatro métodos principales:

| Método | Propósito | Tipo de assert |
|--------|------------|----------------|
| `test_instancia` | Verifica que el objeto creado sea una instancia válida de `CuentaBancaria`. | `assertIsInstance`, `assertNotIsInstance` |
| `test_depositar_retirar` | Evalúa depósitos con varios montos y retiros válidos e inválidos. | `assertEqual` |
| `test_transferencias` | Comprueba transferencias exitosas y fallidas entre cuentas. | `assertTrue`, `assertFalse`, `assertEqual` |
| `test_saldo_final` | Valida el saldo final correcto e incorrecto. | `assertTrue`, `assertFalse` |

Cada prueba cuenta con un **docstring descriptivo** y el modo de ejecución **`verbosity=2`** para mostrar información detallada.

---

## ⚙️ Ejecución

Ejecuta las pruebas desde la terminal:

```bash
python test_cuenta.py -v
```

📄 Ejemplo de salida esperada:

```
test_depositar_retirar ... ok
test_instancia ... ok
test_saldo_final ... ok
test_transferencias ... ok
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
```

---

## 💡 Conceptos aplicados

- **Pruebas unitarias:** validan funciones o métodos individuales.  
- **Subtests (`subTest`):** permiten agrupar casos similares sin detener la ejecución.  
- **Asserts:** comparan resultados esperados con resultados reales.  
- **Automatización:** ejecución repetible sin intervención manual.  
- **Buenas prácticas:** independencia, claridad y modularidad del código probado.

---

## ✅ Conclusión

Este ejercicio demuestra un flujo de trabajo de testing simple pero completo, aplicando `unittest` para validar comportamientos esperados antes de etapas posteriores de integración o despliegue.  
Refuerza la importancia del testing como parte del ciclo de desarrollo y no como un paso posterior.

---

## 👤 Autor

**Saúl Rovelo López**  
🔗 [github.com/SaulRovelo](https://github.com/SaulRovelo)
