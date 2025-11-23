class CommentsException(Exception):
    pass


class InvalidApiTokenException(Exception):
    def __init__(self):
        self.message = ("There was an error on the APIFY Token"
                        "\nCheck your API token and try again")


class ActorCallException(Exception):
    def __init__(self, actor_name: str, original_error):
        self.message = f"There is an error during calling the actor {actor_name}\nDetails: {original_error}"

        self.actor = actor_name
        self.error = original_error

        super().__init__(self.message)


class DatasetException(Exception):
    def __init__(self, dataset_client, original_error):
        self.message = f"There was an error on the Dataset {dataset_client}\nDetails: {original_error}"

        super().__init__(self.message)
