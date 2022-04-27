from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only = ["id", "created_at", "updated_at"]