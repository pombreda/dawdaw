# "THE BELGIAN BEER-WARE LICENSE" (Revision 42):
# <cortex@worlddomination.be> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you
# think this stuff is worth it, you can buy me a belgian beer in return -- Laurent Peuch

from dawdaw.utils import salt_render


def render(*args, **kwargs):
    return salt_render(salt=__salt__, grains=__grains__, opts=__opts__, pillar=__pillar__, *args, **kwargs)
