from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_template(
    """
    You are a real estate development expert.
    Analyze this project:

    Land Cost: {land_cost}
    Permit Cost: {permit_cost}
    Construction Cost: {construction_cost}
    Sale Price: {sale_price}

    Return a short investor-friendly summary.
    """
)

def get_llm_summary(input):
    chain = prompt | llm
    return chain.invoke(input)