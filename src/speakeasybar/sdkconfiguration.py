"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass, field

from enum import Enum

SERVER_PROD = 'prod'
r"""The production server."""
SERVER_STAGING = 'staging'
r"""The staging server."""
SERVER_CUSTOMER = 'customer'
r"""A per-organization and per-environment API."""
SERVERS = {
	SERVER_PROD: 'https://speakeasy.bar',
	SERVER_STAGING: 'https://staging.speakeasy.bar',
	SERVER_CUSTOMER: 'https://{organization}.{environment}.speakeasy.bar',
}
"""Contains the list of servers available to the SDK"""


class ServerEnvironment(str, Enum):
    r"""The environment name. Defaults to the production environment."""
    PROD = 'prod'
    STAGING = 'staging'
    DEV = 'dev'


@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server: str = ''
    server_defaults: dict[str, dict[str, str]] = field(default_factory=dict)
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '1.26.0'
    gen_version: str = '2.96.6'

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        if self.server_url:
            return self.server_url.removesuffix('/'), {}
        if not self.server:
            self.server = SERVER_PROD

        return SERVERS[self.server], self.server_defaults.get(self.server, {})
