from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    counter = models.IntegerField(null=True)

    def __str__(self):
        return "\"pk\": {} , \"name\": '{}', \"counter\": {} ".format(self.pk, self.name, self.counter)

    @staticmethod
    def parse_string_to_user(string):
        user = User()
        user.pk = int(string['pk'])
        user.name = string['name']
        user.counter = int(string['counter'])
        return user


