from aiohttp import ClientSession as Client
from orjson import loads, dumps
from .models import PinterestUser, PinterestPost, PinterestFeed, PinterestReverseAPIResponse, InstagramWebProfileResponse, InstagramPost, InstagramStoryResponse, InstagramTimeline, TwitterUser, TwitterPost, TwitterTimeline, TikTokUser, PostResponse as TikTokPost, FeedResponse as TikTokFeed, ThreadsProfileResponse, ThreadsDLModelsGraphQLPostNode, YouTubeDLModelsChannelVideos
from typing import Optional, List, Dict, Any
__slots__ = ('Eros','Eros.get_url','Eros.request','Instagram','Instagram.get_user','Instagram.get_post','Instagram.get_feed','Instagram.get_story','TikTok','TikTok.get_post','TikTok.get_user','TikTok.get_feed','Threads','Threads.get_post','Threads.get_user','Pinterest','Pinterest.get_user','Pinterest.get_post','Pinterest.get_feed','Pinterest.reverse_search','YouTube','YouTube.get_feed','Twitter','Twitter.get_user','Twitter.get_post','Twitter.get_feed')

class DataNotFound(Exception):
    """Custom Exception to make the exception raised look a bit better"""
    def __init__(self, message: str, **kwargs):
        self.message
        super().__init__(message)

    @property
    def error_message(self) -> str:
        return self.message

class Eros:
    """The main class for the Eros API wrapper"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = Client()
        self.base_url = "https://eros.rest"

    def get_url(self, endpoint: str) -> str:
        """Gets the API URL"""
        return f"{self.base_url}/{endpoint}"

    async def request(self, endpoint: str, params: Dict[Any,Any]) -> Any:
        """Requests the API and returns the json data"""
        response = await self.client.get(self.get_url(endpoint), headers = {'api-key': self.api_key})
        try:
            return await response.json(loads = loads)
        except:
            _type, object_type = endpoint.split('/')
            raise DataNotFound(f"{_type} {object_type} **{list(params.values())[0]}** not found")

class Instagram:
    """
    A class representing the Instagram API.

    Args:
        client (Eros): An instance of the Eros client.

    Attributes:
        client (Eros): The Eros client used for making requests to the Instagram API.
    """

    def __init__(self, client: Eros):
        self.client = client

    async def get_user(self, username: str) -> Optional[InstagramWebProfileResponse]:
        """
        Get information about an Instagram user.

        Args:
            username (str): The username of the Instagram user.

        Returns:
            Optional[InstagramWebProfileResponse]: An instance of InstagramWebProfileResponse if the user exists, else None.
        """
        data = await self.client.request("instagram/user", {"username": username})
        return InstagramWebProfileResponse(**data)
    
    async def get_post(self, url: str) -> Optional[InstagramPost]:
        """
        Get information about an Instagram post.

        Args:
            url (str): The URL of the Instagram post.

        Returns:
            Optional[InstagramPost]: An instance of InstagramPost if the post exists, else None.
        """
        data = await self.client.request("instagram/post", {"url": url})
        return InstagramPost(**data)
    
    async def get_story(self, url: str) -> Optional[InstagramStoryResponse]:
        """
        Get information about an Instagram story.

        Args:
            url (str): The URL of the Instagram story.

        Returns:
            Optional[InstagramStoryResponse]: An instance of InstagramStoryResponse if the story exists, else None.
        """
        data = await self.client.request("instagram/story", {"url": url})
        return InstagramStoryResponse(**data)
    
    async def get_feed(self, username: str) -> Optional[InstagramTimeline]:
        """
        Get the feed of an Instagram user.

        Args:
            username (str): The username of the Instagram user.

        Returns:
            Optional[InstagramTimeline]: An instance of InstagramTimeline if the user exists, else None.
        """
        data = await self.client.request("instagram/feed", {"username": username})
        return InstagramTimeline(**data)
    
class TikTok:
    """
    Represents a TikTok client.

    Args:
        client (Eros): The Eros client used for making requests to the TikTok API.

    Attributes:
        client (Eros): The Eros client used for making requests to the TikTok API.
    """

    def __init__(self, client: Eros):
        self.client = client

    async def get_user(self, username: str) -> Optional[TikTokUser]:
        """
        Retrieves information about a TikTok user.

        Args:
            username (str): The username of the TikTok user.

        Returns:
            Optional[TikTokUser]: An instance of TikTokUser if the user exists, None otherwise.
        """
        data = await self.client.request("tiktok/user", {"username": username})
        return TikTokUser(**data)
    
    async def get_post(self, url: str) -> Optional[TikTokPost]:
        """
        Retrieves information about a TikTok post.

        Args:
            url (str): The URL of the TikTok post.

        Returns:
            Optional[TikTokPost]: An instance of TikTokPost if the post exists, None otherwise.
        """
        data = await self.client.request("tiktok/post", {"url": url})
        return TikTokPost(**data)
    
    async def get_feed(self, username: str) -> Optional[TikTokFeed]:
        """
        Retrieves the feed of a TikTok user.

        Args:
            username (str): The username of the TikTok user.

        Returns:
            Optional[TikTokFeed]: An instance of TikTokFeed if the user exists, None otherwise.
        """
        data = await self.client.request("tiktok/feed", {"username": username})
        return TikTokFeed(**data)
    
class Pinterest:
    """
    A class representing the Pinterest API.

    This class provides methods to interact with the Pinterest API, such as retrieving posts, users, performing reverse searches, and getting feeds.

    Args:
        client (Eros): An instance of the Eros client used for making API requests.

    Attributes:
        client (Eros): The Eros client used for making API requests.
    """

    def __init__(self, client: Eros):
        self.client = client

    async def get_post(self, url: str) -> Optional[PinterestPost]:
        """
        Retrieve a Pinterest post by its URL.

        Args:
            url (str): The URL of the Pinterest post.

        Returns:
            Optional[PinterestPost]: An instance of the PinterestPost class representing the retrieved post, or None if the post was not found.
        """
        data = await self.client.request("pinterest/post", {"url": url})
        return PinterestPost(**data)
    
    async def get_user(self, username: str) -> Optional[PinterestUser]:
        """
        Retrieve a Pinterest user by their username.

        Args:
            username (str): The username of the Pinterest user.

        Returns:
            Optional[PinterestUser]: An instance of the PinterestUser class representing the retrieved user, or None if the user was not found.
        """
        data = await self.client.request("pinterest/user", {"username": username})
        return PinterestUser(**data)
    
    async def reverse_search(self, url: str) -> Optional[PinterestReverseAPIResponse]:
        """
        Perform a reverse search on Pinterest using an image URL.

        Args:
            url (str): The URL of the image to perform the reverse search on.

        Returns:
            Optional[PinterestReverseAPIResponse]: An instance of the PinterestReverseAPIResponse class representing the reverse search result, or None if no result was found.
        """
        data = await self.client.request("pinterest/reverse", {"url": url})
        return PinterestReverseAPIResponse(**data)
    
    async def get_feed(self, username: str) -> Optional[PinterestFeed]:
        """
        Retrieve the feed of a Pinterest user.

        Args:
            username (str): The username of the Pinterest user.

        Returns:
            Optional[PinterestFeed]: An instance of the PinterestFeed class representing the retrieved feed, or None if the user's feed was not found.
        """
        data = await self.client.request("pinterest/feed", {"username": username})
        return PinterestFeed(**data)
    
class Threads:
    """
    Represents a collection of methods for interacting with threads in the Eros client.
    """

    def __init__(self, client: Eros):
        self.client = client

    async def get_post(self, url: str) -> List[ThreadsDLModelsGraphQLPostNode]:
        """
        Retrieves a post from the Eros client based on the given URL.

        Args:
            url (str): The URL of the post.

        Returns:
            List[ThreadsDLModelsGraphQLPostNode]: A list of post nodes matching the URL.
        """
        data = await self.client.request("threads/post", {'url': url})
        return ThreadsDLModelsGraphQLPostNode(**data)
    
    async def get_user(self, username: str) -> Optional[ThreadsProfileResponse]:
        """
        Retrieves user information from the Eros client based on the given username.

        Args:
            username (str): The username of the user.

        Returns:
            Optional[ThreadsProfileResponse]: The profile response of the user, if found. Otherwise, None.
        """
        data = await self.client.request("threads/user", {'username': username})
        return ThreadsProfileResponse(**data)
    
class YouTube:
    """
    Represents a YouTube client.

    Args:
        client (Eros): The Eros client used for making requests to the API.

    Attributes:
        client (Eros): The Eros client used for making requests to the API.
    """

    def __init__(self, client: Eros):
        self.client = client

    async def get_feed(self, user: str) -> Optional[YouTubeDLModelsChannelVideos]:
        """
        Retrieves the feed for a given user.

        Args:
            user (str): The username or ID of the user.

        Returns:
            Optional[YouTubeDLModelsChannelVideos]: The channel videos data, or None if the user does not exist.
        """
        data = await self.client.request("youtube/feed", {'snowflake': user})
        return YouTubeDLModelsChannelVideos(**data)
    
class Twitter:
    """
    A class representing the Twitter API.

    This class provides methods to interact with the Twitter API
    and retrieve user information, posts, and feeds.

    Args:
        client (Eros): An instance of the Eros client.

    Attributes:
        client (Eros): The Eros client used for making API requests.
    """

    def __init__(self, client: Eros):
        self.client = client

    async def get_user(self, username: str) -> Optional[TwitterUser]:
        """
        Retrieve information about a Twitter user.

        Args:
            username (str): The username of the Twitter user.

        Returns:
            Optional[TwitterUser]: An instance of the TwitterUser class
            representing the user, or None if the user is not found.
        """
        data = await self.client.request("twitter/user", {"username": username})
        return TwitterUser(**data)

    async def get_post(self, url: str) -> Optional[TwitterPost]:
        """
        Retrieve information about a Twitter post.

        Args:
            url (str): The URL of the Twitter post.

        Returns:
            Optional[TwitterPost]: An instance of the TwitterPost class
            representing the post, or None if the post is not found.
        """
        data = await self.client.request("twitter/post", {"url": url})
        return TwitterPost(**data)
    
    async def get_feed(self, username: str) -> Optional[TwitterTimeline]:
        """
        Retrieve the feed of a Twitter user.

        Args:
            username (str): The username of the Twitter user.

        Returns:
            Optional[TwitterTimeline]: An instance of the TwitterTimeline class
            representing the user's feed, or None if the user is not found.
        """
        data = await self.client.request("twitter/feed", {"username": username})
        return TwitterTimeline(**data)
    


