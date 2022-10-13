"""
This module encapsulates details about character type.
"""

WIZARD = 'Wizard'
WARRIOR = 'Warrior'
MAGE = 'Mage'

CHAR_TYPES = {WIZARD: {'health': 7, 'magic': 10},
              WARRIOR: {'health': 9, 'strength': 9},
              MAGE: {'health': 6}, }


def get_char_types():
    """
    Returns a list of character types.
    """
    return list(CHAR_TYPES.keys())


def get_char_type_details(char_type):
    return CHAR_TYPES.get(char_type, None)


def main():
    char_types = get_char_types()
    print(char_types)


if __name__ == '__main__':
    main()
