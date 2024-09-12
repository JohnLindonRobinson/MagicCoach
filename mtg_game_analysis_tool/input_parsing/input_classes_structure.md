## Decklist Class

The `Decklist` class represents a player's decklist and contains the main deck and sideboard cards. It has the following attributes:

- `main_deck`: A list of cards representing the main deck.
- `sideboard`: A list of cards representing the sideboard.

The `Decklist` class has the following methods:

- `validate_decklist()`: Validates the decklist, ensuring that it follows the rules of Magic: The Gathering (e.g., correct card names, legal number of cards).
- `is_card_in_deck(card_name)`: Checks if a card is present in the decklist.
- `get_decklist()`: Returns the decklist as a dictionary.
- `add_card_to_main_deck(card)`: Adds a card to the main deck.
- `add_card_to_sideboard(card)`: Adds a card to the sideboard.
- `remove_card_from_main_deck(card)`: Removes a card from the main deck.
- `remove_card_from_sideboard(card)`: Removes a card from the sideboard.

## Card Class

The `Card` class represents a single card and has the following attributes:

- `name`: The name of the card.
- `scryfall_id`: The Scryfall ID of the card (for fetching additional card information).
- `mana_cost`: The mana cost of the card.
- `type_line`: The type of the card (e.g., creature, instant, sorcery).
- `oracle_text`: The rules text of the card.
- `power`: The power of the card (if applicable).
- `toughness`: The toughness of the card (if applicable).
- `loyalty`: The loyalty of the card (if applicable).
- `colors`: The colors of the card.
- `zone`: The current zone of the card (e.g., hand, battlefield, graveyard).
- `owner`: The player who owns the card.
- And other relevant attributes.

The `Card` class has methods to interact with the card, such as casting the card, activating abilities, and moving the card between zones:

- `cast()`: Casts the card from the hand.
- `activate_ability()`: Activates an ability of the card.
- `move_to_zone(zone)`: Moves the card to a specified zone (e.g., battlefield, graveyard).
- `get_card_info()`: Returns the card information as a dictionary.
- `get_card_name()`: Returns the name of the card.
- `get_mana_cost()`: Returns the mana cost of the card.
- `get_type_line()`: Returns the type of the card.
- `get_oracle_text()`: Returns the rules text of the card.
- `get_power()`: Returns the power of the card.
- `get_toughness()`: Returns the toughness of the card.
- `get_loyalty()`: Returns the loyalty of the card.
- `get_colors()`: Returns the colors of the card.
- `get_zone()`: Returns the current zone of the card.
- `get_owner()`: Returns the player who owns the card.
- And other relevant methods.