# Proyecto MVC con Flask

Este es un pequeño proyecto en Flask que implementa el patrón Modelo-Vista-Controlador (MVC) correctamente en una primera vista y de manera incorrecta en una segunda vista para demostrar malas prácticas.

## 🚀 Instalación

### 1️⃣ Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto-mvc-arquitectura
```

### 2️⃣Activar un entorno virtual
- En Windows:
  ```bash
  env-proyecto\Scripts\activate
  ```
- En Linux/Mac:
  ```bash
  source env-proyecto/bin/activate
  ```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🏗️ Estructura del proyecto
```
proyecto-mvc-arquitectura/
│── app.py                  # Archivo principal
│── requirements.txt        # Dependencias del proyecto
│── templates/              # Carpeta con las vistas
│   ├── form.html           # Formulario bien estructurado
│   ├── bad_form.html       # Formulario con mala implementación
│── static/
│   ├── styles.css          # Estilos CSS
│── models/
│   ├── user.py             # Modelo de usuario
│── controllers/
│   ├── user_controller.py  # Controlador
│── views/
│   ├── good_views.py       # Vista correcta
│   ├── bad_views.py        # Vista incorrecta
```

## ▶️ Ejecución del proyecto
```bash
python app.py
```
Luego, abre en tu navegador:
```
http://127.0.0.1:5000/
```

## 📌 Notas
- La vista incorrecta redirige a una ruta inexistente para simular una mala práctica en MVC.
- Si hay problemas con la base de datos, asegúrate de eliminar el archivo `database.db` y volver a ejecutar.

🚀 ¡Listo para probar el proyecto! 🎯

