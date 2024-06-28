from typing import Union, Any, List, Dict

from scrimmage_sdk.components import APIService
from scrimmage_sdk.schema import BaseService


class RewardService(BaseService):
    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def track_rewardable(self, user_id: str, data_type: str, rewards: List[Dict[str, Any]]):
        """
        Tracks rewardable for a user and records them.

        Parameters:
        - user_id (str): The unique identifier for the user.
        - data_type (str): The type of data being rewarded (e.g., "video_view", "purchase").
        - rewards (List[Dict[str, Any]]): A list of dictionaries, each representing a rewardable action.

        Returns:
        - List: A list of all rewardable actions that were successfully recorded.
        """
        results = []
        for reward in rewards:
            results.append(
                self.api_service.create_integration_reward(
                    user_id, data_type, reward)
            )

        return results

    async def track_rewardable_async(self, user_id: str, data_type: str, rewards: List[Dict[str, Any]]):
        """
        Asynchronously tracks rewardable actions for a user and records them.

        Parameters:
        - user_id (str): The unique identifier for the user.
        - data_type (str): The type of data being rewarded (e.g., "video_view", "purchase").
        - rewards (List[Dict[str, Any]]): A list of dictionaries, each representing a rewardable action.

        Returns:
        - List: A list of all rewardable actions that were successfully recorded.
        """
        results = []
        for reward in rewards:
            results.append(
                await self.api_service.create_integration_reward_async(
                    user_id, data_type, reward)
            )

        return results

    def track_rewardable_once(self, user_id: str, data_type: str, unique_id: str, reward: Union[Dict[str, Any], None] = None):
        """
        Tracks a single rewardable action for a user and records it.

        Parameters:
        - user_id (str): The unique identifier for the user.
        - data_type (str): The type of data being rewarded (e.g., "video_view", "purchase").
        - unique_id (str): A unique identifier for the rewardable action.
        - reward (Dict[str, Any]): A dictionary representing the rewardable action.

        Returns:
        - The recorded rewardable action.
        """
        return self.api_service.create_integration_reward(user_id, data_type, unique_id, reward)

    async def track_rewardable_once_async(self, user_id: str, data_type: str, unique_id: str, reward: Union[Dict[str, Any], None] = None):
        """
        Asynchronously tracks a single rewardable action for a user and records it.

        Parameters:
        - user_id (str): The unique identifier for the user.
        - data_type (str): The type of data being rewarded (e.g., "video_view", "purchase").
        - unique_id (str): A unique identifier for the rewardable action.
        - reward (Dict[str, Any]): A dictionary representing the rewardable action.

        Returns:
        - The recorded rewardable action.
        """
        return await self.api_service.create_integration_reward_async(user_id, data_type, unique_id, reward)