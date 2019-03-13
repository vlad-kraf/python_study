class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        self.max_size = max_size or Matrix.MAX_SIZE
        self.matrix = [None]

    def __str__(self):
        """магический метод" _str_ возвращающий строковое представление матрицы - строку, в которой строки матрицы
        разделены переносом строки, а элементы строки разделены пробелами, необходим для вывода матрицы на печать.
        """
        result = ''
        size = int(len(self.matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i) for i in self.matrix[size * row:size * (row + 1)]]) + '\n'
        return result

    def append(self, element=None):
        """метод append, отвечающий за добавление элемента в матрицу. Увеличивает размер матрицы, если необходимо.
        Правила добавления элементов к матрице:
        - матрица заполняется построчно, слева-направо, с первой строки до последней
        - добавляемый элемент занимает позицию первого свободного "нулевого" элемента
        - добавление "нулевого" элемента (None) игнорируется
        - при достижении максимально допустимого размера матрицы добавляет элементы в матрицу, пока в ней есть "нулевые"
          элементы.
        - Попытка добавить элемент в полностью заполненную матрицу(не имеющей "нулевых" элементов) вызывает исключение
        IndexError
        - в случае, когда добавляемый элемент, занимает место первого элемента в последней строке матрицы,
          матрицу необходимо "расширить", увеличив размер матрицы на 1 (добавить один столбец и одну строку),
          при этом добавленные в матрицу элементы сдвигаются к началу таким образом, чтобы между ними не было
          "нулевых" элементов.
          """
        # если добавляемый элемент - None, возвращаем матрицу
        if element is None:
            return self.matrix

        try:
            # узнаем индекс первого "нулевого" элемента
            idx = self.matrix.index(None)
        except ValueError:
            idx = 1001

        # добавляем элемент
        self.matrix[idx] = element

        # определяем размер матрицы
        size = int(len(self.matrix) ** 0.5)

        # проверяем нужно ли увеличивать размер матрицы
        if idx == size * (size - 1):
            # проверяем не превышел ли максимальный размер матрицы
            if size < self.max_size:
                # увеличиваем размер матрицы
                self.matrix.extend([None, ] * ((size + 1) ** 2 - len(self.matrix)))

    def pop(self):
        """метод pop, возвращает последний добавленный в матрицу элемент. Уменьшает размер матрицы,
           если необходимо. Правила извлечения элементов из матрицы:
           - извлекает и возвращает последний добавленный в матрицу элемент, заменяя его "нулевым" элементом
           - при попытке извлечь элемент из матрицы размером size=1, заполненную "нулевым" элементом,
             выбрасывается исключение IndexError
           - в случае, когда после извлечения элемента, количество добавленных элементов можно разместить
             в матрице меньшего размера, таким образом, что последняя строка полученной матрицы будет содержать
             только пустые элементы, матрицу необходимо "сжать" (уменьшить ее размер на 1) перед тем, как вернуть
             извлекаемое значение
        """
        size = int(len(self.matrix) ** 0.5)

        # узнаем индекс последнего "не нулевого" элемента
        if size == 1 and self.matrix[0] is None:
            idx = 1001
        else:
            for i in self.matrix:
                if i is not None:
                    idx = self.matrix.index(i)

        # проверяем нужно ли уменьшать размер матрицы
        count = (size - 1) ** 2
        temp_matrix = []

        # запоминаем не нулевой элемент
        result = self.matrix[idx]

        # заменяем не нулевой элемент на None
        self.matrix[idx] = None

        for i in range(count):
            temp_matrix.append(self.matrix[i])

        if temp_matrix.count(None) >= size - 1:
            self.matrix = temp_matrix.copy()



        return result

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        """метод класса from_iter, который получает в качестве параметра итерируемый объект.
           Возвращает экземпляр класса Matrix с добавленными в него элементами, полученными из итерируемого
           объекта. Если передан не итерируемый объект метод выбрасывает исключение TypeError.
           """
        p = Matrix(max_size)
        for item in iter_obj:
            p.append(item)

        return p
