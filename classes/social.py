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
    def authorize(self, api_credentials: Creds) -> bool:
        """Authorize with external system."""

    @abstractmethod
    def check_status(self, message_id: str) -> Any:
        """Check message status after publishing"""


class Twitter(SocialNetwork):
    def authorize(self, api_credentials: Creds) -> bool:
        try:
            auth = tweepy.OAuthHandler(
                api_credentials.get("consumer_key"),
                api_credentials.get("consumer_secret"),
            )
            auth.set_access_token(
                api_credentials.get("access_token"),
                api_credentials.get("access_token_secret"),
            )
            self.auth = auth
            self.api = tweepy.API(auth)
            return True

        except Exception as e:
            raise Exception(e)

    def check_status(self, message_id: str):
        status = self.api.get_status(message_id)
        return status._json['text']


class Facebook(SocialNetwork):
    def authorize(self, api_credentials: Creds) -> None:
        graph = facebook.GraphAPI(access_token=api_credentials.get("access_token"))
        self.graph = graph


class YouTube(SocialNetwork):
    def authorize(self, api_credentials: Creds) -> None:
        youtube = build("youtube", "v3", developerKey=api_credentials.get("api_key"))
        self.youtube = youtube


class Post:
    def __init__(self, social_network: SocialNetwork) -> None:
        self.social_network = social_network

    def post_message(self, message: str) -> dict[str, str]:
        if isinstance(self.social_network, Twitter):
            return self.social_network.api.update_status(message)
        elif isinstance(self.social_network, Facebook):
            return self.social_network.graph.put_object(
                parent_object="me", connection_name="feed", message=message
            )
        elif isinstance(self.social_network, YouTube):
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
                self.social_network.youtube.videos()
                .insert(part="snippet,status", body=video, media_body=None)
                .execute()
            )
            return response


twitter_api_credentials: dict[str, str] = {
    "consumer_key": "your_consumer_key",
    "consumer_secret": "your_consumer_secret",
    "access_token": "your_access_token",
    "access_token_secret": "your_access_token_secret",
}

facebook_api_credentials: dict[str, str] = {
    "access_token": "your_access_token",
}

youtube_api_credentials: dict[str, str] = {
    "api_key": "your_youtube_api_key",
}

twitter = Twitter()
twitter.authorize(twitter_api_credentials)

fb = Facebook()
fb.authorize(facebook_api_credentials)

youtube = YouTube()
youtube.authorize(youtube_api_credentials)

twitter_post = Post(twitter)
facebook_post = Post(fb)
youtube_post = Post(youtube)

twitter_response = twitter_post.post_message("Hello, Twitter!")
print(f"Twitter response: {twitter_response}")

facebook_response = facebook_post.post_message
