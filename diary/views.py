from diary.forms import DiaryForm
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic
from diary.models import Diary


# 배포하고 싶어요

def index(request):
    return render(request, 'common/index.html', {'message': 'Hi~!'})


class DiaryListView(generic.ListView):
    model = Diary
    ordering = '-create_date'


class DiaryCreateView(generic.CreateView):
    model = Diary
    form_class = DiaryForm

    def get_success_url(self):
        return reverse_lazy('diary:list')

    # # def form_invalid(self, form):
    # #     print('call form invalid')
    # #
    # # # validation 항목은 어떻게 정하나?
    # def form_valid(self, form):
    #     return super(DiaryCreateView, self).form_valid(form)
    #
    # # post함수가 있으면 form_valid함수가 호출되지 않음.
    # def postt(self, request):
    #     # 한번에 inset하고 싶다!
    #     data = request.POST
    #     Diary(title=data['title'],
    #           subtitle=data['subtitle'],
    #           contents=data['contents']).save()
    #
    #     return HttpResponseRedirect(reverse_lazy('diary:list'))


class DiaryUpdateView(generic.UpdateView):
    # This field is required. 이거 왜 있음?
    # update필드 기존 저장된 값은 어떻게 가져오지?
    model = Diary
    form_class = DiaryForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('diary:list')


class DiaryDeleteView(generic.DeleteView):
    model = Diary

    def get_success_url(self):
        return reverse_lazy('diary:list')


class DiaryDetailView(generic.DetailView):
    # delete view가 불리지 않음
    model = Diary


    def get_queryset(self):
        print(self.__dict__)
        print(self.args)
        #self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Diary.objects.all()


