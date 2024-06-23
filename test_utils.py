from test_trees import binary_easement_tree
from utils import TreeNode, assign_ids, find_node_by_id

the_tree = TreeNode(binary_easement_tree)
assign_ids(the_tree)

print(the_tree)

next_node = find_node_by_id(the_tree, 6)

print(next_node.question, next_node.conclusion)
