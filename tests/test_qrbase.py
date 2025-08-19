
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


# --- Tests para UrlQRCodeField ---
from rest_framework.serializers import Serializer
from rest_framework.exceptions import ValidationError as DRFValidationError
from drf_extra_fields.fields import UrlQRCodeField
from PIL import Image

class UrlQRCodeFieldTestSerializer(Serializer):
    qr = UrlQRCodeField()

@pytest.fixture
def url_serializer():
    return UrlQRCodeFieldTestSerializer

def test_valid_url_generates_qr(url_serializer):
    data = {"qr": "https://www.example.com"}
    serializer = url_serializer(data=data)
    assert serializer.is_valid(), serializer.errors

    qr_file = serializer.validated_data["qr"]
    assert qr_file.name.endswith(".png")

    image = Image.open(qr_file)
    assert image.format == "PNG"

def test_invalid_url_scheme(url_serializer):
    data = {"qr": "ftp://example.com"}
    serializer = url_serializer(data=data)
    assert not serializer.is_valid()
    assert "qr" in serializer.errors
    assert "The URL must begin with" in str(serializer.errors["qr"][0])

def test_empty_url(url_serializer):
    data = {"qr": ""}
    serializer = url_serializer(data=data)
    assert not serializer.is_valid()
    assert "qr" in serializer.errors
    assert "cannot be generated from an empty URL" in str(serializer.errors["qr"][0])

def test_non_string_input(url_serializer):
    data = {"qr": 12345}
    serializer = url_serializer(data=data)
    assert not serializer.is_valid()
    assert "qr" in serializer.errors
    assert "A text string (URL) was expected" in str(serializer.errors["qr"][0])
