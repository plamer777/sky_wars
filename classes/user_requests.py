from dataclasses import dataclass
# -------------------------------------------------------------------------


@dataclass
class UserRequest:
    name: str
    unit_class: str
    weapon: str
    armor: str
