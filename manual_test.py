import os
import sys
import base64
import argparse
from io import BytesIO

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_extra_fields.runtests.settings")
import django
django.setup()

from rest_framework import serializers
from drf_extra_fields.fields import vCardQRCodeField

class VCardSerializer(serializers.Serializer):
    vcard = vCardQRCodeField()

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Genera un QR de vCard y lo imprime en Base64 en la consola",
    )
    parser.add_argument("--name", required=True, help="Nombre del contacto")
    parser.add_argument("--phone", required=True, help="Número de teléfono")
    parser.add_argument("--email", required=True, help="Correo electrónico")

    args = parser.parse_args(argv)

    payload = {
        "vcard": {
            "name": args.name,
            "phone": args.phone,
            "email": args.email,
        }
    }

    serializer = VCardSerializer(data=payload)
    try:
        serializer.is_valid(raise_exception=True)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    uploaded_file = serializer.validated_data["vcard"]
    png_bytes = uploaded_file.read()
    b64 = base64.b64encode(png_bytes).decode()
    print(b64)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))