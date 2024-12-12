from customer_agent.core.agent import run_customer_support

# Process a sample query
result = run_customer_support("How do I reset my password?")
print(f"Category: {result['category']}")
print(f"Sentiment: {result['sentiment']}")
print(f"Response: {result['response']}")
