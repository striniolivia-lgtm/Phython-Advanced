# Exceptions erheben
# raise
# wir können selbst einen Fehler erstellen
def checker(text):
    if type(text) != str:
        raise TypeError(
            f"sorry, wir können nicht mit {type(text)} arbeiten"
            f", wir brauchen nähmlich die Klasse str!")
    else:
        return text

checker(123)