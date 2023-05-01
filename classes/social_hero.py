from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from datetime import time as t
from typing import List


@dataclass
class Creds:
    creds: dict[str, str]


class Timer:
    def __init__(self, hh=None, mm=None, ss=None):
        if hh and mm and ss:
            self.time = int(datetime.combine(datetime.today(), t(hour=hh, minute=mm, second=ss)).timestamp() * 1000)
        else:
            self.time = int(datetime.now().timestamp() * 1000)

    def __str__(self):
        return datetime.fromtimestamp(self.time / 1000).strftime("%Y-%m-%d %H:%M:%S")

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __le__(self, other):
        return self.time <= other.time

    def __ge__(self, other):
        return self.time >= other.time


@dataclass
class Post:
    message: str
    timestamp: Timer


class SocialChannel(ABC):
    def __init__(self, followers: int = 0):
        self.followers = followers

    @abstractmethod
    def authorize(self, creds: dict[str, str]) -> None:
        """Authorize with external system."""

    @abstractmethod
    def post(self, post: Post) -> None:
        """Post message with external system"""


class YoutubeChannel(SocialChannel):
    def authorize(self, creds: str) -> None:
        print("Authorized")

    def post(self, post: Post) -> None:
        print(f"{post.message} posted at {post.timestamp} in YouTube")


class FacebookChannel(SocialChannel):
    def authorize(self, creds: str) -> None:
        print("Authorized")

    def post(self, post: Post) -> None:
        print(f"{post.message} posted at {post.timestamp} in Facebook")


class TwitterChannel(SocialChannel):
    def authorize(self, creds: str) -> None:
        print("Authorized")

    def post(self, post: Post) -> None:
        print(f"{post.message} posted at {post.timestamp} in Twitter")


def social_channel_dispatcher(decision: str) -> SocialChannel:
    if decision.lower() == "youtube":
        return YoutubeChannel()
    if decision.lower() == "facebook":
        return FacebookChannel()
    if decision.lower() == "twitter":
        return TwitterChannel()
    raise ValueError("Social Channel not found!")


def post_a_message(channel: str, message: Post, **kwargs) -> None:
    creds = kwargs.get("creds")
    channel= social_channel_dispatcher(channel)
    if creds:
        authorize(channel, creds)
    channel.post(message)


def authorize(channel: SocialChannel, creds: dict[str, str]) -> None:
    channel.authorize(creds)


def process_schedule(posts: List[Post], channels: List[str]) -> None:
    for post in posts:
        if post.timestamp <= Timer():
            for channel in channels:
                post_a_message(channel, post)


def main():
    print("************** Regular post ****************")

    youtube_post = Post("YouTube regular post", Timer())
    post_a_message("youtube", youtube_post)

    facebook_post = Post("Facebook regular post", Timer())
    post_a_message("facebook", facebook_post)

    twitter_post = Post("Twitter regular post", Timer())
    post_a_message("twitter", twitter_post)

    print("\n************** Scheduled post ****************")

    channels = ["youtube", "facebook", "twitter"]

    posts = [
        Post("Regular - Check out my post now!", Timer()),
        Post("Scheduled - Join me for a while!", Timer(11, 11, 11)),
    ]

    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
