import pandas as pd
from django.core.management.base import BaseCommand
from movies_list.models import Movie


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        df = pd.read_excel('files/movies.xlsx')
        for _, row in df.iterrows():
            Movie.objects.create(
                title=row['Title'],
                genre=row['Genre'],
                release_year=row['Release Year'],
                description=row.get('Description', '')
            )
        self.stdout.write(self.style.SUCCESS('Movies imported successfully'))
