from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Transfer(App):
    def build(self):
        # add widgets to window
        self.window = GridLayout()
        self.window.cols = 1

        # label widget
        self.greeting = Label(text='Your number')
        self.window.add_widget(self.greeting)

        # text input
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(text='OK')
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        n = self.user.text
        l1 = ["один", "два", "три", "чотири", "п‘ять", "шість", "сім", "вісім", "дев‘ять",
              "десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п‘ятнадцать",
              "шістнадцять", "сімнадцять", "вісімнадцять", "дев‘ятнадцять", "двадцять"]
        l2 = ["двадцять", "тридцять", "сорок", "п‘ятдесят", "шістдесят", "сімдесят", "вісімдесят", 'дев‘яносто']

        if int(n) <= 20:
            self.greeting.text = l1[int(n) - 1]
        elif int(n) > 20:
            d = int(n) // 10
            o = int(n) % 10
            if d == 2:
                aab = l2[d - 2], l1[o - 1]
                ab = ' '.join(aab)
                self.greeting.text = ab
            if o >= 1:
                a = l2[d - 2], l1[o - 1]
                aa = ' '.join(a)
                self.greeting.text = aa
            if o == 0:
                self.greeting.text = l2[d - 2]

if __name__ == '__main__':
    Transfer().run()
