class Matrix:
    def __init__(self, matrix, value=0):
        """
        Konstruktor klasy Matrix:
        - Jeśli `matrix` to krotka (np. (2, 3)), tworzy macierz o podanych wymiarach wypełnioną wartością `value`.
        - Jeśli `matrix` to lista list (np. [[1, 2], [3, 4]]), używa jej bez zmian.
        """
        if isinstance(matrix, tuple):
            # Tworzymy nową macierz o zadanych wymiarach
            self._matrix = [[value] * matrix[1] for _ in range(matrix[0])]
        else:
            # Używamy gotowej macierzy (listy list)
            self._matrix = matrix

    def __add__(self, other):
        """
        Dodawanie dwóch macierzy element po elemencie.
        Zwraca nowy obiekt Matrix.
        """
        if self.size() != other.size():
            raise Exception("Wrong matrix shape!")  # Wymiar musi być taki sam!

        new_list = []
        for row in range(self.size()[0]):
            # Dodajemy wiersz po wierszu, elementy jeden do jednego
            new_list.append([self[row][i] + other[row][i] for i in range(self.size()[1])])
        return Matrix(new_list)

    def __mul__(self, other):
        """
        Mnożenie macierzy przez inną macierz (standardowe mnożenie macierzowe).
        Zwraca nową macierz wynikową.
        """
        if self.size()[1] != other.size()[0]:
            raise Exception("Wrong matrix shape!")  # Wymagana zgodność wymiarów

        # Tworzymy nową pustą macierz wynikową o odpowiednich wymiarach
        new_matrix = Matrix((self.size()[0], other.size()[1]))
        for i in range(self.size()[0]):  # Iteracja po wierszach macierzy A
            for j in range(other.size()[1]):  # Iteracja po kolumnach macierzy B
                for k in range(other.size()[0]):  # Iteracja po wspólnej długości
                    new_matrix[i][j] += self[i][k] * other[k][j]
        return Matrix(new_matrix)

    def __str__(self):
        """
        Reprezentacja tekstowa macierzy — każda linia osobno.
        """
        return "\n".join([str(row) for row in self._matrix])

    def size(self):
        """
        Zwraca rozmiar macierzy jako krotkę (liczba wierszy, liczba kolumn).
        """
        return len(self._matrix), len(self._matrix[0])

    def __getitem__(self, item):
        """
        Umożliwia dostęp do macierzy przez indeks: matrix[i]
        """
        return self._matrix[item]

    def __setitem__(self, key, value):
        """
        Umożliwia przypisanie nowego wiersza do macierzy: matrix[i] = [...]
        """
        self._matrix[key] = value


def transpose_matrix(matrix: Matrix) -> Matrix:
    """
    Zwraca nową macierz — transponowaną wersję podanej (zamiana wierszy z kolumnami).
    """
    # Nowa macierz będzie miała rozmiar odwrotny: (kolumny, wiersze)
    new_matrix = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(matrix.size()[0]):  # Wiersze oryginalnej macierzy
        for j in range(matrix.size()[1]):  # Kolumny oryginalnej macierzy
            new_matrix[j][i] = matrix[i][j]  # Zamiana miejscami
    return new_matrix


def main():
    """
    Funkcja testowa: sprawdza działanie klasy Matrix i transpozycji.
    """
    A = Matrix([[1, 0, 2],
                [-1, 3, 1]])  # Macierz 2x3

    B = Matrix((2, 3), value=1)  # Macierz 2x3 wypełniona jedynkami

    C = Matrix([[3, 1],
                [2, 1],
                [1, 0]])  # Macierz 3x2

    # Transpozycja macierzy A
    print("Transposed matrix:")
    print(transpose_matrix(A))

    # Dodawanie macierzy A + B
    print("A + B")
    print(A + B)

    # Mnożenie A * C
    print("A * C")
    print(A * C)


# Uruchomienie programu
if __name__ == '__main__':
    main()
