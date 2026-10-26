# Task 26 – Text Cleaning Basics

## Project Overview

This project is part of my Data Analytics Internship at **Veda Technology**.

The task focuses on cleaning and standardizing text data using Python and Excel. I worked with a sample customer dataset containing inconsistent capitalization, unnecessary spaces, and variations in text formatting.

The main goal was to correct these issues and make the dataset more consistent and suitable for further analysis.

## Tools Used

- Python
- Pandas
- Microsoft Excel

## Dataset

I used a synthetic customer dataset containing 20 records created for this task.

The dataset includes the following columns:

- Customer ID
- Customer Name
- Email
- City
- Customer Segment
- Country

Some records intentionally contain extra spaces, inconsistent capitalization, and differently formatted category names to demonstrate the cleaning process.

## Data Cleaning Process

### 1. Removing Unnecessary Spaces

Removed leading and trailing spaces and reduced multiple spaces between words to a single space.

**Example:**
- Before: `"  aNita  sharma "`
- After: `"Anita Sharma"`

### 2. Standardizing Capitalization

Used Python's `title()` method to maintain consistent capitalization in customer names, cities, and countries.

**Example:**
- Before: `"BENGALURU"`
- After: `"Bengaluru"`

### 3. Cleaning Email Addresses

Removed unnecessary spaces and converted email addresses to lowercase.

**Example:**
- Before: `" ANITA.SHARMA@EXAMPLE.COM "`
- After: `"anita.sharma@example.com"`

### 4. Standardizing Customer Segments

Corrected inconsistent formatting in customer segment names.

**Example:**
- Before: `"consumer"`
- After: `"Consumer"`

This helped maintain consistent category values across the dataset.

## Python Functions Used

| Function | Purpose |
|---|---|
| `strip()` | Removes leading and trailing whitespace |
| `split()` | Separates text and helps identify repeated spaces |
| `join()` | Combines words with consistent spacing |
| `title()` | Converts text to title case |
| `lower()` | Converts text to lowercase |
| `map()` | Applies cleaning operations to column values |

## Project Files

| File | Description |
|---|---|
| `Task_26_Text_Cleaning_Basics.py` | Python script used for cleaning the dataset |
| `customer_dirty_data.csv` | Original dataset containing text formatting issues |
| `customer_cleaned_data.csv` | Cleaned dataset generated using Python |
| `Veda_Technology_Task_26_Text_Cleaning_Basics.xlsx` | Excel workbook containing original data, cleaned data, before-and-after examples, and a summary |
| `Veda_Technology_Task_26_Text_Cleaning_Basics_Report.pdf` | Report explaining the task and cleaning methods |

## How to Run the Project

**Step 1:** Download or clone this repository.

**Step 2:** Install the required Python library.

```bash
pip install pandas
```

**Step 3:** Open the project folder in a terminal.

**Step 4:** Run the Python script.

```bash
python Task_26_Text_Cleaning_Basics.py
```

**Step 5:** The script will generate a cleaned CSV file named:

`customer_cleaned_data.csv`

Open the Excel workbook to compare the original and cleaned records.

## What I Learned

Through this task, I practised identifying and correcting common text formatting issues in datasets.

I learned how small inconsistencies, such as extra spaces or different capitalization, can affect filtering, grouping, and matching records.

I also gained more practice using Pandas to apply cleaning operations across multiple columns instead of correcting each record manually.

## Conclusion

This task helped me understand the importance of text cleaning as part of data preprocessing.

By standardizing customer information, the dataset becomes more consistent and easier to use for further analysis.

---

**Internship:** Veda Technology  
**Track:** Data Analytics  
**Task:** 26 – Text Cleaning Basics  
**Tools:** Python, Pandas, Microsoft Excel
