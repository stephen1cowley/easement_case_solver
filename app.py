from json_schemes import decision_node_json_schema
from test_trees import binary_easement_tree, all_trees
from tree_traversal import traverse_tree_json, answer_onenode_json
from utils import TreeNode, assign_ids, find_node_by_id
from langchain_openai import ChatOpenAI
import dotenv
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import os
import time


dotenv.load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0)

the_tree = TreeNode(binary_easement_tree)
assign_ids(the_tree)

app = Flask(__name__)


@app.route('/')
@cross_origin(origin='*')
def home():
    return "Welcome to the easement case solver API."


@app.route('/api/data', methods=['POST'])
@cross_origin(origin='*')
def post_data():
    new_data = request.get_json()
    password = new_data["password"]
    if password == os.environ.get('MY_API_PASSWORD'):
        new_data = request.get_json()

        evidence = new_data["evidence"]

        json_return = traverse_tree_json(
                evidence,
                the_tree,
                llm,
                decision_node_json_schema,
        )
        return jsonify(json_return), 201
    else:
        time.sleep(1)
        return "Incorrect password", 201


@app.route('/api/getNext', methods=['POST'])
@cross_origin(origin='*')
def post_get_next_data():
    new_data = request.get_json()
    q_id = new_data["q_id"]
    des_resp = new_data["decision"]

    node_in_q = find_node_by_id(the_tree, q_id)
    next_node = node_in_q.children[des_resp]
    json_return = {"next_question": next_node.question,
                   "next_conclusion": next_node.conclusion,
                   "next_id": next_node.id
    }

    return jsonify(json_return), 201


@app.route('/api/answer', methods=['POST'])
@cross_origin(origin='*')
def post_get_answer():
    new_data = request.get_json()
    q_id = new_data["q_id"]
    evidence = new_data["evidence"]
    node_in_q = find_node_by_id(the_tree, q_id)

    json_return = answer_onenode_json(evidence,
                        node_in_q,
                        llm,
                        json_schema=decision_node_json_schema,
                        node_id=q_id
    )

    return jsonify(json_return), 201


@app.route('/api/start', methods=['GET'])
@cross_origin(origin='*')
def get_root_node():
    id = the_tree.id
    json_return = {
        "id": id
    }
    return jsonify(json_return), 201


@app.route('/api/tree', methods=['POST'])
@cross_origin(origin='*')
def get_tree():
    new_data = request.get_json()
    tree_id = new_data["tree_id"]
    json_return = all_trees[tree_id]
    return jsonify(json_return), 201


if __name__ == '__main__':
    app.run(debug=True)
