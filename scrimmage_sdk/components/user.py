from scrimmage_sdk.components import APIService
from scrimmage_sdk.schema import BaseService
from typing import List, Dict, Any

class UserService(BaseService):
    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def get_user_token(self, user_id: str, tags: List[str] = [], properties: Dict[str, Any] = {}):
        """
        Retrieves a user token for a given user ID with optional tags and properties.

        This method calls the api_service's get_user_token method, passing the user ID,
        and optionally, tags and properties to further customize the request.

        Parameters:
        - user_id (str): The unique identifier for the user.
        - tags (List[str]): A list of tags associated with the user. Defaults to an empty list.
        - properties (Dict[str, Any]): A dictionary of additional properties related to the user. Defaults to an empty dictionary.

        Returns:
        - The result from the api_service's get_user_token method.
        """
        return self.api_service.get_user_token(user_id, tags=tags, properties=properties)
    
    async def get_user_token_async(self, user_id: str, tags: List[str] = [], properties: Dict[str, Any] = {}):
        """
        Retrieves a user token asynchronously for a given user ID with optional tags and properties.

        This method calls the api_service's get_user_token method, passing the user ID,
        and optionally, tags and properties to further customize the request.

        Parameters:
        - user_id (str): The unique identifier for the user.
        - tags (List[str]): A list of tags associated with the user. Defaults to an empty list.
        - properties (Dict[str, Any]): A dictionary of additional properties related to the user. Defaults to an empty dictionary.

        Returns:
        - The result from the api_service's get_user_token method.
        """
        return await self.api_service.get_user_token_async(user_id, tags=tags, properties=properties)