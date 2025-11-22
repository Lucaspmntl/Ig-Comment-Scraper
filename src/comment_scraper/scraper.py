import os

from dotenv import load_dotenv
from apify_client import ApifyClientAsync

load_dotenv()

class CommentScraper:
    def __init__(self):
        self.TOKEN = os.getenv('APIFY_TOKEN')
        self.apify_client = ApifyClientAsync(token=self.TOKEN)

        if not self.TOKEN:
            raise ValueError("No API token provided")

        if not self.apify_client:
            raise ValueError("No client provided")

    async def get_comments(self, url: str):
        comment_actor = self.apify_client.actor('apify/instagram-comment-scraper')

        run_input = {
            'directUrls': [url],
            "includeNestedComments": False,
            "isNewestComments": False,
            "resultsLimit": 15
        }

        print(f"Initialing for comments from: {url}")

        run_info = await comment_actor.call(run_input=run_input)

        dataset_id = run_info["defaultDatasetId"]

        dataset_client = self.apify_client.dataset(dataset_id)

        results = await dataset_client.list_items()

        return results

