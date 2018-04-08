# -*- coding: utf-8 -*-
from DjangoUeditor.models import UEditorField
from django.db import models
from django.urls import reverse



class Column(models.Model):
    name = models.CharField('分类名称', max_length=256)
    slug = models.CharField('分类网址', max_length=256, unique=True)
    intro = models.TextField('分类简介', default='')

    def get_absolute_url(self):
        return reverse('column', args=(self.slug, ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['name']  # 排序


class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属分类')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, unique=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者', on_delete=models.CASCADE,)
    # 仅修改 content 字段 加入富文本编辑器
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def get_absolute_url(self):
        # args参数是元组，末尾一定要有,号
        return reverse('article', args=(self.pk, self.slug))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'
