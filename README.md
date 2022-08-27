<p align="center">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcRZyWw%2FbtrJ2nbV0Ly%2FV0thL6tNjJKnkPrHsiYlJK%2Fimg.png">
</p>

# 📖[웹소설] 일타강사 AI의 기막힌 추천 (웹타추)
사용자가 좋아요를 누른 소설의 줄거리와 유사도가 높은 작품을 추천해주는 서비스를 제공하는 웹사이트
<br><br/>


## 1. 개발 기간, 참여 인원
* 개발기간: 2022.06.28 - 2022.07.05
* **Team** <a href="https://github.com/cmjcum"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
김동근 <a href="https://github.com/yinmsk"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
노을 <a href="https://github.com/minkkky"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이정아 <a href="https://github.com/zeonga1102"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이현경 <a href="https://github.com/LULULALA2"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* **S.A** <a href="https://cold-charcoal.tistory.com/85">블로그로 이동(☞ﾟヮﾟ)☞</a>
***
<br><br/>


## 2. 사용 기술
* Python 3.8
* Django 3.2
* Crawling(bs4 4.11, selenium 4.2)
* NLP(KoNLPy 0.6)
* Vector Embedding(gensim 3.8 - Doc2Vec)
 
<br><br/>


## 3. API 명세서
<a href="https://typingmylife.notion.site/API-a51b9477e2d54f9fbd36750740175909">API 명세서 자료</a>
<br><br/>


## 4. ERD 설계
![웹타추_erd](https://user-images.githubusercontent.com/104487608/186834495-776b0eaf-55bf-4358-96ee-ba1c7cec9ddc.png)
<br><br/>


## 5. 기능 소개
<details>
  <summary>소설 목록 조회 <a href="https://github.com/yinmsk/webtachu/blob/fb13f919f245fa79718c1779d79bf5f18bf14178/books/views.py#L14">📄코드</a></summary>
  <div markdown="1">
 
* 소설책을 장르별로 필터링해서 objects을 가져온 다음 소설책의 정보를 가져와 html에 보내주었다.
* 프론트에서는 장고 템플릿을 사용하였다.
  </div>
</details>

<details>
  <summary>장고 내장 페이지네이션 <a href="https://github.com/yinmsk/webtachu/blob/fb13f919f245fa79718c1779d79bf5f18bf14178/books/views.py#L14">📄코드</a></summary>
  <div markdown="1">
 
* 장고의 Paginator 를 import 해주어 기능을 만들었다.
* 모델의 objects가 담겨 있는 list를 원하는 횟수만큼 출력해 주도록 설정한 다음 html로 리턴 시켜주었다.
  </div>
</details>

<details>
  <summary>선호작이 없을 때 선호작 추천 문구가 나온다. <a href="https://github.com/yinmsk/webtachu/blob/fb13f919f245fa79718c1779d79bf5f18bf14178/templates/main_genre/main.html#L13">📄코드</a></summary>
  <div markdown="1">
 
* 장고 템플릿에서 if 문으로 선호 작이 없을때는 "좋아하는 작품을 찾아주세요!" 라는 문구가 나오도록 하였다.
  </div>
</details>

<details>
 <summary>작품 검색 <a href="https://github.com/zeonga1102/webtachu/blob/master/books/views.py#L65">📄코드</a></summary>
  <div markdown="1">

* 제목을 기준으로 작품을 검색합니다.<br>
* 사용자가 입력한 검색어를 제목에 포함하고 있으면 결과로 보여줍니다.
 </div>
</details> 
<br><br/>


## 6. 트러블 슈팅
<details>
  <summary>해당 장르의 책을 조회하기에 어려움이 있었다.</summary>
  <div markdown="1">
 
* url에 name을 지정해주고 views.py 의 함수 안에 name 을 넣음으로 해당 장르의 소설책만 가져올 수 있었다.
   [📄코드](https://github.com/yinmsk/webtachu/blob/fb13f919f245fa79718c1779d79bf5f18bf14178/books/views.py#L14)
  </div>
</details>


## 7. 회고 느낀점
* 장고 템플릿을 사용한점이 편리했는데 백엔드의 자료를 손쉽게 html에 띄워줄 수 있다는 점이 좋았습니다.
* 장고를 처음 사용하게 되었는데 반복해서 구현해야 하는 부분들이 이미 만들어져 있어서 좋았습니다.
 * 로그인 / 회원가입 / 인증 등
* 또한 장고는 models.py, views.py 와 같이 파일이 역할별로 구분되어있어서 잘 정리되고 체계적으로 프로그램을 만들 수 있다는 점이 좋았습니다.
* 앞으로 장고를 더 많이 다루게 되고 사용하게 된다고 했는데 잘 익혀 보고 싶다.
