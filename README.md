# nCoV-watchdog

This script automatically fetch news from [dxy.cn](https://3g.dxy.cn/newh5/view/pneumonia) and push them to you.

## Requirements

This python script needs follow requirements:

- python3
- requests (just call `pip install -r requirements.txt`)

## Push Service

I used [Server Chan](http://sc.ftqq.com/) for pushing news, you can write your own push code in send function as you like.

## Runing

I recommend you run this script in python virtual environment.

### Step 1. Installing requirements

```shell
cd WHERE_THE_REPOSITORY_ARE
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Step 2. Run this script

```shell
python main.py
```

## Persistence

There are some ways to run the script as a daemon. I just list what I use often. You could choose others as you like :D

- [nohup](https://en.wikipedia.org/wiki/Nohup)
- [screen](https://www.gnu.org/software/screen/)

## Links

- **wuhan2020**
  - [Website](https://wuhan2020.kaiyuanshe.cn/)
  - [Github](https://github.com/wuhan2020/wuhan2020)

---
**Let us unite together to overcome difficulties!!!**
