# Django Toy Project

<br>

<p> django 공부하면서 만들어 본 페이지들 입니다. <br>
더 많은 기록을 확인하고 싶다면 아래 링크를 참고하세요</p>

### [공부개념 정리](https://github.com/seohyeon2/Django-Toy-Project/wiki)        

<br>

---------------------------------------------------------------------

<br>

### costaurant_complete
* http://127.0.0.1:8000/foods/menu/
* 메뉴판 사이트를 만들고 메뉴 클릭시 해당 메뉴의 상세정보(가격 등)를 확인 할 수 있게 함
* 사이트 왼쪽 상단에는 현재 시간이 뜨도록 설정
<br>
<img width="900" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main.png">

<br>

---------------------------------------------------------------------

<br>

### costory_complete
* http://127.0.0.1:8000/posts
* 나만의 글을 작성할 수 있는 일기 사이트
* 새로운 글 등록, 글 수정, 글 삭제 가능
* 글 저장 시, 저장한 시간이 기록되며 수정 시, 수정일을 명시 함
* 화면 왼쪽 상단의 로고를 클릭할 시, 메인 화면으로 이동됨
* 페이지네이션을 통해 게시글은 한 페이지당 최대 6개의 글이 보이게 했으며 인덱스로 이동 가능
* 유효서 검사를 통해 겹치는 제목, 10글자 이하의 짧은 내용, 지정된 특수문자 외 특수문자 사용 시 경고와 함께 글 등록이 안되도록 함 
<br>
<img width="900" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main2.png">

<br>

---------------------------------------------------------------------

<br>

제목(title), 문자열, 길이 제한 100자
내용(content), 문자열, 길이 제한 없음
감정 상태(feeling), 문자열, 길이 제한 80자
감정 점수(score), 정수형
작성일(dt_created), 날짜
1. '제목'과 '내용'에는 '#'이 들어갈 수 없습니다.
2. '감정 상태' 에는 숫자가 들어갈 수 없습니다.
3. '감정 점수'는 0부터 10사이의 숫자만 들어갈 수 있습니다.
