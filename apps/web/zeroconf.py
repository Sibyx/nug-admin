import socket

from zeroconf import ServiceListener, Zeroconf


class ZeroconfListener(ServiceListener):
    def __init__(self):
        self.services = {}

    def update_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:
        self.services[name] = zc.get_service_info(type_, name)
        if self.services[name]:
            print(self.services[name])
            # print("Service %s added, IP address: %s" % (name, socket.inet_ntoa(self.services[name].addresses)))

    def remove_service(self, zc: 'Zeroconf', type_: str, name: str):
        del self.services[name]

    def add_service(self, zc: 'Zeroconf', type_: str, name: str):
        self.services[name] = zc.get_service_info(type_, name)
        if self.services[name]:
            print(self.services[name])
            # print("Service %s added, IP address: %s" % (name, socket.inet_ntoa(self.services[name].address)))
