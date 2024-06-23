from typing import Any, List

from scrimmage_sdk.components import APIService
from scrimmage_sdk.schema import BaseService


class RewardService(BaseService):
    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def track_rewardable(self, user_id: str, data_type: str, rewards: List[Any]):
        results = []
        for reward in rewards:
            results.append(
                self.api_service.create_integration_reward(
                    user_id, data_type, reward)
            )

        return results

    async def track_rewardable_async(self, user_id: str, data_type: str, rewards: List[Any]):
        results = []
        for reward in rewards:
            results.append(
                await self.api_service.create_integration_reward_async(
                    user_id, data_type, reward)
            )

        return results

    def track_rewardable_once(self, user_id: str, data_type: str, unique_id: str, reward: Any = None):
        return self.api_service.create_integration_reward(user_id, data_type, unique_id, reward)

    async def track_rewardable_once_async(self, user_id: str, data_type: str, unique_id: str, reward: Any = None):
        return await self.api_service.create_integration_reward_async(user_id, data_type, unique_id, reward)