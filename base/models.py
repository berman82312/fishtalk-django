import uuid
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    UUID Model
    Don't use sequential keys as public identifiers. As a result, any data
    that could be accessed directly via API should be using UUID, rather than
    the ID Djnago provided.

    On the other hand, sequential ID still has many benefit in DB query.
    That's why we still keep it and do not utilize UUID as the primary key.
    """

    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, db_index=True
    )

    class Meta:
        abstract = True