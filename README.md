# repltile_dy
关于斗鱼的那几个项目中，还需要添加数据库  
在online.py中，会对每个房间的当前热度存储进数据库  
与此相关联的是room_hn表，其sql语句为
```mysql
  CREATE TABLE `room_hn` (
  `room_id` int(11) NOT NULL,
  `nickname` varchar(255) NOT NULL,
  `room_name` varchar(255) NOT NULL,
  `hn` int(11) DEFAULT NULL,
  `game_cate_id` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`room_id`),
  KEY `gcate` (`game_cate_id`),
  CONSTRAINT `gcate` FOREIGN KEY (`game_cate_id`) REFERENCES `game_cate` (`cate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
以及游戏分类表game_cate,其sql语句为
```mysql
CREATE TABLE `game_cate` (
  `cate_id` int(11) NOT NULL,
  `game_name` varchar(255) NOT NULL,
  `short_name` varchar(255) NOT NULL,
  `game_url` varchar(255) NOT NULL,
  `room_num` int(11) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`cate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
最后还一张表是针对礼物系统礼物图标的展示的  
在dy_rockets_data.py中，其sql语句为
```mysql
CREATE TABLE `image` (
  `img_id` int(11) NOT NULL,
  `img_name` varchar(255) COLLATE utf8_bin NOT NULL,
  `url_gif` varchar(255) COLLATE utf8_bin NOT NULL,
  `url_png` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`img_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
```
