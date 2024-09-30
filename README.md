# Easement Case Solver Backend
## Description
Solves England/Wales legal cases by using RAG to create a binary decision tree.

The tree is then used to query an LLM which provides answers to each question and hence provide a conclusion to the given scenario.

For the frontend, see [Woody Lam's code](https://github.com/woody-lam-cwl/binary-tree-frontend).

## Installation

Create a .env file with the following contents:

```
LANGCHAIN_API_KEY = "xxxx"
OPENAI_API_KEY = "xxxx"
LANGCHAIN_TRACING_V2 = "true"
TAVILY_API_KEY = "xxxx"
```
Then run `app.py`.
