from models import *
import csv
import os


class ExampleDataCreator:
    @staticmethod
    def csv_reader(filename):
        current_file_path = os.path.dirname(os.path.abspath(__file__))
        filename = current_file_path + "/csv/" + str(filename)
        table = []

        with open(filename, "r", encoding='utf-8') as f:
            csvfile = csv.reader(f, delimiter=';')
            next(csvfile)
            for line in csvfile:
                table.append(line)
            return table

    @staticmethod
    def create_user_stories_by_csv(user_story_table):
        for story in user_story_table:
            Entry.create(story_title = story[1], user_story = story[2], acceptance_criteria = story[3], business_value = story[4], estimation = story[5], status = story[6])
