"""
RPLidar scanning module that detects enemy position
"""

from signal import signal, SIGTERM
import sys
import time
import math
from rplidar import RPLidar

running = True

MAX_DISTANCE = 3000

ROBOT_X = 1500
ROBOT_Y = 1000
ROBOT_THETA = math.radians(0)

DEFAULT_PORT = 'COM10'
DEFAULT_BAUDRATE = 256000
DEFAULT_TIMEOUT = 3


def lidar_scan(lidar):
    """
    Scans the environment and detects approaching objects in 8 zones around the robot.
    """
    for scan in lidar.iter_scans():
        if not running:
            break

        for _quality, angle, distance in scan:
            if distance == 0:
                continue
            if distance < MAX_DISTANCE:  # Filter out distant objects
                print(angle, distance)


if __name__ == "__main__":
    try:
        lidar = RPLidar(DEFAULT_PORT, timeout=DEFAULT_TIMEOUT,
                         baudrate=DEFAULT_BAUDRATE)
    except Exception as exc:
        print(f"Impossible de se connecter au lidar sur {DEFAULT_PORT} : {exc}")
        sys.exit(1)

    try:
        lidar.stop_motor()
        lidar.clean_input()
        time.sleep(1)
        print(lidar.get_info())
        lidar.start_motor()
        time.sleep(2)

        lidar_scan(lidar)

    except KeyboardInterrupt:
        print("\nStopping.")

    finally:
        try:
            lidar.stop()
        except Exception:
            pass
        try:
            lidar.disconnect()
        except Exception:
            pass
