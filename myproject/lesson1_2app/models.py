from django.db import models


class Coin(models.Model):
    side = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_last_n_flip(n):

        flips = Coin.objects.order_by('-timestamp')[:n]
        result = {'Орел':0, 'Решка':0}
        for flip in flips:
            if flip.side == 'Орел':
                result['Орел'] += 1
            else:
                result['Решка'] += 1
        return result


