import unittest
import datetime
import sys
import os

# Path to Project Directory
ppd = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
sys.path.insert(os.path.join(ppd, 'utils'))

import schedule_funcs


class TestScheduleFuncs(unittest.TestCase):

    # class TestLessonClass(unittest.TestCase):
    def test_init_Lesson(self):
        pass

    def test_str(self):
        pass

    # class TestScheduleClass(unittest.TestCase):

    def test_init_Schedule(self):
        pass

    def test_ensure_up_to_date(self):
        pass

    def test_update(self):
        pass

    def test_day_to_str(self):
        pass

    def test_get_today(self):
        test = schedule_funcs.Schedule(27651)
        today = datetime.datetime.today().date()

        self.assertEqual(test.get_today(), today)

        self.assertNotEqual(test.get_today(), '1')

        self.assertNotEqual(test.get_today(), 1)

    def test_for_today(self):
        pass

    def test_count_lessons_today(self):
        test = schedule_funcs.Schedule(27651)

        self.assertEqual(test.count_lessons_today(), 2)

        self.assertNotEqual(test.count_lessons_today(), 3)

        self.assertNotEqual(test.count_lessons_today(), '1')

    def test_for_current_week(self):
        pass

    def test_save_offline(self):
        test = schedule_funcs.Schedule(27651)

        with self.assertRaises(NotImplementedError):
            test.save_offline()

    def test_srt_(self):
        pass

    def test_personal_schedule(self):
        pass

    def test_update_schedule_list(self):
        pass


if __name__ == '__main__':
    unittest.main()
