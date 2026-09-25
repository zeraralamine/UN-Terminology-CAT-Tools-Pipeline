# UN Terminology Extractor for CAT Tools
**What this is**
A Python script that pulls clean French-Arabic terminology from the United Nations database and formats it for immediate use in CAT tools.

**The Problem**
While the UN provides massive, free terminology databases, they are notoriously difficult for translators to use. The standard CSV exports mash all six UN languages into single columns with randomized rows. What's even more difficult is that opening these files in Excel often corrupts Right-to-Left scripts like Arabic into unreadable symbols. Manually cleaning this data takes hours.

**The Solution**
This script bypasses the broken CSVs entirely. It connects directly to the UN's raw semantic data (.ttl files), isolates the French and Arabic pairs, removes any duplicates, and exports a clean, two-column CSV with the exact language tags CAT Tools require (fr-CH and ar-SA).

**How to Use It**
1. Download the UNBIS Thesaurus Turtle dataset (.ttl) from the UN Digital Library.
2. Put the .ttl file in the same folder as the script.
3. Run the script from your terminal: python extract_terms.py
4. Take the newly generated CSV file and upload it directly into your CAT Tool project under Translation Memory and Terminology
