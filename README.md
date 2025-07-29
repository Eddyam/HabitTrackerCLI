# 🎯 Gestor de hábitos

HabitTracker CLI, es una aplicacion sencilla  de línea de comandos (CLI) que permita a un usuario registrar, consultar y gestionar sus hábitos diarios.

Tecnologias usadas: Python (con modulos estandar como json, datetime, pathlib), pytest para pruebas.

Almacenamiento: Archivo JSON.

---



## 🌟 Características Principales

* **Añadir Hábitos:** Crea y nombra hábitos con una descripción opcional.
* **Marcar completado:** Registra cada vez que completes un hábito, con marca de tiempo automática.
* **Listar Hábitos:** Obtén un listado claro de todos los hábitos y el número total de veces que se ha completado.
* **Ver detalle:** Consulta el historial de completitud de un hábito especifico.
* **Eliminar Hábitos:** Borra hábitos que ya no sigues.
* **Resumen General:** Obtén una vision rapida de progreso, incluyendo la ultima vez que completaste cada hábito.
* **Persistencia de datos:** Todos los datos y registros se guardan automáticamente en un archivo JSON local, asegurando que la información se mantenga entre sesiones.

---



## 🚀 Cómo Empezar

Sigue estos pasos para poner en marcha el HabitTracker CLI en tu máquina.

### Requisitos

* Python 3.8+

### Instalación 

1. **Clona el Repositorio (o descarga los archivos):**
   Si estás usando Git, clona el repositorio a tu máquina local:

   ```bash
   git clone [https://github.com/tu_usuario/gestor_de_habitos.git](https://github.com/tu_usuario/gestor_de_habitos.git)
   cd gestor_de_habitos
   ```

   (Reemplaza `https://github.com/tu_usuario/gestor_de_habitos.git` con la URL de tu propio repositorio.)
2. **Crea y Activa un Entorno Virtual:

   En Windows (PowerShell):**

   * ```bash
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * **En Windows (CMD):**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate.bat
     ```
   * **En Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Instala las Dependencias:**
   Con tu entorno virtual activado, instala las librerías necesarias:

   ```bash
   pip install colorama
   # Aunque PyInstaller se usa para compilar, no es una dependencia para ejecutar el código fuente
   # pip install pyinstaller # Puedes instalarlo si planeas compilar la app
   ```
4. **Crea el Archivo de Datos:**
   Crea un archivo llamado `habits.json` en la raíz del proyecto (junto a `main.py`). Debe contener un par de corchetes vacíos `[]` para inicializarlo:

   ```json
   []
   ```

---

## 🎮 Uso

Para iniciar la aplicación, asegurate de que tu entorno virtual este activado y ejecuta el script principal. 

```bash
python main.py
```

---



## ⚙️ Estructura del Proyecto

El proyecto está organizado en módulos para una clara separación de responsabilidades:

* `main.py`: El punto de entrada de la aplicación y la interfaz de usuario de la terminal.
* `habit.py`: Define la clase `Habit`, que representa la estructura y el comportamiento de un hábito individual.
* `data_handler.py`: Se encarga de la lectura y escritura de los datos de los hábitos desde/hacia el archivo `habits.json`.
* `habit_manager.py`: Contiene la lógica principal del negocio para gestionar la colección de hábitos (añadir, eliminar, completar, resumir, etc.).
* `habits.json`: El archivo donde se almacenan todos los datos de tus hábitos.
* `tests/`: Contiene las pruebas unitarias para asegurar la calidad y el correcto funcionamiento del código.

---



## 🧪 Pruebas

Para ejecutar las pruebas unitarias del proyecto, asegúrate de tener `pytest` instalado (`pip install pytest`) y ejecuta el siguiente comando en la raíz del proyecto (con el entorno virtual activado):

**Bash**

```
pytest
```

---

## 📦 Generar un Ejecutable (Opcional)

Puedes compilar la aplicación en un solo archivo ejecutable (`.exe` en Windows) usando `PyInstaller`. Esto te permite ejecutar la aplicación sin necesidad de Python instalado en el sistema destino.

1. **Instala PyInstaller:**
   **Bash**

   ```
   pip install pyinstaller
   ```
2. **Genera el Ejecutable:**
   **Bash**

   ```
   pyinstaller --onefile main.py
   ```

   El ejecutable se encontrará en la carpeta `dist/`. Recuerda **copiar el archivo `habits.json`** a la misma carpeta `dist/` para que la aplicación funcione correctamente.

---

## 🔮 Futuras Mejoras

* Implementación de la visualización de hábitos en un calendario.
* Capacidad para editar hábitos existentes.
* Funcionalidades para establecer metas o frecuencias (ej. hábito diario, semanal).
* Integración con una base de datos real (ej. SQLite) para una persistencia de datos más robusta.
* Posible escalado a una interfaz gráfica de usuario (GUI) o una aplicación web.

---



## ✍️ Autor

@Eddyam
