# Customer Support Agent

An intelligent customer support agent built using LangGraph that can categorize queries, analyze sentiment, and provide appropriate responses.

## Overview

This project demonstrates how to create an intelligent customer support agent using LangGraph. The agent can:
- Categorize customer queries (Technical, Billing, General)
- Analyze sentiment (Positive, Neutral, Negative)
- Provide appropriate responses
- Escalate issues when necessary

## Key Components

1. State Management using TypedDict
2. Query Categorization
3. Sentiment Analysis
4. Response Generation
5. Escalation Mechanism
6. Workflow Graph using LangGraph

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -e .
```

3. Set up environment variables:
Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

```python
from customer_agent.core.agent import run_customer_support

# Process a query
result = run_customer_support("How do I reset my password?")
print(f"Category: {result['category']}")
print(f"Sentiment: {result['sentiment']}")
print(f"Response: {result['response']}")
```

## Project Structure

```
customer_support_workflow/
├── README.md
├── requirements.txt
├── main.py                # Entry point for the application
├── config.py              # Configuration settings
├── workflow/
│   ├── __init__.py        # Initialization for workflow package
│   ├── workflow_manager.py  # Core logic for workflow management
│   ├── data_loader.py     # Data handling logic
│   ├── visualization.py   # Workflow visualization logic
├── tests/
│   ├── __init__.py        # Initialization for test package
│   ├── test_workflow_manager.py  # Unit tests for workflow manager
│   ├── test_visualization.py     # Unit tests for visualization
├── docs/
│   ├── project_overview.md # High-level documentation
│   ├── api_reference.md   # API reference
│   ├── installation_guide.md # Installation and setup guide
└── logs/
    └── app.log            # Log file for debugging

```

## Development

To set up the development environment:

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run tests:
```bash
pytest
```

## License

MIT License 
