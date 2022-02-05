#!/usr/bin/python3
"""Reloads all the objects created from precious sessions"""
from .engine.file_storage import FileStorage


__all__ = ['base_model', 'state', 'user', 'place', 'amenity', 'review', 'city']
storage = FileStorage()
storage.reload()
