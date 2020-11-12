# Python - Raspberry Pi camera streamming via websockets  

## Start
All code is written based on python3 compatibility 

`python3 index.py` - will start the project using default configuration 

Project designed to determin configuration, like find active camera or NIC IP address to hook on websocket. 

If your device local IP address starts with other then 192.168.1..., then use example bellow to start project with defined IP:

`wsip=172.10.0.10 python3 index.py`  

### Quick video stream preview
There is a file `test/ws.html` which you will have to edit before you can open in your browser and enter the IP address to connect to.

## Extra 
Project purpose is to represent how to use the most common avaiable python libraries to read and stream CCTV content

The main libraries you will require: 
```
# upadte the repository
sudo apt update

# essential tools for this project
sudo apt install -y tmux vim git subversion mc python3-dev python3-pip python3-opencv python3-webpy python3-websocket python3-websockets python3-rpi.gpio htop
```

## The bigger picture
TOPDAY LTD specialising in AI driven technologies, while some rudamentary UI is essential to run presentation.
More about this project you will find on our main documentation page: [TOPDAY RPI surveilance](https://topday.aje.lt/docs/wiki/ProjectsAiSurveilanceCPU)
