import praw

class User:
    def __init__(self, user):
        self.redditor = user
        self.contacts = []
        self.finished_enrolling = False
        self.notified_contacts = False
    
    def __str__(self):
        return ("User: {0}\tContacts: {1}\tFinished Enrolling?: {2}".format(
            self.redditor, self.contacts, self.finished_enrolling))