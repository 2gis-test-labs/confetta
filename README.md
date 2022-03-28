# confetta

## Installation

```shell
$ pip3 install confetta
```

## Usage

```python
from os import environ as env
from confetta import git_folder_name, docker_port, docker_host

config = {
    "app_name": env.get("APP_NAME", git_folder_name()),
    "app_host": env.get("APP_HOST", docker_host()),
    "app_port": env.get("APP_PORT", docker_port("app", 80))
}

print(config)
```
