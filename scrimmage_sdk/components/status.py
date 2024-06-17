from scrimmage_sdk.components import ConfigService, APIService
from scrimmage_sdk.schema import BaseService

class StatusService(BaseService):
    def __init__(self, config_service: ConfigService, api_service: APIService):
        self.config_service = config_service
        self.api_service = api_service

    def verify(self):
        config = self.config_service.get_config_or_throw()
        if(not config.validate_api_server_endpoint):
            return

        service_status = self.api_service.get_overall_service_status()
        if(not service_status):
            config.logger.error("API Service is not running")
        
        try:
            self.api_service.get_rewarder_key_details()
        except Exception as e:
            config.logger.error('Rewarder API key is invalid')