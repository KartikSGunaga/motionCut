from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class AdventureGame(App):
    def build(self):
        self.storyIndex = 0

        self.story = [
            {
                'text': 'Welcome to the Adventure Game! You find yourself in a dark forest. What do you do?',
                'options': [
                    {'text': 'Go deeper into the forest', 'nextIndex': 1},
                    {'text': 'Turn back and leave the forest', 'nextIndex': 2}
                ]
            },
            {
                'text': 'As you venture deeper into the forest, you come across a mysterious cave. Enter the cave?',
                'options': [
                    {'text': 'Enter the cave', 'nextIndex': 3},
                    {'text': 'Continue exploring the forest', 'nextIndex': 4}
                ]
            },
            {
                'text': 'You decide to leave the forest. The adventure ends.',
                'options': []
            },
            {
                'text': 'Inside the cave, you find a treasure chest. Open it?',
                'options': [
                    {'text': 'Open the chest', 'nextIndex': 5},
                    {'text': 'Leave the cave', 'nextIndex': 6}
                ]
            },
            {
                'text': 'You continue exploring the forest and encounter a friendly elf. What do you want to do?',
                'options': [
                    {'text': 'Talk to the elf', 'nextIndex': 7},
                    {'text': 'Ignore the elf and keep walking', 'nextIndex': 8}
                ]
            },
            {
                'text': 'Congratulations! You found a magic sword in the treasure chest. You win!',
                'options': []
            },
            {
                'text': 'The chest was booby-trapped! You triggered a trap and lose some health.',
                'options': []
            },
            {
                'text': 'You have a pleasant conversation with the elf and receive a magical amulet. You win!',
                'options': []
            },
            {
                'text': 'You ignore the elf and continue walking. The adventure ends.',
                'options': []
            }
        ]

        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.label = Label(text=self.story[self.storyIndex]['text'], font_size=16, halign='center')
        self.layout.add_widget(self.label)

        for option in self.story[self.storyIndex]['options']:
            button = Button(text=option['text'], on_press=self.chooseOption)
            setattr(button, 'nextIndex', option['nextIndex'])
            self.layout.add_widget(button)

        return self.layout

    def chooseOption(self, instance):
        if self.storyIndex < len(self.story) - 1:
            self.storyIndex = getattr(instance, 'nextIndex', 0)
            self.updateScreen()

    def updateScreen(self):
        self.layout.clear_widgets()
        self.label.text = self.story[self.storyIndex]['text']
        self.layout.add_widget(self.label)

        if self.story[self.storyIndex]['options']:
            for option in self.story[self.storyIndex]['options']:
                button = Button(text=option['text'], on_press=self.chooseOption)
                setattr(button, 'nextIndex', option['nextIndex'])
                self.layout.add_widget(button)
        else:
            self.showEndPopup()

    def showEndPopup(self):
        popupContent = BoxLayout(orientation='vertical', spacing=10)
        popupContent.add_widget(Label(text='Congratulations! The adventure has ended.'))

        closeButton = Button(text='Close', size_hint_y=None, height=40)
        closeButton.bind(on_press=self.closePopup)
        popupContent.add_widget(closeButton)

        popup = Popup(title='Adventure Ended', content=popupContent, size_hint=(None, None), size=(300, 200))
        popup.open()

    def closePopup(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    AdventureGame().run()
