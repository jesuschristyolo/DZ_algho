class Node:
    def __init__(self, data): #данные которые хранятся в вершине
        self.data = data
        self.left = self.right = None #указатели


class Tree:
    def __init__(self):
        self.root = None

    #рекурсивный метод поиска нужного узла
    def __find(self, node, parent, value):

        #проверка если нода сразу приняла значение None:
        if node is None:
            return None, parent, False

        #если value равен значению в вершине то мы не будем добавлять новую вершину
        if value == node.data:
            return node, parent, True

        #если значение меньше чем в текущем узле, проход по рекурсии по левой ветви
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        #проход по правой ветви
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        # значит мы не нашли вершину
        return node, parent, False

    def append(self, obj): #передаем объект класса Node
        # если в бин дереве нет объектов
        if self.root is None:
            self.root = obj
            # добавление нового объекта
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data) #поиск родительского узла, аргументами буду являться:
        #корень дерева, родительская вершина, данные objecta

        #добавление новой вершины
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        # возвращаем объект который добавили
        return obj

    def show_tree(self, node): #отображение бинарного дерева рекурсией
        if node is None:
            return

        self.show_tree(node.left)
        # отображение значения в вершине
        print(node.data)
        # (если left и right поменять местами то будет убывающая последовательность)
        self.show_tree(node.right)

    def show_wide_tree(self, node): #отображение дерева в ширину
        # Если вершины  отображения не существует  тогда ничего делать не будем
        if node is None:
            return

        v = [node] # список вершин текущего уровня
        # пока в списке что-то есть:
        while v:
            vn = [] # список вершин следующего уровня
            for x in v:
                print(x.data, end=" ") # список вершин текущ уровня

                if x.left: # формирование вершин следующего уровня
                    vn +=[x.left]
                if x.right:
                    vn += [x.right]
            # перенос курсора на следующую строку
            print()

            v = vn # меняем списки местами

    def __del_leaf(self, s, p): #функция удаления вершины s
        #левой вершины:
        if p.left == s:
            p.left = None
        #правой вершины:
        elif p.right == s:
            p.right = None


    def __del_one_child(self, s, p): #удаления последнего 1 потомка у вершины и
        #переопределение потомка на другую вершину

        # если s вершина подцеплена к левой ветви:
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left

        # ситуация когда вершина подцеплена к правой ветви
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left


    def __find_min(self, node, parent):
        # если существует левый потомок
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, key):
        # метод удаления вершины бинарного дерева
        s, p, fl_find = self.__find(self.root, None, key) #поиск удаляемой вершины

        if not fl_find:
            # Если ничего не будет найдено
            return None

        if s.left is None and s.right is None:
            # метод удаления листа (аргументами являются 1 - удаляемая вершина 2 - род вершина удаляемой)
            self.__del_leaf(s, p)

        elif s.left is None or s.right is None:
            # удаления последнего 1 потомка у вершины
            self.__del_one_child(s, p)

        else:
            sr, pr = self.__find_min(s.right, s) #поиск мин значения и родителя в правом поддереве
            # удаляемая вершина:
            s.data = sr.data
            self.__del_one_child(sr, pr) # удаление вершины


v = [1, 2, 3, 4, 5, 6, 7, 8]

t = Tree() # объект дерева
for x in v:
    t.append(Node(x)) # добавление вершины

t.del_node(5) # удаление узла со значением 5
t.show_wide_tree(t.root) # отображение от корня








