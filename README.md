# Magic: The Gathering (MTG) Game Analysis Tool

## Overview
This project aims to create an AI-powered analysis tool for **Magic: The Gathering (MTG)** games. The tool will analyze game states provided in **JSON format** and suggest optimal moves, much like chess engines do for chess games. The analysis will be based on known decklists for both players.

The tool is designed to provide insight into the current game state, suggest potential plays, and evaluate their impact on the game.

## Features
- Parse and validate JSON-formatted **game states** and **decklists**.
- Analyze game states and provide **legal move suggestions** based on the current board and cards in hand.
- Offer **evaluations of potential moves** with a ranking system.
- Potential for **AI-powered analysis** to improve move suggestions over time.

## Getting Started

### Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Git** (for version control)

### Setting Up the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/mtg-game-analysis-tool.git
   cd mtg-game-analysis-tool
    ```
2. **Set Up a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install the Required Packages:**
   ```bash
    pip install -r requirements.txt
    ```
4. **Run the Project:**
   ```bash
   python main.py
   ```

## Project Structure
```
├── mtg_game_analysis_tool/
│   ├── __init__.py                    
│   ├── game_state_parser.py              # Module for parsing JSON-formatted game state data
│   ├── decklist_parser.py                # Module for parsing decklists
│   ├── move_suggestion.py                # Core logic for analyzing game states and suggesting moves
│   └── tests/
│       └── test_game_state_parser.py     # Unit tests for game state parser
├── .gitignore
├── README.md
└── requirements.txt
```

## Usage
Input JSON game state and decklist files will be passed to the core engine, which will analyze the current state and output potential moves and an evaluation of those moves.
To run the game state analyzer (after implementation):
```bash
python mtg_game_analysis_tool/main.py --game-state game_state.json --decklist1 deck1.json --decklist2 deck2.json
```

## Contributing

We welcome contributions! Here's how you can get started:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and add tests for your feature.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new pull request.

## License
This project is licensed under the GPL-2.0 License - see the [LICENSE](LICENSE) file for details.

## Future Plans
- Integrate AI-based move evaluation using machine learning.
- Add support for multiplayer game analysis.
- Develop a web-based UI or API for easier interaction.

## Contact
For questions or feedback, please feel free to reach out to me at [john@johnlindon.com](mailto:john@johnlindon.com).