from scrimmage_sdk.components import APIService
from scrimmage_sdk.schema import BaseService
from typing import List, Dict, Any

class UserService(BaseService):
    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def get_user_token(self, user_id: str, tags: List[str] = [], properties: Dict[str, Any] = {}):
        return self.api_service.get_user_token(user_id, tags=tags, properties=properties)