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

# Get user token
token = Scrimmage.user.get_user_token('nanachi')

# Track rewardable for a user
response = Scrimmage.reward.track_rewardable('nanachi', 'helloWorld', {
    'amount': 10,
    'currency': 'USD'
})

# Track rewardable for a user only once (with idempotency key)
response = Scrimmage.reward.track_rewardable_once('nanachi', 'helloWorld', 'idempotency_key_12345', {
    'amount': 10,
    'currency': 'USD'
})


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