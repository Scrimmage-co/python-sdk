import asyncio
from scrimmage_sdk import Scrimmage
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()


# Initialize Scrimmage
Scrimmage.init_rewarder(
    api_server_endpoint=os.getenv('SCRIMMAGE_API_SERVER_ENDPOINT'),
    private_key=os.getenv('SCRIMMAGE_PRIVATE_KEY'),
    namespace=os.getenv('SCRIMMAGE_NAMESPACE'),
)


async def main():
    # Get user token
    user_id = 'nanachi'
    token = await Scrimmage.user.get_user_token_async(user_id)


    # Track rewardable for a user
    user_id = 'nanachi'
    data_type = 'helloWorld'
    rewards = [{
        'amount': 10,
        'currency': 'USD'
    }]
    response = await Scrimmage.reward.track_rewardable_async(user_id, data_type, rewards=rewards)
    

    # Track rewardable for a user only once (with idempotency key)
    idempotency_key = 'idempotency_key_12345'
    reward = {
        'amount': 10,
        'currency': 'USD'
    }
    response = await Scrimmage.reward.track_rewardable_once_async(user_id, data_type, idempotency_key, reward=reward)
    

    # Using multiple Scrimmage instances at once
    scrimmage1 = Scrimmage.create_rewarder(
        api_server_endpoint=os.getenv('SCRIMMAGE_API_SERVER_ENDPOINT_1'),
        private_key=os.getenv('SCRIMMAGE_PRIVATE_KEY_1'),
        namespace=os.getenv('SCRIMMAGE_NAMESPACE_1'),
    )
    # await scrimmage1.user.get_user_token_async(...)
    # await scrimmage1.reward.track_rewardable_async(...)

    scrimmage2 = Scrimmage.create_rewarder(
        api_server_endpoint=os.getenv('SCRIMMAGE_API_SERVER_ENDPOINT_2'),
        private_key=os.getenv('SCRIMMAGE_PRIVATE_KEY_2'),
        namespace=os.getenv('SCRIMMAGE_NAMESPACE_2'),
    )
    # await scrimmage2.user.get_user_token_async(...)
    # await scrimmage2.reward.track_rewardable_async(...)


if __name__ == '__main__':
    # Run the async main function
    asyncio.run(main())