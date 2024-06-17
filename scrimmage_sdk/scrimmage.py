import logging
from typing import Optional

from scrimmage_sdk.components import RewardService, UserService
from scrimmage_sdk.container import Container
from scrimmage_sdk.create import create_scrimmage_instance
from scrimmage_sdk.schema import ILogger, LogLevel, RewarderConfig

default_logger = logging.getLogger("scrimmage-sdk")


class Scrimmage:
    _container: Container = None
    user: UserService = None
    reward: RewardService = None

    def __init__(self, container: Container, user: UserService, reward: RewardService):
        self._container = container
        self.user = user
        self.reward = reward

    @staticmethod
    def create_rewarder(api_server_endpoint: str,
                        namespace: str,
                        private_key: str,
                        log_level: Optional[LogLevel] = 'info',
                        logger: Optional[ILogger] = default_logger,
                        secure: Optional[bool] = True,
                        validate_api_server_endpoint: Optional[bool] = True):
        # Create config
        config = RewarderConfig(
            api_server_endpoint=api_server_endpoint,
            namespace=namespace,
            private_key=private_key,
            log_level=log_level,
            logger=logger,
            secure=secure,
            validate_api_server_endpoint=validate_api_server_endpoint
        )
        container, user, reward = create_scrimmage_instance(config)
        return Scrimmage(container, user, reward)

    @staticmethod
    def init_rewarder(api_server_endpoint: str,
                      namespace: str,
                      private_key: str,
                      log_level: Optional[LogLevel] = 'info',
                      logger: Optional[ILogger] = default_logger,
                      secure: Optional[bool] = True,
                      validate_api_server_endpoint: Optional[bool] = True):
        # Create config
        config = RewarderConfig(
            api_server_endpoint=api_server_endpoint,
            namespace=namespace,
            private_key=private_key,
            log_level=log_level,
            logger=logger,
            secure=secure,
            validate_api_server_endpoint=validate_api_server_endpoint
        )

        # Create instance with all services from config
        container, user, reward = create_scrimmage_instance(config)

        # Set variables in static class
        Scrimmage._container = container
        Scrimmage.user = user
        Scrimmage.reward = reward
