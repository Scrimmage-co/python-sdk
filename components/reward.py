from components import APIService
from schema import BaseService
from typing import List, Any

class RewardService(BaseService):
    def __init__(self, api_service: APIService):
        self.api_service = api_service
        

    def track_rewardable(self, user_id: str, data_type: str, rewards: List[Any]):
        results = []
        for reward in rewards:
            results.append(
                self.api_service.create_integration_reward(user_id, data_type, reward)
            )

        return results
    
    
    def track_rewardable_once(self, user_id: str, data_type: str, unique_id: str, reward: Any = None):
        return self.api_service.create_integration_reward(user_id, data_type, unique_id, reward)