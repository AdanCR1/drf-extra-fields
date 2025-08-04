# Guía Técnica para Contribuir en drf-extra-fields

Este documento explica como clonar el repositorio, configurar el entorno de desarrollo, ejecutar pruebas y realizar Pull Requests.
Sigue estos pasos para que tu contribución sea sencilla, efectiva y alineada con las buenas prácticas del proyecto.
---
## 1. Crear y clonar el Fork 

*Este paso es muy importante para la contribucion.*

Ingresa a la pagina de git de AdanCR1, dirijete al proyecto drf-extra-fields (link de referencia https://github.com/AdanCR1/drf-extra-fields) y dale clic en Fork para que se cree el nuevo enlace para tu repositorio.

![imagendeFork](IMAGES/CapturaFork.png)

Una vez creado, crea una carpeta y dentro clona el Fork con el siguiente comando:

```bash
git clone https://github.com/<tu-usuario>/drf-extra-fields.git
```

## 2 Cambiar de directorio en la terminal

```bash
cd drf-extra-fields
```

## 3 Crea una rama de trabajo de acuerdo a tu FUNCIONALIDAD PRINCIPAL 

Para crear y mover una rama ejecuta el siguiente comando:

```bash
git checkout -b docs/guia-tecnica
```

## 4 Pull Request

Desde GitHub de AdanCR1, abre Pull Request (Enlace https://github.com/AdanCR1/drf-extra-fields/pulls), luego dale clic en 'New Pull Requests', en la opcion 'compare:Master' debes seleccionar el nombre de tu Rama.

En la opcion de base Master ahi esta en lo que vamos a trabajar

En base repositorio hipo debes seleccionar el repositorio de Adan 

Create Pull Request es para solicitar a Adan para que nos de un checkout




## 5 Consejos y buenas practicas

* **Nombres de archivos:** Utiliza los siguientes nombres de Rama para mantener el orden:

- Grupo B - CAMPOS ESPECIALIZADOS

Rama para Mary Villca: feature/urlqr/implement

Rama para Jorge Choque Ferrufino: feature/wifiqr/implement

Rama para Celso Velasco: feature/vcardqr/implement

- Grupo C - TESTING AUTOMATIZADO

Rama para Gerardo Burgos:test/baseqr/unit.

Nombre de archivo: test_base_qr_code_field.py.

Rama para Rommel Valda: test/urlqr/unit

Rama para Carlos Marcelo: test/wifiqr/unit

Rama para Jhony Quispe: test/vcardqr/unit

- Grupo D - DOCUMENTACIÓN Y REVISIÓN

Rama para Jhon Escobar, Clemente Isla y Kevin Navia

docs/integration-drf/examples
docs/pull-request/write

* **Mensajes de commit:** Los mensajes de `commit` deben ser cortos donde expliquen el propósito de tus cambios.
* **Capturas de pantalla imagen:** Deben ir en la carpeta `IMAGES`
* **PRs:** Proporciona una descripción detallada en tu `Pull Request` para que los revisores entiendan qué has hecho.






