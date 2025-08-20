# Guía Técnica para Contribuir en el proyecto drf-extra-fields

Este documento explica desde cómo clonar el repositorio, crear ramas, configurar
el entorno de desarrollo, ejecutar pruebas y realizar Pull Requests. Sigue estos
pasos para que tu contribución sea sencilla, efectiva y alineada con las buenas
prácticas del proyecto.

Por el momento, este documento está en español, pero se espera que la comunidad
contribuya a su traducción al inglés y otros idiomas.

---

---

# **Cómo configurar tu entorno de desarrollo**

## 1. Crear un Fork y clonar el repositorio

**Este paso es muy importante para la contribución.**

Crea un Fork del repositorio original en tu cuenta de GitHub. Esto te permitirá
trabajar en tu propia copia del proyecto sin afectar el repositorio principal.
Ingresa a la pagina de tu fork y dale clic en 'Code' para copiar el enlace del
repositorio.

![imagendeFork](IMAGES/Captura1enlace.png)

Una vez copiado, crea una carpeta y dentro clona tu Fork con el siguiente
comando:

```bash
git clone https://github.com/[username]/drf-extra-fields.git
```

## 2. Ingresar al directorio del proyecto

Ingresa al directorio del proyecto para comenzar a trabajar dentro de él con el
siguiente comando:

```bash
cd drf-extra-fields
```

## 2.1 Crea una rama de desarrollo desde master con el nombre de la característica o tarea que te corresponde (Opcional)

```bash
git checkout -b nombre-de-tu-rama
```

## 3. Crear y activar el entorno virtual para aislar las dependencias del proyecto

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
pip install -r requirements_dev.txt
```

**Como probar tu implementación - Ejemplo de uso para configuracion del entorno
(PYTHONPATH)**

## 5. Configurar PYTHONPATH

Primero, necesitamos asegurarnos de que Python pueda encontrar este módulo si lo
usas en otro proyecto. Aquí te explico cómo configurarlo con los siguientes
pasos:

**En Windows:**

1. Pulsa `Windows + R`, escribe `sysdm.cpl` y presiona Enter.

![imagendeFork](IMAGES/1.png)

2. En la ventana que aparece, ve a la pestaña **Opciones avanzadas** y haz clic
   en **Variables de entorno**.

![imagendeFork](IMAGES/2.png)

3. Busca una variable llamada `PYTHONPATH` en **Variables del sistema**, si ya
   lo tienes creada sólo editala y pon aceptar y aceptar.

4. Si no la encuentras, crea una nueva con el nombre `PYTHONPATH` y en el valor
   de esa variable, agrega la ruta completa de tu repositorio, como:
   `C:\Users\Martha\Documents\drf-extra-fields`.

![imagendeFork](IMAGES/3.png)

Haz clic en **Aceptar** y cierra todo.

5. Para verificar si has configurado correctamente la variable de entorno
   `PYTHONPATH`, ejecuta el siguiente comando.

```bash
echo $PYTHONPATH
```

Si esta todo correcto, deberias ver la ruta que as asignado en el valor de
`PYTHONPATH`.

![imagendeFork](IMAGES/4.png)

Nota: Con la variable de entorno `PYTHONPATH` configurada, Python podrá
encontrar el módulo `drf_extra_fields` desde cualquier proyecto que estés
trabajando. Esto es útil si quieres utilizar los campos implementados en un
proyecto de prueba o en otro proyecto sin tener que instalarlo como un paquete.

---

# **Cómo implementar un campo personalizado: Ejemplo con Códigos QR**

Este es un ejemplo de cómo se realizaría la implementación de un campo
personalizado para la generación de códigos QR y cómo usarlo en una
implementación real con Django/DRF.

## 1. Crea el Campo QR:

En este ejemplo usamos una clase llamada vCardQRCodeField que hereda de
BaseQRCodeField. Lo que hace esta clase es convertir datos de contacto (name,
phone, email) en formato vCard y luego generar un código QR en forma de imagen,
implementado en el archivo `drf_extra_fields/fields.py`.

```python
class vCardQRCodeField(BaseQRCodeField):
    """
    Campo que genera un código QR con un diccionario vCard.
    """

    def to_internal_value(self, data):
        if not isinstance(data, dict):
            raise ValidationError("Se esperaba un diccionario para los datos vCard.")

        required_fields = ['name', 'phone', 'email']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValidationError(f"Falta o está vacío el campo requerido: '{field}'")

        vcard_string = (
            f"BEGIN:VCARD\n"
            f"VERSION:3.0\n"
            f"FN:{data['name']}\n"
            f"TEL:{data['phone']}\n"
            f"EMAIL:{data['email']}\n"
            f"END:VCARD"
        )

        return super().to_internal_value(vcard_string)
```

## 2. Crear un proyecto Django para probar el campo QR:

- Crea un proyecto Django y una aplicación llamada `core`.

```bash
django-admin startproject mi_proyecto
cd mi_proyecto
python manage.py startapp core
```

## 3. Crear un Modelo para guardar la imagen del QR:

- En el archivo `core/models.py`, agrega un campo `ImageField` donde se guardará
  la imagen generada:

```python
codigo_qr = models.ImageField(upload_to="codigos/", null=True, blank=True)
```

## 4. Configurar los Archivos de Medios:

- Para poder guardar y mostrar las imágenes de los códigos QR generados,
  configuramos Django para servir archivos multimedia.

**En `settings.py` añadimos:**

```python
MEDIA_URL = "files/"
MEDIA_ROOT = BASE_DIR / "files"
```

**En `urls.py` agregamos los siguiente:**

```bash
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Esto ará que en desarrollo podamos ver las imágenes directamente desde el
navegador.

## 5. Agregar el Campo al Serializer:

- En `serializers.py` usamos nuestro campo especial.

```python
from core.fields import vCardQRCodeField

class ClienteSerializer(serializers.Serializer):
    codigo_qr = vCardQRCodeField()
```

Con esto, cuando llegue la información del cliente, se genera el QR
automáticamente.

## 6. Levanta el Servidor:

- Ejecutamos:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 7. Probar la API

- Enviamos un JSON con los datos de un cliente, por ejemplo:

{ "contacto_qr": { "name": "Martha", "phone": "77889966", "email":
"martha@gmail.com" } }

Al hacer la petición, el sistema generará automáticamente el código QR con esos
datos. Finalmente abrimos en el navegador el siguiente enlace
http://127.0.0.1:8000/api/nombre-de-la-api/ y listo, ya tenemos disponible el
código QR generado con los datos implementados.

## ![imagendeFork](IMAGES/ImagenQr.png)

---

# **Cómo escribir pruebas unitarias para tu campo personalizado**

Este documento describe como ejemplo el test unitario implementado para la clase
`BaseQRCodeField`, un campo personalizado de **Django REST Framework** que
genera códigos QR a partir de texto de entrada.

---

## 1. Estructura del Test

**Archivo:** `test_qrbase.py`  
El test está organizado en una estructura simple y directa que cubre los casos
esenciales de uso de la clase `BaseQRCodeField`.

---

## 2. Dependencias

```python
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from drf_extra_fields.fields import BaseQRCodeField
```

Dependencias Externas Requeridas:

pytest: Framework de testing

Django: Para ValidationError y SimpleUploadedFile

djangorestframework: Framework base

qrcode: Librería para generar códigos QR

pillow: Procesamiento de imágenes

## 3. **Componentes del Test** Fixture: qr_field

```python
@pytest.fixture
def qr_field():
    """Fixture para instanciar la clase BaseQRCodeField."""
    return BaseQRCodeField()
```

Propósito: Proporciona una instancia reutilizable de BaseQRCodeField para todos
los tests. Beneficios:

Evita duplicación de código

Garantiza instancia limpia en cada test

Simplifica la escritura de tests

## 4. Test de Caso Exitoso: test_qrcode_field_valid

```python
def test_qrcode_field_valid(qr_field):
    """Caso exitoso: debe generar un archivo PNG válido cuando se le pasa un string."""
    text = "Hola Gerardo"
    file = qr_field.to_internal_value(text)

    assert isinstance(file, SimpleUploadedFile)
    assert file.content_type == "image/png"
    assert file.name.startswith("qrcode_")
    assert file.name.endswith(".png")
    assert file.size > 0
```

## 5. test de Validación de Tipo: test_qrcode_field_invalid_type

```python
def test_qrcode_field_invalid_type(qr_field):
    with pytest.raises(ValidationError) as exc_info:
        qr_field.to_internal_value(12345)

    assert str(exc_info.value) == "['Expected text to generate QR code']"
```

Objetivo: Rechazar entradas que no sean strings.

Objetivo: Verificar que el campo genere correctamente un código QR válido a
partir de texto.

## 6. Test de String Vacío: test_qrcode_field_empty_string

```python
def test_qrcode_field_empty_string(qr_field):
    with pytest.raises(ValidationError) as exc_info:
        qr_field.to_internal_value("")

    assert str(exc_info.value) == "['Cannot generate QR code from empty text']"
```

Objetivo: Rechazar strings vacíos.

## 7. Ejecución de Tests

Ejecutar todos los tests

```bash
pytest test_qrbase.py -v
```

Ejecutar test específico

```bash
pytest test_qrbase.py::test_qrcode_field_valid -v
```

Con output detallado

```bash
pytest test_qrbase.py -v -s
```

Con información de coverage

```bash
pytest test_qrbase.py --cov=drf_extra_fields.fields
```

Salida Esperada:

```bash
test_qrbase.py::test_qrcode_field_valid PASSED [33%]
test_qrbase.py::test_qrcode_field_invalid_type PASSED [66%]
test_qrbase.py::test_qrcode_field_empty_string PASSED [100%]
======================= 3 passed in 0.42s =======================

```

Test Pasando

<img width="1487" height="294" alt="captura_baseqr" src="https://github.com/user-attachments/assets/dc584050-ac6f-401a-adfe-05ed4d549d99" />

En el archivo tests/test_qrbase.py deben de crear sus nuevas clases siguiendo el
patrón de la clase Base64ImageSerializerTests. La imagen de **test Pasando** es
como deberian de lucir sus pruebas.

## 8. **Ejecutar pruebas con tox** Para automatizar las pruebas y asegurar la calidad

del código, debes usar los siguientes comandos:

```bash
pip install tox
```

```bash
tox
```

---

# **Cómo enviar tus cambios para solicitar la unión**

1. Ve a: https://github.com/Hipo/drf-extra-fields/pulls
2. Haz clic en **"New Pull Request"**
3. Configura así:
   - base: `master` repositorio `Hipo/drf-extra-fields`
   - compare: `tu-rama` repositorio `tu-usuario/drf-extra-fields`
4. Revisa los cambios y asegúrate que todo esté correcto.
5. Añade un título descriptivo y una descripción detallada de tus cambios,
   indicando qué problema resuelven o qué funcionalidad añaden.
6. Haz clic en **"Create pull request"** para enviar tu contribución a revisión.

## Notas

- Describe claramente los cambios en tu Pull Request, un titulo claro y una
  descripción breve.
