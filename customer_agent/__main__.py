"""Command line interface for the customer support agent."""

import argparse
from termcolor import colored

from customer_agent.core.agent import run_customer_support
from customer_agent.utils.config import validate_environment


def main():
    """Main entry point for the customer support agent."""
    parser = argparse.ArgumentParser(
        description="Process customer support queries using LangGraph"
    )
    parser.add_argument(
        "query",
        type=str,
        help="The customer query to process",
    )
    
    args = parser.parse_args()
    
    if not validate_environment():
        return
    
    try:
        result = run_customer_support(args.query)
        
        print("\nResults:")
        print(colored(f"Category: {result['category']}", "blue"))
        print(colored(f"Sentiment: {result['sentiment']}", "blue"))
        print(colored(f"Response: {result['response']}", "green"))
        
    except Exception as e:
        print(colored(f"Error: {str(e)}", "red"))
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main()) 