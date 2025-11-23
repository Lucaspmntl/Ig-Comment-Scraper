from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl

class BaseComment(BaseModel):
    # Section Fields
    postUrl: Optional[HttpUrl] = None
    commentUrl: Optional[HttpUrl] = None
    id: str
    commentContent: Optional[str] = ""

    # Owner Fields
    ownerUsername: str
    ownerId: Optional[str] = None
    ownerFullName: Optional[str] = None
    ownerProfilePicUrl: Optional[str] = None
    ownerProfilePicId: Optional[str] = None

    # Time
    timestamp: datetime

    @classmethod
    def from_apify_item(cls, item: dict):

        owner_data = item.get("owner") or {}

        return cls(
            id=item.get("id"),

            postUrl=item.get("postUrl") or item.get("url"),
            commentUrl=item.get("commentUrl"),

            ownerUsername=item.get("ownerUsername") or owner_data.get("username") or "Anonymous",

            ownerId=item.get("id") or owner_data.get("id"),
            ownerFullName=owner_data.get("full_name"),

            ownerProfilePicUrl=item.get("ownerProfilePicUrl") or owner_data.get("profile_pic_url"),

            ownerProfilePicId=owner_data.get("profile_pic_id"),

            commentContent=item.get("text") or "",

            timestamp=item.get("timestamp"),
        )
