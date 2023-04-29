from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List


class SocialChannel(ABC):
    def __init__(self, followers: int):
        self.followers = followers

    @abstractmethod
    def authorize(self, creds: dict[str, str]):
        """Authorize with external system."""

    @abstractmethod
    def post(self, message: str):
        """Post message with external system"""


class YoutubeChannel(SocialChannel):
    def authorize(self, creds: str):
        print(f"{creds=}")

    def post(self, message: str):
        print(f"{message=}")


class FacebookChannel(SocialChannel):
    def authorize(self, creds: str):
        print(f"{creds=}")

    def post(self, message: str):
        print(f"{message=}")


class TwitterChannel(SocialChannel):
    def authorize(self, creds: str):
        print(f"{creds=}")

    def post(self, message: str):
        print(f"{message=}")


class Post:
    def __init__(self, message: str, timestamp: datetime):
        self.message = message
        self.timestamp = timestamp


def post_a_message(channel: SocialChannel, message: str) -> None:
    channel.post(message)


def authorize(channel: SocialChannel, creds: dict[str, str]) -> None:
    channel.authorize(creds)


def process_schedule(posts: List[Post], channels: List[SocialChannel]) -> None:
    for post in posts:
        if post.timestamp >= datetime.now():
            for channel in channels:
                post_a_message(channel, post.message)


def main():
    # create social channel objects
    youtube_channel = YoutubeChannel(1000)  # 1000 followers
    facebook_channel = FacebookChannel(500)  # 500 followers
    twitter_channel = TwitterChannel(200)  # 200 followers

    # create list of social channel objects
    channels = [youtube_channel, facebook_channel, twitter_channel]

    # create list of posts
    posts = [
        Post("Check out my latest video!", datetime.now() + timedelta(seconds=60)),  # post in 1 minute
        Post("Join me for a live stream!", datetime.now() + timedelta(seconds=120)),  # post in 2 minutes
        Post("New blog post is up!", datetime.now() + timedelta(seconds=180)),  # post in 3 minutes
    ]

    # schedule posts
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
