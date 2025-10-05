from domain.errors import DomainError


class Bpm:
    MIN_BPM = 30
    MAX_BPM = 300

    def __init__(self, bpm: int):
        if not isinstance(bpm, int):
            raise DomainError("BPM must be an integer")
        
        if not (self.MIN_BPM <= bpm <= self.MAX_BPM):
            raise DomainError(f"BPM must be between {self.MIN_BPM} and {self.MAX_BPM}")
        
        self._bpm = bpm

    @property
    def value(self) -> int:
        return self._bpm
    
    def __eq__(self, other):
        if isinstance(other, Bpm):
            return self._bpm == other._bpm
        return False
    
    def __repr__(self):
        return f"Bpm(value={self._bpm})"
        
    
class Key():
    VALID_KEYS = {
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
        "Cm", "C#m", "Dm", "D#m", "Em", "Fm", "F#m", "Gm", "G#m", "Am", "A#m", "Bm"
    }

    def __init__(self, key: str):
        key = key.strip()
        if key not in self.VALID_KEYS:
            raise DomainError(f"Invalid musical key: {key}")
        self._key = key

    @property
    def value(self) -> str:
        return self._key
    
    def __eq__(self, other):
        if isinstance(other, Key):
            return self._key == other._key
        return False

    def __hash__(self):
        return hash(self._key)

    def __repr__(self):
        return f"Key(value={self._key})"