
# test_qrbase.py

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from drf_extra_fields.fields import BaseQRCodeField  # Ajusta según tu proyecto


@pytest.fixture
def qr_field():
    """Fixture para instanciar la clase BaseQRCodeField."""
    return BaseQRCodeField()


def test_qrcode_field_valid(qr_field):
    """Caso exitoso: debe generar un archivo PNG válido cuando se le pasa un string."""
    text = "Hola Gerardo"
    file = qr_field.to_internal_value(text)

    # Verificamos que el resultado sea un archivo subido válido
    assert isinstance(file, SimpleUploadedFile)
    assert file.content_type == "image/png"
    assert file.name.startswith("qrcode_")
    assert file.name.endswith(".png")
    assert file.size > 0  # El archivo no está vacío


def test_qrcode_field_invalid_type(qr_field):
    with pytest.raises(ValidationError) as exc_info:
        qr_field.to_internal_value(12345)

    assert str(exc_info.value) == "['Expected text to generate QR code']"


def test_qrcode_field_empty_string(qr_field):
    with pytest.raises(ValidationError) as exc_info:
        qr_field.to_internal_value("")

    assert str(exc_info.value) == "['Cannot generate QR code from empty text']"
