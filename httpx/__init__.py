"""Minimal httpx stub for offline tests."""

from typing import Any, Dict


class Response:
    def __init__(self, status_code: int, json_data: Dict[str, Any]):
        self.status_code = status_code
        self._json_data = json_data

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self) -> Dict[str, Any]:
        return self._json_data


class AsyncClient:
    def __init__(self, headers: Dict[str, str] | None = None) -> None:
        self.headers = headers or {}

    async def get(self, url: str, params: Dict[str, Any] | None = None) -> Response:
        raise NotImplementedError("Network operations are not available in this environment")

    async def post(self, url: str, json: Dict[str, Any] | None = None) -> Response:
        raise NotImplementedError("Network operations are not available in this environment")
