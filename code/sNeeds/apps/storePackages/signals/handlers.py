from django.db.models.signals import pre_save, post_delete, m2m_changed, post_save, pre_delete

from sNeeds.apps.storePackages.models import (
    StorePackage, StorePackagePhaseThrough, StorePackagePhase, SoldStorePackage,
    SoldStorePaidPackagePhase, SoldStoreUnpaidPackagePhase
)


def pre_save_store_package(sender, instance, *args, **kwargs):
    if instance.price is None:
        instance.price = 0


def pre_save_sold_store_package(sender, instance, *args, **kwargs):
    instance.update_price()


def pre_save_sold_store_paid_package_phase(sender, instance, *args, **kwargs):
    # Update sold_to
    instance.sold_to = instance.sold_store_package.sold_to

    # Update status
    instance.status = instance.get_status()


def pre_save_sold_store_unpaid_package_phase(sender, instance, *args, **kwargs):
    # Update active
    sold_store_paid_package_phases = SoldStorePaidPackagePhase.objects.filter(
        sold_store_package__id=instance.sold_store_package.id
    ).order_by('phase_number')

    if instance.phase_number == sold_store_paid_package_phases.first().phase_number + 1:
        instance.active = True

    # Update status
    instance.status = instance.get_status()


def post_save_store_package_phase(sender, instance, *args, **kwargs):
    store_package_qs = instance.store_packages.all()
    store_package_qs.update()


# Used in place of m2m_changed because due to Django's bug in m2m_changed in
# custom through this signal is not triggered
def post_save_store_package_phase_through(sender, instance, *args, **kwargs):
    instance.store_package.save()


# Used in place of m2m_changed because due to Django's bug in m2m_changed in
# custom through this signal is not triggered
def post_delete_store_package_phase_through(sender, instance, *args, **kwargs):
    instance.store_package.save()


def post_save_store_package(sender, instance, *args, **kwargs):
    from sNeeds.apps.carts.models import Cart
    carts_qs = Cart.objects.filter(products__in=[instance])
    carts_qs.update_price()


def post_save_sold_store_unpaid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()


def post_save_sold_store_paid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()


def post_delete_sold_store_paid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()


def post_delete_sold_store_unpaid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()


def handle_phases(sender, instance, *args, **kwargs):
    sold_store_unpaid_package_phases = SoldStoreUnpaidPackagePhase.objects.filter(
        sold_store_package__id=instance.id
    ).order_by('phase_number')
    sold_store_paid_package_phases = SoldStorePaidPackagePhase.objects.filter(
        sold_store_package__id=instance.id
    ).order_by('phase_number')

    sold_store_unpaid_package_phases.deactivate_all()

    current_phase = sold_store_paid_package_phases.first()


pre_save.connect(pre_save_store_package, sender=StorePackage)
pre_save.connect(pre_save_sold_store_package, sender=SoldStorePackage)
pre_save.connect(pre_save_sold_store_paid_package_phase, sender=SoldStorePaidPackagePhase)
pre_save.connect(pre_save_sold_store_unpaid_package_phase, sender=SoldStoreUnpaidPackagePhase)

post_save.connect(post_save_store_package_phase, sender=StorePackagePhase)
post_save.connect(post_save_store_package, sender=StorePackage)
post_save.connect(post_save_store_package_phase_through, sender=StorePackagePhaseThrough)
post_save.connect(post_save_sold_store_paid_package_phase, sender=SoldStorePaidPackagePhase)
post_save.connect(post_save_sold_store_unpaid_package_phase, sender=SoldStoreUnpaidPackagePhase)

post_delete.connect(post_delete_store_package_phase_through, sender=StorePackagePhaseThrough)
post_delete.connect(post_delete_sold_store_paid_package_phase, sender=SoldStorePaidPackagePhase)
post_delete.connect(post_delete_sold_store_unpaid_package_phase, sender=SoldStoreUnpaidPackagePhase)
