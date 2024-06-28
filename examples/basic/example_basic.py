from scrimmage_sdk import Scrimmage
import os


# Initialize Scrimmage
Scrimmage.init_rewarder(
    api_server_endpoint=os.getenv('SCRIMMAGE_API_SERVER_ENDPOINT'),
    private_key=os.getenv('SCRIMMAGE_PRIVATE_KEY'),
    namespace=os.getenv('SCRIMMAGE_NAMESPACE'),
)


# Get user token
user_id = 'nanachi'
token = Scrimmage.user.get_user_token(user_id)


# Track rewardable for a user
user_id = 'nanachi'
data_type = 'helloWorld'
rewards = [{
    'amount': 10,
    'currency': 'USD'
}]
response = Scrimmage.reward.track_rewardable(user_id, data_type, rewards=rewards)


# Track rewardable for a user only once (with idempotency key)
user_id = 'nanachi'
data_type = 'helloWorld'
idempotency_key = 'idempotency_key_12345'
reward = {
    'amount': 10,
    'currency': 'USD'
}
response = Scrimmage.reward.track_rewardable_once(user_id, data_type, idempotency_key, reward=reward)


# Using multiple Scrimmage instances at once
scrimmage1 = Scrimmage.create_rewarder(
    api_server_endpoint=os.getenv('SCRIMMAGE_API_SERVER_ENDPOINT_1'),
    private_key=os.getenv('SCRIMMAGE_PRIVATE_KEY_1'),
    namespace=os.getenv('SCRIMMAGE_NAMESPACE_1'),
)
# scrimmage1.user.get_user_token(...)
# scrimmage1.reward.track_rewardable(...)

scrimmage2 = Scrimmage.create_rewarder(
    api_server_endpoint=os.getenv('SCRIMMAGE_API_SERVER_ENDPOINT_2'),
    private_key=os.getenv('SCRIMMAGE_PRIVATE_KEY_2'),
    namespace=os.getenv('SCRIMMAGE_NAMESPACE_2'),
)
# scrimmage2.user.get_user_token(...)
# scrimmage2.reward.track_rewardable(...)