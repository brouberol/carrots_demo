# encoding: utf-8

"""Definion of the polls models: Poll and Choices"""
from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

    def __repr__(self):
        return '<%s - %s>' % (self.__class__.__name__, str(self))


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __repr__(self):
        return '<%s - %s>' % (self.__class__.__name__, str(self))
