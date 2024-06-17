from scrimmage_sdk.container import Container
from scrimmage_sdk.schema import RewarderConfig


def create_scrimmage_instance(config: RewarderConfig):
    # Initialize container with all services
    container = Container()
    container.init_resources()

    # Initialize the ConfigService
    config_service = container.config_service()
    config_service.set_config(config)

    # Initialize the StatusService
    status_service = container.status_service()
    status_service.verify()

    # Initialize the LoggerService
    logger_service = container.logger_service()
    logger_service.info("Rewarder Initiated")

    # Get the User and Reward Services
    user_service = container.user_service()
    reward_service = container.reward_service()

    return (container, user_service, reward_service)
