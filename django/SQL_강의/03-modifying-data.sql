-- 1. 테이블 생성
-- articles라는 이름의 테이블을 생성 이 테이블은 다음 필드를 포함
-- id: 정수형 기본키로 자동 증가하는 값
-- title: 최대 100자의 문자열, NULL 허용하지 않음
-- content: 최대 200자의 문자열, NULL 허용하지 않음
-- createAt: 날짜 형식, NULL 허용하지 않음

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createAt DATE NOT NULL
)


-- 2. 단일 데이터 삽입하기
-- articles 테이블에 다음 데이터를 삽입
-- 제목: hello
-- 내용: world
-- 생성일: 2000-01-01

INSERT INTO
    articles (title, content, createAt)
VALUES
    ('hello', 'word', '2000-01-01')


-- 3. 여러 데이터 한 번에 삽입하기
-- articles 테이블에 다음 세 개의 레코드를 한 번에 삽입
-- 제목: title1, 내용: content1, 생성일: 1900-01-01
-- 제목: title2, 내용: content2, 생성일: 1800-01-01
-- 제목: title3, 내용: content3, 생성일: 1700-01-01
INSERT INTO
    articles (title, content, createAt)
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');



-- 4. 현재 날짜를 사용하여 데이터 삽입하기
-- articles 테이블에 다음 데이터를 삽입하되, 생성일은 현재 날짜가 되도록 하기:
-- 제목: title4
-- 내용: content4
-- DATE() 함수

INSERT INTO
    articles (title, content, createAt)
VALUES
    ('title4', 'content4', DATE());



-- 5. 단일 필드 데이터 수정하기
-- articles 테이블에서 id가 1인 레코드의 title을 'update Title'로 수정

UPDATE
    articles
SET
    title = 'update Title'
WHERE
    id = 1;


-- 6. 여러 필드 데이터 수정하기
-- articles 테이블에서 id가 2인 레코드의 title을 'update Title'로, content를 'update Content'로 수정
UPDATE
    articles
SET
    title = 'update Title',
    content = 'update Content'
WHERE
    id = 2;

-- 7. 단일 레코드 삭제하기
-- articles 테이블에서 id가 1인 레코드를 삭제
DELETE FROM
    articles
WHERE
    id = 1;



-- 8. 서브쿼리를 사용한 복합 삭제
-- articles 테이블에서 생성일(createAt) 기준으로 가장 오래된 2개의 레코드를 삭제
-- 힌트: 서브쿼리를 사용하여 삭제할 id를 먼저 찾은 후, 그 id를 기준으로 삭제

-- 서브쿼리
-- SELECT id FROM articles ORDER BY CreateAT LIMIT 2 -- 가장 오래된거 2개

DELETE FROM
    articles
WHERE id IN(
    SELECT id FROM articles
    ORDER BY CreateAt
    LIMIT 2
);