import pytest

from confetta import docker_host


def test_docker_host_default():
    assert docker_host() == "localhost"


@pytest.mark.parametrize(("env", "res"), [
    ("tcp://127.0.0.1:2375", "127.0.0.1"),
    ("tcp://192.168.59.106", "192.168.59.106")
])
def test_docker_host(env, res, monkeypatch):
    monkeypatch.setenv("DOCKER_HOST", env)
    assert docker_host() == res
