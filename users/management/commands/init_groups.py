from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from products.models import Order


class Command(BaseCommand):
    help = 'Creates the groups and permissions.'

    def handle(self, *args, **options):
        order_creators_group, _ = Group.objects.get_or_create(name="order_creators")
        order_deliverers_group, _ = Group.objects.get_or_create(name="order_deliverers")

        ct = ContentType.objects.get_for_model(Order)

        permission_create = Permission.objects.create(codename="can_create_order",
                                                      name="Can create order",
                                                      content_type=ct)

        permission_deliver = Permission.objects.create(codename="can_deliver_order",
                                                       name="Can deliver order",
                                                       content_type=ct)

        order_creators_group.permissions.add(permission_create)
        order_deliverers_group.permissions.add(permission_deliver)

        order_deliverers_group.save()
        order_creators_group.save()
