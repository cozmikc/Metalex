from .models import Chamber, Contact
from lexquirynotifications.models import LawyerNotification
from django.db.models.signals import post_save




def verifiedProfile(sender, instance, **kwargs):
    member = Chamber.objects.get(_id=instance._id)
    print(member, instance.is_verified)
    if member.is_verified == True or member.is_verified == False:
        LawyerNotification.objects.create(
            user = member,
            text = f"You've {'been verified' if member.is_verified else 'not been verified'} as a {'lawyer' if member.is_lawyer else 'lawfirm'}"
            
    )


post_save.connect(verifiedProfile, sender=Chamber)