# Exceptions mit "as" speichern
# man kann einen fehler in einer variable erstellen

try:
    number = int("ABC")
except ValueError as error:
    print("Fehlermeldung:", error)
