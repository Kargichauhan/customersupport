"""Configuration utilities for the customer support agent."""

import os
from typing import Optional

from termcolor import colored


def get_api_key() -> Optional[str]:
    """Get the OpenAI API key from environment variables.
    
    Returns:
        Optional[str]: The API key if found, None otherwise
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(
            colored(
                "Warning: OPENAI_API_KEY not found in environment variables",
                "yellow",
            )
        )
    return api_key


def validate_environment() -> bool:
    """Validate that all required environment variables are set.
    
    Returns:
        bool: True if all required variables are set, False otherwise
    """
    required_vars = ["OPENAI_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(
            colored(
                f"Error: Missing required environment variables: {', '.join(missing_vars)}",
                "red",
            )
        )
        return False
    return True 