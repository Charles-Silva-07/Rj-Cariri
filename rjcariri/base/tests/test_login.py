from django.test import Client


import pytest
from rjcariri.django_assertions import assert_contains
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('login'))
    return resp


def test_status_code(client: Client):
    resp = client.get(reverse('login'))
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>cariri Login</title>')
