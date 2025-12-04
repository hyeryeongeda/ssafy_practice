-- 1. 테이블 생성하기
-- examples라는 이름의 테이블을 생성. 이 테이블은 다음 필드를 포함해야 한다.
-- ExamId: 정수형 기본키로 자동 증가하는 값
-- LastName: 최대 50자의 문자열, NULL 허용하지 않음
-- FirstName: 최대 50자의 문자열, NULL 허용하지 않음

CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);


-- 2. 테이블에 새 필드 추가하기
-- examples 테이블에 다음 필드를 추가
-- Country: 최대 100자의 문자열, NULL 허용하지 않으며 기본값은 'default value'

ALTER TABLE
    examples
ADD COLUMN
    Country VARCHAR(100) NOT NULL DEFAULT 'default value'



-- 3. 여러 필드 추가하기
-- Sqlite는 한번의 명령어에 여러 필드를 추가 할 수 없다. 가각 따로 추가
-- examples 테이블에 다음 두 필드를 각각 별도의 쿼리로 추가:
-- Age: 정수형, NULL 허용하지 않으며 기본값은 0
-- Address: 최대 100자의 문자열, NULL 허용하지 않으며 기본값은 'default value'

ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL DEFAULT 0;

ALTER TABLE examples
ADD COLUMN Address VARCHAR(100) NOT NULL DEFAULT 'default value';
-- 4. 필드 이름 변경하기
-- examples 테이블의 Address 필드 이름을 PostCode로 변경
ALTER TABLE examples
RENAME COLUMN Address TO PostCode;



-- 5. 필드 삭제하기
-- examples 테이블에서 PostCode 필드를 삭제
ALTER TABLE examples
DROP COLUMN PostCode;


-- 6. 테이블 이름 변경하기
-- examples 테이블의 이름을 new_examples로 변경
ALTER TABLE examples
RENAME TO new_examples;


-- 7. 테이블 삭제하기
-- new_examples 테이블을 삭제
-- examples 테이블을 삭제

DROP TABLE new_examples;