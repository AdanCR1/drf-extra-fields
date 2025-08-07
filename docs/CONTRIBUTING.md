# Guía Técnica para Contribuir en al proyecto drf-extra-fields

Este documento explica desde cómo clonar el repositorio, crear ramas, configurar el entorno de desarrollo, ejecutar pruebas y realizar Pull Requests.
Sigue estos pasos para que tu contribución sea sencilla, efectiva y alineada con las buenas prácticas del proyecto.
---
## 1. Clonar el repositorio

**Este paso es muy importante para la contribución.**

Ingresa a la pagina de git de AdanCR1, dirijete a la carpeta del proyecto drf-extra-fields (link de referencia https://github.com/AdanCR1/drf-extra-fields) y dale clic en 'Code' para copiar el enlace del repositorio.

![imagendeFork](IMAGES/Captura1enlace.png)

Una vez copiado, crea una carpeta y dentro clona el Fork de Adan con el siguiente comando:

```bash
git clone https://github.com/AdanCR1/drf-extra-fields.git
```
## 2 Ingresa al directorio del proyecto

Ingresa a la carpeta del proyecto para comenzar a trabajar dentro de ella con el siguiente comando.

```bash
cd drf-extra-fields
```

## 3 Crear y activar el entorno virtual para que aisle las dependencias del proyecto

Para crear:

```bash
python -m venv venv
```

Para activar:

- **En Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **En macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```
## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 5. Crea una rama de trabajo de acuerdo a tu FUNCIONALIDAD PRINCIPAL 

Cada integrante del equipo debe crear una rama de trabajo basada en la funcionalidad que le corresponde, por lo que se les asignará un nombre de rama específico que refleje su tarea.
Busquen sus nombres y ejecuten el comando designado para crear su rama de trabajo en el que realizarán sus contribuciones:

- Grupo B - CAMPOS ESPECIALIZADOS

Rama para Mary Villca:
```bash
git checkout -b feature/urlqr/implement
```

Rama para Jorge Choque:
```bash
git checkout -b feature/wifiqr/implement
```

Rama para Celso Velasco:
```bash
git checkout -b feature/vcardqr/implement
```

- Grupo C - TESTING AUTOMATIZADO

Rama para Gerardo Burgos:
```bash
git checkout -b test/baseqr/unit
```

Rama para Rommel Valda:
```bash
git checkout -b test/urlqr/unit
```

Rama para Carlos Marcelo:
```bash
git checkout -b test/wifiqr/unit
```

Rama para Jhony Quispe: 'test/vcardqr/unit'
```bash
git checkout -b test/vcardqr/unit
```

- Grupo D - DOCUMENTACIÓN Y REVISIÓN

Rama para Jhon Escobar:
```bash
git checkout -b docs/redaction/review
```

Rama para Clemente Isla:
```bash
git checkout -b docs/integration-drf/examples
```

Rama para Kevin Navia:
```bash
git checkout -b docs/pull-request/write
```

----

Haz los cambios que te correspondan en tu rama de trabajo. Luego, ejecuta 'git add .' para agregar los cambios y 'git commit -m "mensaje descriptivo"' para confirmar los cambios y git push origin nombre de tu rama, para posteriormente solicitar el Pull Request.

![imagendeFork](IMAGES/CapturaGadd.png)

## 4. Ejecutar y probar tu código localmente

**Ejecutar pruebas con tox**
Para automatizar las pruebas y asegurar la calidad del código, debes usar los siguientes comandos:

```bash
pip install tox
```

```bash
tox
```
**Probar tu código de forma manual**
Puedes crear una archivo temporal para probar tu código, sin tener la necesidad de instalar librerías.

**Ejemplo de uso**
a).- Asegúrate de estar en el entorno virtual y activalo.
b).- Desde la raíz del proyecto (drf-extra-fields), crea un archivo nuevo llamado probar_urlqr.py.

```bash
probar_urlqr.py
```
c).- Abre el archivo 'probar_urlqr.py' y dentro agrega el siguiente código:

```bash
from drf_extra_fields.fields.url_qr_field import URLQRField
```
```bash
campo = URLQRField()
```
```bash
valor = campo.to_representation("https://github.com/AdanCR1")
```
```bash
print("Resultado del campo URLQRField:")
print(valor)
```
d).- Desde la terminal, asegurate de estar en la carpet raíz del proyecto donde esta 'probar_urlqr.py' y ejecuta:

```bash
python probar_urlqr.py
```

Si las pruebas fallan, arréglalas y vuelve a ejecutar el comanado hasta que pasen todas correctamente.

## 5. Pull Request(PR)

Si estás seguro de que tu rama de trabajo está lista para ser revisada, sigue estos pasos:

- Crea el Pull Request

Desde GitHub de AdanCR1, abre Pull Request (Enlace https://github.com/AdanCR1/drf-extra-fields/pulls), luego dale clic en 'New Pull Requests'.

![imagendeFork](IMAGES/CapturaPullrequests1.png)

![imagendeFork](IMAGES/CapturaPR2.png)

- Crea o modifica tu rama con el Pull Request

GitHub detectará automáticamente que has subido una nueva rama ó realizaste algún cambio y mostrará un botón que dice **'New pull request'** ó **'Compare pull request'**.

![imagendeFork](IMAGES/CapturaComparePR4.png)

Por último dale clic en el botón y redacta el Pull Request, por ejemplo: docs/guia-tecnica, esto para que Adan revise tu contribución y nos de un checkout.

![imagendeFork](IMAGES/CapturaD.png)

### Notas:
- Asegúrate de estar en el repositorio correcto (AdanCR1/drf-extra-fields) al crear el Pull Request.
- Asegúrate de que tu Pull Request sea claro y conciso, describiendo los cambios realizados y su propósito.