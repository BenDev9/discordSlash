__all__ = ()

class DiscordSlashException(Exception):
    """Exception that gets passed when something goes wrong in the library."""
    pass

class HTTPException(DiscordSlashException):
    """Exception that's raised when an HTTP request operation fails."""
    pass

class Forbidden(HTTPException):
    """Exception that's raised for when status code 403 occurs."""
    pass

class NotFound(HTTPException):
    """Exception that's raised for when status code 404 occurs."""
    pass

class DiscordServerError(HTTPException):
    """Exception that's raised for when a 500 range status code occurs."""
    pass

class InvalidData(DiscordSlashException):
    """Exception that's raised when the library encounters unknown
    or invalid data from Discord."""
    pass

class InvalidArgument(DiscordSlashException):
    """Exception that's raised when an argument to a function
    is invalid some way (e.g. wrong value or wrong type).
    This could be considered the analogous of ``ValueError`` and
    ``TypeError`` except inherited from :exc:`DiscordException`.
    """
    pass