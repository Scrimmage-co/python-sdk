from typing import Any, Dict, List, Union

import httpx

from scrimmage_sdk.components import ConfigService
from scrimmage_sdk.schema import BaseService, ScrimmageAPIService


class APIService(BaseService):
    def __init__(self, config_service: ConfigService):
        self.config_service = config_service

    def _prepare_request_create_integration_reward(self, user_id: str, data_type: str, event_id_or_reward: Union[str, Union[Dict[str, Any], None]], reward: Union[Dict[str, Any], None] = None):
        private_key = self.config_service.get_private_key_or_throw()
        namespace = self.config_service.get_namespace_or_throw()

        event_id = event_id_or_reward if type(
            event_id_or_reward) == str else None
        rewardable = reward if type(
            event_id_or_reward) == str else event_id_or_reward

        url = f"{self.config_service.get_service_url(ScrimmageAPIService.api)}/integrations/rewards"

        headers = {
            'Authorization': f"Token {private_key}",
            'Scrimmage-Namespace': namespace
        }
        payload = {
            "eventId": f"py_{event_id}",
            "userId": f"py_{user_id}",
            "dataType": data_type,
            "body": rewardable
        }
        return url, payload, headers

    def create_integration_reward(self, user_id: str, data_type: str, event_id_or_reward: Union[str, Union[Dict[str, Any], None]], reward: Union[Dict[str, Any], None] = None):
        url, payload, headers = self._prepare_request_create_integration_reward(user_id, data_type, event_id_or_reward, reward)
        return self._post_sync(url, payload, headers)
    
    async def create_integration_reward_async(self, user_id: str, data_type: str, event_id_or_reward: Union[str, Union[Dict[str, Any], None]], reward: Union[Dict[str, Any], None] = None):
        url, payload, headers = self._prepare_request_create_integration_reward(user_id, data_type, event_id_or_reward, reward)
        return await self._post_async(url, payload, headers)


    def _prepare_get_user_token(self, user_id: str, tags: List[str] = [], properties: Dict[str, Any] = {}):
        private_key = self.config_service.get_private_key_or_throw()
        namespace = self.config_service.get_namespace_or_throw()

        url = f"{self.config_service.get_service_url(ScrimmageAPIService.api)}/integrations/users"
        headers = {
            'Authorization': f"Token {private_key}",
            'Scrimmage-Namespace': namespace
        }
        payload = {
            'id': user_id,
            "tags": tags,
            "properties": properties
        }
        return url, payload, headers

    def get_user_token(self, user_id: str, tags: List[str] = [], properties: Dict[str, Any] = {}) -> str:
        url, payload, headers = self._prepare_get_user_token(user_id, tags, properties)
        response = self._post_sync(url, payload, headers)
        return response['token']

    async def get_user_token_async(self, user_id: str, tags: List[str] = [], properties: Dict[str, Any] = {}) -> str:
        url, payload, headers = self._prepare_get_user_token(user_id, tags, properties)
        response = await self._post_async(url, payload, headers)
        return response['token']

    def _prepare_get_service_status(self, service: ScrimmageAPIService):
        url = f"{self.config_service.get_service_url(service)}/system/status"
        return url
    
    def get_service_status(self, service: ScrimmageAPIService):
        url = self._prepare_get_service_status(service)
        return self._get_sync(url)
    
    async def get_service_status_async(self, service: ScrimmageAPIService):
        url = self._prepare_get_service_status(service)
        return await self._get_async(url)


    def _prepare_get_overall_service_status(self):
        # Nothing to prepare
        pass

    def get_overall_service_status(self):
        for service in ScrimmageAPIService:
            try:
                status = self.get_service_status(service)
                if not 'uptime' in status:
                    return False
            except Exception:
                return False

        return True
    
    async def get_overall_service_status_async(self):
        for service in ScrimmageAPIService:
            try:
                status = await self.get_service_status_async(service)
                if not 'uptime' in status:
                    return False
            except Exception:
                return False

        return True


    def _prepare_get_rewarder_key_details(self):
        private_key = self.config_service.get_private_key_or_throw()
        namespace = self.config_service.get_namespace_or_throw()

        url = f"{self.config_service.get_service_url(ScrimmageAPIService.api)}/rewarders/keys/@me"

        headers = {
            'Authorization': f"Token {private_key}",
            'Scrimmage-Namespace': namespace
        }

        return url, headers
    
    def get_rewarder_key_details(self):
        url, headers = self._prepare_get_rewarder_key_details()
        return self._get_sync(url, headers)
    
    async def get_rewarder_key_details_async(self):
        url, headers = self._prepare_get_rewarder_key_details()
        return await self._get_async(url, headers)

    # Methods for requests
    def _get_sync(self, url: str, headers: dict = {}):
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    async def _get_async(self, url: str, headers: dict = {}):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()

    def _post_sync(self, url: str, json: dict, headers: dict):
        response = httpx.post(url, json=json, headers=headers)
        response.raise_for_status()
        return response.json()

    async def _post_async(self, url: str, json: dict, headers: dict):
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=json, headers=headers)
            response.raise_for_status()
            return response.json()