# MERGED_AI_DATASET 

## Overview
This dataset contains Malayalam news articles collected and generated from multiple AI sources, labeled with one of four categories. Each entry includes the article text, a numeric label, and the source model.

## Dataset Columns
| Column | Description |
|--------|-------------|
| `text` | Malayalam news article content (1–6 sentences per entry) |
| `label` | Numeric category of the article: <br>0 → Entertainment <br>1 → Sports <br>2 → Business <br>3 → Technology |
| `model` | Source of the article: one of `deepseek`, `gemini`, `openai`, `sarvam` |

## Basic Info
- Total rows: **4682**
- Columns: `['text', 'label', 'model']`
- Memory usage: ~110 KB  

## Sample Entries
| text | label | model |
|------|-------|-------|
| ഇന്ത്യയിലെ ആദ്യത്തെ സ്പേസ് ടൂറിസം മിഷനായ 'ഗഗന്... | 3 | deepseek |
| കേരളത്തിലെ സ്റ്റാർട്ടപ്പ് മേഖലക്കു ഉണർവേകി ക... | 2 | gemini |
| കേരളത്തിൽ നടക്കുന്ന സംസ്ഥാന യോഗ്യതാ പരീക്ഷയിൽ ... | 1 | openai |
| ലോകമെമ്പാടും സൈബർ ആക്രമണങ്ങൾ വർദ്ധിച്ചുവരുന്ന ... | 3 | gemini |
| ചെറുകിട വ്യവസായങ്ങൾക്കായി കേരള സർക്കാർ സബ്സിഡി... | 2 | sarvam |

## Label Distribution
| Label | Count | Category |
|-------|-------|----------|
| 0 | 1260 | Entertainment |
| 1 | 1122 | Sports |
| 2 | 1179 | Business |
| 3 | 1121 | Technology |


