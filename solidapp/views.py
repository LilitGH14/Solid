from django import forms
from django.shortcuts import render


class NewTaskForm(forms.Form):
    subscribtion = forms.CharField(label="Subscribe")


class NewStoryForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter title...",
            }
        ),
    )
    content = forms.CharField(
        label="Story",
        max_length=400,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter story...",
            }
        ),
    )


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


def inspire(request):
    return render(
        request,
        "solidapp/inspire.html",
        {
            "main": {
                "title": "Share Your Story, Inspire the Art",
                "description": "Welcome to our Story Submission page! This is your chance to make an impact on the creative world, and who knows? Your story might just be the spark behind the next masterpiece.",
            },
            "howItWorks": {
                "title": "Why Share Your Story?",
                "description": "Every artist seeks inspiration in the world around them. They strive to connect with stories, emotions, and real-life experiences to create art that resonates. Your story could be the one that ignites a powerful idea, a heartfelt song, a captivating painting, or an unforgettable piece of writing. Here’s why your story matters:",
                "steps": [
                    {
                        "id": "01",
                        "title": "Inspire Creativity",
                        "feature": "Artists need authentic, heartfelt stories to fuel their creativity. By sharing your story, you’re opening a door for them to explore new themes and ideas.",
                    },
                    {
                        "id": "02",
                        "title": "Leave a Legacy",
                        "feature": "Your story could be immortalized in a piece of art, capturing your unique perspective and emotions for the world to see.",
                    },
                    {
                        "id": "03",
                        "title": "Connect with Others",
                        "feature": "By sharing your experience, you’re joining a community of storytellers and art lovers, united by a love for creativity and expression.",
                    },
                ],
            },
            "form": NewStoryForm(),
        },
    )


def gotInspired(request):
    return render(
        request,
        "solidapp/get-inspired.html",
        {
            "main": {
                "title": "Inspiring Stories from Our Community",
                "description": "Welcome to our Story Gallery! Here, you’ll find a collection of heartfelt stories shared by people just like you. Each story offers a unique perspective, capturing moments of joy, resilience, love, and growth. These stories have been shared to inspire artists and art lovers, and we hope they’ll inspire you too",
                "section_title": "Explore Real Stories",
                "section_description": "Our community members have generously shared their personal journeys, memories, and dreams. Take your time to explore each story, let their words resonate, and feel the emotions and experiences that drive human creativity. Whether you're here to find inspiration or simply to connect, these stories are a testament to the beauty of shared experiences.",
            },
            "stories": {
                "title": "Featured Stories",
                "data": [
                    {
                        "id": 1,
                        "title": "The Dawn Within",
                        "content": "A journey of self-discovery, resilience, and finding hope in unexpected places. This story reminds us that even the darkest nights are followed by dawn.",
                        "date": "Submitted by: Anonymous | Date: October 10, 2024",
                    },
                    {
                        "id": 2,
                        "title": "Beyond Familiar Shores",
                        "content": "Emily's reflection on a life-changing trip abroad shows us the beauty of new cultures, connections, and the power of stepping out of our comfort zones.",
                        "date": "Submitted by: Emily W. | Date: September 15, 2024",
                    },
                    {
                        "id": 3,
                        "title": "Echoes of the Heart",
                        "date": "Submitted by: James T. | Date: August 20, 2024",
                        "content": "This powerful story of love and loss is a reminder of the impact of the people we cherish and the strength we gain from their memory.",
                    },
                ],
            },
        },
    )


def story(request, id):
    return render(
        request,
        "solidapp/story.html",
        {
            "story": {
                "title": "The Dawn Within",
                "content": "Once, in a quiet village nestled between mist-covered mountains and sprawling green meadows, there lived a young woman named Liana. From a young age, she’d felt different—always a bit out of place, as though she belonged somewhere else. Her days were filled with the routines of the village, but her heart longed for something deeper, something that pulsed with life and meaning. As the years passed, her longing grew unbearable. She couldn't ignore the nagging feeling that she was missing something important. Then, one autumn evening, when the sky was painted with strokes of amber and purple, a wanderer came through the village. With his dusty boots and road-worn cloak, he had the air of someone who’d seen far more of the world than Liana could imagine. They talked briefly, but his words left an imprint on her soul. 'Sometimes,' he said, 'you have to leave everything behind to find yourself.'",
                "date": "Submitted by: Anonymous | Date: October 10, 2024",
            }
        },
    )
