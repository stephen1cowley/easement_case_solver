def decision_node_json_schema(options):
    """The JSON structure of the response of the LLM at each node"""
    options_string = " ".join(options)

    return {
        "title": "decision",
        "description": "Answer to the question following evidence of the case.",
        "type": "object",
        "properties": {
            "decision": {
                "type": "string",
                "description": f"The option out of the possible options: {options_string}."
            },
            "reasoning": {
                "type": "string",
                "description": "The reasoning as to how the decision was made.",
            },
        },
        "required": ["decision", "reasoning"],
    }
