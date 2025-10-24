# 代码生成时间: 2025-10-25 06:06:43
import requests
import json
from typing import Dict, Any

"""API文档自动生成器：
该程序通过发送HTTP请求到指定的API端点，收集API信息，并生成对应的API文档。"""

class ApiDocumentGenerator:
    def __init__(self, base_url: str):
        """初始化器，接受API的基础URL。"""
        self.base_url = base_url

    def fetch_api_info(self, endpoint: str) -> Dict[str, Any]:
        "