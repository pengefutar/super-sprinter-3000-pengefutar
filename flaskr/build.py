from flaskr.create_entries import ExampleDataCreator


class Builder:
    def __init__(self):
        self.data_creator = ExampleDataCreator()

    def create_dummy_data(self):
        self.data_creator.create_user_stories_by_csv(self.data_creator.csv_reader("product_backlog.csv"))
