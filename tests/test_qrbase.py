'''

import base64
import copy
import datetime
import os
from decimal import Decimal
from unittest.mock import patch

import django
import pytest
pytest.skip("GDAL not installed", allow_module_level=True)
import pytz
from django.core.exceptions import ValidationError
from django.test import TestCase, override_settings
from rest_framework import serializers
from rest_framework.fields import DecimalField

from drf_extra_fields import compat
from drf_extra_fields.compat import DateRange, DateTimeTZRange, NumericRange
from drf_extra_fields.fields import (
    Base64FileField,
    Base64ImageField,
    DateRangeField,
    DateTimeRangeField,
    DecimalRangeField,
    FloatRangeField,
    HybridImageField,
    IntegerRangeField,
    LowercaseEmailField,
)
import io
import uuid
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import ImageField
from drf_extra_fields.fields import BaseQRCodeField  # <-- Ajusta la ruta según tu proyecto

clase de prueba para BaseQRCodeField
Esta clase contiene tests para verificar el correcto funcionamiento del campo QR.

@pytest.fixture
def qr_field():
    """
    Fixture para instanciar la clase BaseQRCodeField.
    
    Returns:
        BaseQRCodeField: Una instancia del campo QR para usar en los tests.
    """
    return BaseQRCodeField()


def test_qrcode_field_valid(qr_field):
    """
    Test caso exitoso: debe generar un archivo PNG válido cuando se le pasa un string.
    
    Este test verifica que:
    - Se genera un SimpleUploadedFile válido
    - El archivo tiene formato PNG correcto
    - El nombre del archivo es único y válido
    - El archivo contiene datos (no está vacío)
    
    Args:
        qr_field: Fixture que proporciona una instancia de BaseQRCodeField
    """
    text = "Hola Gerardo"
    file = qr_field.to_internal_value(text)
    
    # Verificamos que el resultado sea un archivo subido válido
    assert isinstance(file, SimpleUploadedFile)
    assert file.content_type == "image/png"
    assert file.name.startswith("qrcode_")
    assert file.name.endswith(".png")
    assert file.size > 0  # El archivo no está vacío


def test_qrcode_field_invalid_type(qr_field):
    """
    Test caso de error: debe lanzar ValidationError si el dato no es un string.
    
    Este test verifica que el campo valida correctamente el tipo de entrada
    y rechaza datos que no sean strings con el mensaje de error apropiado.
    
    Args:
        qr_field: Fixture que proporciona una instancia de BaseQRCodeField
    """
    with pytest.raises(ValidationError) as exc_info:
        qr_field.to_internal_value(12345)  # Tipo inválido
    
    assert "Expected text to generate QR code" in str(exc_info.value)


def test_qrcode_field_empty_string(qr_field):
    """
    Test caso de error: debe lanzar ValidationError si el string está vacío.
    
    Este test verifica que el campo rechaza correctamente strings vacíos
    con el mensaje de error apropiado.
    
    Args:
        qr_field: Fixture que proporciona una instancia de BaseQRCodeField
    """
    with pytest.raises(ValidationError) as exc_info:
        qr_field.to_internal_value("")
    
    assert "Cannot generate QR code from empty text" in str(exc_info.value)
'''
# test_qrbase.py
# tests/test_qrbase.py

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
