#Eigene Exceptions erstellen
class BuildingError(Exception):
    def __str__(self):
        return "Insufficien Matirial - can't build house"


def check_material(amount_of_material, limit_value):
    if amount_of_material >= limit_value:
        return "enough material"
    else:
        raise BuildingError()

print(check_material(500, 300))
print(check_material(300, 500))
