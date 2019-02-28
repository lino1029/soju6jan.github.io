---
title: "SJ Daum Agent"
date: 2018-10-24 10:49:00 -0900
categories: plex
---
# SJ Daum Agent
### 배경
Plex Daum Agent 최초로 만드신 분은 [hojel](https://github.com/hojel/DaumMovie.bundle)님이십니다.
지금은 업데이트 되지 않고 있지만, 이 소스를 fork 후 유지보수 하시는 분은 [axfree](https://github.com/axfree/DaumMovie.bundle)님과 [wonipapa](https://github.com/wonipapa/DaumMovieTVSeries.bundle)님이 계십니다. wonipapa님 에이전트는 시즌제를 지원합니다.
TV쇼 부분은 API가 없어져서 두 분이 각자 개발하셨고 영화 관련 API는 아직 살아있어 그대로 사용하실겁니다.

저도 두분 꺼를 애용했는데 반년전쯤 TV쇼 API가 사라지면서 작동이 안될 때 한동안 업데이트가 안되길레 fork 하여 수정하기 시작했고 최근 다음이 또 변경되면서 고치는 김에 업데이트 하였습니다. 아마 두분 것과 대동소이 할 겁니다.

### 차이점
 - 에피소드 스샷도 다음에서 가져옵니다.
 - 시즌이름과 번호가 입력됩니다.

### 스캐너
시즌 이름을 수정할 수 있도록 하기 위해, 기존 스캐너를 약간 수정했습니다.
https://github.com/soju6jan/SJVA-Scanners/blob/master/SJVA_Scanner_KoreaTV.py

[스캐너 설명](https://www.clien.net/service/board/cm_nas/12981105)

추가된 기능은 파일명에 S02 같은 시즌 표시를 하지 않아도 폴더 이름으로 시즌을 적용할 수 있습니다.

![2](https://i.imgur.com/xSPeOhi.png)
그림과 같이 이전에는 시즌2를 나타내려면 S02를 파일명에 붙여야 하나 폴더를 하나 만들어 시즌 번호를 넣어주면 내부 파일은 이 시즌 번호가 적용됩니다.

#### 폴더 이름
시즌별 폴더 이름 규칙
 - 첫번째 숫자가 시즌 번호
 - 번호 이후의 글씨는 SJ Daum Agent에서 시즌이름
 - 숫자가 없는 경우 1시즌
 - 시즌 번호는 다음 시리즈 목록 ID 순 index이어야 함.

### 스샷
![3](https://i.imgur.com/vmiz1iR.jpg)

![4](https://i.imgur.com/u2QQ0qB.jpg)

![5](https://i.imgur.com/VdbqaMk.png)

![6](https://i.imgur.com/KUZFQlH.jpg)


### 기타
 - S02, 시즌폴더를 넣지 않는 경우 단일 시즌으로 진행합니다.
 - 시즌 이름 변경 방법
   - [태현맘스님이 알려주신 방법](https://cafe.naver.com/mk802/28088)
   - DB 수정
    ![7](https://i.imgur.com/VhSBUdv.png)
