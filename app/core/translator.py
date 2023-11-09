"""Service for translator."""
import importlib
from typing import Any


class Translator:
    """Service for translator."""

    _instances: dict[str, "Translator"] = {}  # noqa: RUF012

    def __new__(cls, lang: str) -> "Translator":
        """Init translator."""
        if lang not in cls._instances:
            cls._instances[lang] = super().__new__(cls)
        return cls._instances[lang]

    def __init__(self, lang: str):
        self.lang = lang

    def t(self, key: str, **kwargs: dict[str, Any]) -> str:
        """Translate."""
        file_key, *translation_keys = key.split(".")

        locale_module = importlib.import_module(f"app.langs.{self.lang}.{file_key}")

        translation = locale_module.locale
        for translation_key in translation_keys:
            translation = translation.get(translation_key, None)
            if translation is None:
                return f"Key {key} not found in {self.lang} locale"
        if kwargs.keys():
            translation = translation.format(**kwargs)
        return translation
