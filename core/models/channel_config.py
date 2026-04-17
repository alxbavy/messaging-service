from __future__ import annotations

from django.db import models

from core.db.fields import EncryptedJSONField
from core.models.base import BaseModel
from core.models.enums import ChannelType


class ChannelConfig(BaseModel):
    code = models.SlugField("Код", max_length=64)
    name = models.CharField("Название", max_length=255)
    type = models.CharField("Тип", max_length=32, choices=ChannelType.choices)
    is_active = models.BooleanField("Активен", default=True)
    secrets = EncryptedJSONField("Секреты", default=dict, blank=True)
    settings = models.JSONField("Настройки", default=dict, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("type", "code"),
                name="uq_channel_config_type_code",
            ),
        ]
