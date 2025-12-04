-- 1. 기본 SELECT 문제
-- employees 테이블에서 LastName과 FirstName 필드를 선택하는 쿼리를 작성하세요.
-- SQL의 구문 끝에는 ;

SELECT
  LastName, FirstName
FROM
  employees;


-- 2. 모든 필드 선택 문제
-- employees 테이블에서 모든 필드를 조회하는 쿼리를 작성하세요.

SELECT
  *
FROM
  employees;


-- 3. 별칭(AS) 사용 문제
-- employees 테이블에서 FirstName 필드를 '이름'이라는 별칭으로 조회하는 쿼리를 작성하세요.\

SELECT
  FirstName AS '이름'
FROM
  employees;



-- 4. 계산된 필드 문제
-- tracks 테이블에서 Name과 함께 Milliseconds를 60000으로 나눈 값을
-- '재생 시간(분)'이라는 별칭으로 조회하는 쿼리를 작성하세요.

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;



-- 5. 오름차순 정렬 문제(ORDER BY)
-- employees 테이블에서 FirstName을 오름차순으로 정렬하여 조회하는 쿼리를 작성하세요.

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName;


-- 6. 내림차순 정렬 문제
-- employees 테이블에서 FirstName을 내림차순으로 정렬하여 조회하는 쿼리를 작성하세요.

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;



-- 7. 다중 필드 정렬 문제
-- customers 테이블에서 Country를 내림차순으로, 
-- 같은 Country 내에서는 City를 오름차순으로 정렬하여 조회하는 쿼리를 작성하세요.

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City;


-- 8. 계산된 값 기준 정렬 문제
-- tracks 테이블에서 Name과 Milliseconds를 60000으로 나눈 값을 
-- '재생 시간(분)'이라는 별칭으로 조회하고,
-- Milliseconds를 기준으로 내림차순 정렬하는 쿼리를 작성하세요.

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;




-- 9. NULL 다루기 문제
-- 오름차순 정렬 시 NULL 값부터 정렬
-- customers 테이블에서 postalCode를 조회하고 
-- PostalCode 기준으로 정렬하는 쿼리를 작성하세요.
SELECT
  PostalCode
FROM
  customers
ORDER BY
  PostalCode;




-- 10. 중복 없이 조회
-- customers 테이블에서 중복 없이 Country를 조회하고,
-- Country 기준으로 정렬하는 쿼리를 작성하세요.

SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;



-- 11. WHERE 조건 문제
-- customers 테이블에서 city가 'Prague'인 고객의 
-- LastName, FirstName, City를 조회하는 쿼리를 작성하세요.

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  city = 'Prague'


-- 12. 부정 조건 문제
-- customers 테이블에서 city가 'Prague'가 아닌 고객의 
-- LastName, FirstName, City를 조회하는 쿼리를 작성하세요.
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  city != 'Prague'




-- 13. AND 연산
-- customers 테이블에서 Company가 NULL이고, Country가 'USA'인 고객의
-- LastName, FirstName, Company, Country를 조회하는 쿼리를 작성하세요.
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company is NULL
  AND Country = 'USA';




-- 14. OR 연산
-- customers 테이블에서 Company가 NULL이거나 Country가 'USA'인 고객의
-- LastName, FirstName, Company, Country를 조회하는 쿼리를 작성하세요.
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company is NULL
  OR Country = 'USA';



-- 15. BETWEEN 문제
-- tracks 테이블에서 Bytes가 100000과 500000 사이인 트랙의
-- Name과 Bytes를 조회하는 쿼리를 작성하세요.

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000;



-- 16. BETWEEN과 정렬 문제
-- tracks 테이블에서 Bytes가 100000과 500000 사이인 트랙의
-- Name과 Bytes를 조회하고 Bytes 기준으로 정렬하는 쿼리를 작성하세요.ABORT

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;



-- 17. IN 연산자 문제
-- customers 테이블에서 Country가 'Canada', 'Germany', 'France' 중 하나인
-- 고객의 LastName, FirstName, Country를 조회하는 쿼리를 작성하세요.

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country in ('Canada', 'Germany', 'France')



-- 18. NOT IN 문제
-- customers 테이블에서 Country가 'Canada', 'Germany', 'France'가 아닌 
-- 고객의 LastName, FirstName, Country를 조회하는 쿼리를 작성하세요.

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT in ('Canada', 'Germany', 'France')




-- 19. LIKE 패턴 매칭 문제
-- customers 테이블에서 LastName이 'son'으로 끝나는 고객의 
-- LastName, FirstName을 조회하는 쿼리를 작성하세요.
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son'





-- 20. LIKE 패턴 매칭 문제
-- customers 테이블에서 FirstName이 4글자이며 마지막 글자가 'a'인 고객의
-- LastName, FirstName을 조회하는 쿼리를 작성하세요.

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a'



-- 21. LIMIT 문제
-- tracks 테이블에서 TrackId, Name, Bytes를 조회하되, 
-- Bytes를 기준으로 내림차순 정렬하여 상위 7개만 조회하는 쿼리를 작성하세요.ABORT
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7; -- 가장 큰값 7개





-- 22. LIMIT과 OFFSET 문제
-- tracks 테이블에서 TrackId, Name, Bytes를 조회하되,
-- Bytes를 기준으로 내림차순 정렬하여 4번째부터 7번째까지 조회하는 쿼리를 작성하세요.
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4
-- 3번 OFFSET 하면 4번째 부터 4개




-- 23. GROUP BY 문제
-- customers 테이블에서 Country별로 그룹화하여 각 국가의 고객 수를 조회하는 쿼리를 작성하세요.
SELECT
  Country, COUNT(*) -- * : 전체
FROM
  customers
GROUP BY
  Country;





-- 24. AVG 함수 문제
-- tracks 테이블에서 Composer별로 그룹화하여 각 작곡가의 평균 Bytes를 계산하고,
-- 평균 Bytes를 기준으로 내림차순 정렬하는 쿼리를 작성하세요.
SELECT
  Composer,
  AVG(Bytes) AS avgOfBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;



-- 왜 GROUP BY와 WHERE을 같이쓰면 에러가 날까??
-- 과일 가게에 가서 "평균 가격이 5000원 미만인 과일을 담아주세요"
-- 1단계 : 과일 종류별로 GROUP BY (사과, 배, 파인애플....)
-- 2단계 : 각 그룹(과일종류)의 평균 가격 계싼
-- 3단계 : 마지막으로 평균가격이 5000원 미만인 그룹을 선택해서 담는다.

-- 만약 WHERE을 쓰면 그룹 짓기도 전에(1단계 전에) 평균가격을 모르는 상태에서 필터링
-- 결론 : GROUP BY 하기던에 WHERE을 쓰면 에러가난다.
-- HAVING --> 2단계가 이후에 평균가격을 알고 있는 상태에서 필터링



-- 25번 WHERE <-> HAVING 차이
-- tracks 테이블에서 Composer별로 그룹화하여 
-- 각 작곡가의 평균 재생시간(Milliseconds/60000)을 계산하고,
-- 평균 재생시간이 10분 미만인 작곡가만 조회하는 쿼리를 작성하세요.

SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;
