/*
 Navicat Premium Data Transfer

 Source Server         : school_pc
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : 120.24.240.87:3308
 Source Schema         : yunshanqingyu

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 02/03/2022 00:57:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tieba
-- ----------------------------
DROP TABLE IF EXISTS `tieba`;
CREATE TABLE `tieba`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `post_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '此回复的id',
  `main_post_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '此回复对应帖子的id',
  `tieba_id` tinyint(0) UNSIGNED NOT NULL COMMENT '贴吧的id',
  `user_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '回复用户id',
  `level` tinyint(0) UNSIGNED NULL DEFAULT NULL COMMENT '回复用户贴吧等级',
  `is_origin` bit(1) NOT NULL DEFAULT b'0' COMMENT '是否是主贴',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '内容',
  `resource` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '多媒体文件',
  `reply_count` int(0) UNSIGNED NOT NULL DEFAULT 0 COMMENT '回复数',
  `pub_time` datetime(0) NULL DEFAULT NULL COMMENT '发布时间',
  `cole_time` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '爬取时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `post_id`(`post_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
