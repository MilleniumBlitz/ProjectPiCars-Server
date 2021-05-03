#  Project Pi Cars Server
Python server for ProjectPiCars : A Raspberry Pi powered RC Car

## Requirements
- Python Pip `sudo apt-get install python-pip`
- [Flask](http://flask.pocoo.org/) `sudo pip install Flask`
- [WiringPi2 Python](https://github.com/Gadgetoid/WiringPi2-Python)
- [Psutil](http://www.isendev.com/app/entry/39) `sudo pip install psutil`

## Installation

- ### Get Repo
	```
	git clone https://github.com/MilleniumBlitz/ProjectPiCars-Server
	cd ProjectPiCars-Server
    ```

- ### Launch
  ```
  sudo python ProjectPiCars_Server.py
  ```

## Launch at boot

Edit the file :
```
sudo crontab -e
```

Add line to the file :
```
@reboot python /home/pi/ProjectPiCars-Server/ProjectPiCars_Server.py &
```