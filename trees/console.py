from trees.general_tree import GeneralTree
from trees.binary_tree import BinaryTree
from trees.binary_search_tree import BinarySearchTree


def test_general_tree():
    t = GeneralTree('A')
    t.add_child('A', 'B')
    t.add_child('A', 'C')
    t.add_child('A', 'D')
    t.add_child('B', 'E')
    t.add_child('B', 'F')
    t.add_child('C', 'G')
    t.add_child('E', 'H')
    print("Buscar el elemento H:", t.search('H'))
    print("Preorden", t.preorder())
    p = []
    print("Postorden", t.postorder(p))
    inorder = []
    print("Entreorden", t.inorder(inorder))
    print("A lo ancho: ", t.bfs())


def test_binary_tree():
    bt = BinaryTree()
    bt.add_child(None, 'A')
    print(bt.add_child('A', 'B'))
    print(bt.add_child('A', 'C'))
    print(bt.add_child('B', 'D'))
    print(bt.add_child('B', 'E'))
    print(bt.add_child('D', 'H'))
    print(bt.add_child('E', 'I'))
    print(bt.add_child('E', 'J'))
    print(bt.add_child('C', 'F'))
    print(bt.add_child('C', 'G'))
    print("Recorrido en preorden: ", bt.preorder())
    print("Recorrido en postorden: ", bt.postorder())
    print("Recorrido en entreorden: ", bt.inorder())
    print("Recorrido a lo ancho:", bt.bfs())


def test_binary_search_tree():
    bst = BinarySearchTree()
    print(bst.add(5))
    print(bst.add(2))
    print(bst.add(9))
    print(bst.add(4))
    print(bst.add(6))
    print(bst.add(3))
    print(bst.add(7))
    print(bst.add(10))
    print(bst.add(8))
    print("Recorrido en preorden: ", bst.preorder())
    print("Recorrido en entreorden: ", bst.inorder())
    print("Recorrido en postorden: ", bst.postorder())
    print("Recorrido bfs: ", bst.bfs())
    print("Minimo elemento del arbol", bst.search_min())
    bst.delete(2)
    print("Recorrido en preorden: ", bst.preorder())
    print("Buscar 7", bst.search(7).root)


def exp_tree():
    exp = BinaryTree('+')
    exp.add_child('+', '*')
    exp.add_child('+', 'e')
    exp.add_child('*', 'c')
    exp.add_child('*', '+')
    exp.add_child('+', 'd')
    exp.add_child('+', 'g')
    print("Recorrido en preorden", exp.preorder())



if __name__ == '__main__':
    # test_general_tree()
    # test_binary_tree()
    # test_binary_search_tree()
    exp_tree()
