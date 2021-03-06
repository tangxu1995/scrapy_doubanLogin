# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class WeiboItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UserItem(Item):
    id = Field()
    name = Field()
    avatar = Field()
    cover = Field()
    gender = Field()
    description = Field()
    fans_count = Field()
    follows_count = Field()
    weibos_count = Field()
    verified = Field()
    verified_reason = Field()
    verified_type = Field()
    follows = Field()
    fans = Field()
    crawled_at = Field()


class UserRelationItem(Item):
    id = Field()
    follows = Field()
    fans = Field()


class WeiboItem(Item):
    id = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    picture = Field()
    pictures = Field()
    source = Field()
    text = Field()
    raw_text = Field()
    thumbnail = Field()
    user = Field()
    created_at = Field()
    crawled_at = Field()


class WeiboCommentItem(Item):
    weibo_id = Field()
    created_at = Field()
    comment_id = Field()
    reply_id = Field()
    text = Field()
    user_id = Field()
    user_name = Field()
    reply_original_text = Field()
    like_count = Field()


class CommentReplyItem(Item):
    weibo_id = Field()
    comment_id = Field()
    reply_id = Field()
    created_at = Field()
    like_count = Field()
    reply_original_text = Field()
    text = Field()
    user_id = Field()
    user_name = Field()
