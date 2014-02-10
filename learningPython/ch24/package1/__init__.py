#!/usr/bin/env python3
'''
Package initialization file roles
1. serves as a hook for package initialization-time actions
2. declares a directory as a Python package
3. generates a module namespace for a directory
4. implements the behavior of from * statements when used with directory imports
'''
print('Package', __name__, 'is initialized')

x = 1
