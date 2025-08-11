import qrcode
from drf_extra_fields.fields import vCardQRCodeField
from rest_framework import serializers

class VCardQRCodeSerializer(serializers.Serializer):
    qr_code = vCardQRCodeField()

print("Probando con datos válidos")
valid_data = {
    'qr_code': {
        'name': 'Pablo Jane',
        'phone': '32452352',
        'email': 'Jane.doe@example.com'
    }
}
serializer = VCardQRCodeSerializer(data=valid_data)
if serializer.is_valid():
    print("el validador de datos validos funiona .")
    print("datos validados:", serializer.validated_data)
else:
    print("el validador fallo con datos validos.", serializer.errors)
print("-" * 30)

print("Probando con datos invalidos")
invalid_data = {
    'qr_code': {
        'name': 'Pablo Jane',
        'phone': '32452352'
    }
}
serializer = VCardQRCodeSerializer(data=invalid_data)
if not serializer.is_valid():
    print("el validador fallo correctamente con datos invalidos.")
    print("errores de validacion:", serializer.errors)
else:
    print("el validador no detecto el error en los datos invalidos.")