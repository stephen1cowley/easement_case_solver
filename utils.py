class TreeNode:
    """Data structure for holding decision tree"""
    def __init__(self, decision_tree):
        self.children = {"yes": None, "no": None}
        self.id = None

        if isinstance(decision_tree, str):
            self.question = None
            self.conclusion = decision_tree

        else:
            self.question = decision_tree['question']
            self.conclusion = None

            keys = [answer for answer in decision_tree]

            for answer in keys[1:]:
                self.children[answer] = TreeNode(decision_tree[answer])


def assign_ids(node, current_id=1):
    if node is None:
        return current_id

    # Traverse the left subtree
    current_id = assign_ids(node.children["yes"], current_id)

    # Assign the current ID to the node
    node.id = current_id
    current_id += 1

    # Traverse the right subtree
    current_id = assign_ids(node.children["no"], current_id)

    return current_id


def find_node_by_id(node, target_id):
    if node is None:
        return None

    # Check if the current node's ID matches the target ID
    if node.id == target_id:
        return node

    # Traverse the left subtree
    left_result = find_node_by_id(node.children["yes"], target_id)
    if left_result is not None:
        return left_result

    # Traverse the right subtree
    right_result = find_node_by_id(node.children["no"], target_id)
    return right_result
