from typing import Optional

from fastapi import FastAPI, Query
from pydantic import HttpUrl

from comment_scraper.service.InstagramService import InstagramService

app = FastAPI()


@app.get('/instagram/comments')
async def get_messages(url: list[HttpUrl] = Query(...),
                       limit: Optional[int] = Query(...)):

    str_url = [str(u) for u in url]
    instagram_service = InstagramService()
    comments_data = await instagram_service.get_comments(str_url)

    return comments_data
