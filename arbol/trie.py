class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def visualize(self):
        self._visualize_helper(self.root, "")

    def _visualize_helper(self, node, prefix):
        if node.is_end_of_word:
            print(f'[{prefix}]')
        for char, child in node.children.items():
            print(f'[{prefix}]--({char})-->[{prefix + char}]')
            self._visualize_helper(child, prefix + char)

    def find_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_from_node(node, prefix)

    def _find_words_from_node(self, node, current_prefix):
        words = []
        if node.is_end_of_word:
            words.append(current_prefix)
        for char, child in node.children.items():
            if child is not None:
                words.extend(self._find_words_from_node(child, current_prefix + char))
        return words

# Función para agregar una palabra al Trie
def agregar_palabra(trie, palabra):
    trie.insert(palabra)

# Función para buscar una palabra en el Trie
def buscar_palabra(trie, palabra):
    if trie.search(palabra):
        print(f'La palabra "{palabra}" se encuentra en el Trie.')
    else:
        print(f'La palabra "{palabra}" no se encuentra en el Trie.')

# Función para buscar palabras con un prefijo
def buscar_palabras_con_prefijo(trie, prefijo):
    palabras = trie.find_words_with_prefix(prefijo)
    if palabras:
        print(f'Palabras con el prefijo "{prefijo}": {", ".join(palabras)}')
    else:
        print(f'No se encontraron palabras con el prefijo "{prefijo}".')

# Programa principal
trie = Trie()

while True:
    print("\n1. Agregar palabra")
    print("2. Buscar palabra")
    print("3. Buscar palabras con prefijo")
    print("4. Visualizar Trie")
    print("5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        palabra = input("Ingrese la palabra que desea agregar: ")
        agregar_palabra(trie, palabra)

    elif opcion == "2":
        palabra = input("Ingrese la palabra que desea buscar: ")
        buscar_palabra(trie, palabra)

    elif opcion == "3":
        prefijo = input("Ingrese el prefijo para buscar palabras: ")
        buscar_palabras_con_prefijo(trie, prefijo)

    elif opcion == "4":
        print("Árbol Trie (nodo por nodo):")
        trie.visualize()

    elif opcion == "5":
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida.")
