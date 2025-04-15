from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDToolbar

class ContadorApp(MDApp):
    def build(self):
        self.contador = 0 

        screen = Screen()
        layout = MDBoxLayout(orientation="vertical", spacing=20)

        toolbar_layout = MDBoxLayout()
        toolbar = MDToolbar(title="Contador KivyMD")
        toolbar_layout.add_widget(toolbar)
        layout.add_widget(toolbar_layout)

        self.label = MDLabel(
            text=str(self.contador),
            halign="center",
            font_style="H3",
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.label)

        btn_layout = MDBoxLayout(spacing=20)
        btn_mas = MDRaisedButton(text="+", on_release=self.incrementar)
        btn_menos = MDRaisedButton(text="-", on_release=self.decrementar)
        btn_layout.add_widget(btn_menos)
        btn_layout.add_widget(btn_mas)

        layout.add_widget(btn_layout)

        screen.add_widget(layout)
        return screen

    def incrementar(self, instance):
        self.contador += 1
        self.label.text = str(self.contador)

    def decrementar(self, instance):
        self.contador -= 1
        self.label.text = str(self.contador)

ContadorApp().run()
