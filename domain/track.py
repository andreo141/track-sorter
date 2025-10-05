from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from domain.errors import DomainError
from domain.value_objects import Bpm, Key
from pathlib import Path
from datetime import time
from domain.tag import Tag
from typing import Set


@dataclass
class Track:
    id: UUID
    title: str
    artist: str
    album: str
    bpm: Bpm
    key: Key
    genre: str
    duration: time
    file_path: Path
    tags: Set[Tag]


    def __post_init__(self) -> None:
        self.rename(self.title)


    def rename(self, new_title: str) -> None:
        clean_title = new_title.strip().lower()

        if not self.title:
            raise DomainError("Title cannot be empty")

        self.title = clean_title


    def add_tag(self, tag: Tag) -> None:
        if not isinstance(tag, Tag):
            raise DomainError("Please enter a valid tag")
        
        if tag in self.tags:
            raise DomainError("Tag already exists")
        
        self.tags.add(tag)


    def remove_tag(self, tag_id: UUID) -> None:
        self.tags = {tag for tag in self.tags if tag.id != tag_id}


    def __repr__(self) -> str:
        return f"Track(title={self.title}, artist={self.artist}, album={self.album}, bpm={self.bpm}, key={self.key}, genre={self.genre}, duration={self.duration}, file_path={self.file_path}, tags={self.tags})"