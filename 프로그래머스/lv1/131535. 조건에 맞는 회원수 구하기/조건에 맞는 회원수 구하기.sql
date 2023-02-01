-- 코드를 입력하세요
SELECT count(USER_ID) as USERS from USER_INFO where age >= 20 and age <= 29 and 
DATE_FORMAT(JOINED, '%Y') = 2021