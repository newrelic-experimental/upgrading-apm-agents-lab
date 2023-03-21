import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def serviceA(self):
        self.client.get("http://service-a/")

    @task
    def serviceB(self):
        self.client.get("http://service-b/")
    
    @task
    def serviceC(self):
        self.client.get("http://service-c/")