# 🧪 Ingeniería de Pruebas en Python

Este repositorio reúne una colección estructurada de prácticas y módulos orientados al desarrollo de **pruebas automatizadas en Python**, utilizando el framework estándar `unittest`. Su propósito es presentar una implementación sólida y modular de técnicas de testing aplicadas a distintos escenarios: funciones puras, lógica orientada a objetos, jerarquías de clases y componentes con dependencias externas.

El contenido está diseñado para demostrar buenas prácticas, claridad en la estructura del proyecto y un entendimiento de la mantenibilidad dentro del proceso de verificación y validación de software.

---

## 🎯 Enfoque del Repositorio

Este proyecto refleja competencias esenciales en ingeniería de pruebas:

- Diseño de pruebas unitarias con estructura profesional (`TestCase`, `TestSuite`, fixtures).  
- Cobertura de escenarios mediante casos positivos, negativos y de frontera.  
- Pruebas sobre clases y validación de comportamiento interno.  
- Aislamiento de dependencias mediante **mocks**.  
- Organización modular por prácticas completamente independientes.  
- Ejecución desacoplada y replicable en cada componente.

Cada práctica se presenta como una unidad aislada, enfocada en un aspecto específico del proceso de pruebas.

---

## 📂 Estructura del Repositorio

```
Practica1/      → Bases de unittest y asserts esenciales.
Practica2/      → Diseño de casos, múltiples escenarios y subTests.
Practica3/      → Pruebas sobre clases y validación de comportamiento.
Practica4/      → Módulo de biblioteca con excepciones y pruebas completas.
Practica5/      → Fixtures y pruebas sobre una jerarquía de clases.
Practica6/      → Caja blanca con mocks: simulación de BD y verificación interna.
ing_pruebas/    → Área de experimentación y ejercicios adicionales.
```

Cada directorio incluye:

- Código fuente correspondiente.  
- Conjunto de pruebas independiente.  
- Ejecución modular y desacoplada.  
- README propio.

---

## ⚙️ Tecnologías y Estándares

- **Python 3.12.0**  
- **unittest** (framework estándar)  
- **unittest.mock** para pruebas aisladas  
- Enfoque basado en buenas prácticas, diseño modular y organización clara de las pruebas.  

Se sigue una estructura similar a la usada en proyectos reales: separación entre lógica, pruebas y utilidades.

---

## 📦 Instalación

```bash
python3.12 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Ejecución de pruebas

### 1. Ejecutar todas las pruebas de una práctica

Este comando busca automáticamente todos los archivos que comiencen con
`test_` dentro del directorio.

``` bash
python -m unittest discover -v
```

### 2. Ejecutar un archivo de pruebas específico

Útil cuando solo deseas validar un módulo en particular.

``` bash
python -m unittest test_nombre.py -v
```

### 3. Ejecutar una TestSuite definida manualmente

Ideal para prácticas que agrupan varios casos de prueba en una sola
ejecución.

``` bash
python suite_pruebas.py
```


---

## 📈 Contribución del proyecto

Este repositorio reúne diferentes enfoques de pruebas automatizadas aplicados a módulos independientes. Su estructura permite revisar cómo evoluciona el diseño de pruebas desde casos básicos hasta escenarios con aislamiento mediante mocks y uso de suites. Cada práctica aporta una perspectiva distinta del proceso de validación en Python.

---

## 👤 Autor

Desarrollado por **Saul Rovelo** como parte de su formación profesional en desarrollo de software.

