# ChooseGame
선택게임

### 개요
텍스트 어드벤처를 플레이하고 만들 수 있는 웹사이트입니다.
(현재 편집기능은 superuser만 가능하게끔 해놓았습니다.)


### 구현한 것

회원가입 및 로그인

게임 탬플릿 CRUD

자동 세이브

모달
(게임 스토리보드 삭제 시 한 번 더 물어보는 창)

django messages
(로그인, 로그아웃, 사망 등 각종 알림 기능)

복수 앱 사용(game, shopping)
(shopping : 현재는 캐시 획득 외에 별다른 기능 없음. 해당 앱에서 캐쉬 교환이나 스토리 구매 등을 구현할 수 있음.)


### 보완할 점
1. url 직접 입력을 통해서 원하는 선택지로 바로 갈 수 있음. => 페이지를 비동기로 구현하거나, game url을 get 요청으로 접근할 시에 home으로 리다이렉트되게끔 할 수 있음.
2. css가 단순함.
3. 선택지가 2개로 고정되어 있고(초기 의도), 얻을 수 있는 스탯도 고정되어 있음. 추후 수정으로 선택지 다변화, 스탯 다변화, 주관식 선택지(암호), 아이템 획득, 인벤토리 등을 구현할 수 있음.
4. 스탯에 따라 선택지의 결과가 달라지게끔 구현하고 싶음.
5. 하나의 스토리 흐름이 끝나면 다른 스토리 흐름으로 랜덤으로 넘어가게끔 구현하고 싶음.

### 수익 모델
1. 광고 수익
2. 유저 제작 콘텐츠 플랫폼으로서 기능 (유저가 직접 스토리를 짤 수 있게끔) 
  => 추후에 사업이 확대되면 웹툰/웹소설처럼 유료 모델 도입 (스토리 유료 판매)
  => 선택지들을 묶어서 모듈화 : 진행 중인 스토리에 랜덤으로 등장할 수 있게끔 함
3. 정기 결제 도입
4. 하루 행동력 제한 후 유료 과금으로 행동력 늘려주기


### 이미지

<img width="1680" alt="Screen Shot 2022-08-08 at 4 27 06 PM" src="https://user-images.githubusercontent.com/87408958/183364468-cd4d7e5f-2eff-4562-9069-bd445a4c7c3b.png">
<img width="1680" alt="Screen Shot 2022-08-08 at 4 32 48 PM" src="https://user-images.githubusercontent.com/87408958/183364491-208b276f-7f2b-4149-9f22-ce6f6082c85a.png">
<img width="1680" alt="Screen Shot 2022-08-08 at 4 33 03 PM" src="https://user-images.githubusercontent.com/87408958/183364497-e7d51c40-25f1-4c53-ae5b-b3568678d407.png">
<img width="1680" alt="Screen Shot 2022-08-08 at 4 33 26 PM" src="https://user-images.githubusercontent.com/87408958/183364507-aa47e81a-275b-4bfa-a666-874f60a3a777.png">
<img width="1680" alt="Screen Shot 2022-08-08 at 4 33 46 PM" src="https://user-images.githubusercontent.com/87408958/183364516-881bdb06-cc89-484b-bbc6-54b809e006a7.png">
<img width="1680" alt="Screen Shot 2022-08-08 at 4 33 55 PM" src="https://user-images.githubusercontent.com/87408958/183364539-b781b43b-a587-4d26-a3c4-3c6dc390a4cd.png">
<img width="1680" alt="Screen Shot 2022-08-08 at 4 34 20 PM" src="https://user-images.githubusercontent.com/87408958/183364560-9dc8bb1a-1fd3-483f-b76f-74c0fab4abc4.png">


