from verifiables.models import Verifiable
from chamber.models import Chamber
from django.db.models.signals import post_save
from lexquirynotifications.models import LawyerNotification
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

def verifiedProfile(sender, instance, **kwargs):
    member = Chamber.objects.get(_id=instance._id)
    print(member, instance.verified)
    member.is_verified = instance.verified
    member.save()

    LawyerNotification.objects.create(
        user = member,
        text = f"You've {'been verified' if member.is_verified else 'not been verified'} as a {'lawyer' if member.is_lawyer else 'lawfirm'}",
        notificationImage = member.profile_image
    )


post_save.connect(verifiedProfile, sender=Verifiable)



