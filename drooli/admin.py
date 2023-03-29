from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(model_or_iterable=models.students)
admin.site.register(model_or_iterable= models.student_documents)
admin.site.register(model_or_iterable= models.parents)
admin.site.register(model_or_iterable= models.parent_messages)
admin.site.register(model_or_iterable= models.payments)
admin.site.register(model_or_iterable= models.emergency_contacts)
admin.site.register(model_or_iterable= models.authorized_pickup_people)
admin.site.register(model_or_iterable= models.attendance_records)
admin.site.register(model_or_iterable= models.programs)
