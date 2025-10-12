from .session import UcSession
from typing import Tuple, Any
from .API import (
    DRIVE_DOMAIN,
    TASK,
)


class UcTaskManager:
    def __init__(self, session: UcSession):
        self.session = session

    def get_task_status(
        self,
        task_id: str,
        retry_index: int = 0,
    ) -> Tuple[bool, Any]:
        """
        检查任务状态
        :param task_id: 任务ID
        :param retry_index: 重试次数
        :return: (status, 响应数据/错误原因)
        """
        query_params = {"task_id": task_id, "retry_index": retry_index}
        url = DRIVE_DOMAIN + TASK
        status, resp = self.session.request(url, "GET", query_params=query_params)
        if not status:
            return False, resp
        if resp.get("code") == 0 and resp.get("status") == 200:
            return True, resp.get("data", {})
        return False, resp
