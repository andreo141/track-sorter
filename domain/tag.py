from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from domain.errors import DomainError
from domain.value_objects import Key


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


    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name
        return False


    def __hash__(self):
        return hash(self.name)


    def __repr__(self):
        return f"Tag(name={self.name}, created_at={self.created_at})"