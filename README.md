# conf-utils

## Usage

```python
from conf_utils import git_folder_name, docker_port

config = {
    "project_name": git_folder_name(),
    "app_host": "app",
    "app_port": docker_port("app", 5000),
}
```
