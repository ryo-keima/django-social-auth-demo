# Djangoでソーシャルログインを実装

Djangoでソーシャルログインをするでもアプリを紹介

## 実行手順

1. Python の仮想環境を構築

   ```
   % python -m venv venv
   ```

2. 仮想環境をアクティベート

   ```
    % source venv/bin/activate
   ```

3. 必要なライブラリのインストール

   ```
   (venv)% pip install -r requirements.txt
   ```

4. .env.example ファイルを.env にリネーム
5. SECRET_KEY を生成し、.env ファイルの SECRET_KEY に設定

   SECRET_KEY の作成方法

   ```
   (venv)% python manage.py shell
   >>> from django.core.management.utils import get_random_secret_key
   >>> get_random_secret_key()
   'xxx-xxxx' # この文字列を設定
   ```

6. マイグレート

   ```
   (venv)% python manage.py migrate
   ```

7. 開発用サーバーを起動

   ```
   (venv)% python manage.py runserver
   ```

8. ブラウザで[http://127.0.0.1:8000](http://127.0.0.1.8000)にアクセス