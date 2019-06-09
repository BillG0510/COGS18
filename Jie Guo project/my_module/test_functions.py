"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from .functions import generate_range, start_game, calculate
import collections


##
##

def test_generate_range():
	target = generate_range(2, 5)
	assert target >= 2
	assert target <= 5

def test_start_game():
	assert callable(start_game)

def test_calculate():
	assert callable(calculate)