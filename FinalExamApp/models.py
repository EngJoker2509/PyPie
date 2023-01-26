from django.db import models
from LoginAndRegAPP.models import *


class pypie(models.Model):
    name = models.CharField(null=False, max_length=45)
    filling = models.CharField(null=False, max_length=45)
    crust = models.CharField(null=False, max_length=45)
    user = models.ForeignKey(User, related_name='pypie_user', on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    vote = models.ManyToManyField(User, related_name='votes')

    def vote_thispypie_to_this_user(pypie_id, user_id):
        pypie_obj = pypie.objects.get(id=pypie_id)
        user_obj = User.objects.get(id=user_id)
        user_obj.votes.add(pypie_obj)

    def display_all_pies():
        return pypie.objects.all()

    def add_pypie(name, filling, crust, user_id):
        user_obj = User.objects.get(id=user_id)
        pypie.objects.create(name=name, filling=filling,
                             crust=crust, user=user_obj)

    def display_pypie_by_user_id(id):
        return pypie.objects.filter(user=id)

    def _update(id, name, filling, crust, user):
        _pypie = pypie.objects.get(id=id)
        user = User.objects.get(id=user)
        _pypie.name = name
        _pypie.filling = filling
        _pypie.crust = crust
        _pypie.user = user
        _pypie.save()

    def _delete(id):
        _pypie=pypie.objects.get(id=id)
        _pypie.delete()
