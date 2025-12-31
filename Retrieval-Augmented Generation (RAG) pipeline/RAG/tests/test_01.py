import pytest
from rag_generator.rag_generator import rag_test_generator

REQUIREMENTS = {
    "overvoltage_fault": """
    System shall enter FAULT state if DC bus voltage exceeds
    420V continuously for more than 50 ms.
    """,

    "fault_recovery": """
    System shall recover to NORMAL state within 100 ms
    after fault condition is cleared.
    """,

    "undervoltage_warning": """
    System shall raise a WARNING if DC bus voltage
    drops below 300V for more than 100 ms.
    """
}

def test_01():
    rag_test_generator(REQUIREMENTS)