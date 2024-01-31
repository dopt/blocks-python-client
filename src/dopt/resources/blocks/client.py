# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.get_block_response import GetBlockResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_block(
        self, uid: str, *, user_identifier: str, group_identifier: typing.Optional[str] = None, version: float
    ) -> GetBlockResponse:
        """
        Parameters:
            - uid: str.

            - user_identifier: str.

            - group_identifier: typing.Optional[str].

            - version: float.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/block/{uid}"),
            params=remove_none_from_dict(
                {"userIdentifier": user_identifier, "groupIdentifier": group_identifier, "version": version}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetBlockResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def transition(
        self,
        uid: str,
        *,
        transitions: typing.Union[typing.Optional[str], typing.List[str]],
        user_identifier: str,
        group_identifier: typing.Optional[str] = None,
        version: float,
    ) -> None:
        """
        Parameters:
            - uid: str.

            - transitions: typing.Union[typing.Optional[str], typing.List[str]].

            - user_identifier: str.

            - group_identifier: typing.Optional[str].

            - version: float.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/block/{uid}/transition"),
            params=remove_none_from_dict(
                {
                    "transitions": transitions,
                    "userIdentifier": user_identifier,
                    "groupIdentifier": group_identifier,
                    "version": version,
                }
            ),
            json=jsonable_encoder({}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_block(
        self, uid: str, *, user_identifier: str, group_identifier: typing.Optional[str] = None, version: float
    ) -> GetBlockResponse:
        """
        Parameters:
            - uid: str.

            - user_identifier: str.

            - group_identifier: typing.Optional[str].

            - version: float.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/block/{uid}"),
            params=remove_none_from_dict(
                {"userIdentifier": user_identifier, "groupIdentifier": group_identifier, "version": version}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetBlockResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def transition(
        self,
        uid: str,
        *,
        transitions: typing.Union[typing.Optional[str], typing.List[str]],
        user_identifier: str,
        group_identifier: typing.Optional[str] = None,
        version: float,
    ) -> None:
        """
        Parameters:
            - uid: str.

            - transitions: typing.Union[typing.Optional[str], typing.List[str]].

            - user_identifier: str.

            - group_identifier: typing.Optional[str].

            - version: float.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v2/block/{uid}/transition"),
            params=remove_none_from_dict(
                {
                    "transitions": transitions,
                    "userIdentifier": user_identifier,
                    "groupIdentifier": group_identifier,
                    "version": version,
                }
            ),
            json=jsonable_encoder({}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
