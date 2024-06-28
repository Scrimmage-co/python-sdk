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
        """
        Creates a new Scrimmage instance with the given parameters.

        Parameters:
        - api_server_endpoint (str): The endpoint for the Scrimmage API server.
        - namespace (str): The namespace for the Scrimmage instance. E.g. 'staging' or 'production'.
        - private_key (str): Your Scrimmage private API key.
        - log_level (Optional[LogLevel]): The log level for the logger. Defaults to 'info'.
        - logger (Optional[ILogger]): The logger to use. Defaults to the default logger.
        - secure (Optional[bool]): Whether to use secure connections. Defaults to True.
        - validate_api_server_endpoint (Optional[bool]): Whether to validate the API server endpoint. Defaults to True.
        """
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
        """
        Initializes the Scrimmage instance with the given parameters.

        Parameters:
        - api_server_endpoint (str): The endpoint for the Scrimmage API server.
        - namespace (str): The namespace for the Scrimmage instance. E.g. 'staging' or 'production'.
        - private_key (str): Your Scrimmage private API key.
        - log_level (Optional[LogLevel]): The log level for the logger. Defaults to 'info'.
        - logger (Optional[ILogger]): The logger to use. Defaults to the default logger.
        - secure (Optional[bool]): Whether to use secure connections. Defaults to True.
        - validate_api_server_endpoint (Optional[bool]): Whether to validate the API server endpoint. Defaults to True.
        """
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
