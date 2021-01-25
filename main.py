import pytest


# Source Code:

def from_roman(roman: str) -> int:
  return 1


def from_roman2(roman: str) -> int:
  """Converts a string representing a roman numberal into its Arabic numeral integer equivalent"""

  numeral_lookup = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  rev_roman = roman[::-1]

  number = 0
  last_number = 0

  for roman_number in rev_roman:
    current_number = numeral_lookup[roman_number]

    if current_number >= last_number:
      number += current_number
    else:
      number -= current_number

    last_number = current_number

  return number

# Tests: 

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
  ('IV', 4),
  ('V', 5),
  ('VI', 6),
  ('VII', 7),
  ('VIII', 8),
  ('IX', 9),
  ('X', 10),
  ('XII', 12),
  ('LXXIX', 79),
  ('MDXII', 1512),
  ('MCMXCIV', 1994),
  ('MMXXI', 2021)
]

@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman(num: int, roman: str):
  assert from_roman2(num) == roman