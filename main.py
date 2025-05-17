from fastapi import FastAPI, Query
from crawl4ai import AsyncWebCrawler

app = FastAPI()

@app.get("/crawl")
async def crawl_get(url: str = Query(...)):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
    return {"markdown": result.markdown}
@app.post("/crawl")
async def crawl_post(body: dict):
    url = body.get("url")
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
    return {"markdown": result.markdown}
