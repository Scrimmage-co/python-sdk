from create import create_scrimmage_instance
from schema import RewarderConfig, ILogger, LogLevel
from components import UserService, RewardService
from container import Container
from typing import Optional
import logging

default_logger = logging.getLogger("scrimmage-sdk")

class Scrimmage:
    _container: Container = None
    user: UserService = None
    reward: RewardService = None

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
        return create_scrimmage_instance(config)

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