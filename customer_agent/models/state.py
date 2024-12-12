"""State model for the customer support agent."""

from typing import TypedDict


class State(TypedDict):
    """State class to hold query information."""
    
    query: str
    category: str
    sentiment: str
    response: str 