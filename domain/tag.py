from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from domain.errors import DomainError


@dataclass
class Tag:
    id: UUID
    name: str
    created_at: datetime

    def rename(self, new_name: str) -> None:
        self.name = new_name.strip().lower()
        if not self.name:
            raise DomainError("Tag cannot be empty")

    def __post_init__(self):
        self.rename(self.name)