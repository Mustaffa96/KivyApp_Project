from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView


class Calc(FloatLayout):
    pass

class MenuWidget(RelativeLayout):
    pass

class ScrollViewExample(ScrollView):
    pass

class Screen(Screen):
    pass

class AnchorLayout(AnchorLayout):
    pass

class GridLayoutExample(GridLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class TheZakatApp(App):
    pass


TheZakatApp().run()
