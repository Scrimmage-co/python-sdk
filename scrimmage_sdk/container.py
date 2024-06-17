from dependency_injector import containers, providers

from scrimmage_sdk.components import (APIService, ConfigService, LoggerService,
                         RewardService, StatusService, UserService)


class Container(containers.DeclarativeContainer):
    config_service = providers.Singleton(ConfigService)

    api_service = providers.Factory(APIService, config_service=config_service)
    logger_service = providers.Factory(
        LoggerService, config_service=config_service)
    status_service = providers.Factory(
        StatusService, config_service=config_service, api_service=api_service)
    user_service = providers.Factory(UserService, api_service=api_service)
    reward_service = providers.Factory(RewardService, api_service=api_service)
