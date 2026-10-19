# Proyecto de Pruebas Automatizadas con Playwright y Python

Trabajo práctico para la materia **Validación y Verificación de Programas** (Desarrollo de Software - 3er Año).

Este proyecto implementa pruebas automatizadas end-to-end (E2E) sobre un módulo de inicio de sesión web utilizando **Playwright para Python** y **pytest**, aplicando el patrón de diseño **Page Object Model (POM)**.

---

## 📋 Descripción del Proyecto

El objetivo es automatizar y validar el comportamiento de una interfaz web de login (`http://localhost:8080`), verificando:
- Navegación correcta y validación del título de la página.
- Flujo de login exitoso con credenciales válidas.
- Flujo de login fallido con validación de mensajes de error en pantalla.
- Captura de evidencias visuales (screenshots) antes y después de navegar.

### Estructura del Proyecto

```text
playwright-python-tp/
├── evidencias/          # Capturas de pantalla generadas por las pruebas
│   ├── captura_1.png
│   └── captura_2.png
├── pages/               # Page Object Model (POM)
│   └── login_page.py    # Localizadores y acciones de la página de login
├── tests/               # Casos de prueba con pytest
│   └── test_login.py    # Tests organizados por ejercicios (1 al 8)
├── pytest.ini           # Archivo de configuración de pytest
├── README.md            # Documentación del proyecto
└── requirements.txt     # Dependencias del proyecto (opcional)
```

---

## 🛠️ Requisitos Previos

1. **Python 3.8+** instalado en el sistema.
2. Servidor web local corriendo en `http://localhost:8080` que sirva la aplicación a testear (`login-desktop-claro.html`).

---

## 🚀 Instalación y Configuración

1. **Clonar o abrir el repositorio**:
   Asegúrate de estar ubicado en la raíz del proyecto:
   ```bash
   cd playwright-python-tp
   ```

2. **(Opcional pero recomendado) Crear y activar un entorno virtual**:
   - En Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - En Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   *(o alternativamente: `pip install pytest pytest-playwright`)*

4. **Instalar los navegadores de Playwright**:
   ```bash
   playwright install
   ```
   *(Si solo deseas instalar Chromium: `playwright install chromium`)*

---

## ▶️ Ejecución de las Pruebas

> [!NOTE]
> Recuerda tener levantado el servidor web en el puerto `8080` antes de ejecutar los tests.

### 1. Ejecutar todos los tests (modo headless / en segundo plano)
```bash
pytest
```

### 2. Ejecutar con navegador visible (modo headed)
Para observar la interacción en pantalla en tiempo real:
```bash
pytest --headed
```

### 3. Ejecutar de forma pausada (slow motion)
Útil para demostraciones y visualización paso a paso (ejemplo: 1000 ms entre acciones):
```bash
pytest --headed --slowmo 1000
```

### 4. Ejecutar con salida detallada (verbose)
```bash
pytest -v -s
```

### 5. Ejecutar un test o ejercicio específico
```bash
# Ejecutar un archivo específico
pytest tests/test_login.py -v

# Filtrar por nombre de prueba (por ejemplo, ejercicios 3 y 4)
pytest -k "test_ejercicios_3_4" --headed
```

---

## 📸 Evidencias de Prueba

Al ejecutar la prueba `test_ejercicios_7_8`, las capturas de pantalla se generarán automáticamente en el directorio:
```text
evidencias/
```
- `captura_1.png`: Pantalla tras iniciar sesión exitosamente.
- `captura_2.png`: Pantalla tras realizar `go_back()`.
