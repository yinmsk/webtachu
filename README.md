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


## 5. 핵심 기능
이 프로젝트의 핵심 기능은 딥페이크를 이용해 사진을 움직이는 초상화로 만드는 것 입니다.
* 선호작을 누른 작품들의 스토리와 유사도가 높은 작품들을 추천
* 선호작을 아직 누르지 않았다면 별점이 높은 작품들을 추천
* Today best top 20 - 네이버 시리즈의 일간 Top100에서 20위까지 크롤링해서 보여주기
* 회원가입 및 로그인 - 장고 내장 모델 사용
* 장르별 페이지에서 작품들을 Django 내장 Paginator를 사용하여 한 페이지 당 10 개씩 표시
* 작품 상세 페이지에서 리뷰들의 키워드를 분석해서 가장 많은 키워드 상위 5개
* 마이 페이지에서 선호작 누른 작품들의 줄거리 키워드 빈도수 상위 10개 표시
* 리뷰 CRUD
<br><br/>


## 6. 맡은 기능
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
<br><br/>


## 7. 트러블 슈팅
<details>
  <summary>해당 장르의 책을 조회하기에 어려움이 있었다.</summary>
  <div markdown="1">
 
* url에 name을 지정해주고 views.py 의 함수 안에 name 을 넣음으로 해당 장르의 소설책만 가져올 수 있었다.
   [📄코드](https://github.com/yinmsk/webtachu/blob/fb13f919f245fa79718c1779d79bf5f18bf14178/books/views.py#L14)
  </div>
</details>


## 8. 회고 느낀점
* 최종프로젝트는 기간이 길어서 여러 기능들을 구현해 볼 수 있었던 점이 가장 좋았습니다.
* 이전에 사용하지 못했던 여러 기능들을 사용할 수 있었습니다.
* 해킹 방지, 자바스크립트 feach 기능 등 기능을 사용할 수 있었다.
* 전에 사용했던 기능들은 더 깊게 알게되는 시간이 되었고 사용해보지 못했던 여러 기능들도 익히는 시간이 되었다.
