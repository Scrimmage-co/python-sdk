from pydantic import BaseModel
from typing import Optional
from . import LogLevel
from logging import Logger

class RewarderConfig(BaseModel):
    model_config = {
        'arbitrary_types_allowed': True
    }

    api_server_endpoint: str
    private_key: str
    namespace: str
    log_level: Optional[LogLevel] = 'info'
    logger: Optional[Logger] = None
    secure: Optional[bool] = True
    validate_api_server_endpoint: Optional[bool] = True

class PartialRewarderConfig(BaseModel):
    model_config = {
        'arbitrary_types_allowed': True
    }

    api_server_endpoint: Optional[str] = None
    private_key: Optional[str] = None
    namespace: Optional[str] = None
    log_level: Optional[LogLevel] = 'info'
    logger: Optional[Logger] = None
    secure: Optional[bool] = True
    validate_api_server_endpoint: Optional[bool] = True