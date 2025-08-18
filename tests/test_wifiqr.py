import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError

from drf_extra_fields.fields import WiFiQRCodeField


@pytest.fixture
def wifi_field():
    return WiFiQRCodeField()


def test_wifi_qrcode_valid_wpa(wifi_field):
    creds = {
        "ssid": "MyWiFi",
        "password": "supersecret",
        "security": "WPA",
        "hidden": False,
    }

    file = wifi_field.to_internal_value(creds)

    assert isinstance(file, SimpleUploadedFile)
    assert file.content_type == "image/png"
    assert file.name.startswith("qrcode_")
    assert file.name.endswith(".png")
    assert file.size > 0


def test_wifi_qrcode_valid_nopass(wifi_field):
    creds = {
        "ssid": "PublicHotspot",
        "security": "nopass",
    }

    file = wifi_field.to_internal_value(creds)

    assert isinstance(file, SimpleUploadedFile)
    assert file.content_type == "image/png"
    assert file.name.endswith(".png")


def test_wifi_qrcode_invalid_type_not_dict(wifi_field):
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value("not-a-dict")
    assert exc_info.value.messages[0] == "Expected a dictionary with WiFi credentials"


def test_wifi_qrcode_empty_data(wifi_field):
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value("")
    assert exc_info.value.messages[0] == "Cannot generate WiFi QR from empty data"


def test_wifi_qrcode_missing_ssid(wifi_field):
    creds = {"security": "WPA", "password": "x"}
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value(creds)
    assert exc_info.value.messages[0] == "Field 'ssid' must be a string"


def test_wifi_qrcode_empty_ssid(wifi_field):
    creds = {"ssid": "", "security": "WPA", "password": "x"}
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value(creds)
    assert exc_info.value.messages[0] == "Field 'ssid' cannot be empty"


def test_wifi_qrcode_missing_security(wifi_field):
    creds = {"ssid": "MyWiFi", "password": "x"}
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value(creds)
    assert exc_info.value.messages[0] == "Field 'security' must be a non-empty string"


def test_wifi_qrcode_invalid_security_value(wifi_field):
    creds = {"ssid": "MyWiFi", "password": "x", "security": "WPA2"}
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value(creds)
    assert exc_info.value.messages[0] == "Field 'security' must be one of: WPA, WEP, nopass"


def test_wifi_qrcode_password_required_for_wpa(wifi_field):
    creds = {"ssid": "MyWiFi", "security": "WPA"}
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value(creds)
    assert exc_info.value.messages[0] == "Field 'password' must be a string"


def test_wifi_qrcode_hidden_must_be_boolean(wifi_field):
    creds = {"ssid": "MyWiFi", "password": "x", "security": "WEP", "hidden": "yes"}
    with pytest.raises(ValidationError) as exc_info:
        wifi_field.to_internal_value(creds)
    assert exc_info.value.messages[0] == "Field 'hidden' must be a boolean if provided"


def test_wifi_qrcode_escaping_characters(wifi_field):
    creds = {
        "ssid": "Office;Wi,fi:Net\\work\"",
        "password": "p;,:\\\"",
        "security": "WEP",
        "hidden": True,
    }

    file = wifi_field.to_internal_value(creds)
    assert isinstance(file, SimpleUploadedFile)