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

# Resto del código (crear el árbol, solicitar nodos al usuario, imprimir el árbol, etc.)
# Crear tu árbol
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



# Agregar más nodos aquí...

# Solicitar al usuario que ingrese dos nodos para buscar el ancestro común
node1 = input("Ingresa el valor del primer nodo: ")
node2 = input("Ingresa el valor del segundo nodo: ")


ancestor = find_lowest_common_ancestor(root, node1, node2)

# Si el ancestro común es uno de los nodos ingresados por el usuario, buscar el ancestro de ese nodo
while ancestor == node1 or ancestor == node2:
    if ancestor == node1:
        other_node = node2
    else:
        other_node = node1

    new_ancestor = find_lowest_common_ancestor(root, ancestor, other_node)

    if new_ancestor == ancestor:
        break  # Evitar bucle infinito si no se encuentra un nuevo ancestro

    ancestor = new_ancestor

if ancestor:
    print(f"El ancestro común de {node1} y {node2} es: {ancestor}")
else:
    print("No se encontró un ancestro común para los nodos proporcionados.")
