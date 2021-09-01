from typing import Any
from utils.http import HTTPClient

class User:
    id: str
    username: str
    discriminator: int
    avatarHash: str
    avatar:Any
    bot:bool
    system:bool
    mfa_enabled:bool
    banner:str
    locale:str
    verified: bool
    email: str
    flags: int
    accent_color: int
    premium_type: int
    public_flags: int

    @avatar.getter
    def avatarGetter(self):
        return HTTPClient.get_avatar(self.id, self.avatarHash)

    def __init__(
        self, 
        id: str,
        username: str,
        discriminator: int,
        avatarHash: str,
        bot:bool,
        system:bool,
        mfa_enabled:bool,
        banner:str,
        locale:str,
        verified: bool,
        email: str,
        flags: int,
        accent_color: int,
        premium_type: int,
        public_flags: int
        ) -> None:

        self.id = id
        self.username = username
        self.discriminator = discriminator
        self.avatarHash = avatarHash
        self.bot = bot
        self.system = system
        self.mfa_enabled = mfa_enabled
        self.locale = locale
        self.verified = verified
        self.email = email
        self.flags = flags
        self.banner = banner
        self.accent_color = accent_color
        self.premium_type = premium_type
        self.public_flags = public_flags