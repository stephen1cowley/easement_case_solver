from test_trees import test_tree
from utils import TreeNode
from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()
llm = ChatOpenAI(model="gpt-4o", temperature=0)
