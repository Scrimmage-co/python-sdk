# Scrimmage Rewards

The low-code loyalty program maker.

This library is a part of the [Scrimmage Rewards Program](https://scrimmage.co)
that is providing a solution for loyalty programs and rewards.

Tutorial can be found at [Scrimmage Rewards Tutorial](https://scrimmage-rewards.readme.io/docs).

## Getting started

### Install
    pip install scrimmage-sdk
(This PyPi package is not currently available, but will be available soon)

### Configuration
    from scrimmage_sdk import Scrimmage

    Scrimmage.init_rewarder(
        api_server_endpoint="YOUR_SCRIMMAGE_API_SERVER_ENDPOINT",
        private_key="YOUR_SCRIMMAGE_PRIVATE_KEY",
        namespace="YOUR_SCRIMMAGE_NAMESPACE",
    )

### Usage

#### Get user token
    from scrimmage_sdk import Scrimmage

    token = Scrimmage.get_user_token("unique-user-id")

#### Track rewardable for a user
    from scrimmage_sdk import Scrimmage

    user_id = 'nanachi'
    data_type = 'helloWorld'
    rewards = [{
        'amount': 10,
        'currency': 'USD'
    }]
    response = Scrimmage.reward.track_rewardable(user_id, data_type, rewards=rewards)

#### Track rewardable for a user only once (with idempotency key)

#### Using multiple Scrimmage instances at once

### Examples
See the [examples](https://github.com/Scrimmage-co/python-sdk/tree/main/examples) folder for different use cases.


## Usage on other platforms

- Using `<iframe />`: [github.com/Scrimmage-co/scrimmage-rewards-iframe](https://github.com/Scrimmage-co/scrimmage-rewards-iframe)
- Using Android: [github.com/Scrimmage-co/scrimmage-rewards-android](https://github.com/Scrimmage-co/scrimmage-rewards-android)
- Using iOS: [github.com/Scrimmage-co/scrimmage-rewards-ios](https://github.com/Scrimmage-co/scrimmage-rewards-ios)
- Using Flutter: [github.com/Scrimmage-co/scrimmage-rewards-flutter](https://github.com/Scrimmage-co/scrimmage-rewards-flutter)
- Using NodeJS: [github.com/Scrimmage-co/rewards/backend-library](https://github.com/Scrimmage-co/rewards/backend-library)
- Using Ruby: [https://github.com/Scrimmage-co/ruby-sdk](https://https://github.com/Scrimmage-co/ruby-sdk)
- Using Java: [https://github.com/Scrimmage-co/java-sdk](https://https://github.com/Scrimmage-co/java-sdk)
- Using PHP: [https://github.com/Scrimmage-co/php-sdk](https://https://github.com/Scrimmage-co/php-sdk)
- Using Golang: [https://github.com/Scrimmage-co/golang-sdk](https://https://github.com/Scrimmage-co/golang-sdk)

## Development
1. Add .env.test to your environment with the following variables
```
SCRIMMAGE_API_SERVER_ENDPOINT=SCRIMMAGE_API_SERVER_ENDPOINT
SCRIMMAGE_PRIVATE_KEY=YOUR_SCRIMMAGE_PRIVATE_KEY
SCRIMMAGE_NAMESPACE=YOUR_SCRIMMAGE_NAMESPACE
```

2. Install dependencies
```
pip install -r requirements.txt
```

2. Start your development - you can add tests in the tests folder

3. Run tests using pytest from the root directory
```
pytest
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/scrimmage-rewards.

## License

The SDK is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).