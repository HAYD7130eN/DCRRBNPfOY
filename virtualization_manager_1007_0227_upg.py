# 代码生成时间: 2025-10-07 02:27:26
import requests
from requests.exceptions import RequestException

# 虚拟化管理器类
class VirtualizationManager:
    def __init__(self, base_url):
        """
        初始化虚拟化管理器
        :param base_url: 虚拟化管理器的API基础URL
        """
        self.base_url = base_url

    def create_vm(self, vm_config):
        """
        创建虚拟机
        :param vm_config: 虚拟机配置信息，字典格式
        :return: 请求结果
        """
        url = f"{self.base_url}/create_vm"
        try:
            response = requests.post(url, json=vm_config)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error creating VM: {e}")
            return None

    def start_vm(self, vm_id):
        """
        启动虚拟机
        :param vm_id: 虚拟机ID
        :return: 请求结果
        """
        url = f"{self.base_url}/start_vm/{vm_id}"
        try:
            response = requests.post(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error starting VM: {e}")
            return None

    def stop_vm(self, vm_id):
        """
        关闭虚拟机
        :param vm_id: 虚拟机ID
        :return: 请求结果
        """
        url = f"{self.base_url}/stop_vm/{vm_id}"
        try:
            response = requests.post(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error stopping VM: {e}")
            return None

    def delete_vm(self, vm_id):
        """
        删除虚拟机
        :param vm_id: 虚拟机ID
        :return: 请求结果
        """
        url = f"{self.base_url}/delete_vm/{vm_id}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error deleting VM: {e}")
            return None

    def list_vms(self):
        """
        列出所有虚拟机
        :return: 请求结果
        """
        url = f"{self.base_url}/list_vms"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error listing VMs: {e}")
            return None

# 示例用法
if __name__ == '__main__':
    base_url = "http://example.com/api/vm"
    manager = VirtualizationManager(base_url)

    # 创建虚拟机
    vm_config = {"name": "example_vm", "cpu": 2, "memory": 2048}
    result = manager.create_vm(vm_config)
    print(result)

    # 启动虚拟机
    vm_id = "123"
    result = manager.start_vm(vm_id)
    print(result)

    # 停止虚拟机
    result = manager.stop_vm(vm_id)
    print(result)

    # 删除虚拟机
    result = manager.delete_vm(vm_id)
    print(result)

    # 列出所有虚拟机
    result = manager.list_vms()
    print(result)