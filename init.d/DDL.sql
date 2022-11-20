--CREATE DATABASE IF NOT EXISTS coworkerdb;
--CREATE USER worker;

-- CREATE SCHEMA room;
-- CREATE SCHEMA user;

CREATE TABLE room 
(
    room_id SERIAL PRIMARY KEY,
    owner_id NUMERIC,
    room_type VARCHAR(8),
    status VARCHAR(8)
);

COMMENT ON COLUMN room.room_id is '고유 ID, PK, AUTO-INCREMENT';
COMMENT ON COLUMN room.owner_id is '방 소유자 ( 변경될 수 없음 )';
COMMENT ON COLUMN room.room_type is '같이 모드, 따로 모드';
COMMENT ON COLUMN room.status is '방 상태 ( START, END )';


CREATE TABLE room_user
(
    room_user_no SERIAL PRIMARY KEY,
    room_id NUMERIC,
    user_id NUMERIC, -- 
    role VARCHAR(12),
    joined_at TIMESTAMP WITHOUT TIME ZONE,
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    exited_at TIMESTAMP WITHOUT TIME ZONE
);

COMMENT ON COLUMN room_user.room_user_no is 'PK, 같은 사람이어도 퇴장 후 재입장하는 경우 등에는 다른 room_user_no 를 가져요';
COMMENT ON COLUMN room_user.role is '권한 ( OWNER, PARTICIPANT, WATCHER )';
COMMENT ON COLUMN room_user.joined_at is '방 입장 시, OWNER의 경우 방 생성 시간과 같음';
COMMENT ON COLUMN room_user.updated_at is 'role 변경 시';
COMMENT ON COLUMN room_user.exited_at is '방 퇴장 시';


-- CREATE TABLE user
-- (
--     user_id SERIAL PRIMARY KEY,
--     created_at TIMESTAMP WITHOUT TIME ZONE,
--     last_updated_at TIMESTAMP WITHOUT TIME ZONE
-- )