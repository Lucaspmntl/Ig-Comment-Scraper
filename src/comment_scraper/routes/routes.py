from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import HttpUrl

from comment_scraper.exceptions import NoKeywordInCommentsException
from comment_scraper.service.InstagramService import InstagramService

app = FastAPI()


@app.get('/instagram/comments')
async def get_messages(url: list[HttpUrl] = Query(...),
                       limit: Optional[int] = Query(None),
                        keyword: Optional[str] = Query(None)):

    str_url = [str(u) for u in url]
    instagram_service = InstagramService()
    comments_data = await instagram_service.get_comments(str_url, limit)

    if keyword:
        try:
            keyword_comments = instagram_service.keyword_filter(comments_data, keyword)
            return keyword_comments

        except NoKeywordInCommentsException:
            raise HTTPException(
                status_code=404,
                detail=f"No comments with the keyword {keyword}"
            )

    return comments_data
