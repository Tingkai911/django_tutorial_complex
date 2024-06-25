from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField


# Allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON
# Also provide deserialization
class ContactSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)  # Point the name to the "title" field in the model
    message = CharField(source="description", required=True)  # Point the message to the "description" field in the model
    email = EmailField(required=True)

    class Meta:
        model = models.Contact
        fields = (
            'name',
            'email',
            'message'
        )
