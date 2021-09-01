import json
from typing import List, Optional
from discordSlash.abc import Snowflake
import aiohttp
from aiohttp.client import request
from aiohttp.client_reqrep import ClientResponse
from ..errors import Forbidden, HTTPException, NotFound

__all__ = ('HTTPClient')

class HTTPClient:
    baseUrl = "https://www.discord.com/api/v9"
    token:int


    def get_user(id:int):
        return

    async def _get(url, headers) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                data = await response.text()

                try:
                    data = dict(data)
                except:
                    data = str(data)

                #region Error Checks
                if 300 > response.status >= 200:
                    #The request was a success
                    return data

                if not response.headers.get('Via') or isinstance(data, str) and response.status == 429:
                    raise HTTPException("rate limited.")

                if response.status == 403:
                    raise Forbidden()
                elif response.status == 404:
                    raise NotFound()
                else:
                    raise HTTPException("unknown error")

                #endregion

    async def get_avatar(self, id:int, hash:str):
        if hash.startswith("a"): ext = ".gif"
        else: ext = ".png"
        url = f"https://cdn.discordapp.com/avatars/{id}/{hash}.{ext}"
        headers = {
            "Authorization" : f"Bot {self.token}"
        }
        r:ClientResponse = await self._request(url, headers)
        print(r.content)
        if r.status == 200:
            return await r.read()
        else:
            print()

    async def send_message(
        self,
        channelId:Snowflake,
        content:Optional[str],
        *,
        tts:bool = None,
        embed = None,
        embeds:List = None,
    ):
        url = f"{self.baseUrl}/channels/{channelId}/messages"
        payload = {}

        if content:
            payload['content'] = content

        if tts:
            payload['tts'] = True

        if embed:
            payload['embeds'] = [embed]

        if embeds:
            payload['embeds'] = embeds

        headers = {
            "Authorization" : f"Bot {self.token}"
        }

        r = self._request(url, headers)

        return r