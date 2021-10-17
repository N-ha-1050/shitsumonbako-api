"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.socialaccount import adapter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# ソーシャルアカウント用
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.discord.views import DiscordOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# ビュー
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView, SocialAccountListView, SocialAccountDisconnectView
from django.views.generic import TemplateView


# ログインビュー
class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.CALLBACK_URL_GITHUB
    client_class = OAuth2Client

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALLBACK_URL_GOOGLE
    client_class = OAuth2Client

class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter
    callback_url = settings.CALLBACK_URL_DISCORD
    client_class = OAuth2Client


# 接続ビュー
class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.CALLBACK_URL_GITHUB
    client_class = OAuth2Client

class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALLBACK_URL_GOOGLE
    client_class = OAuth2Client

class DiscordConnect(SocialConnectView):
    adapter_class = DiscordOAuth2Adapter
    callback_url = settings.CALLBACK_URL_DISCORD

#  ↑2つのビューはviewに移行を検討


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shitsumonbako.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # ソーシャルログイン用URL
    path('dj-rest-auth/github/', GithubLogin.as_view(), name='github_login'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('dj-rest-auth/discord/', DiscordLogin.as_view(), name='discord_login'),

    # ソーシャルアカウント接続用URL
    path('dj-rest-auth/github/connect/', GithubConnect.as_view(), name='github_connect'),
    path('dj-rest-auth/google/connect/', GoogleConnect.as_view(), name='google_connect'),
    path('dj-rest-auth/discord/connect/', DiscordConnect.as_view(), name='discord_connect'),

    path('socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'),
    path('socialaccounts/<int:pk>/disconnect/', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),

    # フロントエンド
    path('accounts/', include('allauth.urls')),
    path('accounts/home/', TemplateView.as_view(template_name='home.html'), name='accounts_home'),
]
