from unittest import TestLoader
from unittest import TextTestRunner
import sys
import os

project_dir = os.path.join(os.path.dirname(__file__), '..')


def main(path=None):
    if path:
        tests = _get_tests_from_file_path(path)
    else:
        tests = TestLoader().discover(os.path.join(project_dir, 'test\\'), pattern='*.py', top_level_dir=project_dir)

    return_code = not TextTestRunner().run(tests).wasSuccessful()
    sys.exit(return_code)


def _get_tests_from_file_path(path):
    if not path.endswith('.py'):
        raise Exception('test file path should not dir path')

    # path は test/hoge/fuga.py などで与えられる
    path = os.path.relpath(path, project_dir)
    if not path.startswith('test\\'):
        path = 'test\\' + path

    # test.hoge.fuga に変換
    module_name = path.replace('.py', '').replace('\\', '.')
    return TestLoader().loadTestsFromName(module_name)


if __name__ == '__main__':
    args = sys.argv
    path = '.'
    if len(args) > 1:
        main(args[1])
    else:
        main()