"""The file contains different constants like file paths"""
import os
# --------------------------------------------------------------------------

EQUIPMENT_FILE = os.path.join('data', 'equipment.json')
CLASSES_FILE = os.path.join('data', 'hero_classes.json')
SKILLS_FILE = os.path.join('data', 'skills.json')
LOGS_FILE = os.path.join('data', 'unit_phrases.json')

DEFAULT_POSITIVE = ["Великий {0} наносит мощный удар {1} в живот {2} и "
                    "успешно пробивает {3} нанося {4} урона"]
DEFAULT_NEGATIVE = ["{0} в полной уверенности размахивает {2} "
                    "нанося удар {1} в пятую точку, к счастью {3} "
                    "сдерживает такое нападение"]
