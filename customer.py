from person import Person

class Customer(Person):
    '''
    Beschreibt einen Kunden mit seinem Kundenkontakt.
    Dazu muss bei der Erzeugung des Objekts die Referenz auf ein Mitarbeiter-Objekt geliefert werden.

    Die Attribute sind über getter/setter zugreifbar.
    Für die Ausgabe am Stdout wird die Methode print() verwendet. Dabei wird aber immer auch
    die Ausgabe der Oberklasse Person ausgeführt.
    '''

