from django.contrib import admin
from upload_form.models import FileNameModel
from main.models import pokeinfo


class ContentsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'pokename',
                    'pokerate',
                    'waza1',
                    'waza2',
                    'waza3',
                    'waza4',
                    'waza6',
                    'waza7',
                    'waza8',
                    'waza9',
                    'waza10',
                    'waza11',
                    'waza12',
                    'wazarate1',
                    'wazarate2',
                    'wazarate3',
                    'wazarate4',
                    'wazarate5',
                    'wazarate6',
                    'wazarate7',
                    'wazarate8',
                    'wazarate9',
                    'wazarate10',
                    'wazarate11',
                    'wazarate12',
                    )


admin.site.register(pokeinfo, ContentsAdmin)

class FileNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'upload_time')
    list_display_links = ('id', 'file_name')

admin.site.register(FileNameModel, FileNameAdmin)
