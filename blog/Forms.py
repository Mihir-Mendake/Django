from django import forms
from.models import Comment

class CommentForm(forms.ModelForm):
      class Meta:
          model = Comment
          # fields = ["user_name" ,"user_email" ,"comment_text"]
          exclude = ["post"]
          labels = {"user_name" : "Name", "user_email" : "Email" , "comment_text" : "Comment"}