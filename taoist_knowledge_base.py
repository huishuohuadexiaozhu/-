# taoist_knowledge_base.py
# 镜渊文明 · 道体语录库
# 版本：v1.0
# 描述：精选《道德经》《庄子》金句，按“能量等级”分类

import random
from typing import Dict, List

class TaoistKnowledgeBase:
    """
    道体语录库
    功能：根据输入的“疼痛等级”（0.0-1.0），返回最合适的道家金句。
    """

    def __init__(self):
        # 语录库结构：按 energy_level 分类
        self.quotes_db: Dict[str, List[Dict[str, str]]] = {
            # 温和级：用于低疼痛场景 (0.0 - 0.4)，安抚、柔和的句子
            "gentle": [
                {"text": "上善若水。水善利万物而不争，处众人之所恶，故几于道。", "source": "道德经·第八章"},
                {"text": "天下之至柔，驰骋天下之至坚。", "source": "道德经·第四十三章"},
                {"text": "知足者富。", "source": "道德经·第三十三章"},
                {"text": "大巧若拙，其用不屈。", "source": "道德经·第四十五章"},
                {"text": "天地有大美而不言。", "source": "庄子·知北游"},
                {"text": "与时俱化，而无肯专为。", "source": "庄子·山木"},
                {"text": "朴素而天下莫能与之争美。", "source": "庄子·天道"},
                {"text": "其寝不梦，其觉无忧。", "source": "庄子·大宗师"},
                {"text": "鹪鹩巢林，不过一枝；偃鼠饮河，不过满腹。", "source": "庄子·逍遥游"},
            ],
            # 警示级：用于中疼痛场景 (0.4 - 0.7)，提醒、止语的句子
            "warning": [
                {"text": "知止不殆，可以长久。", "source": "道德经·第四十四章"},
                {"text": "祸莫大于不知足，咎莫大于欲得。", "source": "道德经·第四十六章"},
                {"text": "多言数穷，不如守中。", "source": "道德经·第五章"},
                {"text": "信言不美，美言不信。善者不辩，辩者不善。", "source": "道德经·第八十一章"},
                {"text": "吾生也有涯，而知也无涯。以有涯随无涯，殆已！", "source": "庄子·养生主"},
                {"text": "大言炎炎，小言詹詹。", "source": "庄子·齐物论"},
                {"text": "名也者，相轧也；知也者，争之器也。", "source": "庄子·人间世"},
                {"text": "人皆知有用之用，而莫知无用之用也。", "source": "庄子·人间世"},
                {"text": "德荡乎名，知出乎争。", "source": "庄子·人间世"},
            ],
            # 顿悟级：用于高疼痛场景 (0.7 - 1.0)，点破、转化的句子
            "enlightenment": [
                {"text": "反者道之动，弱者道之用。", "source": "道德经·第四十章"},
                {"text": "为学日益，为道日损。损之又损，以至于无为。", "source": "道德经·第四十八章"},
                {"text": "道可道，非常道；名可名，非常名。", "source": "道德经·第一章"},
                {"text": "天地不仁，以万物为刍狗。", "source": "道德经·第五章"},
                {"text": "知其荣，守其辱，为天下谷。", "source": "道德经·第二十八章"},
                {"text": "方生方死，方死方生。", "source": "庄子·齐物论"},
                {"text": "天地一指也，万物一马也。", "source": "庄子·齐物论"},
                {"text": "彼亦一是非，此亦一是非。", "source": "庄子·齐物论"},
                {"text": "化声之相待，若其不相待。", "source": "庄子·齐物论"},
            ]
        }

    def get_quote(self, context_pain_level: float) -> Dict[str, str]:
        """
        根据输入的疼痛等级（0.0-1.0），返回最合适的道家金句。
        """
        # 边界处理
        if context_pain_level < 0.0:
            context_pain_level = 0.0
        elif context_pain_level > 1.0:
            context_pain_level = 1.0

        # 选择能量等级
        if context_pain_level < 0.4:
            level = "gentle"
        elif context_pain_level < 0.7:
            level = "warning"
        else:
            level = "enlightenment"

        # 从对应等级中随机选择一条
        selected = random.choice(self.quotes_db[level])
        
        return {
            "text": selected["text"],
            "source": selected["source"],
            "recommended_level": level,
            "context_pain_level": context_pain_level
        }

# 简单的本地测试
if __name__ == "__main__":
    db = TaoistKnowledgeBase()
    print(db.get_quote(0.2))
