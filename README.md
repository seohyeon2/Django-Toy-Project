# Django Toy Project

<br>

## 🎙 introduction 🎙
* django 공부하면서 만들어 본 페이지들 입니다.
* 더 많은 기록을 확인하고 싶다면 아래 링크를 참고하세요
* [공부개념 정리](https://github.com/seohyeon2/Django-Toy-Project/wiki)        

<br>

## 💿 distribution 💿
* [감정일기 웹 사이트](http://seohyeon2.pythonanywhere.com/)    
ㄴ python version : 3.7    
ㄴ django version : 3.2.3    
ㄴ 권장하는 브라우저 : 크롬    
ㄴ [pythonanywhere](https://www.pythonanywhere.com/)를 이용하여 배포함.    


<br>

---------------------------------------------------------------------

<br>

## 🗂 Project Description 🗂

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

<img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main2/main2.png"><img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main2/main2-pagenation.png">

<img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main2/main2-write.png"><img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main2/main2-modify.png">


<br>

---------------------------------------------------------------------

<br>

### mindnote_complete
* http://127.0.0.1:8000/
* 오늘 하루 감정 점수와 감정 상태까지 글로 적을 수 있는 감정 일기 사이트
* 왼쪽에 목차    
ㄴ 모아보기 : 전체 일기 보기     
ㄴ 감정일기란 : 감정일기에 대한 설명을 써놓은 곳    
ㄴ 일기쓰기 : 누르면 일기쓰기 가능    
* 새로운 글 등록, 글 수정, 글 삭제 가능
* 제목은 100자 이하, 내용은 제한 없음, 감정 상태는 80자 이하, 정수형(1~10)만 가능, 작성일은 '0000-00-00' 형식만 가능하게 함 
* 유효성 검사를 통해 제목과 내용에는 '#'이 들어갈 수 없으며, 감정 상태에는 숫작 들어갈 수 없게 함

<img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main3/main3-home.png"><img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main3/main3-write.png">

<img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main3/main3-all.png"><img width="50%" src="https://github.com/seohyeon2/Django-Toy-Project/blob/master/wiki_img/main3/main3-intro.png">
