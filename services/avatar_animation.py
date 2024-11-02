import asyncio

import requests

from config.config import settings


class AvatarAnimation:
    def __init__(self):
        self.bearer_token = settings.DID_BEARER_TOKEN

    def generate_clip(self, input_text: str) -> str:
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
            "authorization": f"Bearer {self.bearer_token}",
        }

        # Send the POST request
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for unsuccessful requests

        # Parse and return only the ID from the response
        res = response.json()
        return res["id"]

    async def get_video(
        self, clip_id: str, interval: int = 30, max_attempts: int = 10
    ) -> str | None:
        """
        Polls the video generation status every 30 seconds until the result_url is available or max_attempts are reached.

        Parameters:
        - clip_id: ID of the video clip to fetch.
        - interval: Time in seconds to wait between polling attempts.
        - max_attempts: Maximum number of polling attempts.

        Returns:
        - result_url if the video is ready, None if it times out.
        """

        url = f"https://api.d-id.com/clips/{clip_id}"
        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {self.bearer_token}",
        }

        for attempt in range(max_attempts):
            await asyncio.sleep(interval)  # Non-blocking delay
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Check for HTTP errors
                res = response.json()

                if res.get("status") == "done" and res.get("result_url"):
                    print(f"Video generation complete: {res['result_url']}")
                    return res["result_url"]

                print(f"Attempt {attempt + 1}: Status - {res.get('status')}")

            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt + 1}: Request failed with error: {e}")
            except ValueError:
                print("Invalid JSON response received. Skipping this attempt.")

        print("Max attempts reached without finding the result_url.")
        return None


avatar_animation = AvatarAnimation()
