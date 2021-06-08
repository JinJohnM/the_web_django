from django.test import TestCase

from core.models import Profile, Subscriber

class TestProfile(TestCase):
  def test_profile_should_have_defined_fields(self):
      profile = Profile.objects.create(
        name="JinJohn",
      )

      assert profile.name == "JinJohn"


class TestIndexView(TestCase):
  def test_index_view_shoulds_see_Kan(self):
    # Given
    Profile.objects.create(name="Kan Ouivirach")

    # When
    response = self.client.get("/index-view/")
    
    # Then
    assert response.status_code == 200
    assert "Kan Ouivirach" in str(response.content)

  def test_index_view_should_save_subscriber_email_when_input_form(self):
    # Given
    Profile.objects.create(name="Kan Ouivirach")

    # When
    data = {
      "email": "kan@odds.team"
    }
    self.client.post("/index-view/", data=data)

    # Then
    subscriber = Subscriber.objects.last()
    assert subscriber.email == "kan@odds.team"