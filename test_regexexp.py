import pytest
from regexexp import extract_birthday, extract_address, extract_name


@pytest.fixture
def test_cases():
    return [
        ("Mon anniversaire est le 15 août 1990", "1990-08-15"),
        ("Je suis né le 1er janvier 2000", "2000-01-01"),
        ("Mon anniversaire est le 1er décembre 1970", "1970-12-01"),
        ("Je suis né le 29 février 2004", "2004-02-29"),
        ("Mon anniversaire est le 31 septembre", None)
    ]

def test_extract_birthday(test_cases):
    for text, expected in test_cases:
        assert extract_birthday(text) == expected


def test_extract_address():

    # test case 1
    text = "Il a vécu à 5 rue de Police"
    expected_address = "5 rue de Police"
    assert extract_address(text) == expected_address

    # test case 2
    text = "Elle a habité au 5 rue de la Paix."
    expected_address = "5 rue de la Paix"
    assert extract_address(text) == expected_address

    # test case 3
    text = "Le magasin est situé au bout de la rue principale."
    expected_address = "bout de la rue principale"
    assert extract_address(text) == expected_address






def test_extract_name():
    extract_name("Mlle Sophie-Anne Dupont") == "Mlle Sophie-Anne Dupont"
    assert extract_name("M. Jean Dupont est un homme très gentil.") == "M. Jean Dupont"
    assert extract_name("M. Dupont est gentil.") == "M. Dupont"
    assert extract_name("Mme Dupont est gentille.") == "Mme. Dupont"
    assert extract_name("Mlle Dupont est gentille.") == "Mlle. Dupont"
    