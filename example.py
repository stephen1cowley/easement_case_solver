from test_trees import test_tree
from json_schemes import decision_node_json_schema
from tree_traversal import traverse_tree
from utils import TreeNode
from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0)

the_tree = TreeNode(test_tree)

print("-----------------")
print("EXAMPLE CASE 1: HILL V TUPPER")
# https://en.wikipedia.org/wiki/Hill_v_Tupper
evidence = ("The Basingstoke Canal Co gave Hill an exclusive contractual licence in his lease "
"of Aldershot Wharf, Cottage and Boathouse to hire boats out. Hill did so regularly."
" Mr Tupper also occasionally allowed customers to use his boats by his Aldershot Inn"
" to bathe or fish in the canal. Hill wished to stop Tupper from doing so. He sued "
"Tupper, arguing that his lease gave him an exclusive easement and so a direct right"
" to enforce it against third parties (rather than mere licence)."
)

traverse_tree(evidence,
              the_tree,
              llm,
              decision_node_json_schema,
)

print("-----------------")
print("EXAMPLE CASE 2: RE ELLENBOROUGH PARK")
# https://en.wikipedia.org/wiki/Re_Ellenborough_Park
evidence = ("Ellenborough Park is a 7.5-acre (3.0 ha) park in Weston-super-Mare (split by a minor road, not considered by either side, nor the courts consequential).[n 1] The larger park was owned in 1855 by two tenants in common who sold off outlying parts for the building of houses, and granted rights in the purchase/sale deeds to the house owners (and expressly to their successors in title) to enjoy the parkland which remained.[1]"
"The land was enjoyed freely until 1955, when Judge Danckwerts delivered his decision on a complex dispute at first instance. The knub of the case appealed centred on a monetary question affecting the land for the first time. It centred on the fact that the War Office had used the land during World War II, and compensation was due to be paid to the neighbours (if correctly alleging a proprietary interest to use the land, namely an easement) or the landowner, the trustees of the original owner if they were the sole person(s) with an owning interest (under the Compensation Defence Act 1939, section 2 (1)).[n 2]"
"The landowner (of the park), the beneficiaries of the trust of the original owners of the land, challenged the assertion of an 'easement' from the immediate neighbours enjoying the expressed right to use the park in their deeds (title), which they in practice also regularly enjoyed. They stated these neighbouring owner-occupiers (and their tenants) had only a personal advantage (a licence, with no proprietary rights), and not an easement proper (which would include proprietary rights)"
)

traverse_tree(evidence,
              the_tree,
              llm,
              decision_node_json_schema,
)
