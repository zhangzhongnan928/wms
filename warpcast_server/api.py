"""Warpcast API client."""

from __future__ import annotations

from typing import Any, Dict

import httpx


class WarpcastAPI:
    """Minimal asynchronous client for the Warpcast API."""

    def __init__(self, api_token: str) -> None:
        self.api_token = api_token
        self.base_url = "https://api.warpcast.com/v2"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}",
        }
        self.client = httpx.AsyncClient(headers=self.headers)

    async def post_cast(self, text: str, parent_cast_id: str | None = None) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/casts"
        data = {"text": text}
        if parent_cast_id:
            data["parent"] = parent_cast_id
        resp = await self.client.post(endpoint, json=data)
        resp.raise_for_status()
        return resp.json()

    async def get_user_casts(self, username: str) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/user-casts"
        resp = await self.client.get(endpoint, params={"username": username})
        resp.raise_for_status()
        return resp.json()

    async def search_casts(self, query: str) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/search-casts"
        resp = await self.client.get(endpoint, params={"q": query})
        resp.raise_for_status()
        return resp.json()

    async def get_trending_casts(self) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/trending-casts"
        resp = await self.client.get(endpoint)
        resp.raise_for_status()
        return resp.json()

    async def get_all_channels(self) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/all-channels"
        resp = await self.client.get(endpoint)
        resp.raise_for_status()
        return resp.json()

    async def get_channel(self, name: str) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/channel"
        resp = await self.client.get(endpoint, params={"name": name})
        resp.raise_for_status()
        return resp.json()

    async def get_channel_casts(self, name: str) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/channel-casts"
        resp = await self.client.get(endpoint, params={"name": name})
        resp.raise_for_status()
        return resp.json()

    async def follow_channel(self, name: str, follow: bool = True) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/channel-action"
        action = "follow" if follow else "unfollow"
        resp = await self.client.post(endpoint, json={"name": name, "action": action})
        resp.raise_for_status()
        return resp.json()


_api_client: WarpcastAPI | None = None


def init_api_client(token: str) -> WarpcastAPI:
    """Create and store the global API client."""
    global _api_client
    _api_client = WarpcastAPI(token)
    return _api_client


def get_api_client() -> WarpcastAPI:
    if _api_client is None:
        raise RuntimeError("API client not initialized")
    return _api_client
