import os

from apify_client import ApifyClientAsync
from dotenv import load_dotenv
from pydantic import HttpUrl

from comment_scraper.exceptions import *

load_dotenv()


class InstagramClient:

    def __init__(self):
        self.TOKEN = os.getenv('APIFY_TOKEN')

        if not self.TOKEN:
            raise InvalidApiTokenException()

        self.apify_client = ApifyClientAsync(token=self.TOKEN)

    async def get_ig_comments(self, url: list[str], limit: int = 1000):
        actor_name = 'apify/instagram-comment-scraper'

        comment_actor = self.apify_client.actor(actor_name)

        run_input = {
            'directUrls': url,
            "includeNestedComments": False,
            "isNewestComments": False,
            "resultsLimit": limit
        }

        print(f"\n\nINITIALING COMMENT SCRAPING FROM: {url}\n")

        try:
            run_info = await comment_actor.call(run_input=run_input)

        except Exception as e:
            print(e)
            raise ActorCallException(actor_name, e)

        dataset_id = run_info["defaultDatasetId"]

        dataset_client = self.apify_client.dataset(dataset_id)

        pagination_result = await dataset_client.list_items(
            fields=["error", "errorDescription", "text"]
        )

        first_pagination_item = pagination_result.items[0]

        if first_pagination_item and first_pagination_item.get("error"):
            raise DatasetException(dataset_id,
                                   first_pagination_item["error"] or
                                   first_pagination_item["errorDescription"])

        if pagination_result.items:
            first_item = pagination_result.items[0]
            if first_item.get("error"):
                raise DatasetException(dataset_id, first_item.get("error"))

        results = await dataset_client.list_items(
            fields=[
                    "postUrl",
                    "commentUrl",
                    "id",
                    "text",
                    "owner",
                    "timestamp",
                    ])

        return results.items
