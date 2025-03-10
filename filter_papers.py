import re
from typing import List, Dict

def is_non_academic(author_affiliation: str) -> bool:
    """Check if an author is affiliated with a non-academic institution."""
    academic_keywords = ["university", "college", "institute", "research center", "hospital", "school"]
    return not any(keyword.lower() in author_affiliation.lower() for keyword in academic_keywords)

def filter_papers(papers: List[Dict]) -> List[Dict]:
    """Filter papers that have at least one non-academic author."""
    filtered_papers = []

    for paper in papers:
        if "Authors" in paper:
            non_academic_authors = [author for author in paper["Authors"] if is_non_academic(author)]
            if non_academic_authors:
                paper["Non-academic Authors"] = non_academic_authors
                filtered_papers.append(paper)

    return filtered_papers 
