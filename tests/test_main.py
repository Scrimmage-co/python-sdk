import os
import pytest
from dotenv import load_dotenv
from scrimmage_sdk import Scrimmage

# Load environment variables from .env.test
load_dotenv(dotenv_path='.env.test')


@pytest.fixture(autouse=True)
def setup_scrimmage():
    Scrimmage.init_rewarder(
        api_server_endpoint=os.getenv('API_SERVER_ENDPOINT'),
        private_key=os.getenv('PRIVATE_KEY'),
        namespace=os.getenv('NAMESPACE'),
    )


def test_init_rewarder_check():
    assert Scrimmage is not None


def test_user_get_all_for_rewarder_check():
    token = Scrimmage.user.get_user_token('test_user')
    assert token is not None
    assert len(token) > 0


def test_reward_track_rewardable_check():
    response = Scrimmage.reward.track_rewardable('test_user', 'test', {
        'value': 1,
    })
    assert response is not None

if __name__ == '__main__':
    pytest.main()
