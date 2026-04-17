from dataclasses import dataclass, field


@dataclass(slots=True)
class ClientContactDTO:
    type: str
    label: str
    value: str
    metadata: dict = field(default_factory=dict)
