from .session import Yun139Session
from typing import Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    TASK,
)


class Yun139TaskManager:
    def __init__(self, session: Yun139Session):
        self.session = session

    def get_task_status(
        self,
        task_id: str,
    ) -> Tuple[bool, Any]:
        """
        检查任务状态
        :param task_id: 任务ID
        :return: (status, 响应数据/错误原因)
        """

        url = DRIVE_DOMAIN + TASK
        data = {
          "taskId":task_id
        }
        
        return self.session.request(url=url, method="POST", data=data)
