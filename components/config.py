from schema import ScrimmageAPIService, PartialRewarderConfig, PrivateKey, BaseService
from typing import Dict, List, Optional
import logging
import re

logger = logging.getLogger('scrimmage')

class InternalRewarderConfig(PartialRewarderConfig):
    services: Dict[ScrimmageAPIService, str] = {}
    private_keys: Optional[List[PrivateKey]] = []


defaultRewarderConfig: InternalRewarderConfig = InternalRewarderConfig(
    log_level='debug',
    services={
        ScrimmageAPIService.api: 'api',
        ScrimmageAPIService.p2e: 'p2e',
        ScrimmageAPIService.fed: 'fed',
        ScrimmageAPIService.nbc: 'nbc',
    },
    logger=logger,
    secure=True,
    validate_api_server_endpoint=True
)


class ConfigService(BaseService):
    _rewarder_config: InternalRewarderConfig = None

    def set_config(self, config: PartialRewarderConfig):
        api_server_endpoint = config.api_server_endpoint
        if not api_server_endpoint:
            raise Exception('api_server_endpoint is required')
        
        self.validate_protocol(api_server_endpoint, config.secure)
        
        api_endpoint = api_server_endpoint
        if api_endpoint[-1] == '/':
            # Remove trailing slash if present
            api_endpoint = api_endpoint[:-1]
        
        # Create dictionaries from the models
        default_config = defaultRewarderConfig.model_dump()
        config_dict = config.model_dump()

        # Merge dictionaries with config_dict taking precedence
        merged_config = {**default_config, **config_dict}

        # Add or override specific keys
        merged_config.update({
            'api_server_endpoint': api_endpoint,
            'private_keys': [PrivateKey(alias='default', value=config.private_key)]
        })

        # Pass the merged config to InternalRewarderConfig
        self._rewarder_config = InternalRewarderConfig(**merged_config)

    def is_configured(self) -> bool:
        return self._rewarder_config is not None
    
    def get_config_or_throw(self) -> InternalRewarderConfig:
        if self.is_configured():
            return self._rewarder_config
        else:
            raise Exception('Rewarder not initiated')
    
    def get_private_key_or_throw(self, alias: str = 'default') -> str:
        config = self.get_config_or_throw()
        for private_key in config.private_keys:
            if private_key.alias == alias:
                return private_key.value
        
        raise Exception(f'Private key {alias} not found')
    
    def get_service_url(self, service: ScrimmageAPIService) -> str:
        config = self.get_config_or_throw()
        
        return f"{config.api_server_endpoint}/{service}"
    
    def get_namespace_or_throw(self) -> str:
        config = self.get_config_or_throw()

        return config.namespace
    
    def validate_protocol(self, protocol: str, secure: bool):
        protocolRegex = r'^^https:\/\/.+' if secure else r'^https?:\/\/.+'

        if not re.match(protocolRegex, protocol):
            protocol = 'https://' if secure else 'http://'
            raise Exception(f"Service URL must start with {protocol}")