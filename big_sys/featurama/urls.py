from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'featurama'
urlpatterns = [
    path('',
         RedirectView.as_view(url='featurama/pipelines', permanent=False)),
    path('featurama/pipelines',
         views.pipelines, name='pipelines'),
    path('featurama/pipelines/<int:pipeline_id>/upload_file',
         views.upload_file, name='upload_file'),
    path('featurama/pipelines/<int:pipeline_id>/select_target_variable',
         views.select_target_variable, name='select_target_variable'),
    path('featurama/pipelines/<int:pipeline_id>/pre_select_features',
         views.pre_select_features, name='pre_select_features'),
    path('featurama/pipelines/<int:pipeline_id>/configure',
         views.configure_pipeline, name='configure_pipeline'),
    path('featurama/pipelines/<int:pipeline_id>/manual_feature_selection',
         views.manual_feature_selection, name='manual_feature_selection'),
    path('featurama/pipelines/<int:pipeline_id>/results',
         views.results_summary, name='results_summary'),
    path('featurama/pipelines/<int:pipeline_id>/delete',
         views.delete_pipeline, name='delete_pipeline'),
    path('featurama/pipelines/<int:pipeline_id>/export_report',
         views.export_report, name='export_report'),
]
