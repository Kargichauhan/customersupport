"""Tests for the customer support agent."""

import os
import pytest
from unittest.mock import patch

from customer_agent.core.agent import run_customer_support
from customer_agent.utils.config import validate_environment


def test_validate_environment_missing_key():
    """Test environment validation with missing API key."""
    with patch.dict(os.environ, {}, clear=True):
        assert not validate_environment()


def test_validate_environment_with_key():
    """Test environment validation with API key present."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
        assert validate_environment()


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OPENAI_API_KEY environment variable not set",
)
def test_run_customer_support():
    """Test the customer support workflow with a sample query."""
    query = "What are your business hours?"
    result = run_customer_support(query)
    
    assert isinstance(result, dict)
    assert "category" in result
    assert "sentiment" in result
    assert "response" in result
    assert result["category"] in ["Technical", "Billing", "General"]
    assert result["sentiment"] in ["Positive", "Neutral", "Negative"]
    assert isinstance(result["response"], str)


def test_run_customer_support_no_api_key():
    """Test error handling when API key is missing."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError):
            run_customer_support("Test query") 