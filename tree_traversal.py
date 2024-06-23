from utils import find_node_by_id


def traverse_tree(evidence, the_tree, llm, json_schema):
    """Traverse the entire tree making calls to LLM."""
    while the_tree.conclusion is None:
        options = [answer for answer in the_tree.children]
        structured_llm = llm.with_structured_output(json_schema(options))

        cur_prompt = f"""You are an expert in England and Wales law.
        You are given the following case:

        {evidence}

        And must answer the following question:

        {the_tree.question}
        """

        response = structured_llm.invoke(cur_prompt)

        print(f"question: {the_tree.question}")
        print(f"llm_response: {response['decision']}")
        print(f"llm_reasoning: {response['reasoning']}\n")

        the_tree = the_tree.children[response['decision']]

    print(f"conclusion: {the_tree.conclusion}\n")


def traverse_tree_text(evidence, the_tree, llm, json_schema):
    """Traverse the entire tree making calls to LLM."""
    text = []
    while the_tree.conclusion is None:
        options = [answer for answer in the_tree.children]
        structured_llm = llm.with_structured_output(json_schema(options))

        cur_prompt = f"""You are an expert in England and Wales law.
        You are given the following case:

        {evidence}

        And must answer the following question:

        {the_tree.question}
        """

        response = structured_llm.invoke(cur_prompt)

        text.append(f"question: {the_tree.question}")
        text.append(f"llm_response: {response['decision']}")
        text.append(f"llm_reasoning: {response['reasoning']}\n")

        the_tree = the_tree.children[response['decision']]

    text.append(f"conclusion: {the_tree.conclusion}\n")

    return "\n".join(text)


def traverse_tree_json(evidence, the_tree, llm, json_schema):
    """Traverse the entire tree making calls to LLM."""
    questions = []

    while the_tree.conclusion is None:
        options = [answer for answer in the_tree.children]
        structured_llm = llm.with_structured_output(json_schema(options))

        cur_prompt = f"""You are an expert in England and Wales law.
        You are given the following case:

        {evidence}

        And must answer the following question:

        {the_tree.question}
        """

        response = structured_llm.invoke(cur_prompt)

        questions.append({
            "question": the_tree.question,
            "llm_response": response['decision'],
            "llm_reasoning": response['reasoning'],
        })

        the_tree = the_tree.children[response['decision']]

    final_response = {"questions": questions}
    final_response["conclusion"] = (f"Final conclusion: {the_tree.conclusion}\n")

    return final_response


def answer_onenode_json(evidence, the_tree, llm, json_schema, node_id):
    """Given node id, answer the question."""
    node_in_q = find_node_by_id(the_tree, node_id)

    if node_in_q.conclusion is None:
        options = [answer for answer in node_in_q.children]
        structured_llm = llm.with_structured_output(json_schema(options))

        cur_prompt = f"""You are an expert in England and Wales law.
        You are given the following case:

        {evidence}

        And must answer the following question:

        {the_tree.question}
        """

        response = structured_llm.invoke(cur_prompt)

        question = {
            "question": the_tree.question,
            "llm_response": response['decision'],
            "llm_reasoning": response['reasoning'],
        }
        final_response = question
        final_response["conclusion"] = None
        the_tree = the_tree.children[response['decision']]
    else:
        question = {
            "question": None,
            "llm_response": None,
            "llm_reasoning": None,
        }
        final_response = question
        final_response["conclusion"] = (f"Final conclusion: {the_tree.conclusion}\n")

    return final_response
