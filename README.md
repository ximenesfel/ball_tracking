

<div style="text-align: center">
  <img src="figure_1.gif" style="width: 400px; height: 400px;" />
</div>

## Ball tracking

In this project was develop an application for tracking a ball in real-time.

## Installation

1. Install virtualenv using step #3 from this [post](https://www.pyimagesearch.com/2017/09/27/setting-up-ubuntu-16-04-cuda-gpu-for-deep-learning-with-python/).
2. Create a new env using this command ```mkvirtualenv "name_env" -p python3```. Change "name_env" for your choice name.
3. Enter inside env: ```workon "name_env"```. Change "name_env" for your choice name.
4. Clone this respository using ```git clone https://github.com/ximenesfel/face_tracking.git``` command.
5. Install dependences: ```pip install -r requirements.txt```.

## Usage

### Run

Video
```sh
$ cd [project root]
$ python ball_tracking.py --video video/ball_video.mp4
```

Webcam
```sh
$ cd [project root]
$ python ball_tracking.py
```

### Quit

```sh
$ Press "q"
```




