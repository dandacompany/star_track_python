

-- 사용자 테이블 생성

CREATE TABLE users (
    user_id BIGINT NOT NULL,
    registration_date DATE NOT NULL,
    user_type VARCHAR NOT NULL,
    city VARCHAR,
    country VARCHAR
);

-- 사용자 데이터 삽입
INSERT INTO users 
(user_id, registration_date, user_type, city, country)
VALUES
(1, '2022-01-05', 'REGULAR', 'Seoul', 'South Korea'),
(2, '2022-02-15', 'PREMIUM', 'Busan', 'South Korea'),
(3, '2022-03-22', 'REGULAR', 'Incheon', 'South Korea'),
(4, '2022-01-30', 'PREMIUM', 'Daegu', 'South Korea'),
(5, '2022-04-10', 'REGULAR', 'Gwangju', 'South Korea'),
(6, '2022-05-18', 'PREMIUM', 'Seoul', 'South Korea'),
(7, '2022-06-22', 'REGULAR', 'Daejeon', 'South Korea'),
(8, '2022-07-14', 'REGULAR', 'Ulsan', 'South Korea'),
(9, '2022-08-09', 'PREMIUM', 'Seoul', 'South Korea'),
(10, '2022-09-28', 'REGULAR', 'Busan', 'South Korea'),
(11, '2022-10-17', 'PREMIUM', 'Incheon', 'South Korea'),
(12, '2022-11-05', 'REGULAR', 'Daegu', 'South Korea'),
(13, '2022-12-12', 'REGULAR', 'Gwangju', 'South Korea'),
(14, '2023-01-08', 'PREMIUM', 'Seoul', 'South Korea'),
(15, '2023-02-14', 'REGULAR', 'Busan', 'South Korea'),
(16, '2023-03-22', 'PREMIUM', 'Seoul', 'South Korea'),
(17, '2023-04-05', 'REGULAR', 'Incheon', 'South Korea'),
(18, '2023-05-19', 'REGULAR', 'Busan', 'South Korea'),
(19, '2023-06-30', 'PREMIUM', 'Seoul', 'South Korea'),
(20, '2023-07-15', 'REGULAR', 'Daegu', 'South Korea'),
(21, '2023-08-02', 'PREMIUM', 'Incheon', 'South Korea'),
(22, '2023-09-11', 'REGULAR', 'Seoul', 'South Korea'),
(23, '2023-10-24', 'REGULAR', 'Busan', 'South Korea'),
(24, '2023-11-19', 'PREMIUM', 'Daejeon', 'South Korea'),
(25, '2023-12-05', 'REGULAR', 'Seoul', 'South Korea'),
(26, '2024-01-01', 'PREMIUM', 'Busan', 'South Korea'),
(27, '2024-02-14', 'REGULAR', 'Seoul', 'South Korea'),
(28, '2024-03-19', 'REGULAR', 'Incheon', 'South Korea'),
(29, '2024-04-22', 'PREMIUM', 'Seoul', 'South Korea'),
(30, '2024-05-10', 'REGULAR', 'Busan', 'South Korea');

-- 공급업체 테이블 생성
CREATE TABLE suppliers (
    supplier_id BIGINT NOT NULL,
    supplier_name VARCHAR NOT NULL,
    contact_person VARCHAR,
    contact_email VARCHAR,
    country VARCHAR
);

-- 공급업체 데이터 삽입
INSERT INTO suppliers 
(supplier_id, supplier_name, contact_person, contact_email, country)
VALUES
(1, 'Korea Tech Suppliers', 'Park Jisung', 'park.jisung@koreatechsuppliers.com', 'South Korea'),
(2, 'Seoul Fashion Group', 'Kim Minyoung', 'kim.minyoung@seoulfashion.com', 'South Korea'),
(3, 'Busan Home Goods', 'Lee Jaeho', 'lee.jaeho@busanhome.com', 'South Korea'),
(4, 'Gyeonggi Electronics', 'Choi Yerim', 'choi.yerim@gyeonggi-electronics.com', 'South Korea'),
(5, 'Jeju Natural Products', 'Kang Siwon', 'kang.siwon@jejunatural.com', 'South Korea'),
(6, 'Daegu Kitchen Supplies', 'Jung Hana', 'jung.hana@daegukitchen.com', 'South Korea'),
(7, 'Incheon Furniture Co.', 'Yoon Taejun', 'yoon.taejun@incheonfurniture.com', 'South Korea'),
(8, 'Ulsan Industrial Goods', 'Song Minjae', 'song.minjae@ulsanindustrial.com', 'South Korea'),
(9, 'Korean Beauty Essentials', 'Han Miyeon', 'han.miyeon@koreanbeauty.com', 'South Korea'),
(10, 'Gwangju Sports Equipment', 'Lim Junho', 'lim.junho@gwangjusports.com', 'South Korea');

-- 제품 카테고리 테이블 생성
CREATE TABLE categories (
    category_id BIGINT NOT NULL,
    category_name VARCHAR NOT NULL,
    parent_category_id BIGINT
);

-- 카테고리 데이터 삽입
INSERT INTO categories 
(category_id, category_name, parent_category_id)
VALUES
(1, '전자제품', NULL),
(2, '가전제품', 1),
(3, '컴퓨터/노트북', 1),
(4, '모바일/태블릿', 1),
(5, '패션의류', NULL),
(6, '여성의류', 5),
(7, '남성의류', 5),
(8, '아동의류', 5),
(9, '가방/잡화', 5),
(10, '홈/리빙', NULL),
(11, '가구', 10),
(12, '주방용품', 10),
(13, '인테리어', 10),
(14, '뷰티/건강', NULL),
(15, '스킨케어', 14),
(16, '헤어케어', 14),
(17, '메이크업', 14),
(18, '건강식품', 14),
(19, '스포츠/레저', NULL),
(20, '운동용품', 19),
(21, '아웃도어', 19),
(22, '캠핑용품', 19);

-- 제품 테이블 생성
CREATE TABLE products (
    product_id BIGINT NOT NULL,
    product_name VARCHAR NOT NULL,
    category_id BIGINT NOT NULL,
    price NUMERIC NOT NULL,
    stock_quantity BIGINT NOT NULL,
    added_date DATE NOT NULL,
    supplier_id BIGINT NOT NULL
);

-- 제품 데이터 삽입
INSERT INTO products 
(product_id, product_name, category_id, price, stock_quantity, added_date, supplier_id)
VALUES
(101, '프리미엄 4K 스마트 TV 55인치', 2, 899000, 50, '2023-01-15', 4),
(102, '울트라 HD 스마트 TV 65인치', 2, 1299000, 35, '2023-02-05', 4),
(103, '초소형 전자레인지 20L', 2, 89000, 120, '2023-01-20', 6),
(104, '스마트 로봇 청소기', 2, 459000, 80, '2023-03-10', 4),
(105, '고효율 냉장고 500L', 2, 1599000, 25, '2023-02-12', 4),
(201, '울트라 게이밍 노트북', 3, 1699000, 30, '2023-01-10', 1),
(202, '비즈니스 슬림 노트북', 3, 1199000, 45, '2023-01-22', 1),
(203, '고성능 데스크톱 컴퓨터', 3, 1499000, 20, '2023-02-15', 1),
(204, '게이밍 마우스', 3, 89000, 150, '2023-01-05', 1),
(205, '기계식 게이밍 키보드', 3, 159000, 100, '2023-01-07', 1),
(301, '프리미엄 스마트폰', 4, 1299000, 60, '2023-01-15', 4),
(302, '태블릿 PC 10인치', 4, 699000, 55, '2023-02-10', 4),
(303, '무선 블루투스 이어폰', 4, 199000, 150, '2023-01-20', 1),
(304, '스마트워치', 4, 349000, 70, '2023-03-05', 1),
(305, '휴대폰 고속충전기', 4, 35000, 200, '2023-01-10', 1),
(401, '여성 캐시미어 코트', 6, 299000, 40, '2023-02-01', 2),
(402, '여성 슬림핏 진', 6, 89000, 100, '2023-01-10', 2),
(403, '여성 오버사이즈 니트', 6, 79000, 80, '2023-02-15', 2),
(404, '여성 블라우스', 6, 59000, 120, '2023-01-20', 2),
(405, '여성 트렌치코트', 6, 159000, 60, '2023-02-10', 2),
(501, '남성 울 코트', 7, 279000, 50, '2023-02-05', 2),
(502, '남성 슬림핏 수트', 7, 399000, 30, '2023-01-15', 2),
(503, '남성 캐주얼 셔츠', 7, 69000, 100, '2023-01-25', 2),
(504, '남성 면 티셔츠', 7, 29000, 200, '2023-01-10', 2),
(505, '남성 데님 재킷', 7, 129000, 45, '2023-02-20', 2),
(601, '원목 식탁 세트', 11, 799000, 25, '2023-02-01', 7),
(602, '천연 가죽 소파', 11, 1599000, 15, '2023-01-20', 7),
(603, '모던 책장', 11, 259000, 35, '2023-02-10', 7),
(604, '침대 프레임', 11, 459000, 20, '2023-01-15', 7),
(605, '옷장', 11, 359000, 30, '2023-02-05', 7),
(701, '스테인리스 냄비 세트', 12, 199000, 40, '2023-01-10', 6),
(702, '프리미엄 칼 세트', 12, 159000, 30, '2023-01-25', 6),
(703, '전기 커피 메이커', 12, 89000, 50, '2023-02-10', 6),
(704, '에어프라이어', 12, 129000, 70, '2023-01-15', 6),
(705, '식기 세트 20pcs', 12, 79000, 60, '2023-02-20', 6),
(801, '프리미엄 에센스', 15, 79000, 80, '2023-01-05', 9),
(802, '수분 크림', 15, 49000, 120, '2023-01-15', 9),
(803, '안티에이징 세럼', 15, 89000, 60, '2023-02-01', 9),
(804, '클렌징 폼', 15, 19000, 150, '2023-01-10', 9),
(805, '각질 제거 마스크', 15, 29000, 100, '2023-02-15', 9),
(901, '프리미엄 요가 매트', 20, 69000, 90, '2023-01-10', 10),
(902, '무게 조절 덤벨 세트', 20, 199000, 40, '2023-01-25', 10),
(903, '런닝머신', 20, 899000, 15, '2023-02-05', 10),
(904, '스포츠 물병', 20, 15000, 200, '2023-01-15', 10),
(905, '스마트 운동 밴드', 20, 49000, 100, '2023-01-20', 10);

-- 주문 테이블 생성
CREATE TABLE orders (
    order_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    order_date TIMESTAMP NOT NULL,
    total_amount NUMERIC NOT NULL,
    payment_method VARCHAR,
    order_status VARCHAR NOT NULL
);

-- 주문 데이터 삽입
INSERT INTO orders 
(order_id, user_id, order_date, total_amount, payment_method, order_status)
VALUES
(10001, 1, '2023-01-05 14:32:15', 968000, '신용카드', '배송완료'),
(10002, 3, '2023-01-07 10:15:22', 199000, '계좌이체', '배송완료'),
(10003, 5, '2023-01-10 16:45:33', 129000, '신용카드', '배송완료'),
(10004, 2, '2023-01-15 09:22:18', 1299000, '신용카드', '배송완료'),
(10005, 7, '2023-01-18 11:33:45', 108000, '간편결제', '배송완료'),
(10006, 9, '2023-01-22 15:21:10', 1598000, '신용카드', '배송완료'),
(10007, 11, '2023-01-25 14:17:29', 218000, '계좌이체', '배송완료'),
(10008, 13, '2023-01-29 10:05:55', 89000, '간편결제', '배송완료'),
(10009, 2, '2023-02-03 13:12:40', 458000, '신용카드', '배송완료'),
(10010, 4, '2023-02-07 09:45:12', 299000, '계좌이체', '배송완료'),
(10011, 6, '2023-02-10 16:33:22', 1599000, '신용카드', '배송완료'),
(10012, 8, '2023-02-15 11:22:05', 168000, '간편결제', '배송완료'),
(10013, 10, '2023-02-18 14:55:30', 279000, '신용카드', '배송완료'),
(10014, 12, '2023-02-21 10:10:15', 899000, '계좌이체', '배송완료'),
(10015, 14, '2023-02-25 15:40:28', 98000, '간편결제', '배송완료'),
(10016, 1, '2023-02-28 12:12:50', 399000, '신용카드', '배송완료'),
(10017, 3, '2023-03-04 09:30:15', 159000, '계좌이체', '배송완료'),
(10018, 5, '2023-03-08 14:22:30', 459000, '신용카드', '배송완료'),
(10019, 7, '2023-03-12 11:05:45', 79000, '간편결제', '배송완료'),
(10020, 9, '2023-03-16 16:15:10', 1299000, '신용카드', '배송완료'),
(10021, 11, '2023-03-20 10:45:22', 229000, '계좌이체', '배송완료'),
(10022, 13, '2023-03-24 13:33:05', 799000, '신용카드', '배송완료'),
(10023, 15, '2023-03-28 15:20:30', 49000, '간편결제', '배송완료'),
(10024, 2, '2023-04-02 11:15:20', 1699000, '신용카드', '배송완료'),
(10025, 4, '2023-04-06 09:40:32', 108000, '계좌이체', '배송완료'),
(10026, 6, '2023-04-10 14:25:18', 259000, '신용카드', '배송완료'),
(10027, 8, '2023-04-15 16:50:05', 69000, '간편결제', '배송완료'),
(10028, 10, '2023-04-19 10:30:45', 1199000, '신용카드', '배송완료'),
(10029, 12, '2023-04-22 13:15:30', 348000, '계좌이체', '배송완료'),
(10030, 14, '2023-04-26 15:45:22', 199000, '신용카드', '배송완료'),
(10031, 16, '2023-04-30 11:10:40', 35000, '간편결제', '배송완료'),
(10032, 1, '2023-05-04 14:20:15', 1599000, '신용카드', '배송완료'),
(10033, 3, '2023-05-08 10:35:45', 178000, '계좌이체', '배송완료'),
(10034, 5, '2023-05-12 16:42:30', 359000, '신용카드', '배송완료'),
(10035, 7, '2023-05-16 09:30:22', 89000, '간편결제', '배송완료'),
(10036, 9, '2023-05-20 13:25:10', 899000, '신용카드', '배송완료'),
(10037, 11, '2023-05-24 11:10:33', 318000, '계좌이체', '배송완료'),
(10038, 13, '2023-05-28 15:30:45', 129000, '신용카드', '배송완료'),
(10039, 2, '2023-06-01 10:15:20', 1299000, '신용카드', '배송완료'),
(10040, 4, '2023-06-05 14:45:33', 138000, '계좌이체', '배송완료'),
(10041, 6, '2023-06-09 09:30:45', 459000, '신용카드', '배송완료'),
(10042, 8, '2023-06-13 16:20:10', 29000, '간편결제', '배송완료'),
(10043, 10, '2023-06-17 11:40:22', 799000, '신용카드', '배송완료'),
(10044, 12, '2023-06-21 13:15:50', 238000, '계좌이체', '배송완료'),
(10045, 14, '2023-06-25 15:35:15', 159000, '신용카드', '배송완료'),
(10046, 16, '2023-06-29 10:45:30', 49000, '간편결제', '배송완료'),
(10047, 18, '2023-07-03 14:10:25', 1199000, '신용카드', '배송완료'),
(10048, 20, '2023-07-07 09:35:40', 168000, '계좌이체', '배송완료'),
(10049, 22, '2023-07-11 16:25:15', 359000, '신용카드', '배송완료'),
(10050, 24, '2023-07-15 11:30:22', 79000, '간편결제', '배송완료'),
(10051, 26, '2023-07-19 13:45:10', 699000, '신용카드', '배송완료'),
(10052, 28, '2023-07-23 10:20:33', 258000, '계좌이체', '배송완료'),
(10053, 30, '2023-07-27 15:40:45', 149000, '신용카드', '배송완료'),
(10054, 17, '2023-07-31 12:15:30', 49000, '간편결제', '배송완료'),
(10055, 19, '2023-08-04 09:20:15', 1299000, '신용카드', '배송완료'),
(10056, 21, '2023-08-08 14:35:33', 198000, '계좌이체', '배송완료'),
(10057, 23, '2023-08-12 11:45:45', 259000, '신용카드', '배송완료'),
(10058, 25, '2023-08-16 16:10:22', 69000, '간편결제', '배송완료'),
(10059, 27, '2023-08-20 10:30:10', 899000, '신용카드', '배송완료'),
(10060, 29, '2023-08-24 13:25:50', 278000, '계좌이체', '배송완료'),
(10061, 1, '2023-08-28 15:15:15', 129000, '신용카드', '배송완료'),
(10062, 3, '2023-09-01 10:30:25', 1599000, '신용카드', '배송완료'),
(10063, 5, '2023-09-05 14:15:40', 88000, '계좌이체', '배송완료'),
(10064, 7, '2023-09-09 09:45:15', 359000, '신용카드', '배송완료'),
(10065, 9, '2023-09-13 16:30:22', 49000, '간편결제', '배송완료'),
(10066, 11, '2023-09-17 11:20:10', 799000, '신용카드', '배송완료'),
(10067, 13, '2023-09-21 13:40:33', 228000, '계좌이체', '배송완료'),
(10068, 15, '2023-09-25 15:25:45', 159000, '신용카드', '배송완료'),
(10069, 17, '2023-09-29 10:10:30', 29000, '간편결제', '배송완료'),
(10070, 2, '2023-10-03 14:25:15', 1299000, '신용카드', '배송완료'),
(10071, 4, '2023-10-07 09:40:33', 158000, '계좌이체', '배송완료'),
(10072, 6, '2023-10-11 16:15:45', 459000, '신용카드', '배송완료'),
(10073, 8, '2023-10-15 11:45:22', 89000, '간편결제', '배송완료'),
(10074, 10, '2023-10-19 13:30:10', 699000, '신용카드', '배송완료'),
(10075, 12, '2023-10-23 10:35:50', 248000, '계좌이체', '배송완료'),
(10076, 14, '2023-10-27 15:20:15', 129000, '신용카드', '배송완료'),
(10077, 16, '2023-10-31 12:45:30', 35000, '간편결제', '배송완료'),
(10078, 18, '2023-11-04 09:15:25', 1199000, '신용카드', '배송완료'),
(10079, 20, '2023-11-08 14:30:40', 128000, '계좌이체', '배송완료'),
(10080, 22, '2023-11-12 11:25:15', 359000, '신용카드', '배송완료'),
(10081, 24, '2023-11-16 16:40:22', 79000, '간편결제', '배송완료'),
(10082, 26, '2023-11-20 10:15:10', 899000, '신용카드', '배송완료'),
(10083, 28, '2023-11-24 13:35:33', 258000, '계좌이체', '배송완료'),
(10084, 30, '2023-11-28 15:45:45', 149000, '신용카드', '배송완료'),
(10085, 1, '2023-12-02 10:20:15', 1599000, '신용카드', '배송완료'),
(10086, 3, '2023-12-06 14:45:33', 198000, '계좌이체', '배송완료'),
(10087, 5, '2023-12-10 09:30:45', 259000, '신용카드', '배송완료'),
(10088, 7, '2023-12-14 16:15:22', 69000, '간편결제', '배송완료'),
(10089, 9, '2023-12-18 11:40:10', 1299000, '신용카드', '배송완료'),
(10090, 11, '2023-12-22 13:20:50', 328000, '계좌이체', '배송완료'),
(10091, 13, '2023-12-26 15:10:15', 199000, '신용카드', '배송완료'),
(10092, 15, '2023-12-30 12:35:30', 49000, '간편결제', '배송완료'),
(10093, 17, '2024-01-03 14:15:20', 1199000, '신용카드', '배송완료'),
(10094, 19, '2024-01-07 09:30:33', 138000, '계좌이체', '배송완료'),
(10095, 21, '2024-01-11 16:40:45', 459000, '신용카드', '배송완료'),
(10096, 23, '2024-01-15 11:25:22', 29000, '간편결제', '배송완료'),
(10097, 25, '2024-01-19 13:35:10', 899000, '신용카드', '배송완료'),
(10098, 27, '2024-01-23 10:15:50', 278000, '계좌이체', '배송완료'),
(10099, 29, '2024-01-27 15:30:15', 159000, '신용카드', '배송완료'),
(10100, 2, '2024-01-31 12:45:30', 1699000, '신용카드', '배송완료'),
(10101, 4, '2024-02-04 09:20:25', 299000, '계좌이체', '배송완료'),
(10102, 6, '2024-02-08 14:35:40', 1599000, '신용카드', '배송완료'),
(10103, 8, '2024-02-12 11:15:15', 89000, '간편결제', '배송완료'),
(10104, 10, '2024-02-16 16:30:22', 1199000, '신용카드', '배송완료'),
(10105, 12, '2024-02-20 10:45:10', 899000, '계좌이체', '배송완료'),
(10106, 14, '2024-02-24 13:20:33', 129000, '신용카드', '배송완료'),
(10107, 16, '2024-02-28 15:40:45', 49000, '간편결제', '배송완료'),
(10108, 18, '2024-03-03 10:15:15', 1299000, '신용카드', '배송완료'),
(10109, 20, '2024-03-07 14:30:33', 79000, '계좌이체', '배송완료'),
(10110, 22, '2024-03-11 09:45:45', 359000, '신용카드', '배송완료'),
(10111, 24, '2024-03-15 16:20:22', 749000, '간편결제', '배송완료'),
(10112, 26, '2024-03-19 11:30:10', 699000, '신용카드', '배송완료'),
(10113, 28, '2024-03-23 13:45:50', 258000, '계좌이체', '배송완료'),
(10114, 30, '2024-03-27 15:15:15', 149000, '신용카드', '배송완료'),
(10115, 1, '2024-03-31 12:30:30', 899000, '신용카드', '배송완료'),
(10116, 3, '2024-04-04 14:20:20', 199000, '계좌이체', '배송중'),
(10117, 5, '2024-04-08 09:35:33', 259000, '신용카드', '배송중'),
(10118, 7, '2024-04-12 16:10:45', 69000, '간편결제', '배송중'),
(10119, 9, '2024-04-16 11:45:22', 1299000, '신용카드', '배송중'),
(10120, 11, '2024-04-20 13:25:10', 328000, '계좌이체', '배송중'),
(10121, 13, '2024-04-24 10:40:50', 129000, '신용카드', '배송중'),
(10122, 15, '2024-04-28 15:15:15', 49000, '간편결제', '배송준비중'),
(10123, 2, '2024-05-02 10:30:25', 1699000, '신용카드', '배송준비중'),
(10124, 4, '2024-05-06 14:15:40', 299000, '계좌이체', '배송준비중'),
(10125, 6, '2024-05-10 09:35:15', 459000, '신용카드', '배송준비중'),
(10126, 8, '2024-05-14 16:45:22', 89000, '간편결제', '결제완료'),
(10127, 10, '2024-05-15 11:20:10', 1199000, '신용카드', '결제완료'),
(10128, 12, '2024-05-16 13:30:33', 899000, '계좌이체', '결제완료'),
(10129, 14, '2024-05-17 15:45:45', 129000, '신용카드', '결제완료'),
(10130, 16, '2024-05-18 12:15:30', 49000, '간편결제', '결제완료');

-- 주문 상세 테이블 생성
CREATE TABLE order_items (
    order_item_id BIGINT NOT NULL,
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity BIGINT NOT NULL,
    price_per_unit NUMERIC NOT NULL,
    discount NUMERIC DEFAULT 0
);

-- 주문 상세 데이터 삽입
INSERT INTO order_items 
(order_item_id, order_id, product_id, quantity, price_per_unit, discount)
VALUES
(1001, 10001, 201, 1, 899000, 0),
(1002, 10001, 305, 2, 35000, 1000),
(1003, 10002, 303, 1, 199000, 0),
(1004, 10003, 704, 1, 129000, 0),
(1005, 10004, 301, 1, 1299000, 0),
(1006, 10005, 804, 2, 19000, 0),
(1007, 10005, 805, 2, 29000, 0),
(1008, 10005, 904, 1, 15000, 0),
(1009, 10006, 105, 1, 1599000, 1000),
(1010, 10007, 403, 1, 79000, 0),
(1011, 10007, 404, 1, 59000, 0),
(1012, 10007, 904, 5, 15000, 0),
(1013, 10008, 103, 1, 89000, 0),
(1014, 10009, 104, 1, 459000, 1000),
(1015, 10010, 401, 1, 299000, 0),
(1016, 10011, 105, 1, 1599000, 0),
(1017, 10012, 801, 1, 79000, 0),
(1018, 10012, 802, 1, 49000, 0),
(1019, 10012, 804, 2, 19000, 0),
(1020, 10013, 501, 1, 279000, 0),
(1021, 10014, 101, 1, 899000, 0),
(1022, 10015, 802, 2, 49000, 0),
(1023, 10016, 502, 1, 399000, 0),
(1024, 10017, 205, 1, 159000, 0),
(1025, 10018, 104, 1, 459000, 0),
(1026, 10019, 403, 1, 79000, 0),
(1027, 10020, 301, 1, 1299000, 0),
(1028, 10021, 305, 1, 35000, 0),
(1029, 10021, 304, 1, 349000, 155000),
(1030, 10022, 601, 1, 799000, 0),
(1031, 10023, 802, 1, 49000, 0),
(1032, 10024, 201, 1, 1699000, 0),
(1033, 10025, 804, 2, 19000, 0),
(1034, 10025, 805, 2, 29000, 0),
(1035, 10025, 904, 1, 15000, 3000),
(1036, 10026, 603, 1, 259000, 0),
(1037, 10027, 901, 1, 69000, 0),
(1038, 10028, 202, 1, 1199000, 0),
(1039, 10029, 304, 1, 349000, 1000),
(1040, 10030, 303, 1, 199000, 0),
(1041, 10031, 305, 1, 35000, 0),
(1042, 10032, 105, 1, 1599000, 0),
(1043, 10033, 801, 1, 79000, 0),
(1044, 10033, 802, 2, 49000, 0),
(1045, 10033, 904, 1, 15000, 14000),
(1046, 10034, 605, 1, 359000, 0),
(1047, 10035, 103, 1, 89000, 0),
(1048, 10036, 101, 1, 899000, 0),
(1049, 10037, 403, 4, 79000, 0),
(1050, 10038, 704, 1, 129000, 0),
(1051, 10039, 301, 1, 1299000, 0),
(1052, 10040, 804, 2, 19000, 0),
(1053, 10040, 805, 3, 29000, 0),
(1054, 10040, 904, 2, 15000, 0),
(1055, 10041, 104, 1, 459000, 0),
(1056, 10042, 504, 1, 29000, 0),
(1057, 10043, 601, 1, 799000, 0),
(1058, 10044, 703, 1, 89000, 0),
(1059, 10044, 705, 2, 79000, 9000),
(1060, 10045, 205, 1, 159000, 0),
(1061, 10046, 802, 1, 49000, 0),
(1062, 10047, 202, 1, 1199000, 0),
(1063, 10048, 801, 1, 79000, 0),
(1064, 10048, 802, 1, 49000, 0),
(1065, 10048, 804, 2, 19000, 0),
(1066, 10048, 904, 1, 15000, 13000),
(1067, 10049, 605, 1, 359000, 0),
(1068, 10050, 403, 1, 79000, 0),
(1069, 10051, 302, 1, 699000, 0),
(1070, 10052, 701, 1, 199000, 0),
(1071, 10052, 904, 4, 15000, 0),
(1072, 10053, 905, 1, 49000, 0),
(1073, 10053, 801, 1, 79000, 0),
(1074, 10053, 804, 1, 19000, 0),
(1075, 10053, 304, 1, 349000, 347000),
(1076, 10054, 802, 1, 49000, 0),
(1077, 10055, 301, 1, 1299000, 0),
(1078, 10056, 801, 1, 79000, 0),
(1079, 10056, 802, 1, 49000, 0),
(1080, 10056, 804, 2, 19000, 0),
(1081, 10056, 904, 2, 15000, 0),
(1082, 10057, 603, 1, 259000, 0),
(1083, 10058, 901, 1, 69000, 0),
(1084, 10059, 101, 1, 899000, 0),
(1085, 10060, 403, 2, 79000, 0),
(1086, 10060, 404, 2, 59000, 0),
(1087, 10061, 704, 1, 129000, 0),
(1088, 10062, 105, 1, 1599000, 0),
(1089, 10063, 804, 2, 19000, 0),
(1090, 10063, 805, 2, 29000, 9000),
(1091, 10064, 605, 1, 359000, 0),
(1092, 10065, 802, 1, 49000, 0),
(1093, 10066, 601, 1, 799000, 0),
(1094, 10067, 703, 1, 89000, 0),
(1095, 10067, 705, 1, 79000, 0),
(1096, 10067, 904, 4, 15000, 0),
(1097, 10068, 205, 1, 159000, 0),
(1098, 10069, 504, 1, 29000, 0),
(1099, 10070, 301, 1, 1299000, 0),
(1100, 10071, 801, 1, 79000, 0),
(1101, 10071, 802, 1, 49000, 0),
(1102, 10071, 804, 2, 19000, 9000),
(1103, 10072, 104, 1, 459000, 0),
(1104, 10073, 103, 1, 89000, 0),
(1105, 10074, 302, 1, 699000, 0),
(1106, 10075, 403, 1, 79000, 0),
(1107, 10075, 404, 1, 59000, 0),
(1108, 10075, 405, 1, 159000, 49000),
(1109, 10076, 704, 1, 129000, 0),
(1110, 10077, 305, 1, 35000, 0),
(1111, 10078, 202, 1, 1199000, 0),
(1112, 10079, 801, 1, 79000, 0),
(1113, 10079, 802, 1, 49000, 0),
(1114, 10080, 605, 1, 359000, 0),
(1115, 10081, 403, 1, 79000, 0),
(1116, 10082, 101, 1, 899000, 0),
(1117, 10083, 701, 1, 199000, 0),
(1118, 10083, 904, 4, 15000, 1000),
(1119, 10084, 905, 1, 49000, 0),
(1120, 10084, 801, 1, 79000, 0),
(1121, 10084, 804, 1, 19000, 0),
(1122, 10085, 105, 1, 1599000, 0),
(1123, 10086, 801, 1, 79000, 0),
(1124, 10086, 802, 1, 49000, 0),
(1125, 10086, 804, 2, 19000, 0),
(1126, 10086, 904, 2, 15000, 0),
(1127, 10087, 603, 1, 259000, 0),
(1128, 10088, 901, 1, 69000, 0),
(1129, 10089, 301, 1, 1299000, 0),
(1130, 10090, 403, 3, 79000, 0),
(1131, 10090, 404, 2, 59000, 28000),
(1132, 10091, 303, 1, 199000, 0),
(1133, 10092, 802, 1, 49000, 0),
(1134, 10093, 202, 1, 1199000, 0),
(1135, 10094, 801, 1, 79000, 0),
(1136, 10094, 802, 1, 49000, 0),
(1137, 10094, 904, 1, 15000, 5000),
(1138, 10095, 104, 1, 459000, 0),
(1139, 10096, 504, 1, 29000, 0),
(1140, 10097, 101, 1, 899000, 0),
(1141, 10098, 703, 1, 89000, 0),
(1142, 10098, 705, 1, 79000, 0),
(1143, 10098, 904, 4, 15000, 0),
(1144, 10098, 503, 2, 69000, 28000),
(1145, 10099, 205, 1, 159000, 0),
(1146, 10100, 201, 1, 1699000, 0),
(1147, 10101, 401, 1, 299000, 0),
(1148, 10102, 105, 1, 1599000, 0),
(1149, 10103, 103, 1, 89000, 0),
(1150, 10104, 202, 1, 1199000, 0),
(1151, 10105, 101, 1, 899000, 0),
(1152, 10106, 704, 1, 129000, 0),
(1153, 10107, 802, 1, 49000, 0),
(1154, 10108, 301, 1, 1299000, 0),
(1155, 10109, 403, 1, 79000, 0),
(1156, 10110, 605, 1, 359000, 0),
(1157, 10111, 602, 1, 749000, 0),
(1158, 10112, 302, 1, 699000, 0),
(1159, 10113, 701, 1, 199000, 0),
(1160, 10113, 904, 4, 15000, 1000),
(1161, 10114, 905, 1, 49000, 0),
(1162, 10114, 801, 1, 79000, 0),
(1163, 10114, 804, 1, 19000, 0),
(1164, 10115, 101, 1, 899000, 0),
(1165, 10116, 303, 1, 199000, 0),
(1166, 10117, 603, 1, 259000, 0),
(1167, 10118, 901, 1, 69000, 0),
(1168, 10119, 301, 1, 1299000, 0),
(1169, 10120, 403, 3, 79000, 0),
(1170, 10120, 404, 2, 59000, 28000),
(1171, 10121, 704, 1, 129000, 0),
(1172, 10122, 802, 1, 49000, 0),
(1173, 10123, 201, 1, 1699000, 0),
(1174, 10124, 401, 1, 299000, 0),
(1175, 10125, 104, 1, 459000, 0),
(1176, 10126, 103, 1, 89000, 0),
(1177, 10127, 202, 1, 1199000, 0),
(1178, 10128, 101, 1, 899000, 0),
(1179, 10129, 704, 1, 129000, 0),
(1180, 10130, 802, 1, 49000, 0);

-- 제품 리뷰 테이블 생성
CREATE TABLE reviews (
    review_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    rating BIGINT NOT NULL,
    review_text VARCHAR,
    review_date TIMESTAMP NOT NULL
);

-- 제품 리뷰 데이터 삽입
INSERT INTO reviews 
(review_id, product_id, user_id, rating, review_text, review_date)
VALUES
(1, 101, 1, 5, '화질이 정말 좋고 스마트 기능도 완벽해요!', '2023-01-20 15:30:00'),
(2, 101, 14, 4, '가성비 좋은 TV입니다. 다만 설치가 조금 어려웠어요.', '2023-03-05 10:15:00'),
(3, 101, 22, 5, '선명한 화질과 빠른 반응 속도에 만족합니다.', '2023-05-12 18:45:00'),
(4, 102, 9, 5, '대형 TV의 화질이 정말 훌륭합니다!', '2023-03-10 14:20:00'),
(5, 102, 16, 3, '배송 중 약간의 충격이 있었는지 모서리가 살짝 깨져있었어요.', '2023-04-22 09:30:00'),
(6, 103, 3, 4, '컴팩트한 사이즈로 원룸에 딱 맞아요.', '2023-02-10 12:45:00'),
(7, 103, 13, 5, '가격 대비 성능이 훌륭합니다!', '2023-02-28 16:20:00'),
(8, 104, 2, 5, '로봇 청소기가 정말 스마트하게 집안을 청소해줘요!', '2023-02-15 11:10:00'),
(9, 104, 24, 4, '먼지 흡입력이 좋습니다. 다만 좁은 틈새는 청소가 어려워요.', '2023-03-30 14:50:00'),
(10, 105, 6, 5, '넓은 용량과 효율적인 냉각 시스템이 마음에 들어요.', '2023-03-01 13:25:00'),
(11, 201, 1, 5, '게임할 때 정말 빠르고 발열도 적어요!', '2023-01-25 17:40:00'),
(12, 201, 19, 4, '그래픽 성능이 좋지만 배터리 소모가 빠른 편입니다.', '2023-04-18 09:15:00'),
(13, 202, 4, 5, '가볍고 성능도 좋아 업무용으로 완벽해요.', '2023-02-12 15:30:00'),
(14, 202, 18, 4, '휴대성이 좋고 디자인도 세련되었습니다.', '2023-05-05 11:20:00'),
(15, 203, 10, 5, '빠른 처리 속도로 작업 효율이 높아졌어요!', '2023-04-10 14:15:00'),
(16, 204, 7, 5, '게임할 때 정확한 조준이 가능해요. 감도 조절도 쉽습니다.', '2023-02-08 16:40:00'),
(17, 204, 15, 4, '그립감이 좋고 반응속도도 빠릅니다.', '2023-03-22 10:05:00'),
(18, 205, 5, 5, '타건감이 정말 좋고 RGB 라이팅도 멋있어요!', '2023-02-10 18:30:00'),
(19, 205, 20, 3, '키감은 좋으나 소음이 생각보다 커요.', '2023-05-15 13:45:00'),
(20, 301, 9, 5, '카메라 성능이 뛰어나고 배터리도 오래 갑니다!', '2023-02-20 15:15:00'),
(21, 301, 11, 4, '디자인이 세련되었지만 가격이 조금 비싼 편이에요.', '2023-04-05 10:30:00'),
(22, 302, 26, 5, '화면이 크고 선명해서 영상 시청이나 그림 그리기에 좋아요.', '2023-03-15 16:45:00'),
(23, 303, 2, 5, '음질이 뛰어나고 노이즈 캔슬링 기능도 훌륭해요!', '2023-02-10 14:20:00'),
(24, 303, 14, 4, '편안한 착용감과 좋은 음질에 만족합니다.', '2023-03-25 11:10:00'),
(25, 304, 21, 4, '건강 관리 기능이 다양하고 정확해요.', '2023-04-08 17:30:00'),
(26, 305, 3, 5, '충전 속도가 정말 빠릅니다!', '2023-02-05 09:45:00'),
(27, 401, 4, 5, '소재가 정말 고급스럽고 따뜻해요.', '2023-02-15 13:20:00'),
(28, 402, 8, 4, '핏이 예쁘고 신축성이 좋아요.', '2023-03-10 16:45:00'),
(29, 403, 12, 5, '포근하고 스타일리시한 니트입니다.', '2023-02-25 11:30:00'),
(30, 404, 16, 4, '소재가 좋고 디자인이 세련되었어요.', '2023-04-02 15:10:00'),
(31, 501, 5, 5, '따뜻하고 고급스러운 코트입니다.', '2023-02-18 14:25:00'),
(32, 502, 9, 4, '핏이 좋고 디테일이 세심해요.', '2023-03-12 17:40:00'),
(33, 503, 13, 5, '편안하면서도 멋스러운 셔츠입니다.', '2023-04-05 10:15:00'),
(34, 504, 17, 4, '소재가 좋고 착용감이 편안해요.', '2023-04-15 13:50:00'),
(35, 601, 6, 5, '고급스러운 디자인과 견고한 제작에 만족합니다.', '2023-03-02 15:20:00'),
(36, 602, 10, 4, '편안한 착석감과 고급스러운 질감이 좋아요.', '2023-04-08 14:35:00'),
(37, 603, 14, 5, '실용적이고 인테리어 효과도 좋습니다.', '2023-03-18 11:45:00'),
(38, 604, 18, 4, '튼튼하고 디자인도 깔끔해요.', '2023-05-05 16:30:00'),
(39, 701, 7, 5, '열전도율이 좋고 디자인도 예뻐요.', '2023-02-12 10:25:00'),
(40, 702, 11, 4, '날카롭고 손잡이가 편안해요.', '2023-03-25 13:40:00'),
(41, 703, 15, 5, '커피 맛이 좋고 사용이 간편합니다.', '2023-04-15 09:20:00'),
(42, 704, 19, 4, '기름 없이 요리할 수 있어 건강에 좋아요.', '2023-05-08 14:15:00'),
(43, 801, 8, 5, '피부 흡수력이 좋고 효과가 빠르게 나타나요.', '2023-02-15 11:30:00'),
(44, 802, 12, 4, '촉촉함이 오래 지속되고 향이 좋아요.', '2023-03-28 16:50:00'),
(45, 803, 16, 5, '사용 후 피부가 확실히 탄력있어 보여요.', '2023-04-20 13:25:00'),
(46, 804, 20, 4, '순하면서도 세정력이 좋아요.', '2023-05-10 10:45:00'),
(47, 805, 24, 5, '사용 후 피부가 한결 부드러워졌어요.', '2023-05-25 14:20:00'),
(48, 901, 1, 5, '쿠션감이 좋고 미끄럼 방지 기능이 탁월해요.', '2023-02-05 15:45:00'),
(49, 902, 5, 4, '무게 조절이 편리하고 품질이 좋아요.', '2023-03-15 12:30:00'),
(50, 903, 9, 5, '다양한 프로그램과 안정적인 주행감이 좋아요.', '2023-04-10 17:20:00'),
(51, 904, 13, 4, '디자인이 세련되고 보온/보냉 효과가 좋아요.', '2023-03-22 09:50:00'),
(52, 905, 17, 5, '정확한 측정과 다양한 기능이 마음에 들어요.', '2023-05-02 14:15:00'),
(53, 201, 21, 4, '디자인이 멋지고 성능도 좋아요.', '2023-06-10 11:30:00'),
(54, 301, 25, 5, '배터리 수명이 길고 카메라 품질이 훌륭해요.', '2023-06-15 15:45:00'),
(55, 401, 29, 4, '따뜻하고 스타일리시한 코트에요.', '2023-06-20 13:20:00'),
(56, 501, 2, 5, '소재가 고급스럽고 핏이 완벽해요.', '2023-06-25 16:40:00'),
(57, 601, 6, 4, '조립이 쉽고 품질이 우수해요.', '2023-07-05 10:15:00'),
(58, 701, 10, 5, '열전도율이 좋고 손잡이가 뜨거워지지 않아요.', '2023-07-10 14:50:00'),
(59, 801, 14, 4, '피부 톤이 밝아지고 보습 효과가 좋아요.', '2023-07-15 12:30:00'),
(60, 901, 18, 5, '접이식이라 보관이 편리하고 쿠션감이 좋아요.', '2023-07-20 09:45:00'),
(61, 101, 22, 4, '화질은 좋으나 스피커 음질이 조금 아쉬워요.', '2023-07-25 16:20:00'),
(62, 201, 26, 5, '게임 성능이 뛰어나고 발열 관리가 잘 돼요.', '2023-08-01 13:10:00'),
(63, 301, 30, 4, '속도가 빠르고 화면이 선명해요.', '2023-08-05 15:30:00'),
(64, 401, 3, 5, '디자인이 세련되고 보온성이 뛰어나요.', '2023-08-10 11:45:00'),
(65, 501, 7, 4, '소재는 좋으나 사이즈가 조금 작은 편이에요.', '2023-08-15 14:20:00'),
(66, 601, 11, 5, '견고하고 디자인이 모던해요.', '2023-08-20 10:35:00'),
(67, 701, 15, 4, '열이 고르게 전달되고 세척이 용이해요.', '2023-08-25 16:50:00'),
(68, 801, 19, 5, '피부 진정 효과가 뛰어나고 흡수가 잘 돼요.', '2023-09-01 13:15:00'),
(69, 901, 23, 4, '내구성이 좋고 미끄럼 방지 효과가 탁월해요.', '2023-09-05 09:40:00'),
(70, 102, 27, 5, '선명한 화질과 다양한 스마트 기능이 마음에 들어요.', '2023-09-10 15:25:00'),
(71, 202, 1, 4, '가볍고 배터리 수명이 좋아요.', '2023-09-15 12:10:00'),
(72, 302, 5, 5, '반응 속도가 빠르고 화면이 선명해요.', '2023-09-20 16:35:00'),
(73, 402, 9, 4, '신축성이 좋고 착용감이 편안해요.', '2023-09-25 11:50:00'),
(74, 502, 13, 5, '핏이 완벽하고 소재가 고급스러워요.', '2023-10-01 14:30:00'),
(75, 602, 17, 4, '편안함과 디자인 모두 만족스러워요.', '2023-10-05 10:45:00'),
(76, 702, 21, 5, '날카롭고 손잡이가 그립감이 좋아요.', '2023-10-10 15:20:00'),
(77, 802, 25, 4, '피부 보습력이 뛰어나고 흡수가 잘 돼요.', '2023-10-15 12:40:00'),
(78, 902, 29, 5, '튼튼하고 실용적이에요.', '2023-10-20 09:15:00'),
(79, 103, 2, 4, '크기가 적당하고 성능이 우수해요.', '2023-10-25 16:30:00'),
(80, 203, 6, 5, '처리 속도가 빠르고 화면이 선명해요.', '2023-11-01 13:50:00'),
(81, 303, 10, 4, '음질이 좋고 착용감이 편안해요.', '2023-11-05 10:25:00'),
(82, 403, 14, 5, '소재가 부드럽고 디자인이 세련됐어요.', '2023-11-10 15:40:00'),
(83, 503, 18, 4, '디자인이 세련되고 착용감이 좋아요.', '2023-11-15 12:15:00'),
(84, 603, 22, 5, '조립이 쉽고 견고해요.', '2023-11-20 09:30:00'),
(85, 703, 26, 4, '사용이 간편하고 커피 맛이 좋아요.', '2023-11-25 16:45:00'),
(86, 803, 30, 5, '피부에 효과가 눈에 띄게 나타나요.', '2023-12-01 13:20:00'),
(87, 903, 3, 4, '다양한 프로그램과 모니터 기능이 유용해요.', '2023-12-05 10:40:00'),
(88, 104, 7, 5, '청소 성능이 우수하고 소음이 적어요.', '2023-12-10 15:15:00'),
(89, 204, 11, 4, '반응 속도가 빠르고 디자인이 깔끔해요.', '2023-12-15 12:30:00'),
(90, 304, 15, 5, '기능이 다양하고 배터리 수명이 긴 편이에요.', '2023-12-20 09:55:00'),
(91, 404, 19, 4, '소재가 좋고 디자인이 우아해요.', '2023-12-25 16:10:00'),
(92, 504, 23, 5, '착용감이 좋고 소재가 부드러워요.', '2024-01-01 13:35:00'),
(93, 604, 27, 4, '조립이 쉽고 디자인이 모던해요.', '2024-01-05 10:50:00'),
(94, 704, 1, 5, '요리가 빨리되고 세척이 간편해요.', '2024-01-10 15:05:00'),
(95, 804, 5, 4, '피부에 자극이 없고 세정력이 좋아요.', '2024-01-15 12:25:00'),
(96, 904, 9, 5, '디자인이 예쁘고 보온 효과가 좋아요.', '2024-01-20 09:40:00'),
(97, 105, 13, 4, '용량이 넉넉하고 절전 기능이 우수해요.', '2024-01-25 16:55:00'),
(98, 205, 17, 5, '타건감이 좋고 디자인이 멋있어요.', '2024-02-01 13:30:00'),
(99, 305, 21, 4, '충전 속도가 빠르고 휴대가 간편해요.', '2024-02-05 10:45:00'),
(100, 405, 25, 5, '디자인이 우아하고, 핏이 좋아요.', '2024-02-10 15:20:00');
