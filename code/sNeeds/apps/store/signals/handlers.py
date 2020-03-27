from django.db.models.signals import post_save, pre_delete, pre_save, m2m_changed

from sNeeds.apps.carts.models import Cart
from sNeeds.apps.consultants.models import ConsultantProfile
from sNeeds.apps.store.models import TimeSlotSale, SoldTimeSlotSale, Product
from sNeeds.apps.store.tasks import notify_sold_time_slot
from sNeeds.apps.chats.models import Chat
from sNeeds.settings.config.variables import FRONTEND_URL
from sNeeds.utils.custom.time_functions import utc_to_jalali_string


def pre_delete_product_receiver(sender, instance, *args, **kwargs):
    """
    When TimeSlotSale obj deletes, no signal will not trigger.
    This signal fix this problem.
    """
    Cart.objects.filter(products=instance).remove_product(instance)


def pre_save_time_slot_receiver(sender, instance, *args, **kwargs):
    consultant = instance.consultant
    if instance.price is None:
        instance.price = consultant.time_slot_price


def post_save_time_slot_sold_receiver(sender, instance, created, *args, **kwargs):
    # This is sent for consultants
    if created:
        sold_time_slot_url = FRONTEND_URL + "user/sessions/"
        start_time = utc_to_jalali_string(instance.start_time)
        end_time = utc_to_jalali_string(instance.end_time)

        notify_sold_time_slot.delay(
            send_to=instance.consultant.user.email,
            name=instance.consultant.user.get_full_name(),
            sold_time_slot_url=sold_time_slot_url,
            start_time=start_time,
            end_time=end_time
        )


def post_save_product_receiver(sender, instance, *args, **kwargs):
    cart_qs = Cart.objects.filter(products__in=[instance])

    # Used when time slot sold price is changed and its signal is triggered to update this model
    for obj in cart_qs:
        obj.update_price()


def create_chat(sender, instance, *args, **kwargs):
    user = instance.sold_to
    consultant = instance.consultant
    if not Chat.objects.filter(user=user, consultant=consultant).exists():
        Chat.objects.create(user=user, consultant=consultant)


pre_save.connect(pre_save_time_slot_receiver, sender=TimeSlotSale)

post_save.connect(post_save_product_receiver, sender=Product)
post_save.connect(post_save_time_slot_sold_receiver, sender=SoldTimeSlotSale)
post_save.connect(create_chat, sender=SoldTimeSlotSale)

pre_delete.connect(pre_delete_product_receiver, sender=Product)
