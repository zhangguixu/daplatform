CREATE TABLE `originText` (
  `id` varchar(50) NOT NULL COMMENT '文本的id号，用以唯一地区分文本',
  `title` varchar(1000) DEFAULT NULL COMMENT '法律判决书名',
  `type` varchar(200) DEFAULT NULL COMMENT '法律文本类型。--有以下种类：民事，刑事，行政，知识产权，执行，赔偿',
  `date` text COMMENT '法律文本提交时间',
  `accuser` text COMMENT '原告。只有 民事案件 才有此字段',
  `defendant` text COMMENT '被告',
  `publicProsecutionOrgan` text COMMENT '公诉机关。刑事案件特有的字段',
  `authorizedAgent` text COMMENT '委托代理人。通常是代理律师',
  `issue` text COMMENT '纠纷。民事案件和知识产权中的纠纷。例如，保险事故责任纠纷，侵犯商标纠纷，婚姻财产纠纷等',
  `crime` text COMMENT '罪名。刑事案件中的罪名，例如危险驾驶罪，受贿罪等',
  `law` text COMMENT '法律依据',
  `judgement` text COMMENT '判决结果',
  `content` longtext COMMENT '法律判决书全文内容',
  `place` text COMMENT '案件所发生的地点，',
  PRIMARY KEY (`id`),
  KEY `index_id` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文本内容和浅层结构化数据表'


CREATE TABLE `type_translate` (
  `code` bigint(200) NOT NULL DEFAULT '0' COMMENT '编码',
  `type` varchar(1000) DEFAULT NULL COMMENT '对应的意义、类型',
  PRIMARY KEY (`code`),
  KEY `index_code` (`code`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='类型转换，将文本与数值相对应\r\n1位和2位数表示年月日等基本数字信息\r\n3位数为案件类型\r\n4位数为案件详细纠纷或者罪名（学名：案由）1000-1999为刑事案件，2000-2999为民事案件，3000-3999为行政案件\r\n5位数为法律法规\r\n6位数为地名'

CREATE TABLE `caseTypeToCode`(
  `id` int not null AUTO_INCREMENT COMMENT '案件类型的代码',
  `name` varchar(50) not null COMMENT '案件类型名称',
  PRIMARY KEY(`id`)
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8

CREATE TABLE `placetocode`(
  `code` bigint(200) NOT NULL COMMENT '编码',
  `name` varchar(1000) NOT NULL COMMENT '地点名称',
  PRIMARY KEY (`code`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8