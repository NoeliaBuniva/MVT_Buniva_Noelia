from ejemplo.models import Familiar

Familiar(nombre="Noelia", direccion="Rivadavia 374", numero_pasaporte=123123).save()
Familiar(nombre="Magui", direccion="San Luis 1281", numero_pasaporte=890890).save()
Familiar(nombre="Penny", direccion="Rivadavia 374", numero_pasaporte=345345).save()
Familiar(nombre="Potus", direccion="San Luis 1281", numero_pasaporte=567567).save()

print("Se cargaron con éxito los usuarios de pruebas")