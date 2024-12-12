"""Main agent functionality for the customer support system."""

import os
from typing import Dict

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from termcolor import colored

from customer_agent.core.nodes import (
    categorize,
    analyze_sentiment,
    handle_technical,
    handle_billing,
    handle_general,
    escalate,
    route_query,
)
from customer_agent.models.state import State


def create_workflow() -> StateGraph:
    """Create and configure the workflow graph."""
    print(colored("Creating workflow graph...", "blue"))
    
    # Create the graph
    workflow = StateGraph(State)
    
    # Add nodes
    workflow.add_node("categorize", categorize)
    workflow.add_node("analyze_sentiment", analyze_sentiment)
    workflow.add_node("handle_technical", handle_technical)
    workflow.add_node("handle_billing", handle_billing)
    workflow.add_node("handle_general", handle_general)
    workflow.add_node("escalate", escalate)
    
    # Add edges
    workflow.add_edge("categorize", "analyze_sentiment")
    workflow.add_conditional_edges(
        "analyze_sentiment",
        route_query,
        {
            "handle_technical": "handle_technical",
            "handle_billing": "handle_billing",
            "handle_general": "handle_general",
            "escalate": "escalate",
        },
    )
    workflow.add_edge("handle_technical", END)
    workflow.add_edge("handle_billing", END)
    workflow.add_edge("handle_general", END)
    workflow.add_edge("escalate", END)
    
    # Set entry point
    workflow.set_entry_point("categorize")
    
    print(colored("Workflow graph created", "green"))
    return workflow.compile()


def run_customer_support(query: str) -> Dict[str, str]:
    """Process a customer query through the LangGraph workflow.
    
    Args:
        query (str): The customer's query
        
    Returns:
        Dict[str, str]: A dictionary containing the query's category, sentiment, and response
    """
    try:
        # Load environment variables
        load_dotenv()
        
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError(
                "OPENAI_API_KEY environment variable not found. "
                "Please set it in your .env file."
            )
        
        print(colored(f"\nProcessing query: {query}", "blue"))
        
        # Create workflow if not already created
        app = create_workflow()
        
        # Process query
        results = app.invoke({"query": query})
        
        print(colored("\nProcessing complete!", "green"))
        return {
            "category": results["category"],
            "sentiment": results["sentiment"],
            "response": results["response"],
        }
        
    except Exception as e:
        print(colored(f"\nError processing query: {str(e)}", "red"))
        raise 