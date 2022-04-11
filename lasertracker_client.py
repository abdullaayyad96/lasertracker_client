import socket
import json


class Measurement:
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        self.qw = None
        self.qx = None
        self.qy = None
        self.qz = None
        self.roll = None
        self.pitch = None
        self.yaw = None

class Server:
    def __init__(self, ip="10.10.105.55", port=11000):      
        self.HOST = "10.10.105.55"  # The server's hostname or IP address
        self.PORT = 11000  # The port used by the server

        self.measurement = Measurement()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def get_pose(self):
        req_msg = "get_pose<EOF>"
        self.s.sendall(req_msg.encode("ascii"))
        data = self.s.recv(1024)
        string_data = data.decode("ascii")
        measurement_json = json.loads(string_data)

        self.measurement.x = measurement_json['X']
        self.measurement.y = measurement_json['X']
        self.measurement.z = measurement_json['X']
        self.measurement.qw = measurement_json['qw']
        self.measurement.qx = measurement_json['qx']
        self.measurement.xy = measurement_json['qy']
        self.measurement.xz = measurement_json['qz']
        self.measurement.roll = measurement_json['roll']
        self.measurement.pitch = measurement_json['pitch']
        self.measurement.yaw = measurement_json['yaw']

        return self.measurement()

    def close_port(self):
        self.s.close()
