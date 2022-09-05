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

 Date: 11/08/2022 11:02:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for assessment_scorerule
-- ----------------------------
DROP TABLE IF EXISTS `assessment_scorerule`;
CREATE TABLE `assessment_scorerule`  (
  `id` mediumint NOT NULL AUTO_INCREMENT,
  `indexType` enum('dev','test') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '考核指标类型(dev研发指标，test测试指标)',
  `indexName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '考核指标名称',
  `indexID` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '考核指标标识',
  `scoreInterval` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '扣分区间，如3,2,1,0',
  `rule` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '规则区间，如0-10,11-20,21-30,31-100(百分数值)',
  `deleted` enum('0','1') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of assessment_scorerule
-- ----------------------------
INSERT INTO `assessment_scorerule` VALUES (1, 'test', '严重缺陷', 'severityBug', '0|1|2|3', '30%-100%|20%-30%|10%-20%|0-10%', '0');
INSERT INTO `assessment_scorerule` VALUES (2, 'test', '无效缺陷', 'invalidBug', '0|1|2|4|10', '0-1%|1%-2%|2%-5%|5%-10%|10%-100%', '0');
INSERT INTO `assessment_scorerule` VALUES (3, 'dev', '严重缺陷', 'severityBug', '0|3|8|13|16', '0-5%|5%-10%|10%-15%|15%-25%|25%-100%', '0');
INSERT INTO `assessment_scorerule` VALUES (4, 'dev', '激活缺陷', 'activatedBug', '0|1|2|5', '0-2%|2%-5%|5%-10%|10%-100%', '0');
INSERT INTO `assessment_scorerule` VALUES (5, 'test', '遗漏缺陷', 'missingBug', '0|1|3|5', '0-1|1-2|2-5|5-100', '0');
INSERT INTO `assessment_scorerule` VALUES (6, 'dev', '冒烟测试', 'smokeTest', '0|1|3|5', '0-1|1-2|2-5|5-100', '0');
INSERT INTO `assessment_scorerule` VALUES (7, 'test', '遗漏缺陷', 'missingBug', '0|1|3|5', '0-0|1-2|3-5|6-100', '1');
INSERT INTO `assessment_scorerule` VALUES (8, 'dev', '遗漏缺陷', 'missingBug', '0|1|3|5', '0-1|1-2|2-5|5-100', '0');


SET FOREIGN_KEY_CHECKS = 1;
