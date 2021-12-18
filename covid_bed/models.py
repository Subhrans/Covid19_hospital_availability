from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# class User(AbstractUser):
#     contact = models.CharField(max_length=10,null=True,blank=True)

# class Meta(AbstractUser.Meta):
#     app_label="user"
#     db_table = "auth.user"
from django.template.defaultfilters import slugify


class State(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=120)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    contact = models.CharField(max_length=13, null=True, blank=True)
    alternative_contact = models.CharField(max_length=13, null=True, blank=True)
    total_ICU = models.PositiveIntegerField(default=0, null=True, blank=True)
    occupied_ICU = models.PositiveIntegerField(default=0, null=True, blank=True)
    vacant_ICU = models.PositiveIntegerField(default=0, null=True, blank=True)

    total_general = models.PositiveIntegerField(default=0, null=True, blank=True)
    occupied_general = models.PositiveIntegerField(default=0, null=True, blank=True)
    vacant_general = models.PositiveIntegerField(default=0, null=True, blank=True)

    total_oxygen_general = models.PositiveIntegerField(default=0, null=True, blank=True)
    occupied_oxygen_general = models.PositiveIntegerField(default=0, null=True, blank=True)
    vacant_oxygen_general = models.PositiveIntegerField(default=0, null=True, blank=True)
    total_ventilators = models.PositiveIntegerField(default=0, null=True, blank=True)

    total_HDU = models.PositiveIntegerField(default=0, null=True, blank=True,
                                            verbose_name="Total_HDU (High dependency unit) beds")
    occupied_HDU = models.PositiveIntegerField(default=0, null=True, blank=True,
                                               verbose_name="Occupied_HDU (High dependency unit) beds")
    vacant_HDU = models.PositiveIntegerField(default=0, null=True, blank=True,
                                             verbose_name="Vacant_HDU (High dependency unit) beds")

    total_isolation = models.PositiveIntegerField(default=0, null=True, blank=True)
    occupied_isolation = models.PositiveIntegerField(default=0, null=True, blank=True)
    vacant_isolation = models.PositiveIntegerField(default=0, null=True, blank=True)

    total_NMC_reserved = models.PositiveIntegerField(default=0, null=True, blank=True,
                                                     verbose_name="Total NMC (National Medical Commission) reserved"
                                                     )
    occupied_NMC_reserved = models.PositiveIntegerField(default=0, null=True,
                                                        blank=True,
                                                        verbose_name="Occupied NMC (National Medical Commission) reserved")
    vacant_NMC_reserved = models.PositiveIntegerField(default=0, null=True, blank=True,
                                                      verbose_name="Vacant NMC (National Medical Commission) reserved"
                                                      )

    location = models.URLField(null=True, blank=True,)
    lat = models.CharField(max_length=30, null=True, blank=True,)
    long = models.CharField(max_length=30, null=True, blank=True,)
    has_ICU_beds = models.BooleanField(default=False)
    has_ventilators = models.BooleanField(default=False)
    is_new_hospital = models.BooleanField(default=False)
    category = models.CharField(max_length=20, null=True, blank=True,)
    total_beds = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True,)
    type = models.CharField(max_length=20, null=True, blank=True,)
    update_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True,null=True,blank=True)

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Hospital, self).save(*args,**kwargs)

    def __str__(self):
        return self.name
