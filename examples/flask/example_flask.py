from flask import Flask, jsonify, request
from scrimmage_sdk import Scrimmage
import os


app = Flask(__name__)

# Initialize Scrimmage SDK
Scrimmage.init_rewarder(
    api_server_endpoint=os.getenv('SCRIMMAGE_API_SERVER_ENDPOINT'),
    private_key=os.getenv('SCRIMMAGE_PRIVATE_KEY'),
    namespace=os.getenv('SCRIMMAGE_NAMESPACE'),
)


@app.route('/get_user_token/<user_id>', methods=['GET'])
def get_user_token(user_id):
    token = Scrimmage.user.get_user_token(user_id)
    return jsonify({'user_id': user_id, 'token': token})


@app.route('/track_rewardable', methods=['POST'])
def track_rewardable():
    data = request.json
    user_id = data.get('user_id')
    data_type = data.get('data_type')
    rewards = data.get('rewards')
    response = Scrimmage.reward.track_rewardable(user_id, data_type, rewards=rewards)
    return jsonify(response)


@app.route('/track_rewardable_once', methods=['POST'])
def track_rewardable_once():
    data = request.json
    user_id = data.get('user_id')
    data_type = data.get('data_type')
    idempotency_key = data.get('idempotency_key')
    reward = data.get('reward')
    response = Scrimmage.reward.track_rewardable_once(user_id, data_type, idempotency_key, reward=reward)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)