from django.core.urlresolvers import reverse
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
    # create_time 형식 변경하고 싶음.. strftime("%y/%m/%d")


class DiaryCreateView(generic.CreateView):
    model = Diary
    fields = ['title', 'subtitle', 'contents', ]

    def get_success_url(self):
        return reverse('diary:list')

    # def form_invalid(self, form):
    #     print('call form invalid')

    # validation 항목은 어떻게 정하나?
    def form_valid(self, form):
        return super(DiaryCreateView, self).form_valid(form)

    # post함수가 있으면 form_valid함수가 호출되지 않음.
    def postt(self, request):
        # 한번에 inset하고 싶다!
        data = request.POST
        Diary(title=data['title'],
              subtitle=data['subtitle'],
              contents=data['contents']).save()

        return HttpResponseRedirect(reverse('diary:list'))


class DiaryUpdateView(generic.UpdateView):
    # This field is required. 이거 모임?
    # update필드 데이터 어떻게 가져오지.?
    model = Diary
    fields = ['title', 'subtitle', 'contents', ]

    def get_success_url(self):
        return reverse('diary:list')


class DiaryDeleteView(generic.DeleteView):
    model = Diary

    def get_success_url(self):
        return reverse('diary:list')


class DiaryDetailView(generic.DetailView):
    model = Diary
