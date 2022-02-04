#!/usr/bin/python3
"""Reloads all the objects created from precious sessions"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
