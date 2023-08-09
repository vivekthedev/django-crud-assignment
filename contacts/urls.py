from django.urls import path
from .views import ContactCreate, HomeView, ContactDelete, ContactUpdate
urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("update/<int:pk>/", ContactUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", ContactDelete.as_view(), name="delete"),
    path("create", ContactCreate.as_view(), name="create"),
]
 