from __future__ import annotations

from django.conf import settings
from django.db import models

from core.models.base import BaseModel
from core.models.client import ClientContact
from core.models.enums import CampaignStatus, DeliveryStatus
from core.models.channel_config import ChannelConfig


class Campaign(BaseModel):
    title = models.CharField("Название", max_length=255)
    channel_config = models.ForeignKey(
        ChannelConfig,
        on_delete=models.PROTECT,
        related_name="campaigns",
    )
    message_text = models.TextField("Текст сообщения")

    status = models.CharField(
        "Статус",
        max_length=32,
        choices=CampaignStatus.choices,
        default=CampaignStatus.DRAFT,
    )

    scheduled_at = models.DateTimeField("Запланировано на", null=True, blank=True)
    started_at = models.DateTimeField("Старт отправки", null=True, blank=True)
    finished_at = models.DateTimeField("Окончание отправки", null=True, blank=True)

    filter_payload = models.JSONField("Фильтр аудитории", default=dict, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_campaigns",
    )


class Delivery(BaseModel):
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="deliveries",
    )
    client_contact = models.ForeignKey(
        ClientContact,
        on_delete=models.PROTECT,
        related_name="deliveries",
    )

    status = models.CharField(
        "Статус",
        max_length=32,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.PENDING,
    )

    recipient_snapshot = models.CharField("Снимок адреса", max_length=255, blank=True)
    provider_recipient_id = models.CharField("ID получателя у провайдера", max_length=255, blank=True)
    provider_message_id = models.CharField("ID сообщения у провайдера", max_length=255, blank=True)

    attempts_count = models.PositiveIntegerField("Количество попыток", default=0)
    sent_at = models.DateTimeField("Отправлено", null=True, blank=True)
    last_attempt_at = models.DateTimeField("Последняя попытка", null=True, blank=True)

    error_code = models.CharField("Код ошибки", max_length=64, blank=True)
    error_message = models.TextField("Текст ошибки", blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("campaign", "client_contact"),
                name="uq_delivery_campaign_contact",
            ),
        ]