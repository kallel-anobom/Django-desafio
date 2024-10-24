from django.shortcuts import render
from django.urls import path
from django.contrib import admin

from core.models import Post, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)