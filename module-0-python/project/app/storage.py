"""Tiny JSON-file store for favorites (a real DB comes in later modules)."""
from pathlib import Path

from app.models import Favorite, FavoriteIn


class FavoritesStore:
    def __init__(self, path: str) -> None:
        self.path = Path(path)

    def list(self) -> list[Favorite]:
        """Return all favorites. Missing or broken file -> []."""
        raise NotImplementedError  # TODO

    def add(self, data: FavoriteIn) -> Favorite:
        """Save a new favorite with id = (highest existing id) + 1, starting at 1. Return it."""
        raise NotImplementedError  # TODO

    def delete(self, fav_id: int) -> bool:
        """Remove the favorite. Return True if it existed, else False."""
        raise NotImplementedError  # TODO
