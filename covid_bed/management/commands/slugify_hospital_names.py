from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from covid_bed.models import Hospital


class Command(BaseCommand):
    help = "to update all hospital slugs with hospital names"

    def handle(self, *args, **options):
        hospitals = Hospital.objects.all().select_related('state')
        for i in hospitals:
            print(i.name + "---------" + i.state.name)
            i.slug = slugify(i.name)
            i.save()
        print("Done")
