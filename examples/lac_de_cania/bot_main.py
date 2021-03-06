import atexit
import datetime
import os
from core.bot import ResourceFarmer


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    from core import Zone, env
    import logging

    work_dir = os.path.dirname(os.path.abspath(__file__))

    log_file = os.path.join(work_dir, 'bot.log')
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')

    patterns_dir = os.path.join(work_dir, "patterns")
    saves_dir = os.path.join(work_dir, 'saves')
    now = datetime.datetime.now()

    spell = {
        "range": 13,
        "nbr": 4,
        "shortcut": "z"
    }

    character_name = "John-shooter"

    zone_file_path = os.path.join(saves_dir, "cania_18_12_2020.yaml")
    plaines_de_cania = Zone("cania")

    zone_zaap = {
        "name": "plaines rocheuses",
        "coords": (-17, -47)
    }



    plaines_de_cania.loadFromFile(zone_file_path, patterns_dir)

    bot = ResourceFarmer(plaines_de_cania, zone_zaap, spell, work_dir, character_name)

    bot.mapChangeTimeOut = 12
    bot.memoTime = 60
    bot.famPatternThreshold = 0.85

    atexit.register(tearDown, bot)
    bot.start()
    bot.join()
    env.focusIDEWindow()
