#!/usr/bin/env python
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'core_service'))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()