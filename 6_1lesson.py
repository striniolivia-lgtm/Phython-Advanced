# Exceptions kommen bei Fehlern vor
# z.B.:
# - falscher Variablenname
# - Division durch 0
# - Man greift auf etwas zu, dass es nicht gibr´t
# - Falscher Datentyp
# sorgt dafür, dass das Programm angehalten wird / "abstürzt"

# Fehler abfangen mit try & except
try:
    pass
    # Code, der bei einem Fehler ausgeführt werden soll
except:
    pass
    # Code, der bei einem Fehler ausgeführt werden soll

# Beispiel
try:
    print("Start code...")
    print(error)
    print("No errors")
except:
    print("We have an error")

print("Code after try/except")

# Nur bestimmte Fehler abfangen
# Besser, nicht jeden Fehler blind abzufangen, sondern gezielt
try:
    number = int("Hello")
except ValueError:
    print("Kann nicht String in Integer umwandeln")


# mehrere except Blöcke
try:
    value = int("Hello")
    result = 10 / 10
except ValueError:
    print("Fehler beim umwandeln")
except ZeroDivisionError:
    print("Darf nicht durch 0 dividieren")
# except ZeroDivisionError wird nicht durchgeführt, weil beim
# try-Block beim ersten Fehler angehalten / abgebrochen wird.

# Mehrere Fehler in einem except
try:
    value = int(input("Geben sie eine Nummer ein: "))
except (ValueError, TypeError):
    print("Es gab einen Eingabefehler")

# Verschachtelte Fehlerbehandlung
# Ein try-Block kann auch einen anderen try-Block liegen

try:
    number = int(input("Geben sie eine Nummer ein: "))
except ValueError:
    print("Fehler bei der Benutzereingabe")
else:
    print(f"Das zweifache von {number} ist {number * 2}")

# Der finally-Block
# finally wird immer ausgeführt
try:
    print("Start")
    x = 1 / 0
except ZeroDivisionError:
    print("Fehler wurde abgefangen")
finally:
    print("Dieser Block läuft immer")

# Komplettes Beispiel mit allen Blöcken
print("\n\n\nKomplettes Beispiel mit allen Blöcken")
try:
    text = input("Gebe eine Zahl an: ")
    under = int(text)
except ValueError:
    print("Das war keine Zahl")
else:
    print("Umwandlung Erfolgreich")
finally:
    print("Einführung in Try/Except beendet!")