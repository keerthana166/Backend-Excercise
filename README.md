# Research Paper Fetcher 

A Python-based tool to fetch research papers from `PubMed` based on a user-specified query. The program identifies papers where at least one author is affiliated with a `pharmaceutical or biotech company` and saves the results as a CSV file.  

---

## *Table of Contents*  
- Features 
- Installation
- Usage
- Project Structure
- How It Works 
- Dependencies
- Development and Contribution 
- License 

---

## *Features*  
Fetches research papers from *PubMed* using its API  
Filters papers to include only those with at least one *non-academic author*  
Extracts details like *PubMed ID, Title, Publication Date, Company Affiliation, and Corresponding Author Email*  
Saves results in *CSV format*  
Provides a *command-line interface* for easy usage  

---

## *Installation*  

### *1. Clone the Repository*  
git clone https://github.com/keerthana166/research-paper-fetcher.git
cd research-paper-fetcher


### *2. Install Dependencies using Poetry*  
Ensure you have *Poetry* installed. If not, install it first:  
pip install poetry

Now, install project dependencies:  
poetry install


---

## *Usage*  

### *Run the Program*  
To fetch research papers, use:  
python -m research_papers.cli "cancer therapy" -f results.csv

This will:  
- Fetch research papers related to *"cancer therapy"*  
- Save the results in results.csv  

### *Command-Line Options*  
- -h or --help: Show usage instructions  
- -d or --debug: Print debug information  
- -f <filename> or --file <filename>: Save results to a specified CSV file  

---

## *Project Structure*  

research-paper-fetcher/
│── research_papers/                # Main package
│   ├── __init__.py                  # Package initialization
│   ├── fetch_papers.py               # Fetches papers from PubMed API
│   ├── filter_papers.py              # Filters papers with non-academic authors
│   ├── cli.py                        # Command-line interface
│
│── tests/                            # Unit tests
│   ├── test_fetch_papers.py
│   ├── test_filter_papers.py
│
│── results.csv                       # Output file (optional)
│── README.md                         # Documentation
│── pyproject.toml                    # Poetry configuration


---

## *How It Works*  
1. *Fetches Papers* → Uses *PubMed API* to search for papers based on a query  
2. *Filters Results* → Identifies papers with *non-academic authors* based on their affiliations  
3. *Extracts Key Information* → Collects *title, PubMed ID, author affiliations, and emails*  
4. *Saves to CSV* → Outputs the results for easy access  

The results CSV file will have the following columns:  

| PubmedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |  
|----------|-------|------------------|-------------------------|-------------------------|---------------------------|  
| 12345678 | Example Paper | 2025-03-10 | Dr. John Doe | XYZ Biotech Inc. | johndoe@xyzbiotech.com |  

---

## *Dependencies*  
The project requires the following Python libraries:  
- requests → To interact with the PubMed API  
- biopython → To parse PubMed data  
- pandas → To process and save data  

All dependencies will be installed automatically using poetry install.  

---

## *Development and Contribution*  
### *1. Setting Up the Development Environment*  
git clone https://github.com/keerthana166/research-paper-fetcher.git
cd research-paper-fetcher
poetry install


### *2. Running Tests*  
pytest tests/


### *3. Contributing*  
Contributions are welcome! To contribute:  
1. Fork the repository  
2. Create a new branch (git checkout -b feature-branch)  
3. Commit changes (git commit -m "Add new feature")  
4. Push to your fork (git push origin feature-branch)  
5. Open a *Pull Request*  

---