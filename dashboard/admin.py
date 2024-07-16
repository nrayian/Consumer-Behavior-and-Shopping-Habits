from django.contrib import admin
from .models import ConsumerBehavior

class ConsumerBehaviorAdmin(admin.ModelAdmin):
    list_display = (
        'gender', 'age', 'ethnic', 'occupation', 'income', 
        'use_social_media', 'experience_purchasing', 'reviews_affect', 
        'internet_hours', 'attention_ads', 'PB1', 'PB2', 'PB3', 
        'PB4', 'ATTD1', 'ATTD2', 'ATTD3', 'ATTD4', 'SN1', 'SN2', 'SN3', 'SN4', 
        'PBC1', 'PBC2', 'PBC3', 'PBC4'
    )
    list_display_links = ('gender', 'age', 'ethnic')

admin.site.register(ConsumerBehavior, ConsumerBehaviorAdmin)