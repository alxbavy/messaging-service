from __future__ import annotations

from django.db import models

from core.models.base import BaseModel
from core.models.enums import ContactStatus, ContactType, ContactLabel


class Client(BaseModel):
    external_id = models.BigIntegerField("Внешний ID клиента", unique=True)

    full_name = models.CharField("ФИО", max_length=255)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=32, blank=True)
    parent_primary = models.CharField("Родитель 1", max_length=255, blank=True)
    parent_secondary = models.CharField("Родитель 2", max_length=255, blank=True)
    student_status = models.CharField("Статус ученика", max_length=64, blank=True)
    student_tag = models.CharField("Тег ученика", max_length=255, blank=True)
    student_branch = models.CharField("Филиал ученика", max_length=255, blank=True)

    can_receive = models.BooleanField("Подписан на рассылку", default=False)

    class Meta:
        ordering = ("full_name",)


class ClientContact(BaseModel):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name="Клиент",
    )
    type = models.CharField("Тип контакта", max_length=32, choices=ContactType.choices)
    label = models.CharField("Метка", max_length=32, blank=True, choices=ContactLabel.choices)
    value = models.CharField("Значение", max_length=255)

    status = models.CharField(
        "Статус",
        max_length=32,
        choices=ContactStatus.choices,
        default=ContactStatus.ACTIVE,
    )

    metadata = models.JSONField("Метаданные", default=dict, blank=True)
    last_check_at = models.DateTimeField("Последняя проверка", null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("client", "type", "value"),
                name="uq_client_contact_type_value",
            ),
        ]
