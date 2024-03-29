from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("me/photos", views.MyPhotos.as_view()),
    path("me/texts", views.MyTexts.as_view()),
    path("me/likes", views.MyLikes.as_view()),
    path("me/bookmarks", views.MyBookmarks.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    path("sign-up", views.SignUp.as_view()),
    path("github", views.GithubLogIn.as_view()),
    path("kakao", views.KakaoLogIn.as_view()),
]
