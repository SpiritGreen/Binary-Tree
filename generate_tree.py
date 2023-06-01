import json

import generation_data


class Node:
    # noinspection PyShadowingNames
    def __init__(self, ID, message, phone, datetime):
        self.ID = ID
        self.message = message
        self.phone = phone
        self.datetime = datetime
        self.left = None
        self.right = None


# noinspection PyShadowingNames
def insert(root, ID, message, phone, datetime):
    if root is None:
        return Node(ID, message, phone, datetime)
    elif ID < root.ID:
        root.left = insert(root.left, ID, message, phone, datetime)
    else:
        root.right = insert(root.right, ID, message, phone, datetime)
    return root


data = []
for i in range(32):
    ID = generation_data.ID_lst.pop(0)
    phone = generation_data.phone_lst.pop(0)
    message = generation_data.message_lst.pop(0)
    datetime = generation_data.datetime_lst.pop(0)
    data.append((ID, phone, message, datetime))

root = None
for ID, phone, message, datetime in data:
    root = insert(root, ID, message, phone, datetime)

tree_dict = {}


# noinspection PyShadowingNames
def to_dict(node):
    if not node:
        return None
    d = {
        'ID': node.ID,
        'phone': node.phone,
        'message': node.message,
        'datetime': node.datetime,
    }
    if node.left:
        d['leftID'] = node.left.ID
    if node.right:
        d['rightID'] = node.right.ID
    return d


queue = [root]
while queue:
    node = queue.pop(0)
    tree_dict[node.ID] = to_dict(node)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

with open('tree.json', 'w') as f:
    json.dump(tree_dict, f, ensure_ascii=False)


def print_tree(cur_root):
    # Рекурсивная функция для обхода дерева в глубину и печати узлов.
    def get_depth(cur_node):
        # Рекурсивная функция для определения глубины узла.
        if cur_node is None:
            return 0
        return 1 + max(get_depth(cur_node.left), get_depth(cur_node.right))

    def print_node(cur_node, level):
        # Рекурсивная функция для печати узла с указанием его уровня.
        if cur_node is None:
            return
        print_node(cur_node.right, level + 1)
        print("  " * level + str(cur_node.ID))
        print_node(cur_node.left, level + 1)

    depth = get_depth(cur_root)
    print_node(cur_root, 0)


print_tree(root)
