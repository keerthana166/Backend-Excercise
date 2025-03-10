import argparse
import pandas as pd
from research_papers.fetch_papers import fetch_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results", default="results.csv")
    
    args = parser.parse_args()

    papers = fetch_papers(args.query)

    if not papers:
        print("No papers found for the given query.")
        return

    # Convert list of dictionaries to a DataFrame
    df = pd.DataFrame(papers)

    # Save to CSV
    df.to_csv(args.file, index=False)
    print(f"Results saved to {args.file}")

if __name__ == "__main__":
    main() 
