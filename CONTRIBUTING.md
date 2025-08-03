# Guía Técnica para Contribuir en drf-extra-fields

Este documento explica como clonar el repositorio, configurar el entorno de desarrollo, ejecutar pruebas y realizar Pull Requests.
Sigue estos pasos para que tu contribución sea sencilla, efectiva y alineada con las buenas prácticas del proyecto.
---

## 1. Clonar el repositorio

Clona el repositorio en una carpeta personalizada:

```bash
git clone https://github.com/<tu-usuario>/drf-extra-fields.git
```
## 2. Crear y activar un entorno virtual

Crea un entorno virtual:

```bash
python -m venv venv
```

Actívalo según tu sitema operativo:

- **En Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **En macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```
  
## 3. Instalar las dependencias

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```
## 4. Ejecuta las pruebas automatizadas

Antes de hacer cambios, asegúrate de que las pruebas existentes pasan correctamente:

Primero instala tox y luego ejecuta:

```bash
pip install tox
tox
```

O directamente con pytest:

```bash
pytest
```

## 5. Crea una rama de trabajo

Crear una rama para cada funcionalidad o tarea:

```bash
git checkout -b mi-nueva-funcionalidad
```
## 6. Guardar y subir los cambios

Cuando termines, guarda y sube tus cambios a tu fork:

```bash
git add .
git commit -m "Explica brevemente qué hiciste"
git push origin mi-nueva-funcionalidad
```
## 7. Abre un Pull Request

Desde GitHub, abre un Pull Request desde tu rama hacia la rama principal del repositorio original.  
Incluye una descripción clara de los cambios, mejoras o correcciones que realizaste.

---
### Consejos útiles

- Sigue el estilo de código del proyecto.
- Escribe mensajes de commit claros y concisos.
- Asegúrate de que las pruebas pasen antes de enviar tu Pull Request.
- Si tienes dudas, ¡pregunta! Estamos para ayudarte.