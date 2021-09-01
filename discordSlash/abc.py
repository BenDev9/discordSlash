from discordSlash.utilClasses.http import HTTPClient
from discordSlash.errors import InvalidArgument
from typing import (
    List,
    Optional,
    Protocol,
    Sequence,
    Union,
    overload,
    runtime_checkable
)

@runtime_checkable
class Snowflake(Protocol):
    __slots__ = ()
    id:int

class User(Snowflake, Protocol):
    """An ABC that details the common operations on a Discord user."""
    __slots__ = ()

    name:str
    discriminator:str
    avatar:None #TODO: make Asset class
    bot:bool

    @property
    def display_name(self) -> str:
        """:class:`str`: Returns the user's display name."""
        raise NotImplementedError

    @property
    def mention(self) -> str:
        """:class:`str`: Returns a string that allows you to mention the given user."""
        raise NotImplementedError

#TODO: add GuildChannel object

class Messageable:
    """An ABC that details the common operations on a model that can send messages."""
    
    __slots__ = ()
    client:HTTPClient

    def _get_channel():
        return NotImplementedError

    async def send(
        self,
        content:Optional[str] = None,
        *,
        tts:bool = None,
        embed = None,
        embeds:List = None,
        delete_after:float = None,
    ):
        """Sends a message to the destination with the content given.
            The content must be a type that can convert to a string through ``str(content)``.
            If the content is set to ``None`` (the default), then the ``embed`` parameter must
            be provided.

            To upload a single embed, the ``embed`` parameter should be used with a
            single :class:`~discord.Embed` object. To upload multiple embeds, the ``embeds``
            parameter should be used with a :class:`list` of :class:`~discord.Embed` objects.
            **Specifying both parameters will lead to an exception**."""

        channel = self._get_channel()
        content =  content = str(content) if content is not None else None

        #Check if both embed and embeds got passed
        if embed is not None and embeds is not None:
            raise InvalidArgument("cannot pass both embed and embeds paramater to send()")

        if embed is not None:
            embed = embed.to_dict()

        elif embeds is not None:
            if len(embeds) > 10:
                raise InvalidArgument("embeds paramater must be a list of up to 10 elements.")
            embeds = [embed.to_dict() for embed in embeds]