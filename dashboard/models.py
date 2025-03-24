from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Task(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board',default=None)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    voice = models.CharField(max_length=255, blank=True)
    script = models.CharField(max_length=255, blank=True)
    lines = models.IntegerField(default=0)
    recorded_lines = models.IntegerField(default=0)
    remaining_lines = models.IntegerField(default=0)
    recorded_total = models.IntegerField(default=0)
    origin_id = models.CharField(max_length=255, blank=True, null=True)
    base_name = models.CharField(max_length=255, blank=True)  # Optional field for duplicates or additional naming

    STATUS_CHOICES = [
        ("open", "Open"),
        ("renaming", "Renaming"),
        ("session_prep", "Session Prep"),
        ("to_be_recorded", "To Be Recorded"),
        ("recorded", "Recorded"),
        ("for_post", "For Post"),
        ("from_post", "From Post"),
        ("leveling", "Leveling"),
        ("for_qa", "For Qa"),
        ("bugfixing", "Bugfixing"),
        ("in_regression", "In Regression"),
        ("qa_done", "Qa Done"),
        ("ready_for_delivery", "Ready For Delivery"),
        ("delivered", "Delivered"),
        ("completed_recordings", "Completed Recordings"),
    ]

    status = models.CharField(
        max_length=25,  # Adjust max_length as necessary
        choices=STATUS_CHOICES,
        default="open"
    )
    

    def __str__(self):
        return f"{self.name} in {self.group.name}"
