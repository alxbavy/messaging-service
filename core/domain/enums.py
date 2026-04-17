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


class ImportFileHeader(StrEnum):
    CLIENT_ID = "№ клиента"
    FULL_NAME = "ФИО"
    BIRTH_DATE = "Дата рождения"
    GENDER = "Пол"
    PARENT_PRIMARY = "Родитель (имя, телефон)"
    PARENT_SECONDARY = "Родитель 2"
    STATUS = "Статус ученика"
    TAG = "Тег ученика"
    BRANCH = "Филиал ученика"
    CAN_RECEIVE = "Подписан на рассылку"

    PHONE_CHILD = "Телефон"
    PHONE_SECONDARY = "Телефон Родителя 2"
    PHONE_EXTRA = "Доп. телефон"
    EMAIL = "Email"
    TELEGRAM_PRIMARY = "Telegram"
    TELEGRAM_SECONDARY = "Телеграмм Родителя 2"
    VK = "VK"
    MAX = "Мессенджер MAX"
