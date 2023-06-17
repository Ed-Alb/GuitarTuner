"""
Proiect PIMS
"""
import toga
from . import tuner
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, CENTER

class GuitarTuner(toga.App):
    status_image_view = toga.ImageView(image="check.png")

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        title = toga.Label(
            "Tune your guitar!",
            style=Pack(text_align=CENTER, font_size=24, font_weight="bold")
        )
        description = toga.Label(
            "Choose the chord you want to tune.",
            style=Pack(text_align=CENTER, font_size=18)
        )

        title_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        title_box.add(title)
        title_box.add(description)

        chord_title = toga.Label(
            "Chord",
            style=Pack(text_align=CENTER, font_size=15, font_weight="bold")
        )
        
        self.title = chord_title
        
        image_view = toga.ImageView(image="tuner.png")

        left_box = toga.Box(style=Pack(direction=COLUMN, alignment=LEFT, flex=1))
        chord_e2 = toga.Button(
            "E2",
            on_press=self.tune_e2,
            style=Pack(alignment=LEFT)
        )

        chord_a2 = toga.Button(
            "A2",
            on_press=self.tune_a2,
            style=Pack(alignment=LEFT)
        )

        chord_d3 = toga.Button(
            "D3",
            on_press=self.tune_d3,
            style=Pack(alignment=LEFT)
        )

        right_box = toga.Box(style=Pack(direction=COLUMN, alignment=RIGHT, flex=1))
        chord_g3 = toga.Button(
            "G3",
            on_press=self.tune_g3,
            style=Pack(alignment=RIGHT)
        )

        chord_b3 = toga.Button(
            "B3",
            on_press=self.tune_b3,
            style=Pack(alignment=RIGHT)
        )

        chord_e4 = toga.Button(
            "E4",
            on_press=self.tune_e4,
            style=Pack(alignment=RIGHT)
        )

        left_box.add(chord_d3)
        left_box.add(chord_a2)
        left_box.add(chord_e2)

        middle_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, flex=1))
        middle_box.add(self.title)
        middle_box.add(self.status_image_view)

        right_box.add(chord_e4)
        right_box.add(chord_b3)
        right_box.add(chord_g3)

        chords_box = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
        chords_box.add(left_box)
        chords_box.add(middle_box)
        chords_box.add(right_box)

        main_box.add(title_box)
        main_box.add(chords_box)
        # main_box.add(image_view)
        main_box.add(self.status_image_view)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        app_tuner = tuner.Tuner()
        app_tuner.start()

    def tune_e2(self, widget):
        self.title.text = "E2"
        tuner.SELECTION = "E2"

    def tune_a2(self, widget):
        self.title.text = "A2"
        tuner.SELECTION = "A2"

    def tune_d3(self, widget):
        self.title.text = "D3"
        tuner.SELECTION = "D3"

    def tune_g3(self, widget):
        self.title.text = "G3"
        tuner.SELECTION = "G3"

    def tune_b3(self, widget):
        self.title.text = "B3"
        tuner.SELECTION = "B3"

    def tune_e4(self, widget):
        self.title.text = "E4"
        tuner.SELECTION = "E4"


def main():
    return GuitarTuner()
