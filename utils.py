class TreeNode:
    """Data structure for holding decision tree"""
    def __init__(self, decision_tree):
        self.children = {}

        if isinstance(decision_tree, str):
            self.question = None
            self.conclusion = decision_tree

        else:
            self.question = decision_tree['question']
            self.conclusion = None

            keys = [answer for answer in decision_tree]

            for answer in keys[1:]:
                self.children[answer] = TreeNode(decision_tree[answer])
