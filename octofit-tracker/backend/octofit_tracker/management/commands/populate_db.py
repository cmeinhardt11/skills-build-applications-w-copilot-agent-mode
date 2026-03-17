from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user='ironman@marvel.com', type='run', duration=30),
            Activity(user='batman@dc.com', type='cycle', duration=45),
            Activity(user='superman@dc.com', type='swim', duration=60),
            Activity(user='captain@marvel.com', type='walk', duration=20),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups'),
            Workout(name='Situps', description='Do 30 situps'),
            Workout(name='Squats', description='Do 40 squats'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
