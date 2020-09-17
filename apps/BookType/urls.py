from apps.BookType.views import FrontAddView, FrontListView, ListAllView, FrontEditView, FrontDeleteView
from django.conf.urls import url

# 正在部署的应用的名称
app_name = 'BookType'

urlpatterns = [
    url(r'^frontAdd$', FrontAddView.as_view(), name='frontAdd'),  # 前台添加
    url(r'^frontList', FrontListView.as_view(), name='frontList'),  # 前台查询列表
    url(r'^listAll', ListAllView.as_view(), name='listAll'),  # 前台查询所有图书类型
    url(r'^frontEdit', FrontEditView.as_view(), name='frontEdit'),  # 前台修改
    url(r'^frontDelete', FrontDeleteView.as_view(), name='frontDelete'),  # 前台删除
]
