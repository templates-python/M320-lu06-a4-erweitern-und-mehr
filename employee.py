from person import Person

class Employee(Person):
    '''
    Beschreibt eine Mitarbeiterin mit den für eine Firma typischen Merkmalen wie
    - Personal-Nummer
    - Lohn
    - Telefon-Nummer

    Die Attribute sind über getter/setter zugreifbar.
    Für die Ausgabe am Stdout wird die Methode print() verwendet. Dabei wird aber immer auch
    die Ausgabe der Oberklasse Person ausgeführt.
    '''

