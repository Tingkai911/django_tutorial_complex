import uuid
from django.db import models


# Uses a UUID instead of the default ID field
class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)  # Primary Key

    class Meta:
        abstract = True  # Can be inherited
