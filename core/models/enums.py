from django.db import models
from core.domain.enums import ChannelType as DomainChannelType
from core.domain.enums import CampaignStatus as DomainCampaignStatus
from core.domain.enums import DeliveryStatus as DomainDeliveryStatus


class ContactType(models.TextChoices):
    PHONE = "phone", "Телефон"
    EMAIL = "email", "Email"
    TELEGRAM = "telegram", "Telegram"
    VK = "vk", "VK"
    MAX = "max", "MAX"


class ContactStatus(models.TextChoices):
    ACTIVE = "active", "Активен"
    BLOCKED = "blocked", "Заблокирован"
    UNSUBSCRIBED = "unsubscribed", "Отписан"
    INVALID = "invalid", "Невалиден"


class ContactLabel(models.TextChoices):
    PRIMARY = "primary", "Родитель 1"
    SECONDARY = "secondary", "Родитель 2"
    EXTRA = "extra", "Дополнительный"


class ChannelType(models.TextChoices):
    TELEGRAM_BOT = DomainChannelType.TELEGRAM_BOT, "Telegram Bot"
    # TELEGRAM_USER = "telegram_user", "Telegram User"
    # EMAIL = "email", "Email"
    # WHATSAPP = "whatsapp", "WhatsApp"
    # MAX = "max", "MAX"


class CampaignStatus(models.TextChoices):
    DRAFT = DomainCampaignStatus.DRAFT, "Черновик"
    QUEUED = DomainCampaignStatus.QUEUED, "В очереди"
    PROCESSING = DomainCampaignStatus.PROCESSING, "Отправляется"
    COMPLETED = DomainCampaignStatus.COMPLETED, "Завершена"
    PARTIAL = DomainCampaignStatus.PARTIAL, "Завершена с ошибками"
    FAILED = DomainCampaignStatus.FAILED, "Ошибка"


class DeliveryStatus(models.TextChoices):
    PENDING = DomainDeliveryStatus.PENDING, "Ожидает отправки"
    RETRY = DomainDeliveryStatus.RETRY, "Повтор"
    SENT = DomainDeliveryStatus.SENT, "Отправлено"
    FAILED = DomainDeliveryStatus.FAILED, "Ошибка"
    SKIPPED = DomainDeliveryStatus.SKIPPED, "Пропущено"
