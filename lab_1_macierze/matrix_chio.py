class Matrix:
    def __init__(self, data, fill_value=0):
        """
        Konstruktor klasy Matrix.
        - Jeśli podano krotkę (np. (3, 3)) — tworzy macierz o zadanych wymiarach wypełnioną `fill_value`.
        - Jeśli podano listę list — używa jej jako danych.
        """
        if isinstance(data, tuple):
            rows, cols = data
            self._matrix = [[fill_value for _ in range(cols)] for _ in range(rows)]
        else:
            self._matrix = data

    def __add__(self, other):
        """
        Dodawanie macierzy (element po elemencie).
        """
        if self.size() != other.size():
            raise Exception("Nieprawidłowe wymiary macierzy!")

        result = []
        for r in range(self.rows()):
            result.append([self[r][c] + other[r][c] for c in range(self.cols())])
        return Matrix(result)

    def __mul__(self, other):
        """
        Mnożenie macierzy A * B (iloczyn macierzowy).
        """
        if self.cols() != other.rows():
            raise Exception("Nieprawidłowe wymiary macierzy do mnożenia!")

        result = Matrix((self.rows(), other.cols()))
        for i in range(self.rows()):
            for j in range(other.cols()):
                for k in range(self.cols()):
                    result[i][j] += self[i][k] * other[k][j]
        return result

    def __str__(self):
        """Wypisywanie macierzy w czytelnej formie."""
        return "\n".join(str(row) for row in self._matrix)

    def size(self):
        """Zwraca (liczba wierszy, liczba kolumn)."""
        return self.rows(), self.cols()

    def rows(self):
        return len(self._matrix)

    def cols(self):
        return len(self._matrix[0]) if self._matrix else 0

    def __getitem__(self, index):
        """Umożliwia odczyt: macierz[i]"""
        return self._matrix[index]

    def __setitem__(self, index, value):
        """Umożliwia zapis: macierz[i] = [...]"""
        self._matrix[index] = value


def transpose_matrix(matrix: Matrix) -> Matrix:
    """
    Transpozycja macierzy: zamiana wierszy z kolumnami.
    """
    transposed = Matrix((matrix.cols(), matrix.rows()))
    for i in range(matrix.rows()):
        for j in range(matrix.cols()):
            transposed[j][i] = matrix[i][j]
    return transposed


def determinant_2x2(matrix: Matrix) -> float:
    """
    Obliczanie wyznacznika macierzy 2x2:
    |a b|
    |c d| = ad - bc
    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def recursive_chio(coeff: float, matrix: Matrix) -> float:
    """
    Rekurencyjna metoda Chio — obliczanie wyznacznika macierzy kwadratowej (n > 2).
    """
    if matrix.size() == (2, 2):
        return coeff * determinant_2x2(matrix)

    # Jeśli lewy górny element to 0 — zamieniamy wiersze
    if matrix[0][0] == 0:
        for i in range(1, matrix.rows()):
            if matrix[i][0] != 0:
                # Zamiana wierszy
                matrix[0], matrix[i] = matrix[i], matrix[0]
                coeff *= -1  # Zmiana znaku wyznacznika
                break

    # Obliczamy nowy współczynnik
    pivot = matrix[0][0]
    n = matrix.rows()
    new_coeff = coeff / (pivot ** (n - 2))

    # Tworzymy zredukowaną macierz (rozmiar o 1 mniejszy)
    reduced = []
    for i in range(1, n):
        row = []
        for j in range(1, n):
            # Tworzymy podmacierz 2x2 i liczymy z niej wyznacznik
            submatrix = Matrix([[matrix[0][0], matrix[0][j]],
                                [matrix[i][0], matrix[i][j]]])
            row.append(determinant_2x2(submatrix))
        reduced.append(row)

    return recursive_chio(new_coeff, Matrix(reduced))


def compute_determinant(matrix: Matrix) -> float:
    """
    Obliczanie wyznacznika macierzy za pomocą metody Chio.
    Dla macierzy 2x2 — bezpośredni wzór.
    Dla większych — wywołanie rekurencyjne.
    """
    if matrix.size() == (2, 2):
        return determinant_2x2(matrix)
    return recursive_chio(1.0, matrix)


# Przykład użycia
if __name__ == '__main__':
    A = Matrix([[5, 1, 1, 2, 3],
                [4, 2, 1, 7, 3],
                [2, 1, 2, 4, 7],
                [9, 1, 0, 7, 0],
                [1, 4, 7, 2, 2]])

    B = Matrix([[0, 1, 1, 2, 3],
                [4, 2, 1, 7, 3],
                [2, 1, 2, 4, 7],
                [9, 1, 0, 7, 0],
                [1, 4, 7, 2, 2]])

    print("Wyznacznik macierzy A:", compute_determinant(A))
    print("Wyznacznik macierzy B:", compute_determinant(B))
