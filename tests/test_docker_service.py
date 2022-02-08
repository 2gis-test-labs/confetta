from unittest.mock import Mock, call

import pytest

from conf_utils._docker_service import DockerService


@pytest.fixture()
def docker_client():
    return Mock()


@pytest.fixture()
def docker_service(docker_client):
    return DockerService(lambda: docker_client)


def test_docker_service_no_containers(docker_service, docker_client):
    name = "app"
    cont_port = 5000
    docker_client.containers.list = Mock(return_value=[])

    ports = docker_service.get_host_ports(name, cont_port)

    assert len(ports) == 0
    assert docker_client.mock_calls == [
        call.containers.list(filters={
            "status": "running",
            "label": [f"com.docker.compose.service={name}"]
        })
    ]


@pytest.mark.parametrize("cont_port", [5000, "5000", "5000/tcp"])
def test_docker_service_containers(cont_port, docker_service, docker_client):
    name = "app"
    host_port = 49321

    container = Mock(ports={
        f"{cont_port}/tcp": [{
            "HostIp": "0.0.0.0",
            "HostPort": f"{host_port}"
        }],
        "8080/tcp": [{
            "HostIp": "0.0.0.0",
            "HostPort": "49322"
        }],
    })
    docker_client.containers.list = Mock(return_value=[container])

    ports = docker_service.get_host_ports(name, cont_port)

    assert ports == [host_port]
    assert docker_client.mock_calls == [
        call.containers.list(filters={
            "status": "running",
            "label": [f"com.docker.compose.service={name}"]
        })
    ]
