# Generatoren
# Sind eng mit Iteratoren verwandt
# Spezielle Funktion, die Werte nach und nach liefert.
def raise_to_the_degrees(number, max_degree):
    i = 0
    # _, falls die Variable des for-loops nicht verwendet wird
    for _ in range(max_degree):
        yield number ** i
        i += 1


res = raise_to_the_degrees(2, 5)
print(res)

for value in res:
    print(value)

# yield ist besonders, weil
# gibt einen Wert zurück, wie return aber bricht nicht ab
# und weiteres merkt sich den Zustand wie eine Variable
