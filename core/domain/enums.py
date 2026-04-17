from enum import StrEnum, auto


class ChannelType(StrEnum):
    TELEGRAM_BOT = auto()


class TelegramBotChannelSecrets(StrEnum):
    BOT_TOKEN = auto()


class TelegramBotChannelSettings(StrEnum):
    pass


class CampaignStatus(StrEnum):
    DRAFT = auto()
    QUEUED = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    PARTIAL = auto()
    FAILED = auto()


class DeliveryStatus(StrEnum):
    PENDING = auto()
    RETRY = auto()
    SENT = auto()
    FAILED = auto()
    SKIPPED = auto()
