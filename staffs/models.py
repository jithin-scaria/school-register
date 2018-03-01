from django.db import models

# Create your models here.

def staff_file_rename(instance, filename):
    return 'staffs/{}_{}_{}'.format("staff", instance.staff_id, filename)

class staff(models.Model):
    staff_id = models.AutoField(primary_key=True, db_column='id', unique=True)
    staff_first_name = models.CharField(max_length=50, db_column='first_name')
    staff_middle_name = models.CharField(
        max_length=50, db_column='middle_name', default=None, blank=True, null=True)
    staff_last_name = models.CharField(max_length=50, db_column='last_name')
    staff_image = models.FileField(
        upload_to=staff_file_rename, default=None, blank=True, null=True, db_column='staff_image')
    date_of_birth = models.DateField(
        db_column='date_of_birth', default=None, blank=True, null=True)
    date_of_join = models.DateField(
        db_column='date_of_join', default=None, blank=True, null=True)
    department_id = models.ForeignKey(
        'department', db_column='department_id', on_delete=models.CASCADE)
    designation_id = models.ForeignKey(
        'designation', db_column='designation_id', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.staff_first_name + " " + self.staff_last_name)


class department(models.Model):
    dep_id = models.AutoField(primary_key=True, db_column='id', unique=True)
    dep_name = models.CharField(max_length=50, db_column='dep_name')

    def __str__(self):
        return str(self.dep_name)


class designation(models.Model):
    des_id = models.AutoField(primary_key=True, db_column='id', unique=True)
    designation = models.CharField(max_length=50, db_column='designation')
    department_id = models.ForeignKey(
        'department', db_column='department_id', on_delete=models.CASCADE)
    specialization = models.CharField(
        max_length=50, db_column='specialization')

    def __str__(self):
        return str(self.designation + ", spec: " + self.specialization)

