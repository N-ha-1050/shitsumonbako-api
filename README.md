# メモ
メール送信などメールアドレス関係は作成中

## リポジトリをクローン
```
git clone https://github.com/N-ha-1050/shitsumonbako-api.git
cd shitsumonbako-api
```
以下すべて `shitsumonbako-api` ディレクトリ内

## 仮想環境の設定
```
python -m venv .venv
.venv\Scripts\activate.bat
```

## パッケージのインストール
```
python -m pip install django
python -m pip install djangorestframework
python -m pip install djangorestframework-simplejwt
python -m pip install dj-rest-auth[with_social]
python -m pip install django-environ
```

または、バージョン指定済み一括
```
python -m pip install -r requirements.txt
```

## 環境設定
.envファイルの作成
```
copy nul .env
```
```.env
DEBUG=True
SECRET_KEY=(ランダムな50文字以上の文字列)
CALLBACK_URL_GITHUB=http://127.0.0.1:8000/accounts/github/login/callback/
CALLBACK_URL_GOOGLE=http://127.0.0.1:8000/accounts/google/login/callback/
CALLBACK_URL_DISCORD=http://127.0.0.1:8000/accounts/discord/login/callback/
```

SECRET_KEYは以下の取得用関数を使用可能
```
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
(SECRET_KEY)
>>>exit()
```

## データベースの作成
```
python manage.py migrate
```

## 起動
```
python manage.py runserver
```
[local host(default)](http://127.0.0.1:8000/) にアクセス

## 管理者アカウント作成
```
python manage.py createsuperuser
```
```
ユーザー名 (leave blank to use 'admin'): 
メールアドレス: 
Password:
Password (again):
```
をそれぞれ入力
```
Superuser created successfully.
```
で完了

[/admin/](http://127.0.0.1:8000/admin/) にログイン

## 初期設定
[/admin/](http://127.0.0.1:8000/admin/) にて
1. サイト > サイト [/admin/sites/site/](http://127.0.0.1:8000/admin/sites/site/)

	表示されているサイトの設定ページ [/admin/sites/site/1/change/](http://127.0.0.1:8000/admin/sites/site/1/change/)

	ドメイン名、表示名をデフォルトを参考に書き換えて保存

	間違えても削除や新規作成はせず、更新する(サイトIDを変更しないため)
	```
	ドメイン名: 127.0.0.1:8000
	表示名: 127.0.0.1:8000
	```
2. 外部アカウント > Social applications [/admin/socialaccount/socialapp/](http://127.0.0.1:8000/admin/socialaccount/socialapp/)

	右上の `SOCIAL APPLICATIONを追加` から新規作成

	プロバイダー、名前、Client id、Secret keyなどを入力、選択(GitHub、Google、Discordはこの4つ)

	一番下のSitesで 1. で作成したサイトを `選択された sites` に移動
	```
	プロバイダー: Google
	名前: Google
	Client id: 
	Secret id: 
	...
	Sites: 127.0.0.1:8000
	```
	3つすべてのプロバイダーで入力

## 主な機能
### Api: [/](http://127.0.0.1:8000/)
右上からログインなども可能(認証情報を付加できる)
それぞれのメソッドも実行可

[dj-rest-auth ドキュメント エンドポイント](https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html)
これの大体が使えます

[django-allauth ドキュメント サポート済み](https://django-allauth.readthedocs.io/en/latest/overview.html#supported-providers)
追加することも可能

### Admin: [/admin/](http://127.0.0.1:8000/admin/)
管理者用

### Account: [/accounts/home/](http://127.0.0.1:8000/accounts/home/)
最低限の動作確認用

[django-allauth ドキュメント ビュー](https://django-allauth.readthedocs.io/en/latest/views.html)
基本的に同じ
