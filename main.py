from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

from google_translation import GoogleCloudTranslation as TranslationClient


class DemoExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        text = event.get_argument()
        if not text:
            return RenderResultListAction(items)

        text = text.strip()
        langs = map(lambda x: x.strip(), extension.preferences['id_langs'].split(','))
        api_key = extension.preferences['api_key']
        client = TranslationClient(api_key)
        for lang in langs:
            detect, result = client.translate_text(lang, text)
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=result,
                                             description=f"{detect}->{lang}",
                                             on_enter=CopyToClipboardAction(result)))

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
