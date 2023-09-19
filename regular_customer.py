from customer import Customer


class RegularCustomer(Customer):
   '''
    Beschreibt einen Stammkunden mit seinem Kundenkontakt und dem Rabatt, den er bekommt.
    Dazu muss bei der Erzeugung des Objekts die Referenz auf ein Mitarbeiter-Objekt geliefert werden.

    Die Attribute sind über getter/setter zugreifbar.
    Für die Ausgabe am Stdout wird die Methode print() verwendet. Dabei wird aber immer auch
    die Ausgabe der Oberklasse Customer ausgeführt.
   '''

