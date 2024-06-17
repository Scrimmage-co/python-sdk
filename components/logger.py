from components import ConfigService
from schema import BaseService, LogLevel
from typing import Dict

log_level_order: Dict[LogLevel, int] = {
  'debug': 0,
  'info': 1,
  'warn': 2,
  'error': 3,
}

class LoggerService(BaseService):
    def __init__(self, config_service: ConfigService):
        self.config_service = config_service

    def warn(self, message, *args, **kwargs):
        config = self.config_service.get_config_or_throw()
        if log_level_order[config.log_level] <= log_level_order['warn']:
            config.logger.warn(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        config = self.config_service.get_config_or_throw()
        if log_level_order[config.log_level] <= log_level_order['debug']:
            config.logger.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        config = self.config_service.get_config_or_throw()
        if log_level_order[config.log_level] <= log_level_order['info']:
            config.logger.info(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        config = self.config_service.get_config_or_throw()
        if log_level_order[config.log_level] <= log_level_order['error']:
            config.logger.error(message, *args, **kwargs)