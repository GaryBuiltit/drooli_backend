from django.db import models

# Create your models here.
class programs(models.Model):
    program_name = models.CharField(max_length=500)
    program_description = models.TextField()

    def __str__(self):
        return self.program_name


class parents(models.Model):
    parent_firstname = models.CharField(max_length=500)
    parent_lastname = models.CharField(max_length=500)
    parent_fullname = models.CharField(max_length= 500)
    email = models.EmailField(max_length=250)
    phone_cell = models.CharField(max_length=100)
    phone_work = models.CharField(max_length=100, null=True)
    street_address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length= 250)
    _zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.parent_fullname


class students(models.Model):
    student_firstname = models.CharField(max_length= 250)
    student_lastname = models.CharField(max_length= 250)
    student_fullname = models.CharField(max_length= 500)
    parents = models.ManyToManyRel(to=parents, field= 'id')
    tuition = models.CharField(max_length=100)
    birth_date = models.DateField()
    photo_url = models.URLField(max_length=250, null=True)
    age = models.IntegerField(null=True)
    program = models.ForeignKey(programs, on_delete= models.CASCADE)
    street_address = models.CharField(max_length= 500)
    city = models.CharField(max_length= 250)
    state = models.CharField(max_length= 250)
    _zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.student_fullname


# class kids_parents(models.Model):
#     parent = models.ManyToManyRel(parents)
#     student = models.ManyToManyRel(students)
    

class attendance_records(models.Model):
    student = models.ForeignKey(students, on_delete = models.CASCADE)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.student.student_fullname + self.date


class student_documents(models.Model):
    student = models.ForeignKey(students, on_delete = models.CASCADE)
    document_name = models.CharField(max_length=250)
    document_url = models.URLField()
    date_added = models.DateField().auto_now

    def __str__(self):
        return self.student.student_fullname + self.document_name
    

class payments(models.Model):
    student = models.ForeignKey(students, on_delete = models.CASCADE)
    payment_purpose = models.CharField(max_length=250)
    payment_amount = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.student.student_fullname


class emergency_contacts(models.Model):
    student = models.ForeignKey(students, on_delete = models.CASCADE)
    contact_fullname = models.CharField(max_length=250)
    relationship = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.student.student_fullname

 
class authorized_pickup_people(models.Model):
    student = models.ForeignKey(students, on_delete = models.CASCADE)
    fullname = models.CharField(max_length=250)
    relationship = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.student.student_fullname

 
class parent_messages(models.Model):
    sender = models.CharField(max_length= 250)
    recipient = models.CharField(max_length= 250)
    date_time = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.sender

