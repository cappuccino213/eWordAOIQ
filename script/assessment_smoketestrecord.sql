/*
 Navicat Premium Data Transfer

 Source Server         : 禅道
 Source Server Type    : MySQL
 Source Server Version : 100414
 Source Host           : 192.168.1.43:3306
 Source Schema         : zentao

 Target Server Type    : MySQL
 Target Server Version : 100414
 File Encoding         : 65001

 Date: 05/09/2022 10:58:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for assessment_smoketestrecord
-- ----------------------------
DROP TABLE IF EXISTS `assessment_smoketestrecord`;
CREATE TABLE `assessment_smoketestrecord`  (
  `id` mediumint NOT NULL AUTO_INCREMENT,
  `testTaskID` mediumint NOT NULL COMMENT '测试单id',
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试单标题',
  `product` mediumint NOT NULL COMMENT '产品id',
  `project` mediumint NOT NULL COMMENT '项目id',
  `build` char(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '版本号',
  `tester` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试人',
  `smokeResult` enum('pass','fail') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'pass' COMMENT '冒烟结果',
  `failedReason` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '失败原因',
  `relatedPerson` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '失败关系人',
  `begin` date NOT NULL COMMENT '测试开始日期',
  `end` date NOT NULL COMMENT '测试结束日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
