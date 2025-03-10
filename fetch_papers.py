import requests
from Bio import Entrez

Entrez.email = "mkeerthana201@gmail.com"  

def fetch_papers(query):
    """Fetch research papers from PubMed based on a query."""
    
    # Fetch articles from PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=10)  # Adjust retmax as needed
    record = Entrez.read(handle)
    handle.close()
    
    paper_ids = record["IdList"]
    
    if not paper_ids:
        return []

    # Fetch article details
    handle = Entrez.efetch(db="pubmed", id=paper_ids, rettype="medline", retmode="xml")
    records = Entrez.read(handle)
    handle.close()

    papers = []
    
    for article in records["PubmedArticle"]:
        citation = article["MedlineCitation"]
        article_info = citation["Article"]

        # Extract details
        pubmed_id = citation["PMID"]
        title = article_info.get("ArticleTitle", "N/A")
        if "ArticleDate" in article_info and article_info["ArticleDate"]:
            publication_date = article_info["ArticleDate"][0].get("Year", "N/A")
        elif "Journal" in article_info and "JournalIssue" in article_info["Journal"]:
            publication_date = article_info["Journal"]["JournalIssue"].get("PubDate", "N/A")
        else:
            publication_date = "N/A"
        # Placeholder for non-academic author identification logic
        non_academic_authors = "N/A"  
        company_affiliations = "N/A"
        corresponding_author_email = "N/A"

        # Append to list
        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academic Author(s)": non_academic_authors,
            "Company Affiliation(s)": company_affiliations,
            "Corresponding Author Email": corresponding_author_email
        })

    return papers
