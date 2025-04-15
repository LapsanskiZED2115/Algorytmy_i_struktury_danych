from copy import deepcopy
from typing import Tuple


class Node:
    """
    Klasa reprezentująca węzeł listy powiązanej.
    Przechowuje dane uczelni (nazwa, miasto, rok) i wskaźnik na następny węzeł.
    """
    def __init__(self, data: Tuple[str, str, int]):
        # Zainicjalizowanie danych węzła
        self.university = data[0]  # Nazwa uczelni
        self.city = data[1]        # Miasto uczelni
        self.date = data[2]        # Rok założenia uczelni
        self.next = None            # Wskaźnik na następny węzeł w liście

    def __str__(self):
        return f"{self.university} {self.city} {self.date}"

    def __repr__(self):
        return str(self)


class LinkedList:
    """
    Klasa reprezentująca jednokierunkową listę powiązaną.
    Umożliwia dodawanie, usuwanie i manipulowanie węzłami w liście.
    """
    def __init__(self):
        self.head = None  # Inicjalizacja pustej listy (brak węzłów)

    def destroy(self) -> None:
        """
        Zniszczenie listy, czyli usunięcie wszystkich węzłów.
        """
        self.head = None

    def add(self, node: Node) -> None:
        """
        Dodanie węzła na początek listy (head).
        """
        node = deepcopy(node)  # Kopiujemy węzeł, aby nie modyfikować oryginału
        node.next = self.head   # Nowy węzeł wskazuje na obecny pierwszy węzeł
        self.head = node        # Aktualizujemy head, aby nowy węzeł był pierwszym

    def remove(self) -> None:
        """
        Usunięcie pierwszego węzła (head).
        """
        if self.is_empty():
            raise IndexError("List is empty!")  # Obsługa próby usunięcia z pustej listy
        self.head = self.head.next  # Ustawiamy head na następny węzeł

    def is_empty(self) -> bool:
        """
        Sprawdzenie, czy lista jest pusta.
        """
        return self.head is None

    def length(self) -> int:
        """
        Zwrócenie długości listy (liczba węzłów).
        """
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next  # Przechodzimy do następnego węzła
        return length

    def get(self) -> Node:
        """
        Zwrócenie pierwszego węzła listy (head).
        """
        if self.is_empty():
            raise IndexError("List is empty!")  # Obsługa próby dostępu do pustej listy
        return self.head

    def add_to_end(self, node: Node) -> None:
        """
        Dodanie węzła na koniec listy.
        """
        node = deepcopy(node)  # Kopiujemy węzeł
        if not self.head:
            self.head = node  # Jeśli lista jest pusta, nowy węzeł staje się head
            return
        current = self.head
        while current.next:
            current = current.next  # Szukamy ostatniego węzła
        current.next = node  # Dodajemy nowy węzeł na końcu

    def remove_last(self) -> None:
        """
        Usunięcie ostatniego węzła w liście.
        """
        if self.is_empty():
            raise IndexError("List is empty!")  # Obsługa próby usunięcia z pustej listy
        if self.head.next is None:
            self.head = None  # Jeśli lista ma tylko jeden węzeł, usuwamy go
            return
        current = self.head
        while current.next and current.next.next:  # Szukamy przedostatniego węzła
            current = current.next
        current.next = None  # Usuwamy ostatni węzeł

    def show_list(self) -> None:
        """
        Wypisanie zawartości całej listy.
        """
        current = self.head
        index = 1
        print("<< HEAD >>")  # Oznaczenie początkowego elementu listy
        while current:
            print(f"{index} - {current}")  # Wyświetlamy każdy węzeł
            current = current.next
            index += 1

    def take(self, n: int):
        """
        Tworzenie nowej listy z pierwszych n węzłów.
        """
        if n < 1:
            raise Exception("Can't take less than one node!")
        if n >= self.length():
            return deepcopy(self)  # Zwracamy kopię całej listy, jeśli n >= długości listy
        copied = deepcopy(self)  # Tworzymy kopię listy
        current = copied.head
        for _ in range(n - 1):
            current = current.next  # Przechodzimy do n-tego węzła
        current.next = None  # Usuwamy wszystkie węzły po n-tym
        return copied

    def drop(self, n: int):
        """
        Tworzenie nowej listy z węzłami po pierwszych n elementach.
        """
        if n < 1:
            raise Exception("Can't take less than one node!")
        if n >= self.length():
            return LinkedList()  # Jeśli n >= długości listy, zwracamy pustą listę
        new_list = LinkedList()  # Tworzymy nową pustą listę
        current = self.head
        for _ in range(n):
            current = current.next  # Przechodzimy do n-tego węzła
        while current:
            new_list.add_to_end(Node((current.university, current.city, current.date)))  # Dodajemy do nowej listy
            current = current.next
        return new_list


if __name__ == '__main__':
    # Przykładowe dane o uczelniach
    data = [
        ('AGH', 'Kraków', 1919),
        ('UJ', 'Kraków', 1364),
        ('PW', 'Warszawa', 1915),
        ('UW', 'Warszawa', 1915),
        ('UP', 'Poznań', 1919),
        ('PG', 'Gdańsk', 1945)
    ]

    ll = LinkedList()
    print("Dodawanie dwóch uczelni na początek:")
    ll.add(Node(data[0]))  # Dodajemy pierwszą uczelnię na początek
    ll.add(Node(data[1]))  # Dodajemy drugą uczelnię na początek
    ll.show_list()

    print("\nDodawanie uczelni na koniec:")
    ll.add_to_end(Node(data[2]))  # Dodajemy trzecią uczelnię na koniec
    ll.show_list()

    print("\nUsuwanie ostatniego elementu:")
    ll.remove_last()  # Usuwamy ostatnią uczelnię
    ll.show_list()

    print("\nPierwszy element listy:")
    print(ll.get())  # Pokazujemy pierwszy element listy

    print("\nUsuwanie pierwszego elementu:")
    ll.remove()  # Usuwamy pierwszy element
    ll.show_list()

    print("\nCzy lista jest pusta?")
    print(ll.is_empty())  # Sprawdzamy, czy lista jest pusta

    print("\nDługość listy:")
    print(ll.length())  # Pokazujemy długość listy

    print("\nCzyszczenie listy:")
    ll.destroy()  # Usuwamy wszystkie elementy listy
    print("Czy pusta?", ll.is_empty())

    print("\nTworzenie listy ze wszystkich uczelni:")
    for uni in data:
        ll.add(Node(uni))  # Dodajemy wszystkie uczelnie
    ll.show_list()

    print("\nNowa lista bez 3 pierwszych uczelni:")
    dropped = ll.drop(3)  # Tworzymy nową listę bez pierwszych 3 uczelni
    dropped.show_list()

    print("\nNowa lista tylko z 4 pierwszych uczelni:")
    taken = ll.take(4)  # Tworzymy nową listę z 4 pierwszymi uczelniami
    taken.show_list()
