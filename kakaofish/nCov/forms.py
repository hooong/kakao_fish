from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(error_messages = {'required':"제목을 입력해주세요"}, label = "제목", max_length=128)
    contents = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)
    # thumbImg =
    ### 태그 추가 부분 ###
    tag = forms.CharField(required = False, label = "태그")