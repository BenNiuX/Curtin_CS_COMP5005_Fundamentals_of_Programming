"""
testConfig.py - test for config.py

Written by : Ben Niu
Student ID : 21678145

Usage:
    Execute py file

Versions:
    - initial version by Ben Niu 26/04/24
"""

import unittest

from config import Config


class TestConfig(unittest.TestCase):

    def test_config(self):
        config = Config()
        self.assertEqual(config.myclass, config.__class__.__name__)
        cfg = config.get_cfg()
        self.assertIsNotNone(cfg)
        attrs = dir(config)
        sections = []
        for a in attrs:
            if a.startswith("SECTION_"):
                s = a.split("_")
                # (section_name, section_key)
                sections.append((s[1], a))
        for sect in sections:
            for a in attrs:
                s = a.split("_")
                if (not a.startswith("__")) and sect[0].startswith(s[0]) \
                        and len(s[0]) < 5:
                    try:
                        key = (
                            f"[{config.__getattribute__(sect[1])}]"
                            f"[{config.__getattribute__(a)}]"
                        )
                        value = cfg.get(config.__getattribute__(sect[1]),
                                        config.__getattribute__(a))
                        self.assertTrue(len(value) > 0,
                                        f"key={key} value={value}")
                        print(f"{key}={value}")
                    except KeyError as e:
                        self.assertTrue(False, e)


if __name__ == "__main__":
    unittest.main()
