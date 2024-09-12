import unittest

from validate_decklist import (get_decklist_length, get_sideboard_length,
                               validate_basic_lands,
                               validate_minimum_deck_size,
                               validate_sideboard_allowed,
                               validate_unique_cards)


class TestDecklistValidation(unittest.TestCase):

    def setUp(self):
        # Setup a sample valid decklist
        self.valid_decklist = {
            "DeckName": "Test Deck",
            "DeckOwner": "John Doe",
            "DeckFormat": "Standard",
            "MainDeck": [
                {"CardName": "Llanowar Elves", "Quantity": 4},
                {"CardName": "Forest", "Quantity": 54},
                {"CardName": "Tarmogoyf", "Quantity": 2}
            ],
            "Sideboard": [
                {"CardName": "Nature's Claim", "Quantity": 3},
                {"CardName": "Pithing Needle", "Quantity": 2}
            ]
        }

        # Invalid decklist (duplicates in MainDeck and Sideboard)
        self.invalid_decklist_duplicate = {
            "DeckName": "Test Deck",
            "DeckOwner": "John Doe",
            "DeckFormat": "Standard",
            "MainDeck": [
                {"CardName": "Llanowar Elves", "Quantity": 4},
                {"CardName": "Forest", "Quantity": 24}
            ],
            "Sideboard": [
                {"CardName": "Llanowar Elves", "Quantity": 1}
            ]
        }

        # Invalid sideboard decklist (too many cards in sideboard)
        self.invalid_sideboard = {
            "DeckName": "Test Deck",
            "DeckOwner": "John Doe",
            "DeckFormat": "Modern",
            "MainDeck": [
                {"CardName": "Llanowar Elves", "Quantity": 4},
                {"CardName": "Forest", "Quantity": 24}
            ],
            "Sideboard": [
                {"CardName": "Nature's Claim", "Quantity": 16}
            ]
        }

        # Decklist with non-basic lands exceeding the limit
        self.invalid_non_basic_land = {
            "DeckName": "Test Deck",
            "DeckOwner": "John Doe",
            "DeckFormat": "Standard",
            "MainDeck": [
                {"CardName": "Non-basic Land", "Quantity": 5},
                {"CardName": "Forest", "Quantity": 24}
            ]
        }

    def test_minimum_deck_size(self):
        # Test with a valid deck
        self.assertTrue(validate_minimum_deck_size(self.valid_decklist))

        # Test with an invalid small deck
        small_deck = {
            "DeckName": "Test Deck",
            "DeckOwner": "John Doe",
            "DeckFormat": "Standard",
            "MainDeck": [
                {"CardName": "Llanowar Elves", "Quantity": 4},
                {"CardName": "Forest", "Quantity": 4}
            ]
        }
        self.assertFalse(validate_minimum_deck_size(small_deck))

    def test_unique_cards(self):
        # Test a valid deck with no duplicates
        self.assertTrue(validate_unique_cards(self.valid_decklist))

        # Test a deck with duplicates across MainDeck and Sideboard
        self.assertFalse(validate_unique_cards(self.invalid_decklist_duplicate))

    def test_sideboard_allowed(self):
        # Test valid formats with sideboards
        self.assertTrue(validate_sideboard_allowed(self.valid_decklist))

        # Test Commander format which does not allow sideboards
        commander_deck = {
            "DeckName": "Commander Deck",
            "DeckOwner": "John Doe",
            "DeckFormat": "Commander",
            "MainDeck": [
                {"CardName": "Llanowar Elves", "Quantity": 1},
                {"CardName": "Forest", "Quantity": 99}
            ],
            "Sideboard": [
                {"CardName": "Nature's Claim", "Quantity": 1}
            ]
        }
        self.assertFalse(validate_sideboard_allowed(commander_deck))

    def test_basic_lands(self):
        # Test valid deck with basic lands
        self.assertTrue(validate_basic_lands(self.valid_decklist))

        # Test invalid deck with non-basic land exceeding the limit
        self.assertFalse(validate_basic_lands(self.invalid_non_basic_land))

    def test_get_decklist_length(self):
        # Check that the valid decklist has the correct number of cards
        self.assertEqual(get_decklist_length(self.valid_decklist), 60)

    def test_get_sideboard_length(self):
        # Check that the valid decklist has the correct sideboard length
        self.assertEqual(get_sideboard_length(self.valid_decklist), 5)

    def test_sideboard_limit(self):
        # Test valid sideboard (no more than 15 cards)
        self.assertTrue(validate_sideboard_allowed(self.valid_decklist))

        # Test sideboard with too many cards
        self.assertFalse(validate_sideboard_allowed(self.invalid_sideboard))


if __name__ == '__main__':
    unittest.main()
