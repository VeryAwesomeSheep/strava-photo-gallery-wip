"""Contains all functions related to storing athletes data locally."""

import os
import time
import shutil
import json

SUMMARY_ACTIVITIES_FILE_NAME = "summary_activities.json"

def get_athlete_storage_path(athlete_id: int) -> str:
  """Return path to directory of athlete.

  Args:
    athlete_id: athlete ID

  Returns:
    athleteDir: Directory for athlete

  """
  storage_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "..",
                                  "athletes")

  # Check if athletes storage exists, create if not
  if not os.path.exists(storage_root_dir):
    # TODO: Log initialized athletes storage
    os.mkdir(storage_root_dir)

  # Check if given athlete directory exists, create if not
  athlete_dir = os.path.join(storage_root_dir, str(athlete_id))
  if not os.path.exists(athlete_dir):
    # TODO: Log initialized athlete storage for athlete ID
    os.mkdir(athlete_dir)

  return athlete_dir

def delete_athlete_data(athlete_id: int) -> None:
  """Remove all data related to the athlete.

  Args:
    athlete_id: athlete ID

  Returns:
    None

  """
  storage_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "..",
                                  "athletes")

  # Check if athletes storage exists, return if not as there is nothing to remove
  if not os.path.exists(storage_root_dir):
    # TODO: Log attempt to remove athlete when storage not initialized
    return

  # Check if given athlete directory exists, remove if it does
  athlete_dir = os.path.join(storage_root_dir, str(athlete_id))
  if os.path.exists(athlete_dir):
    # TODO: Log athlete removed
    shutil.rmtree(athlete_dir)
  else:
    # TODO: Log athlete not found
    pass

def save_summary_activities(athlete_id: int, activities: list[dict[str, int]]) -> None:
  """Save summary activities to athlete's directory.

  Args:
    athlete_id: athlete ID
    activities: list of dicts of processed activities

  Returns:
    None

  """
  summary_file_path = os.path.join(get_athlete_storage_path(athlete_id),
                                   SUMMARY_ACTIVITIES_FILE_NAME)

  with open(summary_file_path, "w") as f:
    json.dump(activities, f)

  # TODO: Log athlete summary file created

def athlete_data_exists(athlete_id: int) -> bool:
  """Check if athelte data exists.

  Args:
    athlete_id: athlete ID

  Returns:
    True if there is data in storage
    False if no data is found

  """
  summary_file_path = os.path.join(get_athlete_storage_path(athlete_id),
                                   SUMMARY_ACTIVITIES_FILE_NAME)

  # Check if activity summary file exists
  return os.path.exists(summary_file_path)

def check_summary_file_age(athlete_id: int) -> bool:
  """Check if summary file is older than 10 minutes.

  Args:
    athlete_id (int): athlete ID

  Returns:
    True if summary file is older than 10 minutes
    False if summary file isn't older than 10 minutes

  """
  summary_file_path = os.path.join(get_athlete_storage_path(athlete_id),
                                   SUMMARY_ACTIVITIES_FILE_NAME)

  # Check if summary file exists
  if os.path.exists(summary_file_path):
    # Check if file is older than 10 minutes (600s)
    return (time.time() - os.stat(summary_file_path).st_ctime) > 600
  else:
    # File doesn't exists so it's technically older than 10m, but this else
    # should never happen
    # TODO: Log error about user being able to refetch data when no data is present
    return True

def read_activities(athlete_id: int) -> list[dict]:
  """Read activity summary file from storage.

  Args:
    athlete_id: athlete ID

  Returns:
    activities: list of dicts with activities

  """
  # Make sure athlete data exists
  if not athlete_data_exists(athlete_id):
    # TODO Log error, but this should never happen
    return

  summary_file_path = os.path.join(get_athlete_storage_path(athlete_id),
                                   SUMMARY_ACTIVITIES_FILE_NAME)

  with open(summary_file_path) as f:
    activities = json.load(f)

  return activities
