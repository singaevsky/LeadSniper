# Russian Companies Using CAT Systems

This project collects data about Russian companies that use CAT (Computer-Assisted Translation) systems and have revenue of at least 100 million rubles.

## Sources
- list-org.com for company data including revenue and website
- Company websites for CAT system usage verification

## CAT System Keywords
- "CAT", "Translation Memory", "TMS", "локализация", "память переводов", "терминологическая база", "переводческий", "переводов", "SDL Trados", "MemoQ", "Smartcat", "Memsource", "Wordfast", "OmegaT", "XTM", "Lokalise", "Crowdin", "Transifex", "Phrase", "Smartling", "переводческие технологии", "программное обеспечение для перевода"

## Requirements
- Python 3.8+
- Dependencies listed in requirements.txt

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python src/main.py
```

## Output
The script will create:
- `data/all_companies.csv` - All companies collected from the source
- `data/companies.csv` - Companies that meet the criteria (revenue >= 100M + CAT system usage)

## OKVED Codes Used
- 63.11 - Data processing activities
- 62.01 - Software development
- 58.29 - Publishing of other software products
- 74.30 - Translation activities

## Limitations
- Data may be incomplete due to website availability
- Some companies may use CAT systems but not mention them on their websites
- Parsing may be slow due to rate limiting
- Website structures may change, breaking the parser