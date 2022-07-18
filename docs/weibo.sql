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

 Date: 06/05/2022 13:43:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for weibo
-- ----------------------------
DROP TABLE IF EXISTS `weibo`;
CREATE TABLE `weibo`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `blog_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '博客id',
  `parent_blog_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '父博客id',
  `weibo_id` int(0) NULL DEFAULT NULL COMMENT '学校微博id',
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户id',
  `user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '微博名',
  `text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '内容',
  `like_count` bigint(0) NULL DEFAULT NULL COMMENT '点赞数',
  `reply_count` bigint(0) NULL DEFAULT NULL COMMENT '评论数目',
  `reposts_count` bigint(0) NULL DEFAULT NULL COMMENT '转发数量',
  `is_origin` bit(1) NULL DEFAULT NULL COMMENT '是否为主贴，如果是则为1，否则为0',
  `resource` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '多媒体文件',
  `pub_time` datetime(0) NULL DEFAULT NULL COMMENT '发布时间',
  `cole_time` datetime(0) NULL DEFAULT NULL COMMENT '爬取时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3397 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
