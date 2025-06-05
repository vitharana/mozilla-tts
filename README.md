# mozilla-tts

https://www.youtube.com/live/CK-9tXfyW8M?si=RBIHSqjJdcZbhnTP

```jsx
pip install TTS
```

```jsx
sudo apt update
sudo apt install libportaudio2 libportaudio-dev
```

```jsx
pip uninstall sounddevice
pip install sounddevice
```



docker image
https://hub.docker.com/r/synesthesiam/mozilla-tts

docker run -it -p 5002:5002 synesthesiam/mozilla-tts

and run dcker_speak.py

may need to configure docker gpu
for nvidia


on cpu response 4.6 sec
on gpu 4.25 sec bit faster


sudo apt purge nvidia-container-toolkit
sudo apt install -y nvidia-container-toolkit

sudo nano /etc/docker/daemon.json



{
  "default-runtime": "nvidia",
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}


sudo systemctl restart docker



check 

docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi



run on gpu

docker run --gpus all -p 5002:5002 synesthesiam/mozilla-tts




on browser may download the files 

http://localhost:5002/api/tts?text=Hello+from+my+GPU

url for the server

http://localhost:5002⁠

for windows

pip install soundfile
