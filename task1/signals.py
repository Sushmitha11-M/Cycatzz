# from django.dispatch import receiver
# from django.db.models.signals import post_save,pre_save
#
# @receiver(pre_save, sender=Question)
# def do_something(sender, instance, **kwargs):
#     try:
#         obj = Question.objects.get(pk=instance.pk)
#     except sender.DoesNotExist:
#         pass
#     else:
#         if not obj.user == instance.user: # Field has changed
#             # do something
#             print('change: user, old=%s new=%s' % (obj.user, instance.user))