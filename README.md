# About

본 Repository 는 [2020 데이터야놀자](https://datayanolja.github.io/) 의 `출근길에서 생각난 데이터 토이 프로젝트` 에 사용된 코드를 공개하는 것을 목적으로 합니다.

## 세팅

사용한 python version 은 `3.6.4` 입니다.

추가로 사용한 python package 들은 `requirements.txt` 에 정리되어 있습니다.

## 사용법

### Crawler

`config.example.cfg` 의 이름을 바꾸거나 복사하여 `config.cfg` 를 만들고, [서울 열린데이터 광장](http://data.seoul.go.kr/) 에서 발급 받은 인증키를 입력합니다.
(`authkey` 하위 이름은 취향에 맞추어 지정하시면 됩니다.)

구동은 아래와 같은 방식으로 합니다.

```
$ python crawler.py Aries(config.cfg 에 사용한 key 이름)
```

`crontab` 을 이용하는 경우는 `scripts/run_crawler.sh` 를 수정하고 아래와 같은 방식으로 사용합니다.
(순서대로 홀수분, 짝수분, 시간(timezone 반영), 평일)

```
*/2 14-23 * * 1-5 ~/Workspace/train-de-train/run_crawler_even.sh
1-59/2 14-23 * * 1-5 ~/Workspace/train-de-train/run_crawler_odd.sh
*/2 0-9  * * 1-5 ~/Workspace/train-de-train/run_crawler_even.sh
1-59/2 0-9 * * 1-5 ~/Workspace/train-de-train/run_crawler_odd.sh
```


### Note

* 우분투에서 자료가 없는 빈 파일을 삭제하는 경우 아래 명령어를 사용합니다.

```
$ find ./ -size  0 -print -delete
```

* Jupyter 사용시 독립적인 커널을 사용하는 경우 아래 명령어를 사용합니다.

```
$ pip install ipykernel
$ python -m ipykernel install --user --name [virtualEnv] --display-name "[displayKenrelName]"
```
