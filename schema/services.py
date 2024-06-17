from enum import Enum

class BaseService:
    def __init__(self) -> None:
        print(f"{__name__}.{self.__class__.__name__} init")


class ScrimmageAPIService(Enum):
    api = 'api'
    p2e = 'p2e'
    fed = 'fed'
    nbc = 'nbc'
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    
    @classmethod
    def from_str(cls, service: str):
        return cls(service)