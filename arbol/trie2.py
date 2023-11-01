# Clase que define un nodo del Trie
class TrieNode:
    def __init__(self):
        # Un diccionario que mapea caracteres a nodos hijos
        self.children = {}
        # Indicador para marcar si este nodo es el final de una palabra
        self.is_end_of_word = False

# Clase que define la estructura del Trie
class Trie:
    def __init__(self):
        # Inicializa el Trie con un nodo raíz vacío
        self.root = TrieNode()

    # Método para insertar una palabra en el Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                # Si el carácter no existe como hijo, crea un nuevo nodo para él
                node.children[char] = TrieNode()
            node = node.children[char]
        # Marca el último nodo como el final de una palabra
        node.is_end_of_word = True

    # Método para buscar una palabra en el Trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                # Si un carácter no se encuentra, la palabra no está en el Trie
                return False
            node = node.children[char]
        # La palabra se encuentra si el último nodo está marcado como el final de una palabra
        return node.is_end_of_word

    # Método para visualizar el Trie
    def visualize(self):
        self._visualize_helper(self.root, "")

    # Función auxiliar para visualizar el Trie recursivamente
    def _visualize_helper(self, node, prefix):
        if node.is_end_of_word:
            print(f'[{prefix}]')
        for char, child in node.children.items():
            print(f'[{prefix}]--({char})-->[{prefix + char}]')
            self._visualize_helper(child, prefix + char)

    # Método para encontrar palabras con un prefijo específico
    def find_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                # Si el prefijo no se encuentra, no hay palabras que coincidan
                return []
            node = node.children[char]
        return self._find_words_from_node(node, prefix)

    # Función auxiliar para encontrar palabras con un prefijo desde un nodo específico
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
