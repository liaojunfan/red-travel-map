CREATE DATABASE red_tour;
USE red_tour;

CREATE TABLE red_site(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL COMMENT '点位名称',
    lon DOUBLE COMMENT '经度',
    lat DOUBLE COMMENT '纬度',
    address VARCHAR(200) COMMENT '详细地址',
    intro TEXT COMMENT '红色文化简介',
    county VARCHAR(50) COMMENT '所属区县'
);

INSERT INTO red_site(name,lon,lat,address,intro,county)
VALUES
('猴场会议会址',107.48,27.05,'黔南州瓮安县猴场镇','猴场会议被称为伟大转折的前夜，在遵义会议之前作出一系列重要决策。','瓮安县'),
('邓恩铭故居',107.37,26.58,'黔南州荔波县玉屏街道','邓恩铭是中共一大代表，贵州革命先驱。','荔波县');