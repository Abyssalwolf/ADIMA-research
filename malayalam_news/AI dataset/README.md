# Merged News Dataset

This dataset is a combination of multiple Malayalam news datasets, structured for text classification tasks.

---

## Basic Information

- **Total rows:** 4682
- **Columns:**
  - `text` — the news article content in Malayalam
  - `label` — numerical category label

**Column details:**

| Column | Type   | Description                        |
|--------|--------|------------------------------------|
| text   | object | Malayalam news article             |
| label  | int64  | Category label (0-3)               |

---

## Label Information

| Label | Count | Category |
|-------|-------|----------|
| 0     | 1260  | Entertainment |
| 1     | 1122  | Sports |
| 2     | 1179  | Business |
| 3     | 1121  | Technology |

**Unique labels:** `[0, 1, 2, 3]`
---

**Categories Mapping:**

| Label | Category     |
|-------|--------------|
| 0     | Entertainment |
| 1     | Sports        |
| 2     | Business      |
| 3     | Technology    |
