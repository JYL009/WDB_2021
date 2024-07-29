# WDB_2021
### 사교육놀이터 (Hiseduplay)
**[Duration: 2021.11.22 ~ 2021.12.15]**\
This is a personal project I did in college. \
I majored in History, and I thought it would be good to make a website for people to learn about the history of Korea. \
I used Django, Python, HTML, and CSS to make the overall website.

`The website is written with Korean, and I am still working on it`

**Feel free to explore!**

## 📋 Description about the website
#### 소개 (Introduction)
> 원전공인 사학과를 살려, 사람들에게 한국사와 관련된 정보를 전하고자 웹사이트 개발\
> (Develop a website to deliver information related to Korean history to people by using my history major)

#### 기술 스택 (Tech Stack)
> Python, Django, HTML, CSS, MySQL

#### 인원 (Personnel)
* 1인 개인 프로젝트

#### 세부 기능 (Detailed Function)
   > 메인 페이지\
> 내비게이션 바를 위쪽에 고정해서 여러 페이지들의 접근성 높임.\
> '오늘의 역사 퀴즈'를 역사 퀴즈 페이지에서 불러와서 카드 형식으로 표출.\
> '역사 관련 최신 정보나 박물관 전시 일정' 등의 정보 전달용 캐러셀 표출.\
> '역사와 관련된 기사'를 카드 형식으로 표출.\

   > 로그인 및 회원가입 페이지\
> 회원가입할 때 이용자의 아이디, 별명, 이름, 비밀번호 등의 정보를 입력 받음.\
> 필수적으로 입력해야 하는 값들이 채워지지 않으면 에러 메세지 뱉게 만듦.\
> 회원가입 시 입력한 정보는 DB에서 Member 클래스에 저장됨.\

   > 퀴즈 페이지\
> 이전 날짜의 역사 퀴즈를 포함해서 오늘의 역사 퀴즈 등 다양한 역사 지식에 대한 퀴즈들을 확인할 수 있음.\

   > Merch 페이지\
> 역사 관련 상품 제공. 구매하기 위해서는 로그인 필요하게 만듦.\

   > QnA 페이지\
> 질의응답을 할 수 있음. 글을 작성하려면 로그인 필요하게 만듦

## 🖥️ Implementation
* Welcoming Page
  * The first screen that pops up when you connect to the site
  * If you click [답 보기 및 퀴즈 더보기] in '오늘의 역사 퀴즈', you will be directed to the Quiz page
  * The three photos that is peeking below are taken from the news. When you press it in each card format, you can go to the linked news site.
	<img width="951" alt="image" src="https://github.com/JYL009/WDB_2021/assets/150312081/b495f477-e675-42f5-8597-cbde8df214a5">
* Merch Page
  * If you are curious about historical products, you can come in and check them
  * You have to log in to purchase it
  * You are not currently logged in, buttons such as [홈페이지 바로 이동] are not active
	<img width="1002" alt="image" src="https://github.com/JYL009/WDB_2021/assets/150312081/513e2106-6c12-498a-8833-d7c98d4b190a">
* Quiz Page
  * If you want to see more quizzes or are curious about the answer, you can check this page
	<img width="1011" alt="image" src="https://github.com/JYL009/WDB_2021/assets/150312081/1af7b7e3-a57e-483e-8b56-033f5a3814c6">
* QnA Page
  * Implementation of a Q&A page and a writing page
	<img width="969" alt="image" src="https://github.com/JYL009/WDB_2021/assets/150312081/0ee7cf9c-f621-41eb-94ef-551c3708912b">
 
 	<img width="969" alt="image" src="https://github.com/JYL009/WDB_2021/assets/150312081/877f5f68-93e9-4ea2-b388-aa94048fbbcf">
* Login Page
	<img width="1124" alt="image" src="https://github.com/JYL009/WDB_2021/assets/150312081/438e2398-989a-4243-a732-290dbeb6f384">
* Sign-up Page
	<img width="1024" alt="image" src="https://github.com/JYL009/WDB_2021/assets/150312081/fb9e949b-cf96-4ff9-8fee-56cccffc23fb">
