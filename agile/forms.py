from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)


class ForgetFrom(forms.Form):
    username = forms.CharField(max_length=20, required=True)


class ResetForm(forms.Form):
    newpwd = forms.CharField(max_length=20, required=True, error_messages={'required':'密碼不能為空'})
    renewpwd = forms.CharField(max_length=20, required=True, error_messages={'required':'密碼不能為空'})