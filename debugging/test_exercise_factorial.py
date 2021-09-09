import exercise_factorial
import pytest 

def test_fact():
    assert exercise_factorial.fact(0) == 1

def test_fact_5():
    assert exercise_factorial.fact(5) == 120






