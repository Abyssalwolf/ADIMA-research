# Combined Malayalam News Dataset

## Description
This dataset is a combination of two Malayalam news datasets, consolidated into a single file for classification and analysis purposes. The dataset contains news articles along with their corresponding numeric labels.

## Dataset Details
- **Number of rows:** 5118  
- **Columns:**  
  - `text` — the news article content  
  - `label` — numeric category label  

## Label Mapping
| Label | Category        |
|-------|----------------|
| 0     | entertainment  |
| 1     | sports         |
| 2     | business       |
| 3     | technology     |

## Notes
- Duplicate articles (same text + label) were removed.  
- All entries are in Malayalam.  
- This dataset can be used for text classification, NLP experiments, or model training.  

## File
- `combined_dataset.csv` — the consolidated dataset with `text` and `label` columns.
