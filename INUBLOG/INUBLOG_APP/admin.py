from django.contrib import admin
import INUBLOG_APP.models

appModels = INUBLOG_APP.models

admin.site.register(appModels.BlogContents)
