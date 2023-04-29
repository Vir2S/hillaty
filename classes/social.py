import tweepy
import facebook

from abc import ABC, abstractmethod
from dataclasses import dataclass
from googleapiclient.discovery import build
from typing import Dict, Any


@dataclass
class Creds:
    api_credentials: Dict[str, str]


class SocialNetwork(ABC):
    @abstractmethod
    def authorize(self, api_credentials: Creds) -> None:
        """Authorize with external system."""

    @property
    @abstractmethod
    def check_status(self, message_id: str) -> Any:
        """Check message status after publishing"""


class Twitter(SocialNetwork):
    api = None

    def authorize(self, api_credentials: Creds) -> None:
        auth = tweepy.OAuthHandler(
            api_credentials.get("consumer_key"),
            api_credentials.get("consumer_secret"),
        )
        auth.set_access_token(
            api_credentials.get("access_token"),
            api_credentials.get("access_token_secret"),
        )
        self.api = tweepy.API(auth)

    @property
    def check_status(self, message_id: str):
        ...


class Facebook(SocialNetwork):
    graph = None

    def authorize(self, api_credentials: Creds) -> None:
        self.graph = facebook.GraphAPI(access_token=api_credentials.get("access_token"))

    @property
    def check_status(self, message_id: str):
        ...


class YouTube(SocialNetwork):
    youtube = None

    def authorize(self, api_credentials: Creds) -> None:
        self.youtube = build(
            "youtube", "v3", developerKey=api_credentials.get("api_key")
        )

    @property
    def check_status(self, message_id: str):
        ...


class Post:
    def __init__(self, social_network: SocialNetwork) -> None:
        self._social_network = social_network

    def post_message(self, message: str) -> dict[str, str]:
        if isinstance(self._social_network, Twitter):
            return self._social_network.api.update_status(message)

        if isinstance(self._social_network, Facebook):
            return self._social_network.graph.put_object(
                parent_object="me", connection_name="feed", message=message
            )

        if isinstance(self._social_network, YouTube):
            video = {
                "snippet": {
                    "title": "New video",
                    "description": message,
                    "tags": ["new", "video"],
                    "categoryId": "22",
                },
                "status": {"privacyStatus": "public"},
            }
            response = (
                self._social_network.youtube.videos()
                .insert(part="snippet,status", body=video, media_body=None)
                .execute()
            )
            return response

        return {"error": "Not supported social network."}


def main():
    twitter_api_credentials = {
        "consumer_key": "your_consumer_key",
        "consumer_secret": "your_consumer_secret",
        "access_token": "your_access_token",
        "access_token_secret": "your_access_token_secret",
    }

    facebook_api_credentials = {
        "access_token": "your_access_token",
    }

    youtube_api_credentials = {
        "api_key": "your_youtube_api_key",
    }

    tw = Twitter()
    tw.authorize(twitter_api_credentials)

    fb = Facebook()
    fb.authorize(facebook_api_credentials)

    yt = YouTube()
    yt.authorize(youtube_api_credentials)

    Post(tw).post_message("twitter message")
    Post(fb).post_message("facebook message")
    Post(yt).post_message("youtube message")


if __name__ == "__main__":
    main()
