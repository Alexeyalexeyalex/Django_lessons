from django import forms


class RandomGames(forms.Form):
    games = [['Coin', 'Бросить монету'],['Cube', 'Бросить игральную кость'],['Number', 'Сгенерировать случайное число']]
    
    game = forms.ChoiceField(choices=games, label='Игра')
    count = forms.IntegerField(min_value=1, max_value=64, label='Количество попыток')