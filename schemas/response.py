from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

T = TypeVar("T")


class ResponseSchema(GenericModel, Generic[T]):

    status: str
    message: str
    data: Optional[T] = None
