from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name(): welcome_message.value= my_name.get()

def change_text_size(slider_value): welcome_message.size = slider_value;

app = App(title="Hello World", width=1000, bg="#33bbbb")
welcome_message = Text(app, "welcome to my app", size="40", font="Helvetica", color="green", bg="#33bbbb");
my_name = TextBox(app, width="200");
update_text = PushButton(app, command=say_my_name, text="Display My Name")
update_text.bg = "#33bbbb"
text_size = Slider(app, command=change_text_size, start=10, end=80)
text_size.bg = "#33bbbb"
my_image = Picture(app, image="flower.gif")
app.display


