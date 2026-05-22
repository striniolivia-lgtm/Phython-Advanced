# Unterschied zwischen Exception und warning
# Exception - echter Fehler - Programm stürzt ab.
# Warning - problematisch Code - aber läuft weiter
import warnings

warnings.warn("Das könnte später Probleme machen.", UserWarning)

# Warning Filter with simplefilter()
# Phyton kann Warnungen unterschiedlich behandeln
warnings.simplefilter("always", UserWarning)
warnings.warn("Diese Warnung wird immer angezeigt.", UserWarning)

# Warning als Exception behandeln
# Wenn beim simplefilter "error" angegeben wird, kann die Warnung als Exception abgefangen werden im except-block
warnings.simplefilter("error", UserWarning)

try:
    warnings.warn("Das ist jetzt wie ein Fehler.", UserWarning)
except UserWarning:
    print("Die Warnung wird jetzt als Exception behandeln.")

# Vergleich - das alleine macht nur einen Fehler aus und bricht das Programm ab.
warnings.warn("Die Warnung ist jetzt ein Fehler .")