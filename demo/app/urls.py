from django.urls import path

from . import views


urlpatterns = [
    path(
        "matching-results",
        views.ViewWithMatchingResults.as_view(),
        name="matching-results",
    ),
    path(
        "nonmatching-results",
        views.ViewWithNonMatchingResults.as_view(),
        name="nonmatching-results",
    ),
    path(
        "exceptional-results",
        views.ViewWithExceptionalResults.as_view(),
        name="exceptional-results",
    ),
]
