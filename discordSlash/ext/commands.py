from asyncio.coroutines import coroutine
import requests
import asyncio
from functools import wraps
from decorator import decorator
from ..utils.http import HTTPClient

token:int

argTypes = {
    int:4,
    str:3,
    bool:5
}

class Option:
    name:str
    type:int

    def __init__(self, _name, _type) -> None:
        self.name = _name
        self.type = _type
        

class CommandStore:
    name:str
    desc:str
    options:list
    token:int

    def __init__(self, _name, _desc, _annotations):
        self.name = _name
        self.desc = _desc
        self.options = []

        for a in _annotations:
            self.options.append(
                Option(a, argTypes[_annotations[a]])
            )

    #region str override
    def __str__(self) -> str:
        return f"""Command Object
Name: {self.name}
Description: {self.desc}
Options: {self.options}"""
    #endregion

    def __dict__(self):
        dictionary = {}

        options = []

        for o in self.options:
            options.append(o.__dict__)

        dictionary['name'] = self.name
        if self.desc != None: dictionary['description'] = self.desc
        dictionary['options'] = str(options)

        return dictionary

commands = []

def Command(**kwargs):
    def inner(func) -> coroutine:
        @wraps(func)
        def wrapper():
            if not asyncio.iscoroutinefunction(func):
                raise TypeError('Callback must be a coroutine.')

            name = kwargs.get('name') or func.__name__
            description = kwargs.get('description') or func.__doc__

            commands.append(
                CommandStore(name, description, func.__annotations__)
            )
            print("Loaded " + name)
            return func
        return wrapper()
    return inner

def initialize(token:int):
    HTTPClient.token = token
    for command in commands:
        print(command)
    return

def test():
    for c in commands:
        print(c.__dict__())