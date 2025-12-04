-- 1. 관계형 테이블 생성하기

-- users와 articles 두 개의 테이블을 생성

-- users 테이블은 다음 필드를 포함
-- id: 정수형 기본키로 자동 증가하는 값
-- name: 최대 50자의 문자열, NULL 허용하지 않음

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
);

-- articles 테이블은 다음 필드를 포함
-- id: 정수형 기본키로 자동 증가하는 값
-- title: 최대 50자의 문자열, NULL 허용하지 않음
-- content: 최대 100자의 문자열, NULL 허용하지 않음
-- userId: 정수형, NULL 허용하지 않음, users 테이블의 id를 참조하는 외래키
CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INTEGER NOT NULL,
    FOREIGN KEY (userId) -- 외래키 설정
        REFERENCES users(id) -- users 테이블의 id를 참조
);



-- 2. users 테이블에 데이터 삽입하기
-- users 테이블에 다음 세 개의 레코드를 삽입
-- 
-- 이름: 하석주
-- 이름: 송윤미
-- 이름: 유하선
INSERT INTO
    users (name)
VALUES
    ('하석주'),
    ('송윤미'),
    ('유하선');


-- 3. articles 테이블에 데이터 삽입하기
-- articles 테이블에 다음 다섯 개의 레코드를 삽입하세요:

-- 제목: 제목1, 내용: 내용1, 작성자ID: 1
-- 제목: 제목2, 내용: 내용2, 작성자ID: 2
-- 제목: 제목3, 내용: 내용3, 작성자ID: 1
-- 제목: 제목4, 내용: 내용4, 작성자ID: 4
-- 제목: 제목5, 내용: 내용5, 작성자ID: 1

INSERT INTO
    articles (title, content, UserId)
VALUES
    ('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 1),
    ('제목4', '내용4', 4),
    ('제목5', '내용5', 1);


-- 4. INNER JOIN 사용하기
-- articles 테이블과 users 테이블을 INNER JOIN하여 모든 필드를 조회
-- 두 테이블은 articles의 userId와 users의 id 필드를 기준으로 연결
SELECT * FROM articles
INNER JOIN users
    ON users.id = articles.userId;


-- MISSION : INNER JOIN 후 특정 사용자(user.id = 1)인 글의 제목과 이름 조회
-- 5. 특정 사용자의 게시글 조회하기
-- articles 테이블과 users 테이블을 INNER JOIN한 후, 사용자 ID가 1인 사용자가 작성한 게시글의 제목과 작성자 이름만 조회
SELECT articles.title, users.name
FROM articles
INNER JOIN users
    ON users.id = articles.userId
WHERE users.id = 1;



-- 6. LEFT JOIN 사용하기
-- articles 테이블을 기준으로 users 테이블과 LEFT JOIN하여 모든 필드를 조회
-- 두 테이블은 articles의 userId와 users의 id 필드를 기준으로 연결




-- 1단계: LEFT JOIN
SELECT * FROM articles
LEFT JOIN users
    ON users.id = articles.userId;


-- 2단계: 게시글이 없는 사용자 찾기
-- (없는 데이터는 NULL값으로 채워져있음)
SELECT * FROM users
LEFT JOIN articles
    ON users.id = articles.userId
WHERE articles.userId IS NULL;


-- 3단계: 게시글이 없는 사용자의 이름만 조회하기
SELECT name FROM users
LEFT JOIN articles
    ON users.id = articles.userId
WHERE articles.userId IS NULL;



