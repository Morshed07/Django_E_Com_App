# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user,get_user_model
# from django.db.models import Q


# User = get_user_model

# class UsernameOrEmail(ModelBackend):
#     def authenticate(self,request,user_name,password,**kwagrs):
#         try:
#             user = User.objects.get(Q(username__iexact=user_name)  | Q(email__iexact=user_name))

#         except User.DoesNotExist:
#             User().set_password(password)
#             return None
#         except User.MultipleObjectsReturned:
#             user = User.objects.filter(Q(username__iexact=user_name)  | Q(email__iexact=user_name))
#         else:
#             if user.check_password(password):
#                 return user
#         return None
