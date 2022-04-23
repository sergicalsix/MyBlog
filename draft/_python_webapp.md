# fastapi
## 概要
docsを自動で作成可能で早い。
`uvicorn`によってアプリを起動する



# django
## 概要
自動でadminサイトを作成できる。
セキュア
### Serializer
### 用いる変数
fields = '__all__'で全てのカラム、excludeで用いないカラム

## View
django_filter(pp.194)

### 複数モデルを使用する場合(DRF)
https://jpcodeqa.com/q/c1321bd3cc5ddf274e68270ac492be78
```
class TimelineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that lists all tweet/article objects in rev-chrono.
    """
    queryset = itertools.chain(Tweet.objects.all(), Article.objects.all())
    serializer_class = TimelineSerializer
```
```
class TimeLineList(generics.ListAPIView):
    serializer_class = TimeLineSerializer

    def get_queryset(self):
        return list(itertools.chain(Tweet.objects.all(), Article.objects.all()))
```
## API仕様書
自動生成

## セキュリティ
### SECRET_KEY
setting.pyで設定する。設定しなければエラーになる。githubにあげてはいけないので、ローカルのファイルを読むか環境変数にする。ファイルはアプリ内ではなく、manage.pyと同じ場所に配置する。

### CSRFの検証
settings.pyに記載されている'django.middleware.csrf.CsrfViewMiddleware'によってCSRF検証機能が存在する。
POSTメソッドのフォームには、csrf_tokenタグを入れればOKです。

`<form method="post">{% csrf_token %}`

注意点として、外部のURLに対してPOSTするフォームにはこの{% csrf_token %}タグを使ってはいけません。CSRFトークンが外部にもれることになり、セキュリティ上よくないからです。(https://djangobrothers.com/blogs/django_csrf/)

## shell
django-extensionsを事前にinstallし、setting.pyのINSTALLED APPSに'django_extensions'を追記する。
```
% python manage.py shell_plus
%
```

### 参考サイト
- https://djangobrothers.com/blogs/
