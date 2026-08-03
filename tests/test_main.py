import asyncio
import os
import sys

import pytest
from fastapi import HTTPException

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import authorized, health


def test_health_returns_ok():
    result = asyncio.run(health())
    assert result == {"status": "ok"}


class DummyRequest:
    def __init__(self, headers=None):
        self.headers = headers or {}


def test_authorized_rejects_missing_token():
    with pytest.raises(HTTPException):
        authorized(DummyRequest())


def test_authorized_accepts_valid_token():
    request = DummyRequest(
        headers={"Authorization": "Bearer demo-session-token"}
    )

    # Should not raise an exception
    authorized(request)