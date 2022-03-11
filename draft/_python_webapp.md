## fastapi
### 概要
docsを自動で作成可能で早い。
`uvicorn`によってアプリを起動する


## django
### 概要
自動でadminサイトを作成できる。
セキュア

### CSRFの検証
settings.pyに記載されている'django.middleware.csrf.CsrfViewMiddleware'によってCSRF検証機能が存在する。
POSTメソッドのフォームには、csrf_tokenタグを入れればOKです。

`<form method="post">{% csrf_token %}`

注意点として、外部のURLに対してPOSTするフォームにはこの{% csrf_token %}タグを使ってはいけません。CSRFトークンが外部にもれることになり、セキュリティ上よくないからです。(https://djangobrothers.com/blogs/django_csrf/)


### 参考サイト
- https://djangobrothers.com/blogs/
