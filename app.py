from json_schemes import decision_node_json_schema
from test_trees import easement_tree
from tree_traversal import traverse_tree_json
from utils import TreeNode
from langchain_openai import ChatOpenAI
import dotenv
from flask import Flask, jsonify, request


dotenv.load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0)

the_tree = TreeNode(easement_tree)

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the easement case solver API."


@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.get_json()

    evidence = new_data["evidence"]

    json_return = traverse_tree_json(
            evidence,
            the_tree,
            llm,
            decision_node_json_schema,
    )

    return jsonify(json_return), 201


if __name__ == '__main__':
    app.run(debug=True)
