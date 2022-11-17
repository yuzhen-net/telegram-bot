from nonebot import get_driver, on_command

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass


ping_command = on_command("ping")

@ping_command.handle()
async def ping():
    await ping_command.send('Hello, world!')
