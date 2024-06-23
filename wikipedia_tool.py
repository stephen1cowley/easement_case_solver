from bs4 import BeautifulSoup
from langchain_core.tools import tool
from langgraph.checkpoint import MemorySaver
from langgraph.prebuilt import create_react_agent
import requests
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import HumanMessage


@tool
def get_wikipedia_content(topic):
    """Get the wikipedia page content for a given topic."""
    try:
        url = 'https://en.wikipedia.org/w/api.php' #Wikipedia API URL
        params = {
            'action': 'parse', #Action to be performed on the Wikipedia API, indicating that the request is for parsing content.
            'format': 'json', #Indicating that the response should be in JSON format.
            'page': topic, #Specifies the title of the Wikipedia page for which content is being requested. The value is dynamic and is determined by the topic variable.
            'prop': 'text', #Specifies the properties of the page that should be included in the response.
            'redirects': '' #An empty string indicates that redirects should not be followed, and the response should include information from the original page.
        }

        response = requests.get(url, params=params).json() #Sends an HTTP GET request to the specified URL (url) with the given parameters (params). The requests.get() function is part of the requests library and is used to make HTTP requests. The .json() method is then called on the response to parse it as JSON.
        raw_html = response['parse']['text']['*'] #Extracts the raw HTML content of the Wikipedia page from the JSON response. The JSON structure likely has a nested dictionary, where response['parse'] retrieves the parsed content of the page, and ['text']['*'] accesses the actual HTML content
        soup = BeautifulSoup(raw_html, 'html.parser') #BeautifulSoup object is created to parse and navigate the HTML content. The BeautifulSoup class, from the bs4 (Beautiful Soup) library, provides tools for web scraping by transforming a complex HTML document into a tree of Python objects.

        # Extract text from paragraphs
        paragraphs = soup.find_all('p') #This line uses the find_all method of the BeautifulSoup object (soup) to locate all <p> (paragraph) tags in the HTML content.
        text = ' '.join([p.get_text() for p in paragraphs]) #Creates a list comprehension to iterate through each paragraph (<p> tag) in the ResultSet (paragraphs). For each paragraph, p.get_text() is called to extract the text content inside the paragraph tag. The resulting list of text from all paragraphs is then joined into a single string using the join method with a space ' ' as the separator.

        return text

#If an exception occurs, it prints an error message and returns None. 
    except Exception as e:
        print(f"Topic '{topic}' not found on Wikipedia")
        return None


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

system_message = "You are an agent with access to a Wikipedia tool."
agent_executor = create_react_agent(llm,
                                    tools=[get_wikipedia_content],
                                    checkpointer=MemorySaver(),
                                    messages_modifier=system_message)

config = {"configurable": {"thread_id": "abc12349088543"}}
response = agent_executor.invoke({"messages": [HumanMessage(content="Hi! I'm bob")]}, config=config)
print(response)
print(type(response))

