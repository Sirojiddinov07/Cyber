from django.db import models

# Create your models here.

class Header(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')



class Twitch(models.Model):
    pass



class News(models.Model):
    pass





class Info(models.Model):
    img = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)
    text = models.TextField()




class Games(models.Model):
    name = models.CharField(max_length=200)




class Team(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/')
    special_game = models.ManyToManyField(Games)
    rating = models.IntegerField()


class Turnir(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    game = models.ForeignKey(Games, on_delete=models.PROTECT)
    comp_date = models.DateField()


class Galery(models.Model):
    img = models.ImageField(upload_to='media/')




