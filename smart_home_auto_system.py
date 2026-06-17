from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self,device_name, **kwargs):
        super().__init__(**kwargs)
        self.device_name = device_name

    def perform_diagnostic(self):
        pass

class PowerConsumerMixin:
    def __init__(self, wattage, **kwargs):
        super().__init__(**kwargs)
        self.wattage = wattage

    def report_power(self):
        print(f"[{self.device_name}] consuming {self.wattage} watts.")


class NetworkConnectedMixin:
    def __init__(self,ip_address, **kwargs):
        super().__init__(**kwargs)
        self.ip_address = ip_address

    def ping_status(self):
        print(f"[{self.device_name}] online at IP: {self.ip_address} .")


class SmartCamera(PowerConsumerMixin,NetworkConnectedMixin, SmartDevice):
    def __init__(self,device_name,wattage,ip_address):
        super().__init__(device_name=device_name,wattage=wattage,ip_address=ip_address)

    def perform_diagnostics(self):
        print(f"[{self.device_name}] Diagnostic: Camera lens clear and streaming active.")



try:
    broken_device =  SmartDevice("Generic Ghost")
except TypeError:
    print("Success: Cannot instantiate abstract base classes directly")


camera = SmartCamera(device_name="Front Door Camera",wattage=55, ip_address="192.168.1.26")

print("\n----- Testing Methods -----")

camera.report_power()
camera.ping_status()
camera.perform_diagnostics()

print("\n---- Checking MRO map -----")

for cls in SmartCamera.mro():
    print(cls)







    