
'''
create some records for demo database
'''

from AlgYun.wsgi import *
from news.models import Column, Article


def main():
    columns_urls = [
      ('社交新闻', 'sports'),
      ('社会新闻', 'society'),
      ('科技新闻', 'tech'),
    ]

    for column_name, url in columns_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url)[0]
        # 创建 10 篇新闻
        for i in range(1, 11):
            article = Article.objects.get_or_create(
                title='{}_{}'.format(column_name, i),
                slug='article_{}'.format(i),
                content='新闻详细内容： {} {}'.format(column_name, i),
            )[0]
            article.column.add(c)


if __name__ == '__main__':
    main()
    print("Done!")
