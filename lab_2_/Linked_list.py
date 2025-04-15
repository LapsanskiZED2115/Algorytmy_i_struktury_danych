from copy import deepcopy
from typing import Tuple


# Klasa reprezentująca węzeł listy powiązanej
class Node:
    def __init__(self, node_as_tuple: Tuple[str, str, int]):
        self.university = node_as_tuple[0]  # Nazwa uczelni
        self.city = node_as_tuple[1]        # Miasto
        self.date = node_as_tuple[2]        # Rok założenia
        self.next = None                    # Wskaźnik na następny węzeł

    def __str__(self):
        return f"{self.university} {self.city} {self.date}"

    def __repr__(self):
        return f"{self.university} {self.city} {self.date}"


# Funkcje operujące na liście powiązanej

def nil():
    """ Zwraca pustą listę (None) """
    return None


def cons(el: Node, lst):
    """ Dodaje element na początek listy """
    el = deepcopy(el)
    el.next = lst
    return el


def first(lst):
    """ Zwraca pierwszy element listy jako nowy węzeł """
    if lst is None:
        return None
    lst = deepcopy(lst)
    lst.next = None
    return lst


def rest(lst):
    """ Zwraca resztę listy po pierwszym elemencie """
    if lst is None:
        return None
    return lst.next


def create():
    """ Tworzy pustą listę """
    return nil()


def destroy(lst: Node):
    """ Niszczy listę """
    return None


def add(el, lst):
    """ Dodaje element na początek listy """
    return cons(el, lst)


def remove(lst):
    """ Usuwa pierwszy element listy """
    return rest(lst)


def is_empty(lst):
    """ Sprawdza, czy lista jest pusta """
    return lst is None


def length(lst):
    """ Zwraca długość listy """
    if lst is None:
        return 0
    else:
        return 1 + length(rest(lst))


def get(lst):
    """ Zwraca pierwszy element listy """
    return first(lst)


def get_last(lst):
    """ Zwraca ostatni element listy """
    if lst is None:
        return None
    if rest(lst) is None:
        return lst
    else:
        return get_last(rest(lst))


def show_list(lst):
    """ Wyświetla zawartość listy """
    if lst is None:
        return " << TAIL >> "
    return str(lst) + "\n" + show_list(rest(lst))


def add_end(el, lst):
    """ Dodaje element na koniec listy """
    if is_empty(lst):
        return cons(el, lst)
    first_el = first(lst)
    rest_lst = rest(lst)
    recreated_lst = add_end(el, rest_lst)
    return cons(first_el, recreated_lst)


def remove_last(lst):
    """ Usuwa ostatni element listy """
    if is_empty(rest(lst)):
        return None
    first_el = first(lst)
    rest_lst = rest(lst)
    recreated_lst = remove_last(rest_lst)
    return cons(first_el, recreated_lst)


def take(n, lst, new_lst):
    """ Tworzy nową listę z pierwszych n elementów """
    if n > length(lst):
        return deepcopy(lst)
    else:
        return take_recursive(n, lst, new_lst)


def take_recursive(n, lst, new_lst):
    """ Rekurencyjna funkcja do tworzenia listy z n elementów """
    if n < 1:
        raise Exception("Can't take less than one node!")

    lst = deepcopy(lst)
    if length(new_lst) == n:
        return new_lst

    new_lst = add_end(first(lst), new_lst)  # Dodajemy pierwszy element do nowej listy
    return take_recursive(n, rest(lst), new_lst)


def drop(n, lst, new_lst):
    """ Tworzy nową listę z elementów po n pierwszych elementach """
    if n > length(lst):
        return None
    return drop_recursive(length(lst) - n, lst, new_lst)


def drop_recursive(n, lst, new_lst):
    """ Rekurencyjna funkcja do tworzenia listy z elementów po n pierwszych """
    if n < 1:
        raise Exception("Can't take less than one node!")

    lst = deepcopy(lst)
    if length(new_lst) == n:
        return new_lst

    new_lst = add(first(get_last(lst)), new_lst)  # Dodajemy ostatni element do nowej listy
    lst_without_tail = remove_last(lst)
    return drop_recursive(n, lst_without_tail, new_lst)


if __name__ == '__main__':
    # Przykładowe dane o uczelniach
    nodes = [('AGH', 'Kraków', 1919),
             ('UJ', 'Kraków', 1364),
             ('PW', 'Warszawa', 1915),
             ('UW', 'Warszawa', 1915),
             ('UP', 'Poznań', 1919),
             ('PG', 'Gdańsk', 1945)]

    head = create()
    for node in nodes:
        head = add(Node(node), head)

    print("Lista ze wszystkimi elementami:")
    print(show_list(head))

    print("Kopiowanie listy z pominięciem 2 pierwszych elementów:")
    new_head = create()
    new_head = drop(2, head, new_head)
    print(show_list(new_head))

    print("Kopiowanie 4 pierwszych elementów listy:")
    new_head = create()
    new_head = take(4, head, new_head)
    print(show_list(new_head))
