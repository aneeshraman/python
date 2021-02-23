from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor.
        super().__init__(**kwargs)

        # Setting columns.
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        # Creating another layout.
        self.top_grid = GridLayout(row_force_default=True, row_default_height=40, col_force_default=True,
                                   col_default_width=100)
        self.top_grid.cols = 2
        self.add_widget(self.top_grid)

        # Add widgets.
        self.top_grid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favourite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favourite Color: "))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Creating the submit button.
        self.submit = Button(text="Submit", font_size=32, size_hint_y=None, height=50, size_hint_x=None, width=200)
        # Functionality
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        self.add_widget(
            Label(text=f"Hello {name}, you like {pizza} pizza, and your favourite color is {color}!"))

        # Clearing the input boxes.
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
