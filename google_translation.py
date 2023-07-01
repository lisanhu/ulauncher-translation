import urllib.request
import json
from typing import Tuple

class GoogleCloudTranslation:
    def __init__(self, api_key):
        self.api_key = api_key

    def translate_text(self, target, text) -> Tuple[str, str]:
        # Create the request body
        body = {
            "target": target,
            "q": text
        }

        # Make the POST request
        request = urllib.request.Request(
            f"https://translation.googleapis.com/language/translate/v2?key={self.api_key}",
            headers={
                "Content-Type": "application/json; charset=utf-8"
            },
            data=json.dumps(body).encode("utf-8")
        )

        print(request.full_url)
        print(request.headers)
        print(request.data)
        with urllib.request.urlopen(request) as f:
            response_data = f.read()
        translation = json.loads(response_data)["data"]["translations"][0]["translatedText"]
        lang = json.loads(response_data)["data"]["translations"][0]["detectedSourceLanguage"]
        return lang, translation

