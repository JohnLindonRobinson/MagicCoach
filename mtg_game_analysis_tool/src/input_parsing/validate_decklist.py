import json

import jsonschema
from jsonschema import validate


def validate_minimum_deck_size(decklist):
    """
    Validate that the decklist has at least the minimum number of cards required
    for the format.

    :param decklist: decklist to validate
    :return: True if the decklist has at least the minimum number of cards , False otherwise
    """
    format_minimums = {
        "Standard": 60,
        "Modern": 60,
        "Commander": 100
    }
    min_size = format_minimums.get(decklist['DeckFormat'], 60)
    if get_decklist_length(decklist) < min_size:
        print(f"Decklist must have at least {min_size} cards for {decklist['DeckFormat']} format.")
        return False
    return True


def validate_unique_cards(decklist):
    """
    Validate that each card in the decklist appears at most once across MainDeck and Sideboard.

    :param decklist: decklist to validate
    :return: True if each card appears at most once, False otherwise
    """
    seen = set()
    for card in decklist['MainDeck']:
        if card['CardName'] in seen:
            print(f"Card {card['CardName']} appears more than once in the MainDeck.")
            return False
        seen.add(card['CardName'])

    for card in decklist.get('Sideboard', []):
        if card['CardName'] in seen:
            print(f"Card {card['CardName']} appears more than once across MainDeck and Sideboard.")
            return False
        seen.add(card['CardName'])
    return True

def validate_sideboard_allowed(decklist):
    """
    Validate that the sideboard exists only in formats that allow it and has no more than 15 cards.

    :param decklist: decklist to validate
    :return: True if sideboard is allowed for the format and has no more than 15 cards, False otherwise
    """
    formats_with_sideboards = ["Standard", "Modern", "Legacy"]
    
    # Check if sideboard is allowed for the format
    if 'Sideboard' in decklist and decklist['DeckFormat'] not in formats_with_sideboards:
        print(f"Sideboards are not allowed in {decklist['DeckFormat']} format.")
        return False
    
    # Check if sideboard has at most 15 cards
    if get_sideboard_length(decklist) > 15:
        print(f"Sideboard must have at most 15 cards. Current sideboard has {get_sideboard_length(decklist)} cards.")
        return False

    return True


def validate_basic_lands(decklist):
    """
    Validate that only basic lands can have more than 4 copies in the MainDeck.

    :param decklist: decklist to validate
    :return: True if no non-basic land exceeds 4 copies, False otherwise
    """
    basic_lands = ["Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"]
    for card in decklist['MainDeck']:
        if card['Quantity'] > 4 and card['CardName'] not in basic_lands:
            print(f"Non-basic land {card['CardName']} has more than 4 copies.")
            return False
    return True


def get_decklist_length(decklist):
    """
    Get the number of cards in a decklist.

    :param decklist: decklist to get the length of
    :return: number of cards in the decklist
    """
    return sum(card["Quantity"] for card in decklist['MainDeck'])


def get_sideboard_length(decklist):
    """
    Get the number of cards in the sideboard.

    :param decklist: decklist to get the length of
    :return: number of cards in the sideboard
    """
    return sum(card["Quantity"] for card in decklist.get('Sideboard', []))


def validate_card_legality(decklist):
    """
    Stub function for card legality validation (can be implemented using an external service).

    :param decklist: decklist to validate
    :return: True if all cards are legal in the format, False otherwise
    """
    # In a full implementation, you would check the legality of each card using an API.
    return True


def validate_commander_rules(decklist):
    """
    Stub function for validating Commander-specific rules (such as singleton rules).

    :param decklist: decklist to validate
    :return: True if the deck follows Commander rules, False otherwise
    """
    # Placeholder for future Commander-specific validation logic.
    return True


def validate_decklist(decklist):
    """
    Validate the decklist against multiple rules and constraints.

    :param decklist: decklist to validate
    :return: True if the decklist is valid, False otherwise
    """
    # Load schema
    try:
        with open('decklist_schema.json') as f:
            schema = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False

    # Validate decklist schema
    try:
        validate(decklist, schema)
    except jsonschema.exceptions.ValidationError as e:
        print("Decklist is invalid: ")
        print(e)
        return False

    # Initialise issue flag
    issue = True

    # Validate deck size (at least 60 cards for most formats)
    if not validate_minimum_deck_size(decklist):
        issue = False

    # Validate no more than 15 cards in sideboard
    if get_sideboard_length(decklist) > 15:
        # print(f"Sideboard must have at most 15 cards.")
        issue = False

    # Validate at most 4 copies of each non-basic card
    if not validate_basic_lands(decklist):
        issue = False

    # Validate card format legality
    if not validate_card_legality(decklist):
        issue = False

    # Ensure Commander rules are followed, if applicable
    if not validate_commander_rules(decklist):
        issue = False

    # Ensure there are no duplicate cards in MainDeck and Sideboard
    if not validate_unique_cards(decklist):
        issue = False

    return issue


if __name__ == "__main__":
    # Load the JSON file
    try:
        with open("example_decklist.json") as file:
            decklist_json = json.load(file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)

    # Validate the decklist
    if validate_decklist(decklist_json):
        print("Decklist passed validation.")
    else:
        print("Decklist failed validation.")
