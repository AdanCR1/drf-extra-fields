import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError

from drf_extra_fields.fields import vCardQRCodeField


@pytest.fixture
def vcard_field():
    return vCardQRCodeField()


def test_vcard_qrcode_valid(vcard_field):
    data = {
        "name": "John Doe",
        "phone": "+1-555-1234",
        "email": "john@example.com",
    }

    file = vcard_field.to_internal_value(data)

    assert isinstance(file, SimpleUploadedFile)
    assert file.content_type == "image/png"
    assert file.name.startswith("qrcode_")
    assert file.name.endswith(".png")
    assert file.size > 0


def test_vcard_qrcode_invalid_type_not_dict(vcard_field):
    with pytest.raises(ValidationError) as exc_info:
        vcard_field.to_internal_value("not-a-dict")
    assert exc_info.value.messages[0] == "Expected a dictionary with vCard credentials"


def test_vcard_qrcode_empty_data(vcard_field):
    with pytest.raises(ValidationError) as exc_info:
        vcard_field.to_internal_value("")
    assert exc_info.value.messages[0] == "Cannot generate vCard QR from empty data"


def test_vcard_qrcode_missing_name(vcard_field):
    data = {"phone": "+1-555-1234", "email": "john@example.com"}
    with pytest.raises(ValidationError) as exc_info:
        vcard_field.to_internal_value(data)
    assert exc_info.value.messages[0] == "Required fields are missing: name"


def test_vcard_qrcode_missing_phone(vcard_field):
    data = {"name": "John Doe", "email": "john@example.com"}
    with pytest.raises(ValidationError) as exc_info:
        vcard_field.to_internal_value(data)
    assert exc_info.value.messages[0] == "Required fields are missing: phone"


def test_vcard_qrcode_missing_email(vcard_field):
    data = {"name": "John Doe", "phone": "+1-555-1234"}
    with pytest.raises(ValidationError) as exc_info:
        vcard_field.to_internal_value(data)
    assert exc_info.value.messages[0] == "Required fields are missing: email"


def test_vcard_qrcode_multiple_missing_fields(vcard_field):
    data = {"name": "John Doe"}
    with pytest.raises(ValidationError) as exc_info:
        vcard_field.to_internal_value(data)
    # El orden de los campos faltantes sigue la lógica de construcción de la lista
    assert exc_info.value.messages[0] in (
        "Required fields are missing: phone, email",
        "Required fields are missing: email, phone",
    )