import time

import requests

from config.config import settings

# Retrieve the bearer token from environment variables
bearer_token = settings.DID_BEARER_TOKEN


def generate_clip(input_text: str) -> str:
    url = "https://api.d-id.com/clips"

    payload = {
        "presenter_id": "anita-6_uTzyZtNR",
        "script": {
            "type": "text",
            "subtitles": "false",
            "provider": {"type": "microsoft", "voice_id": "Sara"},
            "input": input_text,
            "ssml": "false",
        },
        "config": {"result_format": "mp4"},
        "presenter_config": {"crop": {"type": "wide"}},
        "driver_id": "Ecg7Fd7cJz",
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {bearer_token}",
    }

    # Send the POST request
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for unsuccessful requests

    # Parse and return only the ID from the response
    res = response.json()
    return res["id"]


def get_video(clip_id: str, interval: int = 10, max_attempts: int = 40) -> str | None:
    """
    Polls the video generation status every 10 seconds until the result_url is available or max_attempts are reached.

    Parameters:
    - clip_id: ID of the video clip to fetch.
    - interval: Time in seconds to wait between polling attempts.
    - max_attempts: Maximum number of polling attempts.

    Returns:
    - result_url if the video is ready, None if it times out.
    """

    url = f"https://api.d-id.com/clips/{clip_id}"
    headers = {"accept": "application/json", "authorization": f"Bearer {bearer_token}"}

    for attempt in range(max_attempts):
        response = requests.get(url, headers=headers)

        # Parse the JSON response
        res = response.json()

        # Check if the video generation is complete and the result_url is available
        if res.get("status") == "done" and res.get("result_url"):
            return res["result_url"]

        time.sleep(interval)

    # If max attempts are reached without getting the result_url
    print("Max attempts reached without finding the result_url.")
    return None
