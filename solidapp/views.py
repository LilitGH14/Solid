from django import forms
from django.shortcuts import render


class NewTaskForm(forms.Form):
    subscribtion = forms.CharField(label="")


def index(request):
    return render(
        request,
        "solidapp/index.html",
        {
            "main": {
                "title": "Bridging the worlds of fans and creators, one story at a time.",
                "description": "Explore a digital library of creations inspired by real lives, and dive deeper into the art that speaks to you.",
            },
            "features": [
                {
                    "id": "01",
                    "title": "Inspire Your Favorite Artists",
                    "feature": "Let your story be a muse. Share your experiences, emotions, and dreams to inspire the creators you love. Every story has the potential to become part of something bigger.",
                },
                {
                    "id": "02",
                    "title": "Explore Online Galleries",
                    "feature": "Browse through virtual galleries showcasing art inspired by real stories. From illustrations to digital artwork, find the visuals that resonate with you and uncover the emotions behind them.",
                },
                {
                    "id": "03",
                    "title": "Audiobook Library",
                    "feature": "Immerse yourself in a growing library of audiobooks, each one crafted from stories that span the human experience. Enjoy these heartfelt narratives anytime, anywhere.",
                },
                {
                    "id": "04",
                    "title": "Translated Song Lyrics",
                    "feature": "Connect more deeply with your favorite music by exploring translated lyrics that capture the essence of songs inspired by fans. Language won’t be a barrier to feeling the music.",
                },
                {
                    "id": "05",
                    "title": "Exclusive Creator Updates",
                    "feature": "Stay updated with exclusive news from the artists you inspire. Get the latest on new projects, behind-the-scenes insights, and messages of appreciation straight from the creators.",
                },
                {
                    "id": "06",
                    "title": "Community for Art & Literature Lovers",
                    "feature": "Join a community that appreciates the fusion of personal stories with artistic expression. Share your thoughts, connect with other fans, and find friends who appreciate the power of words, art, and music.",
                },
            ],
            "about": {
                "title": "Where Stories Inspire Art",
                "description": "Welcome to Solid a place where art is inspired by you. Share your personal stories with your favorite artists—singers, writers, painters—and watch them turn your emotions into songs, visual art, and more. ",
            },
            "form": NewTaskForm(),
        },
    )
