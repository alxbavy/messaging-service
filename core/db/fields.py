from __future__ import annotations

from django.db import models


class EncryptedJSONField(models.TextField):
    description = "JSON encrypted at application level"
