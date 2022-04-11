import imp
from lasertracker_client import Measurement, LaserTrackerClient

if __name__ == "__main__":
    client = LaserTrackerClient()
    
    while(True):
        if input("Press e to exit, or any button to get measurement") == "e":
            break

        new_measurement = client.get_pose()
        assert isinstance(new_measurement, Measurement)

        print("Measurement: ")
        print("X: ", new_measurement.x)
        print("Y: ", new_measurement.y)
        print("Z: ", new_measurement.z)
        print("Qx: ", new_measurement.qx)
        print("Qy: ", new_measurement.qy)
        print("Qz: ", new_measurement.qz)
        print("Qw: ", new_measurement.qw)

    client.close_port()
    exit()