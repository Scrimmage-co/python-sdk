import requests
from components import ConfigService
from schema import BaseService, ScrimmageAPIService
from typing import Union, List, Dict, Any


class APIService(BaseService):
    def __init__(self, config_service: ConfigService):
        self.config_service = config_service

    def create_integration_reward(self, user_id: str, data_type: str, event_id_or_reward: Union[str, Any], reward: Any = None):
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
        try:
            response = requests.post(url, json=payload, headers=headers)

            return response.json()
        except Exception as e:
            print("create_integration_reward exception")
            print(e)
            return None

    def get_user_token(self, user_id: str, tags: List[str] = [], properties: Dict[str, Any] = {}) -> str:
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

        try:
            response = requests.post(url, json=payload, headers=headers)

            return response.json()['token']
        except Exception as e:
            print("get_user_token exception")
            print(e)
            return None

    def get_service_status(self, service: ScrimmageAPIService):
        url = f"{self.config_service.get_service_url(service)}/system/status"
        
        try:
            response = requests.get(url)

            return response.json()
        except Exception as e:
            print("get_service_status exception")
            print(e)
            return None

    def get_overall_service_status(self):
        for service in ScrimmageAPIService:
            try:
                status = self.get_service_status(service)
                if not 'uptime' in status:
                    return False
            except Exception:
                return False

        return True

    def get_rewarder_key_details(self):
        private_key = self.config_service.get_private_key_or_throw()
        namespace = self.config_service.get_namespace_or_throw()

        url = f"{self.config_service.get_service_url(ScrimmageAPIService.api)}/rewarders/keys/@me"

        headers = {
            'Authorization': f"Token {private_key}",
            'Scrimmage-Namespace': namespace
        }

        try:
            response = requests.get(url, headers=headers)

            return response.json()
        except Exception as e:
            print("get_rewarder_key_details exception")
            print(e)
            return None