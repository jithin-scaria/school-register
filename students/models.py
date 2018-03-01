from django.db import models

# Create your models here.


def student_file_rename(instance, filename):
    return 'students/{}_{}_{}'.format("student", instance.student_id, filename)

class student(models.Model):
    student_id = models.AutoField(primary_key=True, db_column='id')
    student_first_name = models.CharField(
        max_length=50, db_column='first_name')
    student_middle_name = models.CharField(
        max_length=50, db_column='middle_name', default=None, blank=True, null=True)
    student_last_name = models.CharField(max_length=50, db_column='last_name')
    student_image = models.FileField(
        upload_to=student_file_rename, default=None, blank=True, null=True, db_column='student_image')
    date_of_birth = models.DateField(
        db_column='date_of_birth', default=None, blank=True, null=True)
    date_of_join = models.DateField(
        db_column='date_of_join', default=None, blank=True, null=True)
    std_join = models.IntegerField(db_column='std_join')
    std_curr = models.IntegerField(db_column='std_curr')
    std_curr_div = models.CharField(max_length=50, db_column='std_curr_div')

    def __str__(self):
        return 'Name: {} {}, Std: {} {}'.format(self.student_first_name, self.student_last_name, self.std_curr, self.std_curr_div)
