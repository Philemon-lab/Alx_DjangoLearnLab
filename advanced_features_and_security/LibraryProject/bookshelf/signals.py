from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'bookshelf':
        # Create groups
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        Book = apps.get_model('bookshelf', 'Book')
        can_create = Permission.objects.get(codename='can_create', content_type__app_label='bookshelf')
        can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='bookshelf')
        can_view = Permission.objects.get(codename='can_view', content_type__app_label='bookshelf')
        can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='bookshelf')

        editors.permissions.set([can_create, can_edit])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_create, can_edit, can_view, can_delete])