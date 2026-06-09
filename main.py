import hashlib
from datetime import datetime, timezone, timedelta

from astrbot.api import star
from astrbot.api.event import AstrMessageEvent, filter

CST = timezone(timedelta(hours=8))

def _get_luck_value(user_id: str) -> int:
    """Deterministic luck score per day."""
    day = int(datetime.now(CST).replace(hour=0, minute=0, second=0, microsecond=0).timestamp() / 86400)
    seed = f"{user_id}{day}42"
    h = int(hashlib.sha256(seed.encode()).hexdigest(), 16)
    return h % 101

def _get_luck_comment(luck: int) -> str:
    jackpots = {0: "怎，怎么会这样……", 42: "感觉可以参透宇宙的真理。", 77: "要不要去抽一发卡试试呢……？", 100: "买彩票可能会中大奖哦！"}
    if luck in jackpots:
        return jackpots[luck]
    if luck <= 20:
        return "推荐闷头睡大觉。"
    elif luck <= 40:
        return "也许今天适合摆烂。"
    elif luck <= 60:
        return "又是平凡的一天。"
    elif luck <= 80:
        return "太阳当头照，花儿对你笑。"
    else:
        return "出门可能捡到 1 块钱。"

class Main(star.Star):
    """今日人品 - 看看你今天运气如何？ 发送 jrrp 即可查询。"""

    @filter.command("jrrp")
    async def jrrp(self, event: AstrMessageEvent) -> None:
        sender = event.get_sender_name()
        user_id = event.get_sender_id()
        luck = _get_luck_value(user_id)
        comment = _get_luck_comment(luck)
        yield event.plain_result(f"{sender} 的今日人品是：{luck}。{comment}")
