import arxiv

def fetch_papers(query, max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "url": result.entry_id
        })
    return papers

query = "Swin Transformer for Object Detection"
papers = fetch_papers(query)
for paper in papers:
    print(paper["title"], paper["url"])
