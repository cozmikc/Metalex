from django.contrib import admin
from .models import *


# Register your models here.

class PaymentPlanAdmin(admin.ModelAdmin):
    readonly_fields = ("paidAt",)



admin.site.register(Chamber)
admin.site.register(PracticeArea)
admin.site.register(Qualification)
admin.site.register(Contact)
admin.site.register(MemberReview)
admin.site.register(PaymentPlan, PaymentPlanAdmin)


