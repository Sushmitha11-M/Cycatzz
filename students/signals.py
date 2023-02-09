from .models import Student, Student_info
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db import transaction

# @receiver(post_save,sender=Student)
# def user_post_save_receiver(sender, instance, created, *args, **kwargs):
#     if instance.Stu_id:
# 		if not instance.groups.filter(id=instance.Stu_id.id).exists():
# 			group = Group.objects.get(name=instance.Stu_id.name)
# 			transaction.on_commit(lambda: instance.groups.set([group], clear=True))
# 			print("UPdated Group")
@receiver(pre_save, sender=Student)
def do_something(sender, instance, **kwargs):
    try:
        obj = Student.objects.get(Student_id=instance.Student_id)
    except sender.DoesNotExist:
        pass
    else:
        if not obj.user == instance.user: # Field has changed
            # do something
            print('change: user, old=%s new=%s' % (obj.user, instance.user))
