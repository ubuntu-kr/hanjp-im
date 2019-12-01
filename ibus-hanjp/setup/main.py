import sys
import os
import gobject
import gtk
import ibus
import config

class Setup():
    def __init__(self):
        self.__bus = ibus.Bus()
        self.__config = self.__bus.get_config()
        self.__config.connect("value-changed", self.on_value_changed, None)

        ui_file = os.path.join(os.path.dirname(__file__), "setup.ui")
        self.__builder = gtk.Builder()
        self.__builder.add_from_file(ui_file)

        # Hangul tab
        self.__hangul_keyboard = self.__builder.get_object("HangulKeyboard")
        model = gtk.ListStore(str, str, int)
        model.append([_("Dubeolsik-Hanjp"), "2hj", 0])
        model.append([_("Dubeolsik"), "2h", 0])
        model.append([_("Sebeolsik Final"), "3f", 1])
        model.append([_("Sebeolsik 390"), "39", 2])
        model.append([_("Sebeolsik No-shift"), "3s", 3])
        model.append([_("Sebeolsik 2 set"), "32", 4])

        self.__hangul_keyboard.set_model(model)
        renderer = gtk.CellRendererText()
        self.__hangul_keyboard.pack_start(renderer)
        self.__hangul_keyboard.add_attribute(renderer, "text", 0)

        current = self.__read("HangulKeyboard", "2")
        for i in model:
            if i[1] == current:
                self.__hangul_keyboard.set_active(i[2])
                break
        
        # advanced tab
        notebook = self.__builder.get_object("SetupNotebook")
        notebook.remove_page(2)

        # setup dialog
        self.__window = self.__builder.get_object("SetupDialog")
        icon_file = os.path.join(config.datadir, "ibus-hanjp", "icons", "ibus-hanjp.svg")
        self.__window.set_icon_from_file(icon_file)
        self.__window.connect("response", self.on_response, None)
        self.__window.show()

        ok_button = self.__builder.get_object("button_cancel")
	    ok_button.grab_focus()

    def on_value_changed(self, config, section, name, value, data):
        pass

    def __write(self, name, v):
        return self.__config.set_value("engine/Hangul", name, v)

    def apply(self):
        model = self.__hangul_keyboard.get_model()
        i = self.__hangul_keyboard.get_active()
        self.__write("HangulKeyboard", model[i][1])

    def on_ok(self):
	    self.apply()

    def run(self):
        res = self.__window.run()
        if (res == gtk.RESPONSE_OK):
            self.on_ok()
        self.__window.destroy()


if __name__ == "__main__":
    Setup().run()