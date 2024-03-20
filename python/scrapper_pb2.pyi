from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SiteInformationRequest(_message.Message):
    __slots__ = ("name", "country")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    name: str
    country: str
    def __init__(self, name: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...

class SiteInformationResponse(_message.Message):
    __slots__ = ("site_code",)
    SITE_CODE_FIELD_NUMBER: _ClassVar[int]
    site_code: str
    def __init__(self, site_code: _Optional[str] = ...) -> None: ...
