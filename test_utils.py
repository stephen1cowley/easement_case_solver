from test_trees import binary_easement_tree
from utils import TreeNode, assign_ids

the_tree = TreeNode(binary_easement_tree)
assign_ids(the_tree)

print(the_tree)
