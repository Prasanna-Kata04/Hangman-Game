import random
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Predefined word list
WORD_LIST = ['apple', 'banana', 'orange', 'grape', 'mango']

# Helper function to pick a random word
def get_random_word():
    return random.choice(WORD_LIST)

from django.shortcuts import render, get_object_or_404
from .models import Game

def play_game_with_id(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game/play.html', {'game': game})

# Play game view
def play_game(request):
    word = request.session.get('word', '')
    guessed_letters = request.session.get('guessed_letters', [])
    attempts = request.session.get('attempts', 6)

    if not word:
        return redirect('home')

    # Check if the player has won or lost
    if attempts <= 0:
        context = {'word': word, 'message': 'You lost!'}
        return render(request, 'game/result.html', context)

    if all(letter in guessed_letters for letter in word):
        context = {'word': word, 'message': 'You won!'}
        return render(request, 'game/result.html', context)

    # Game state
    context = {
        'word': ''.join([letter if letter in guessed_letters else '_' for letter in word]),
        'guessed_letters': guessed_letters,
        'attempts': attempts,
    }
    return render(request, 'game/play.html', context)

# Handle guessing a letter
def guess_letter(request):
    if request.method == 'POST':
        guessed_letter = request.POST.get('letter', '').lower()
        word = request.session.get('word', '')
        guessed_letters = request.session.get('guessed_letters', [])
        attempts = request.session.get('attempts', 6)

        if guessed_letter and guessed_letter not in guessed_letters:
            guessed_letters.append(guessed_letter)
            if guessed_letter not in word:
                attempts -= 1

        request.session['guessed_letters'] = guessed_letters
        request.session['attempts'] = attempts

    return redirect('play_game')

from django.shortcuts import render

def home(request):
    return render(request, 'game/new_game.html')  # Make sure the path is correct

from django.shortcuts import render

# Remove @login_required
def new_game(request):
    # Logic to create a new game
    return render(request, 'game/new_game.html')

