from pydantic import HttpUrl

from comment_scraper.client.InstagramClient import InstagramClient
from comment_scraper.exceptions import SchemaConverterException, NoKeywordInCommentsException
from comment_scraper.schemas.instagramSchemas import BaseComment


class InstagramService:

    async def get_comments(self, url: list[str], limit: int = 1000):
        client = InstagramClient()

        raw_comment_data = await client.get_ig_comments(url, limit)

        comments_schema = []

        for raw_comment in raw_comment_data:
            try:
                comment_obj = BaseComment.from_apify_item(raw_comment)
                comments_schema.append(comment_obj)

            except Exception as e:
                raise SchemaConverterException(e)

        return comments_schema

    def keyword_filter(self, comments_data: list, keyword: str):
        keyword_comments_data = []

        lower_keyword = keyword.lower()

        for comment in comments_data:
            if lower_keyword in (comment.commentContent or "").lower():
                keyword_comments_data.append(comment)

        if not keyword_comments_data:
            raise NoKeywordInCommentsException(keyword)

        return keyword_comments_data