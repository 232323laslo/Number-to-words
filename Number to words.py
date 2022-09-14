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
        self.window.size_hint = (0.3, 0.3)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # label widget
        self.number = Label(
                      text='Please, enter a number from 1 to 99',
                      font_size=55,
                      color='FFFFFF'
                      )
        self.window.add_widget(self.number)

        # text input
        self.user = TextInput(
                    multiline=False,
                    padding_y = (15, 15),
                    size_hint = (1, 0.5)
                    )
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text='OK',
                      size_hint = (1, 0.5),
                      bold = True,
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        n = self.user.text

        l1 = ["один", "два", "три", "чотири", "п‘ять", "шість", "сім", "вісім", "дев‘ять",
              "десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п‘ятнадцать",
              "шістнадцять", "сімнадцять", "вісімнадцять", "дев‘ятнадцять", "двадцять"]
        l2 = ["двадцять", "тридцять", "сорок", "п‘ятдесят", "шістдесят", "сімдесят", "вісімдесят", 'дев‘яносто']

        if int(n) <= -1 or int(n) >= 100:
            self.number.text = 'Only numbers in range 1-99'

        if int(n) <= 20 and int(n) >= 1:
            self.number.text = l1[int(n) - 1]
        elif int(n) > 20 and int(n) < 100:
            d = int(n) // 10
            o = int(n) % 10
            if d == 2:
                aab = l2[d - 2], l1[o - 1]
                ab = ' '.join(aab)
                self.number.text = ab
            if o >= 1:
                a = l2[d - 2], l1[o - 1]
                aa = ' '.join(a)
                self.number.text = aa
            if o == 0:
                self.number.text = l2[d - 2]

if __name__ == '__main__':
    Transfer().run()
