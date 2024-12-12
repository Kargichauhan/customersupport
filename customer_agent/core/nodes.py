"""Node functions for the customer support workflow graph."""

from termcolor import colored
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from customer_agent.models.state import State


def categorize(state: State) -> State:
    """Categorize the customer query into Technical, Billing, or General."""
    print(colored("Categorizing query...", "blue"))
    
    prompt = ChatPromptTemplate.from_template(
        "Categorize the following customer query into one of these categories: "
        "Technical, Billing, General. Query: {query}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    category = chain.invoke({"query": state["query"]}).content
    
    print(colored(f"Category: {category}", "green"))
    return {"category": category}


def analyze_sentiment(state: State) -> State:
    """Analyze the sentiment of the customer query as Positive, Neutral, or Negative."""
    print(colored("Analyzing sentiment...", "blue"))
    
    prompt = ChatPromptTemplate.from_template(
        "Analyze the sentiment of the following customer query. "
        "Respond with either 'Positive', 'Neutral', or 'Negative'. Query: {query}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    sentiment = chain.invoke({"query": state["query"]}).content
    
    print(colored(f"Sentiment: {sentiment}", "green"))
    return {"sentiment": sentiment}


def handle_technical(state: State) -> State:
    """Provide a technical support response to the query."""
    print(colored("Generating technical response...", "blue"))
    
    prompt = ChatPromptTemplate.from_template(
        "Provide a technical support response to the following query: {query}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    response = chain.invoke({"query": state["query"]}).content
    
    print(colored("Response generated", "green"))
    return {"response": response}


def handle_billing(state: State) -> State:
    """Provide a billing support response to the query."""
    print(colored("Generating billing response...", "blue"))
    
    prompt = ChatPromptTemplate.from_template(
        "Provide a billing support response to the following query: {query}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    response = chain.invoke({"query": state["query"]}).content
    
    print(colored("Response generated", "green"))
    return {"response": response}


def handle_general(state: State) -> State:
    """Provide a general support response to the query."""
    print(colored("Generating general response...", "blue"))
    
    prompt = ChatPromptTemplate.from_template(
        "Provide a general support response to the following query: {query}"
    )
    chain = prompt | ChatOpenAI(temperature=0)
    response = chain.invoke({"query": state["query"]}).content
    
    print(colored("Response generated", "green"))
    return {"response": response}


def escalate(state: State) -> State:
    """Escalate the query to a human agent due to negative sentiment."""
    print(colored("Escalating to human agent...", "yellow"))
    
    return {
        "response": "This query has been escalated to a human agent due to its negative sentiment."
    }


def route_query(state: State) -> str:
    """Route the query based on its sentiment and category."""
    print(colored("Routing query...", "blue"))
    
    if state["sentiment"] == "Negative":
        print(colored("Routing to escalation", "yellow"))
        return "escalate"
    elif state["category"] == "Technical":
        print(colored("Routing to technical support", "green"))
        return "handle_technical"
    elif state["category"] == "Billing":
        print(colored("Routing to billing support", "green"))
        return "handle_billing"
    else:
        print(colored("Routing to general support", "green"))
        return "handle_general" 