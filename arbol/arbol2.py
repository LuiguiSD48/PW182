class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_descendant(node, target):
    if node is None:
        return False

    if node.value == target:
        return True

    return is_descendant(node.left, target) or is_descendant(node.right, target)

def find_lowest_common_ancestor(node, node1, node2):
    if node is None:
        return None

    # Verificar si node1 o node2 son descendientes del nodo actual
    is_node1_descendant = is_descendant(node, node1)
    is_node2_descendant = is_descendant(node, node2)

    # Si uno de los nodos es igual al nodo actual y el otro es un descendiente, este es el ancestro común.
    if (node.value == node1 and is_node2_descendant) or (node.value == node2 and is_node1_descendant):
        return node.value

    # Busca en los subárboles izquierdo y derecho.
    left_ancestor = find_lowest_common_ancestor(node.left, node1, node2)
    right_ancestor = find_lowest_common_ancestor(node.right, node1, node2)

    # Si se encuentra en ambos subárboles, el nodo actual es el ancestro común.
    if left_ancestor and right_ancestor:
        return node.value

    # Si solo se encuentra en un subárbol, se devuelve ese valor.
    if left_ancestor:
        return left_ancestor
    if right_ancestor:
        return right_ancestor

    return None  # Si no se encuentra ningún ancestro común

# Función para crear un árbol de prueba (código omitido)

# Solicitar al usuario el número de nodos
num_nodes = int(input("Ingresa el número de nodos de los cuales deseas encontrar el ancestro común: "))

# Crear una lista para almacenar los valores de los nodos
node_values = []

# Pedir al usuario que ingrese los valores de los nodos
for i in range(num_nodes):
    node_value = input(f"Ingrese el valor del nodo {i + 1}: ")
    node_values.append(node_value)

# Crear el árbol y los nodos a partir de los valores ingresados
# ...
root = TreeNode("Xavier")

root.left = TreeNode("EmilioI")
root.right = TreeNode("XavierII")

root.left.left = TreeNode("Harry")
root.left.right = TreeNode("Juan")
root.right.left = TreeNode("Pablo")
root.right.right = TreeNode("Alan")

root.left.left.left = TreeNode("Carlos")
root.left.left.right = TreeNode("Patricio")
root.left.right.left = TreeNode("Carla")
root.left.right.right = TreeNode("Carlota")
root.right.left.left = TreeNode("Domingo")
root.right.left.right = TreeNode("Anastacio")
root.right.right.left = TreeNode("Jorge")
root.right.right.right= TreeNode("Rodrigo")

root.left.left.left.left = TreeNode("CarlosII")
root.left.left.left.right = TreeNode("Carmen")
root.left.left.right.left = TreeNode("Gepeto")
root.left.left.right.right = TreeNode("Victor")
root.left.right.right.right = TreeNode("Guadalupe")
root.right.left.right.right = TreeNode("Petra")
root.right.right.left.left = TreeNode("Adrian")
root.right.right.right.left = TreeNode("Cesaria")
root.right.right.right.right = TreeNode("Helena")

root.left.left.left.left.left = TreeNode("CarlosIII")
root.left.left.left.right.left = TreeNode("Karol")
root.left.left.left.right.right = TreeNode("Carola")
root.left.right.right.right.left = TreeNode("Lucero")
root.left.right.right.right.right = TreeNode("Andres")
root.right.right.left.left.left = TreeNode("Fernando")
root.right.right.left.left.right = TreeNode("Ricardo")
root.right.right.right.right.left = TreeNode("Misael")
root.right.right.right.right.right = TreeNode("Claudia")

root.left.right.right.right.left.left = TreeNode("Larry")
root.right.right.right.right.left.left = TreeNode("Kebin")
root.right.right.right.right.right.left = TreeNode("Santiago")
root.right.right.right.right.right.right = TreeNode("Britany")

# Solicitar al usuario que ingrese los valores de los nodos de los cuales desea encontrar el ancestro común
node1 = input("Ingresa el valor del primer nodo: ")
node2 = input("Ingresa el valor del segundo nodo: ")

# Encontrar el ancestro común (código omitido)

if ancestor:
    print(f"El ancestro común de {node1} y {node2} es: {ancestor}")
else:
    print("No se encontró un ancestro común para los nodos proporcionados.")
