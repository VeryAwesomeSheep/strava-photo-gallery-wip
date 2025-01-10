"""Contains all functions related to fetching data from Strava."""

from stravalib.client import Client
from utils.storage import (
  save_summary_activities,
  check_summary_file_age,
)

def get_all_activities(client: Client, athlete_id: int) -> None:
  """Get all public activities from Strava and saves them into local storage.

  Args:
    client: client structure
    athlete_id: athlete ID

  Returns:
    None

  """
  activities_raw = client.get_activities(limit=10, before='2024-08-11') # TODO remember to fucking remove the limiter
  activities_processed = []

  # TODO: In theory there is a "full_photos" field inside the activity summary, but
  # no clue how to call that with specified size and leaving it
  # empty returns placeholders, so for now there is an extra function call
  # TODO: Is using model_dump really better than making your own dict if there are
  # modifications to it afterwards anyway?
  for activity in activities_raw:
    print(f"DEBUG: processing activity {activity.id}")
    current_activity = activity.model_dump(
      mode="json",
      include={"id",
               "name",
               "sport_type",
               "start_date",
               "distance",
               "moving_time",
               "elapsed_time",
               "total_elevation_gain",
               "polyline",
               "total_photo_count",
               "full_photos", # Doesn't dump
               "kudos_count",
               "comment_count",
               "comments", # Doesn't dump
               "commute",
               })

    # Get rid of useless data from map and just keep the polyline
    current_activity["polyline"] = current_activity["polyline"]["summary_polyline"]

    # Check if there are any media (photos/videos) in the activity
    if activity.total_photo_count > 0:
      photos_urls = []

      # Retrive media URLs, strip photo size and append URLs to tmp list
      for photo in client.get_activity_photos(activity.id, 4000):
        photos_urls.append(next(iter(photo.urls.values())))

      # Add photo URLs to current_activity dict
      current_activity["photos"] = photos_urls

    # Append current_activity to activities_processed list
    activities_processed.append(current_activity)

  save_summary_activities(athlete_id, activities_processed)

def update_data_on_demand(client: Client, athlete_id: int) -> bool:
  """Update data if user demands it. Delete old and replace it with a fresh fetch.

  Args:
    client: client structure
    athlete_id (int): athlete ID

  Returns:
    True if data has been refetched
    False if user wasn't allowed to refetch

  """
  # Check if fetched data is older than 10 minutes
  if check_summary_file_age(athlete_id):
    get_all_activities(client, athlete_id)
    return True
  else:
    return False

  # TODO handle return value on frontend and display feedback to user
