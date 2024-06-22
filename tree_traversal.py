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

        print(f"Question: {the_tree.question}")
        print(f"LLM response: {response['decision']}")
        print(f"LLM reasoning: {response['reasoning']}\n")

        the_tree = the_tree.children[response['decision']]

    print(f"Final conclusion: {the_tree.conclusion}\n")
